#!/usr/bin/env python3
"""Split one over-long subtitle Dialogue line into two events at a clause boundary.

Used to fix 3-row lines (see detect_long_lines.py) when rewording isn't preferred.
The *text* split point is a clause boundary you pass (--before); the *time* split is
chosen so the sub switches on a real breath:

  1. proportional estimate = start + dur * len(A) / (len(A)+len(B))
  2. if --transcript given, look for the largest inter-word silence within
     ±--window of that estimate (inside the cue) and snap to its midpoint;
  3. reject the snap if it makes either half shorter than --min-display (unreadable),
     or if no qualifying pause is found — fall back to the proportional estimate.

Why bounded, not the globally-largest gap: the biggest silence in a cue is often a
mid-sentence hesitation *after* the clause boundary, so snapping to it desyncs the
sub from the speech. The clause boundary lands near the proportional estimate, so we
only trust a pause near there. (The transcript words are the source-language STT, so
we use them only for *timing* — silence is language-agnostic — never to pick the text
split point.)

Preserves a leading {\\pos(...)} tag on both halves (PiP lines).

Usage:
    split_subtitle_line.py TARGET.ass --line N --before "SUBSTRING" \\
        [--transcript T.json] [--window 1.0] [--min-display 1.0] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys


def cs(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def fmt(x):
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = x - h * 3600 - m * 60
    return f"{h}:{m:02d}:{s:05.2f}"


def pause_snap(words, start, end, prop, window, min_gap=0.20):
    """Largest inter-word gap midpoint within ±window of prop (and inside cue)."""
    best = None
    for i in range(len(words) - 1):
        gap = words[i + 1]["start_time"] - words[i]["end_time"]
        if gap < min_gap:
            continue
        mid = (words[i + 1]["start_time"] + words[i]["end_time"]) / 2
        if start < mid < end and abs(mid - prop) <= window:
            if best is None or gap > best[0]:
                best = (gap, mid)
    return best  # (gap, mid) or None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ass")
    ap.add_argument("--line", type=int, required=True, help="1-based Dialogue line number")
    ap.add_argument("--before", required=True, help="split the text before this substring")
    ap.add_argument("--transcript", help="transcript.json for pause-snapping")
    ap.add_argument("--window", type=float, default=1.0, help="±seconds to search for a pause")
    ap.add_argument("--min-display", type=float, default=1.0, help="min seconds per half")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    lines = open(args.ass, encoding="utf-8").read().split("\n")
    ln = lines[args.line - 1]
    if not ln.startswith("Dialogue:"):
        sys.exit(f"line {args.line} is not a Dialogue line")
    p = ln.split(",", 9)
    text = p[9]
    if args.before not in text:
        sys.exit(f"--before substring not found on line {args.line}")

    i = text.index(args.before)
    a, b = text[:i].strip(), text[i:].strip()
    pos = re.match(r"\{\\pos\([0-9]+,[0-9]+\)\}", text)
    if pos and not b.startswith(pos.group(0)):
        b = pos.group(0) + b  # keep \pos on the 2nd half

    start, end = cs(p[1]), cs(p[2])
    dur = end - start
    a_len = len(re.sub(r"\{[^}]*\}", "", a))
    b_len = len(re.sub(r"\{[^}]*\}", "", b))
    prop = start + dur * (a_len / (a_len + b_len))

    split, how = prop, "proportional"
    if args.transcript:
        words = [w for w in json.load(open(args.transcript, encoding="utf-8"))["words"]
                 if w.get("start_time") is not None]
        words.sort(key=lambda w: w["start_time"])
        snap = pause_snap(words, start, end, prop, args.window)
        if snap:
            cand = snap[1]
            if cand - start >= args.min_display and end - cand >= args.min_display:
                split, how = cand, f"pause-snap (gap {snap[0]:.2f}s, {cand-prop:+.2f}s)"
            else:
                how = "proportional (snap rejected: too-short half)"

    head = p[:9]
    la = ",".join([head[0], p[1], fmt(split)] + head[3:]) + "," + a
    lb = ",".join([head[0], fmt(split), p[2]] + head[3:]) + "," + b

    print(f"cue {p[1]}–{p[2]}  split @ {fmt(split)}  [{how}]")
    print(f"  A: {a}")
    print(f"  B: {b}")
    if args.dry_run:
        print("[dry-run] not written")
        return
    lines[args.line - 1:args.line] = [la, lb]
    open(args.ass, "w", encoding="utf-8").write("\n".join(lines))
    print("written.")


if __name__ == "__main__":
    main()
