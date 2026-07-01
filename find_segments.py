#!/usr/bin/env python3
"""Find hardsub keep-segments from a translated .ass by gap analysis.

An AfterTalk recording interleaves the host's talk (which we keep + hardsub) with
watchalongs we cut: the intro delay, an opening PV/digest, the in-game story
watchalong, and the song/2DMV viewing. Those cut regions are marked as
non-rendering ``Comment:`` lines (or nothing at all), so they show up as GAPS in
the rendered ``Dialogue`` timeline. This script finds those gaps and prints the
contiguous keep-segments between them, ready to feed to ``hardsub_trim.sh``.

Optionally cross-checks each gap against the raw transcript: a gap with ~0 words
is genuinely silent (safe to cut), while a gap full of words is a story/song
watchalong (the host/game audio you're deliberately dropping) — either way it's
cut, but the word count tells you *why* so you don't cut real host talk by mistake.

Usage:
    find_segments.py TRANSLATED.ass [--gap 25] [--transcript TRANSCRIPT.json]
                     [--pad 1] [--hardsub MKV:OUT.mp4]

--gap        minimum gap (seconds) in the rendered timeline to treat as a cut (default 25)
--transcript raw transcript.json — report word counts inside each gap
--pad        seconds to extend each keep-segment outward when emitting timestamps (default 1)
--hardsub    print a ready-to-run hardsub_trim.sh command for MKV -> OUT.mp4
"""
from __future__ import annotations

import argparse
import json
import sys


def _cs(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def _fmt(x):
    x = max(0, x)
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = int(x % 60)
    return f"{h}:{m:02d}:{s:02d}"


def _rendered_rows(path):
    rows = []
    for ln in open(path, encoding="utf-8"):
        if not ln.startswith("Dialogue:"):  # Comment: lines don't render
            continue
        p = ln.split(",", 9)
        if len(p) < 10:
            continue
        st, en = _cs(p[1]), _cs(p[2])
        txt = p[9].strip()
        if en <= st or not txt or txt == "[":  # zero-dur / empty / stray marker
            continue
        rows.append((st, en))
    rows.sort()
    return rows


def _segments(rows, gap):
    segs = [[rows[0][0], rows[0][1]]]
    gaps = []
    for st, en in rows[1:]:
        if st - segs[-1][1] > gap:
            gaps.append((segs[-1][1], st))
            segs.append([st, en])
        else:
            segs[-1][1] = max(segs[-1][1], en)
    return segs, gaps


def _gap_word_counts(transcript_path, gaps):
    d = json.load(open(transcript_path, encoding="utf-8"))
    words = d.get("words", [])
    out = []
    for a, b in gaps:
        n = sum(1 for w in words
                if w.get("start_time") is not None and a <= w["start_time"] < b)
        out.append(n)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ass", help="the _translated.ass file")
    ap.add_argument("--gap", type=float, default=25.0)
    ap.add_argument("--transcript")
    ap.add_argument("--pad", type=float, default=1.0)
    ap.add_argument("--hardsub", help="MKV:OUT.mp4 — emit a hardsub_trim.sh command")
    args = ap.parse_args(argv)

    rows = _rendered_rows(args.ass)
    if not rows:
        sys.exit("No rendered Dialogue lines found.")
    segs, gaps = _segments(rows, args.gap)

    print(f"Rendered dialogue lines: {len(rows)}")
    print(f"Span: {_fmt(rows[0][0])} -> {_fmt(rows[-1][1])}\n")

    counts = _gap_word_counts(args.transcript, gaps) if args.transcript else None
    print(f"=== CUT regions (gaps > {args.gap:.0f}s) ===")
    for i, (a, b) in enumerate(gaps):
        tag = ""
        if counts is not None:
            n = counts[i]
            tag = f"  [{n} words in transcript — {'SILENT, safe' if n < 5 else 'watchalong audio'}]"
        print(f"  {_fmt(a)} -> {_fmt(b)}  ({b-a:.0f}s){tag}")

    print(f"\n=== KEEP segments (host talk, pad {args.pad:.0f}s) ===")
    pairs = []
    for i, (a, b) in enumerate(segs, 1):
        s, e = _fmt(a - args.pad), _fmt(b + args.pad)
        pairs.append((s, e))
        print(f"  {i}: {s} -> {e}   ({b-a:.0f}s)")

    if args.hardsub:
        mkv, _, out = args.hardsub.partition(":")
        subs = args.ass
        seg_args = " \\\n  ".join(f"{s} {e}" for s, e in pairs)
        print("\n=== hardsub command (run from projects repo root) ===")
        print(f'./hardsub_trim.sh \\\n  "{mkv}" \\\n  "{subs}" \\\n  "{out}" \\\n  {seg_args}')


if __name__ == "__main__":
    main()
