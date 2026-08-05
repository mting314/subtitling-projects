#!/usr/bin/env python3
"""Measure each character style's outline-vs-background contrast in a real episode.

Subtitles here are white fill + a character-coloured outline. The outline is what
separates the white text from the video, so readability depends on
**outline-vs-background** contrast where the subs actually sit — NOT outline-vs-white-fill.
A light outline (Shizuku, Saki, Len…) vanishes on a bright background.

This samples the real video under each used character style's on-screen region and reports
the WCAG contrast of that style's outline against the brightest background it sits over. Use
it to decide whether an episode needs a per-episode outline override (see the "Readability
override for bright backgrounds" note in subtitle_review_guide.md).

Usage:
    uv run --with pillow --with numpy python3 scripts/check_outline_contrast.py \
        "projects/Project Sekai/<event>/<name>_translated.ass" \
        "projects/Project Sekai/<event>/<name>.mkv" [--frames 10] [--flag 1.5]
"""

from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

POS_RE = re.compile(r"\\pos\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)")


def _lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _lum(rgb):  # rgb float HxWx3 (0-255) -> relative luminance 0-1
    r, g, b = _lin(rgb[..., 0]), _lin(rgb[..., 1]), _lin(rgb[..., 2])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _lum_hex_ass(ass_colour):  # &H00BBGGRR -> luminance 0-1
    h = ass_colour.replace("&H", "").replace("&", "").zfill(8)
    b, g, r = int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16)
    return float(_lum(np.array([[[r, g, b]]], float))[0, 0])


def _contrast(a, b):
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def _secs(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def _parse(ass_path):
    styles, play = {}, (1920, 1080)
    fmt = None
    dialogues = []  # (start_sec, style, pos_or_None)
    for ln in Path(ass_path).read_text(encoding="utf-8", errors="replace").split("\n"):
        s = ln.lstrip("﻿")
        if s.startswith("PlayResX:"):
            play = (int(s.split(":", 1)[1]), play[1])
        elif s.startswith("PlayResY:"):
            play = (play[0], int(s.split(":", 1)[1]))
        elif s.startswith("Format:") and "Alignment" in s:
            fmt = [f.strip() for f in s.split(":", 1)[1].split(",")]
        elif s.startswith("Style:") and fmt:
            v = dict(zip(fmt, [x.strip() for x in s.split(":", 1)[1].split(",")]))
            styles[v["Name"]] = {
                "outline": v["OutlineColour"],
                "align": int(v["Alignment"]),
                "ml": int(v["MarginL"]), "mr": int(v["MarginR"]), "mv": int(v["MarginV"]),
                "fs": float(v["Fontsize"]),
            }
        elif s.startswith("Dialogue:"):
            p = s.split(":", 1)[1].split(",", 9)
            st, text = p[3].strip(), p[9]
            pm = POS_RE.search(text)
            pos = (float(pm.group(1)), float(pm.group(2))) if pm else None
            dialogues.append((_secs(p[1].strip()), st, pos))
    return styles, play, dialogues


def _band(style, pos, W, H):
    """Return (y0, y1, x0, x1) pixel band where this line's text sits."""
    fs = style["fs"]
    h = int(fs * 1.2)
    if pos:
        x, y = pos
        al = style["align"]
        # vertical anchor from alignment (7-9 top, 4-6 mid, 1-3 bottom)
        if al in (7, 8, 9):
            y0 = y
        elif al in (4, 5, 6):
            y0 = y - h / 2
        else:
            y0 = y - h
        return (int(max(0, y0)), int(min(H, y0 + h)),
                int(max(0, x - 500)), int(min(W, x + 500)))
    al = style["align"]
    if al in (1, 2, 3):       # bottom
        y1 = H - style["mv"]; y0 = y1 - h
    elif al in (7, 8, 9):     # top
        y0 = style["mv"]; y1 = y0 + h
    else:                     # middle
        y0 = H / 2 - h / 2; y1 = y0 + h
    return (int(max(0, y0)), int(min(H, y1)), style["ml"], W - style["mr"])


def _frame(video, ts):
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{ts:.2f}", "-i", str(video),
         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
        capture_output=True)
    if not r.stdout:
        return None
    return np.asarray(Image.open(io.BytesIO(r.stdout)).convert("RGB"), float)


def main() -> int:
    ap = argparse.ArgumentParser(description="Measure outline-vs-background contrast per character style.")
    ap.add_argument("ass", type=Path)
    ap.add_argument("video", type=Path)
    ap.add_argument("--frames", type=int, default=10, help="sample frames per style (default 10)")
    ap.add_argument("--flag", type=float, default=1.5, help="flag styles below this contrast (default 1.5)")
    args = ap.parse_args()

    styles, (W, H), dialogues = _parse(args.ass)
    # only styles actually used by dialogue, and skip Default / TL-note / non-character
    used = {}
    for start, st, pos in dialogues:
        if st in ("Default",) or st.startswith("DefaultOnibe"):
            continue
        if st not in styles:
            continue
        used.setdefault(st, []).append((start, pos))
    if not used:
        print("No character-style dialogue found.")
        return 0

    white = _lum(np.array([[[255, 255, 255]]], float))[0, 0]
    print(f"{args.ass.name}  ({W}x{H})")
    # readability = max(white-fill/bg, outline/bg): the text is legible if EITHER the fill
    # or the outline separates from the background. A light outline only matters when the
    # white fill also fails to separate (i.e. a bright background).
    print(f"{'style':22} {'outline':11} {'worst bg':>8} {'fill/bg':>8} {'outline/bg':>11} {'legible':>8}")
    print("-" * 74)
    worst_any = []
    for st in sorted(used):
        lines = used[st]
        step = max(1, len(lines) // args.frames)
        sample = lines[::step][: args.frames]
        outL = _lum_hex_ass(styles[st]["outline"])
        brights = []
        for start, pos in sample:
            f = _frame(args.video, start + 0.4)
            if f is None:
                continue
            y0, y1, x0, x1 = _band(styles[st], pos, W, H)
            if y1 <= y0 or x1 <= x0:
                continue
            brights.append(float(np.percentile(_lum(f[y0:y1, x0:x1]), 90)))
        if not brights:
            continue
        bg = max(brights)
        c_out = _contrast(outL, bg)
        c_white = _contrast(white, bg)
        legible = max(c_out, c_white)          # the operative readability metric
        flag = "  <-- LOW" if legible < args.flag else ""
        print(f"{st:22} {styles[st]['outline']:11} {bg:8.3f} {c_white:7.2f}x {c_out:10.2f}x {legible:7.2f}x{flag}")
        worst_any.append((legible, st))
    if worst_any:
        lo = min(worst_any)
        print(f"\nworst legibility: {lo[1]} at {lo[0]:.2f}x"
              f"{'  -> consider a per-episode override' if lo[0] < args.flag else '  -> ok'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
