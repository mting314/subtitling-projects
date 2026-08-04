#!/usr/bin/env python3
"""Migrate legacy `img2ass` \\p vector drawings out of an .ass into image overlays.

Background
----------
The old flow embedded a bitmap into the subtitle file as an ASS `\\p1` vector drawing:
each pixel run became a 1px-tall rectangle (`{\\c&HBBGGRR&}m 0 0 l 0 1 W 1 W 0`) that
flows like a glyph, with `\\N` starting the next pixel row. It works, but a single small
image becomes hundreds of thousands of characters, bloating the .ass to 1MB+, and libass
has to re-rasterize thousands of shapes every frame (subpixel rendering lag).

The current flow keeps the .ass clean and burns images in with an ffmpeg `overlay` filter,
driven by `popups.json` (see the root CLAUDE.md "Image Popups & Overlays").

This script does the migration: it decodes each embedded drawing back to a PNG, works out
the equivalent ffmpeg overlay position (accounting for `\\fscx/\\fscy` scaling and the
ASS anchor), writes `popups.json` entries, and can strip the drawing lines from the .ass.

Usage:
    # inspect what's embedded (no writes)
    python3 scripts/img2ass_extract.py "<project>/<name>_translated.ass" --dry-run

    # decode to PNGs + write popups.json + remove the drawing lines
    python3 scripts/img2ass_extract.py "<project>/<name>_translated.ass" --write-popups --strip
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RUN_RE = re.compile(r"\\c&H([0-9A-Fa-f]{6})&[^m]*m 0 0 l 0 1 (\d+) 1 \d+ 0")
POS_RE = re.compile(r"\\pos\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)")
AN_RE = re.compile(r"\\an(\d)")
FSCX_RE = re.compile(r"\\fscx([\d.]+)")
FSCY_RE = re.compile(r"\\fscy([\d.]+)")
SLUG_RE = re.compile(r"[^a-z0-9]+")

EVENT_FIELDS = 10  # Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text


def parse_styles(lines: list[str]) -> dict[str, int]:
    """Map style name -> Alignment (for anchor when a line has no \\an override)."""
    fmt: list[str] = []
    out: dict[str, int] = {}
    for ln in lines:
        if ln.startswith("Format:") and "Alignment" in ln:
            fmt = [f.strip() for f in ln.split(":", 1)[1].split(",")]
        elif ln.startswith("Style:") and fmt:
            vals = [v.strip() for v in ln.split(":", 1)[1].split(",")]
            row = dict(zip(fmt, vals))
            try:
                out[row["Name"]] = int(row["Alignment"])
            except (KeyError, ValueError):
                pass
    return out


def decode_drawing(text: str) -> tuple[list[list[tuple[int, int, int]]], int, int]:
    """Decode the RLE pixel runs into rows of RGB tuples. Returns (rows, width, height)."""
    rows: list[list[tuple[int, int, int]]] = []
    for chunk in text.split("\\N"):
        px: list[tuple[int, int, int]] = []
        for hexcol, width in RUN_RE.findall(chunk):
            # ASS colour literals are BGR, not RGB
            b, g, r = int(hexcol[0:2], 16), int(hexcol[2:4], 16), int(hexcol[4:6], 16)
            px.extend([(r, g, b)] * int(width))
        if px:
            rows.append(px)
    if not rows:
        return [], 0, 0
    width = max(len(r) for r in rows)
    for r in rows:  # pad ragged rows so the image is rectangular
        if len(r) < width:
            r.extend([r[-1]] * (width - len(r)))
    return rows, width, len(rows)


def anchor_topleft(px: float, py: float, w: float, h: float, an: int) -> tuple[int, int]:
    """Convert an ASS anchored position to the overlay's top-left corner."""
    if an in (1, 4, 7):
        x = px
    elif an in (3, 6, 9):
        x = px - w
    else:
        x = px - w / 2
    if an in (7, 8, 9):
        y = py
    elif an in (1, 2, 3):
        y = py - h
    else:
        y = py - h / 2
    return int(round(x)), int(round(y))


