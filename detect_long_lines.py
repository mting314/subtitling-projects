#!/usr/bin/env python3
"""Detect subtitle lines that render to more than 2 rows on screen.

Three+ rows is bad subtitling practice — it forces the viewer's eyes to sweep
too far and eats screen real estate. Row count depends on libass's actual
wrapping (font, size, \\fscx, wrap width from margins, \\N, WrapStyle), which you
can't predict from the text, so this measures the ground truth: it renders each
Dialogue line under its real style over a black background and counts the text
rows by horizontal projection. No video needed — line count is pure text layout.

Rendering matches production (the `ass=` libass filter, fontconfig font
resolution), so the counts reflect what the hardsub actually burns in. Lines are
batched one-per-second into a single synthetic .ass and rendered in one ffmpeg
pass.

Requires pillow + numpy — run via uv:
    uv run --with pillow --with numpy python3 detect_long_lines.py TRANSLATED.ass [--flag-over 2]

Skips Comment: lines (don't render), \\p drawings (img2ass memes), and empty lines.
Prints a table of every line with its row count, flagging those over the limit.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image
import numpy as np


def _fmt_time(sec):
    return f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}.00"


def _parse(path):
    """Return (header_text, events_format_line, [(lineno, fields)])."""
    lines = open(path, encoding="utf-8").read().split("\n")
    header, fmt, dialogues = [], None, []
    in_events = False
    for i, ln in enumerate(lines, 1):
        if ln.strip().lower().startswith("[events]"):
            in_events = True
            header.append(ln)
            continue
        if not in_events:
            header.append(ln)
            continue
        if ln.startswith("Format:") and fmt is None:
            fmt = ln
        elif ln.startswith("Dialogue:"):
            p = ln.split(",", 9)
            if len(p) < 10:
                continue
            text = p[9]
            # skip empty / stray / img2ass drawings (\p1..\pN drawing mode).
            # NOTE: match \p<digit> only — plain "\p" would also match \pos (PiP lines)!
            if not text.strip() or text.strip() == "[" or re.search(r"\\p\d", text):
                continue
            dialogues.append((i, p))
    return "\n".join(header[:-1]), fmt, dialogues  # drop the [Events] line itself


def _playres(header):
    x, y = 1920, 1080
    for ln in header.split("\n"):
        if ln.startswith("PlayResX:"):
            x = int(ln.split(":", 1)[1].strip())
        elif ln.startswith("PlayResY:"):
            y = int(ln.split(":", 1)[1].strip())
    return x, y


def _count_rows(png, rel=0.10, min_band=15):
    """Count contiguous horizontal text bands in a black-bg render."""
    arr = np.asarray(Image.open(png).convert("L"))
    proj = (arr > 20).sum(axis=1)  # non-bg px per row
    peak = proj.max()
    if peak == 0:
        return 0
    text = proj > max(peak * rel, 3)
    rows, run = 0, 0
    for t in text:
        if t:
            run += 1
        else:
            if run >= min_band:
                rows += 1
            run = 0
    if run >= min_band:
        rows += 1
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ass")
    ap.add_argument("--flag-over", type=int, default=2,
                    help="flag lines rendering to MORE than this many rows (default 2)")
    ap.add_argument("--keep", action="store_true", help="keep rendered frames")
    args = ap.parse_args(argv)

    header, fmt, dialogues = _parse(args.ass)
    if not dialogues:
        sys.exit("No renderable Dialogue lines found.")
    W, H = _playres(header)
    fmt = fmt or ("Format: Layer, Start, End, Style, Name, MarginL, MarginR, "
                  "MarginV, Effect, Text")

    tmp = tempfile.mkdtemp(prefix="linecheck_")
    synth = os.path.join(tmp, "synth.ass")
    with open(synth, "w", encoding="utf-8") as f:
        f.write(header.rstrip() + "\n\n[Events]\n" + fmt + "\n")
        for idx, (_, p) in enumerate(dialogues):
            q = list(p)
            q[1] = _fmt_time(idx)          # retime to its own 1-second slot
            q[2] = _fmt_time(idx + 1)
            f.write(",".join(q) + "\n")

    n = len(dialogues)
    # one render pass: black bg at PlayRes, 1 fps, N frames -> N PNGs
    cmd = ["ffmpeg", "-v", "error", "-f", "lavfi",
           "-i", f"color=c=black:s={W}x{H}:r=1:d={n}",
           "-vf", f"ass={synth}", "-frames:v", str(n),
           "-y", os.path.join(tmp, "f%05d.png")]
    subprocess.run(cmd, check=True)

    flagged = []
    print(f"{'line':>5}  {'time':>10}  {'rows':>4}  {'style':<18}  text")
    print("-" * 100)
    for idx, (lineno, p) in enumerate(dialogues):
        png = os.path.join(tmp, f"f{idx + 1:05d}.png")
        rows = _count_rows(png) if os.path.exists(png) else -1
        style = p[3].strip()
        text = p[9].strip()
        text_disp = text if len(text) <= 60 else text[:57] + "..."
        mark = "  <== FLAG" if rows > args.flag_over else ""
        if rows > args.flag_over:
            flagged.append((lineno, p[1], style, rows, text))
        # only print flagged + a compact all-rows tally to keep output readable
        if rows > args.flag_over:
            print(f"{lineno:>5}  {p[1]:>10}  {rows:>4}  {style:<18}  {text_disp}{mark}")

    print("-" * 100)
    print(f"Scanned {n} renderable lines. Flagged {len(flagged)} with > {args.flag_over} rows.")
    if not args.keep:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    else:
        print(f"Frames kept in {tmp}")


if __name__ == "__main__":
    main()
