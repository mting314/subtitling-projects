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

FADE-AWARE (--mkv): watchalongs/MVs often fade to/from black at their edges. The
segment pad can push a cut into such a fade, and when two cut-adjacent half-fades
meet at a concat join you get a black flash. With --mkv (or --hardsub), each
boundary is checked with ffmpeg blackdetect and pulled just clear of any source
black — no subtitles are lost (the pad region beyond the last/first sub is
sub-free).

Usage:
    find_segments.py TRANSLATED.ass [--gap 25] [--transcript T.json]
                     [--pad 1] [--mkv V.mkv] [--hardsub MKV:OUT.mp4]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

FADE_MARGIN = 0.08  # cut this many extra seconds clear of a detected fade


def _cs(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def _fmt(x):
    x = max(0.0, x)
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = x - h * 3600 - m * 60
    return f"{h}:{m:02d}:{s:05.2f}"


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
    words = json.load(open(transcript_path, encoding="utf-8")).get("words", [])
    return [sum(1 for w in words if w.get("start_time") is not None and a <= w["start_time"] < b)
            for a, b in gaps]


def _black_intervals(mkv, ws, we, d=0.05, pix=0.10):
    """Source-black intervals (absolute seconds) in [ws, we] via ffmpeg blackdetect."""
    ws = max(0.0, ws)
    dur = we - ws
    if dur <= 0:
        return []
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-ss", f"{ws:.3f}", "-i", mkv, "-t", f"{dur:.3f}",
         "-vf", f"blackdetect=d={d}:pix_th={pix}", "-an", "-f", "null", "-"],
        capture_output=True, text=True)
    return [(ws + float(m.group(1)), ws + float(m.group(2)))
            for m in re.finditer(r"black_start:([\d.]+)\s+black_end:([\d.]+)", p.stderr)]


def _fade_adjust(mkv, content_start, content_end, pad):
    """Padded boundaries pulled clear of source fades. Returns (start, end, notes)."""
    start, end = max(0.0, content_start - pad), content_end + pad
    notes = []
    # END: a fade-out beginning after the last sub -> cut just before it
    for bs, _ in _black_intervals(mkv, content_end - 0.05, end + 0.3):
        if bs > content_end - 0.05:
            new_end = max(content_end, bs - FADE_MARGIN)
            if new_end < end:
                notes.append(f"end {_fmt(end)}->{_fmt(new_end)} (source fade)")
                end = new_end
            break
    # START: a fade-in completing before the first sub -> begin just after it
    best_be = None
    for _, be in _black_intervals(mkv, start - 0.3, content_start + 0.05):
        if be < content_start + 0.05:
            best_be = be if best_be is None else max(best_be, be)
    if best_be is not None:
        new_start = min(content_start, best_be + FADE_MARGIN)
        if new_start > start:
            notes.append(f"start {_fmt(start)}->{_fmt(new_start)} (source fade)")
            start = new_start
    return start, end, notes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ass", help="the _translated.ass file")
    ap.add_argument("--gap", type=float, default=25.0)
    ap.add_argument("--transcript")
    ap.add_argument("--pad", type=float, default=1.0)
    ap.add_argument("--mkv", help="source video — enable fade-aware boundary snapping")
    ap.add_argument("--hardsub", help="MKV:OUT.mp4 — emit a hardsub_trim.sh command")
    args = ap.parse_args(argv)

    rows = _rendered_rows(args.ass)
    if not rows:
        sys.exit("No rendered Dialogue lines found.")
    segs, gaps = _segments(rows, args.gap)
    mkv = args.mkv or (args.hardsub.split(":", 1)[0] if args.hardsub else None)

    print(f"Rendered dialogue lines: {len(rows)}")
    print(f"Span: {_fmt(rows[0][0])} -> {_fmt(rows[-1][1])}\n")

    counts = _gap_word_counts(args.transcript, gaps) if args.transcript else None
    print(f"=== CUT regions (gaps > {args.gap:.0f}s) ===")
    for i, (a, b) in enumerate(gaps):
        tag = ""
        if counts is not None:
            n = counts[i]
            tag = f"  [{n} words — {'SILENT, safe' if n < 5 else 'watchalong audio'}]"
        print(f"  {_fmt(a)} -> {_fmt(b)}  ({b-a:.0f}s){tag}")

    fade = "fade-aware" if mkv else f"pad {args.pad:.0f}s"
    print(f"\n=== KEEP segments ({fade}) ===")
    pairs = []
    for i, (a, b) in enumerate(segs, 1):
        if mkv:
            s, e, notes = _fade_adjust(mkv, a, b, args.pad)
            note = ("  " + "; ".join(notes)) if notes else ""
        else:
            s, e, note = a - args.pad, b + args.pad, ""
        pairs.append((_fmt(s), _fmt(e)))
        print(f"  {i}: {_fmt(s)} -> {_fmt(e)}   ({b-a:.0f}s){note}")

    if args.hardsub:
        mkv_path, _, out = args.hardsub.partition(":")
        seg_args = " \\\n  ".join(f"{s} {e}" for s, e in pairs)
        print("\n=== hardsub command (run from projects repo root) ===")
        print(f'./hardsub_trim.sh \\\n  "{mkv_path}" \\\n  "{args.ass}" \\\n  "{out}" \\\n  {seg_args}')


if __name__ == "__main__":
    main()