def slugify(s: str, fallback: str) -> str:
    s = SLUG_RE.sub("-", s.strip().lower()).strip("-")
    return s or fallback


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract img2ass \\p drawings into PNG overlays.")
    ap.add_argument("ass", type=Path)
    ap.add_argument("--outdir", type=Path, default=None, help="where to write PNGs (default: alongside the .ass)")
    ap.add_argument("--write-popups", action="store_true", help="create/merge popups.json")
    ap.add_argument("--strip", action="store_true", help="remove the drawing Dialogue lines from the .ass")
    ap.add_argument("--min-runs", type=int, default=50, help="min pixel runs for a line to count as a drawing")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.ass.exists():
        print(f"Error: {args.ass} not found", file=sys.stderr)
        return 1
    outdir = args.outdir or args.ass.parent
    lines = args.ass.read_text(encoding="utf-8").split("\n")
    styles = parse_styles(lines)

    try:
        from PIL import Image
    except ImportError:
        print("Pillow required: run via `uv run --with pillow python3 ...`", file=sys.stderr)
        return 1

    found, drop_idx = [], []
    for i, ln in enumerate(lines):
        if not ln.startswith("Dialogue:") or "\\p1" not in ln:
            continue
        parts = ln.split(":", 1)[1].split(",", EVENT_FIELDS - 1)
        if len(parts) < EVENT_FIELDS:
            continue
        start, end, style, effect, text = parts[1], parts[2], parts[3], parts[8], parts[9]
        if len(RUN_RE.findall(text)) < args.min_runs:
            continue

        rows, w, h = decode_drawing(text)
        if not rows:
            continue

        scale_x = float(m.group(1)) / 100 if (m := FSCX_RE.search(text)) else 1.0
        scale_y = float(m.group(1)) / 100 if (m := FSCY_RE.search(text)) else 1.0
        rw, rh = w * scale_x, h * scale_y

        pm = POS_RE.search(text)
        if pm:
            px, py = float(pm.group(1)), float(pm.group(2))
        else:
            px, py = 960.0, 540.0  # no \pos: fall back to frame centre
        an = int(m.group(1)) if (m := AN_RE.search(text)) else styles.get(style.strip(), 2)
        x, y = anchor_topleft(px, py, rw, rh, an)

        eff = effect.strip()
        ident = slugify(eff.split("img2ass:", 1)[-1] if eff else "", f"img{len(found) + 1}")
        # several cues can share an effect tag (e.g. two "human" reaction shots) — keep ids unique
        if any(e["id"] == ident or e["id"].startswith(f"{ident}-") for e in found):
            ident = f"{ident}-{sum(1 for e in found if e['id'].split('-')[0] == ident.split('-')[0]) + 1}"
        png = outdir / f"{ident}.png"

        if not args.dry_run:
            img = Image.new("RGB", (w, h))
            img.putdata([p for row in rows for p in row])
            if (scale_x, scale_y) != (1.0, 1.0):
                img = img.resize((max(1, int(rw)), max(1, int(rh))), Image.LANCZOS)
            img.save(png, "PNG")

        found.append({
            "id": ident, "image": png.name,
            "start": start.strip(), "end": end.strip(),
            "pos": [x, y],
        })
        drop_idx.append(i)
        print(f"line {i + 1}: {ident}  {w}x{h}"
              f"{f' -> {int(rw)}x{int(rh)} (x{scale_x:g})' if scale_x != 1 else ''}"
              f"  an={an}  pos=({x},{y})  {start.strip()}-{end.strip()}")

    if not found:
        print("No img2ass drawings found.")
        return 0

    if args.dry_run:
        print(f"\n[dry-run] would write {len(found)} PNG(s)"
              f"{', popups.json' if args.write_popups else ''}"
              f"{', and strip ' + str(len(drop_idx)) + ' line(s)' if args.strip else ''}")
        return 0

    if args.write_popups:
        pj = outdir / "popups.json"
        existing = json.loads(pj.read_text(encoding="utf-8")) if pj.exists() else []
        have = {e.get("id") for e in existing}
        merged = existing + [e for e in found if e["id"] not in have]
        pj.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"popups.json: {len(merged)} entr{'y' if len(merged) == 1 else 'ies'}")

    if args.strip:
        for i in reversed(drop_idx):
            del lines[i]
        args.ass.write_text("\n".join(lines), encoding="utf-8")
        print(f"stripped {len(drop_idx)} drawing line(s) from {args.ass.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
