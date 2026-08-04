#!/usr/bin/env python3
"""Generate PNG popup cards (split VA photo + Character illustration) with English text.

Reads character image colors from sekai-story-indexer (`meta.json`) and downloads official
character card artwork from sekai.best CDN.

Popup manifest (`popups.json`) field contract
---------------------------------------------
Each entry describes one on-screen popup. Two fields drive the image, and they are
DELIBERATELY SEPARATE because two different tools read them:

  - `source`  — the RAW build input this script reads (a VA photo `.webp`/`.png`, or a meme
                image). Optional; if omitted, falls back to `image`, then `<id>.webp`.
  - `image`   — the FINISHED card this script WRITES and that `hardsub_trim.py` overlays into
                the video at burn time. This must always point at the generated card
                (`<Id>_card.png`), never at the raw — otherwise hardsub burns the full-res raw.

  - `type`    — OMIT for a plain raw burn-in (the default and the common case: memes,
                reference shots, screenshots). Set `"type": "card"` to build the VA split
                card (VA photo left + character art right + name banner). `"type": "raw"`
                is still accepted and means the same as omitting it.
  - `width`   — raw only, optional. Resize the overlay to this width; omit to keep the
                source's native size.
  - `id`      — used to name the downloaded character art (`<id>_art.png`).
  - `character`/`title`/`subtitle`/`color` — card only: banner text + right-half tint.
  - `start`/`end`/`pos` — consumed by hardsub_trim.py, ignored here.

Re-running is safe: an entry with no `source` reads its own `image` (the card) and rewrites it
unchanged. Add a `source` to (re)build a card from its raw.

Usage:
    uv run --with pillow python scripts/generate_overlays.py "projects/projects/Project Sekai/<event>"
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Card width in px. Split cards are this wide; raw popups are resized to it so every
# overlay reads at a consistent on-screen size.
CARD_W = 480

# meta.json (character colors) — first existing path wins; override with --meta.
INDEXER_META_CANDIDATES = [
    Path.home() / "github" / "sekai-story-indexer" / "webapp" / "static" / "meta.json",
    Path("C:/Users/Michael/Documents/GitHub/sekai-story-indexer/webapp/static/meta.json"),
]

# Lato ExtraBold (subtitle font) — first existing path wins. The project dir is checked
# first (each event folder ships its own LATO-EXTRABOLD.TTF), so this runs cross-platform.
FONT_CANDIDATES = [
    Path("C:/Users/Michael/AppData/Local/Microsoft/Windows/Fonts/LATO-EXTRABOLD.TTF"),
]

# Character ID mapping for Project Sekai
CHARA_ID_MAP = {
    "ichika hoshino": 1, "saki tenma": 2, "honami mochizuki": 3, "shiho hinomori": 4,
    "minori hanasato": 5, "haruka kiritani": 6, "airi momoi": 7, "shizuku hinomori": 8,
    "kohane azusawa": 9, "an shiraishi": 10, "akito shinonome": 11, "toya aoyagi": 12,
    "tsukasa tenma": 13, "emu otori": 14, "nene kusanagi": 15, "rui kamishiro": 16,
    "kanade yoisaki": 17, "mafuyu asahina": 18, "ena shinonome": 19, "mizuki akiyama": 20,
    "hatsune miku": 21, "kagamine rin": 22, "kagamine len": 23, "megurine luka": 24,
    "meiko": 25, "kaito": 26
}


def resolve_meta_path(override: Path | None) -> Path | None:
    """Pick the meta.json path: explicit override, else first existing candidate."""
    if override and override.exists():
        return override
    for cand in INDEXER_META_CANDIDATES:
        if cand.exists():
            return cand
    return override  # may be None / non-existent; load_character_colors handles that


def resolve_font_path(project_dir: Path) -> Path | None:
    """Find LATO-EXTRABOLD.TTF: project dir first (shipped per event), then known installs."""
    for cand in [project_dir / "LATO-EXTRABOLD.TTF", *FONT_CANDIDATES]:
        if cand.exists():
            return cand
    return None


def load_character_colors(meta_path: Path | None) -> dict[str, str]:
    """Load character hex colors from sekai-story-indexer meta.json."""
    if not meta_path or not meta_path.exists():
        return {}
    with open(meta_path, encoding="utf-8") as f:
        data = json.load(f)
    return {
        info["en"].lower(): info["color"]
        for info in data.get("characters", {}).values()
        if "en" in info and "color" in info
    }


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    hex_str = hex_str.lstrip("#")
    return tuple(int(hex_str[i : i + 2], 16) for i in (0, 2, 4))


def load_fonts(font_path: Path | None) -> tuple[ImageFont.FreeTypeFont, ImageFont.FreeTypeFont]:
    """Load (title, subtitle) fonts, falling back gracefully when Lato is unavailable."""
    try:
        if font_path and font_path.exists():
            return (ImageFont.truetype(str(font_path), 32), ImageFont.truetype(str(font_path), 22))
        return (ImageFont.truetype("arialbd.ttf", 32), ImageFont.truetype("arial.ttf", 22))
    except Exception:
        default = ImageFont.load_default()
        return (default, default)


def fetch_character_artwork(chara_name_en: str, dst_path: Path) -> bool:
    """Download character card illustration from sekai.best CDN (skips if already present)."""
    if dst_path.exists() and dst_path.stat().st_size > 1000:
        return True
    cid = CHARA_ID_MAP.get(chara_name_en.lower())
    if not cid:
        return False
    try:
        url = "https://sekai-world.github.io/sekai-master-db-diff/cards.json"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        cards = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
        chara_cards = [c for c in cards if c.get("characterId") == cid]
        if not chara_cards:
            return False
        asset_name = chara_cards[0].get("assetbundleName")
        cdn_url = f"https://storage.sekai.best/sekai-jp-assets/character/member/{asset_name}/card_normal.png"
        img_req = urllib.request.Request(cdn_url, headers={"User-Agent": "Mozilla/5.0"})
        img_bytes = urllib.request.urlopen(img_req).read()
        dst_path.write_bytes(img_bytes)
        print(f"Downloaded character artwork for {chara_name_en} -> {dst_path.name}")
        return True
    except Exception as exc:
        print(f"Failed to fetch character artwork for {chara_name_en}: {exc}", file=sys.stderr)
        return False


def save_raw_overlay(source_path: Path, output_path: Path, width: int | None = None) -> None:
    """Prepare a raw (no-banner) overlay: convert to RGBA, optionally resize to `width`.

    With no `width` the source is kept at its native size — a raw burn-in is usually just
    "put this image on screen", so we don't impose the card geometry on it.
    """
    img = Image.open(source_path).convert("RGBA")
    if width and img.width != width:
        h = round(img.height * width / img.width)
        img = img.resize((width, h), Image.LANCZOS)
    img.save(output_path, "PNG")
    print(f"Prepared raw image overlay: {output_path.name} ({img.width}x{img.height})")


def create_split_card(
    va_img_path: Path,
    chara_img_path: Path,
    title_text: str,
    subtitle_text: str,
    chara_color_hex: str,
    output_path: Path,
    font_path: Path | None = None,
    total_w: int = CARD_W,
    img_h: int = 340,
):
    """Generate a split-screen VA photo (left) + Character Illustration (right) card with centered English text."""
    half_w = total_w // 2

    # Left half: VA photo
    va_raw = Image.open(va_img_path).convert("RGBA")
    aspect_va = va_raw.width / va_raw.height
    scaled_va_w = int(img_h * aspect_va)
    if scaled_va_w < half_w:
        scaled_va_h = int(half_w / aspect_va)
        va_scaled = va_raw.resize((half_w, scaled_va_h), Image.LANCZOS)
        y0 = (scaled_va_h - img_h) // 2
        left_half = va_scaled.crop((0, y0, half_w, y0 + img_h))
    else:
        va_scaled = va_raw.resize((scaled_va_w, img_h), Image.LANCZOS)
        x0 = (scaled_va_w - half_w) // 2
        left_half = va_scaled.crop((x0, 0, x0 + half_w, img_h))

    # Right half: Character artwork on character color background
    chara_rgb = hex_to_rgb(chara_color_hex if chara_color_hex else "#ddaacc")
    right_bg = Image.new("RGBA", (half_w, img_h), (chara_rgb[0], chara_rgb[1], chara_rgb[2], 255))

    chara_raw = Image.open(chara_img_path).convert("RGBA")
    aspect_ch = chara_raw.width / chara_raw.height
    scaled_ch_w = int(img_h * aspect_ch)
    if scaled_ch_w < half_w:
        scaled_ch_h = int(half_w / aspect_ch)
        chara_scaled = chara_raw.resize((half_w, scaled_ch_h), Image.LANCZOS)
        y0 = (scaled_ch_h - img_h) // 2
        right_art = chara_scaled.crop((0, y0, half_w, y0 + img_h))
    else:
        chara_scaled = chara_raw.resize((scaled_ch_w, img_h), Image.LANCZOS)
        x0 = (scaled_ch_w - half_w) // 2
        right_art = chara_scaled.crop((x0, 0, x0 + half_w, img_h))

    right_bg.paste(right_art, (0, 0), mask=right_art if right_art.mode == "RGBA" else None)

    # Unrounded split image container (flush with bottom banner)
    img_container = Image.new("RGBA", (total_w, img_h), (0, 0, 0, 0))
    img_container.paste(left_half, (0, 0))
    img_container.paste(right_bg, (half_w, 0))

    # Fonts (Lato ExtraBold, resolved cross-platform)
    title_font, sub_font = load_fonts(font_path)

    t_bbox = title_font.getbbox(title_text)
    s_bbox = sub_font.getbbox(subtitle_text)

    t_w = t_bbox[2] - t_bbox[0]
    t_h = t_bbox[3] - t_bbox[1]
    s_w = s_bbox[2] - s_bbox[0]
    s_h = s_bbox[3] - s_bbox[1]

    line_spacing = 12
    padding_v = 16
    text_block_h = t_h + line_spacing + s_h
    banner_h = text_block_h + padding_v * 2

    card_h = img_h + banner_h

    # Combine split image container and text banner flush (0 gap)
    card_raw = Image.new("RGBA", (total_w, card_h), (0, 0, 0, 0))
    card_raw.paste(img_container, (0, 0))

    # Banner background filled with FULL character image color (#8888cc / #ccaa88)
    banner = Image.new("RGBA", (total_w, banner_h), (chara_rgb[0], chara_rgb[1], chara_rgb[2], 255))
    draw_b = ImageDraw.Draw(banner)

    # 100% Exact Vertical and Horizontal Centering
    start_y = (banner_h - text_block_h) // 2 - 2
    t_y = start_y
    s_y = t_y + t_h + line_spacing

    t_x = (total_w - t_w) // 2
    s_x = (total_w - s_w) // 2

    # Text color: dark navy/slate for high contrast readability
    dark_text_color = (25, 25, 35, 255)
    sub_text_color = (15, 35, 75, 255)

    draw_b.text((t_x, t_y), title_text, font=title_font, fill=dark_text_color)
    draw_b.text((s_x, s_y), subtitle_text, font=sub_font, fill=sub_text_color)

    card_raw.paste(banner, (0, img_h))

    # Single outer rounded rectangle mask around the ENTIRE card
    radius = 20
    mask = Image.new("L", (total_w, card_h), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (total_w, card_h)], radius=radius, fill=255)

    final_card = Image.new("RGBA", (total_w, card_h), (0, 0, 0, 0))
    final_card.paste(card_raw, (0, 0), mask=mask)
    final_card.save(output_path, "PNG")
    print(f"Generated large centered Lato card: {output_path.name} ({total_w}x{card_h}) color={chara_color_hex}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate split-screen popup cards with English text.")
    ap.add_argument("project_dir", type=Path, help="path to project directory")
    ap.add_argument("--meta", type=Path, default=None, help="path to sekai-story-indexer meta.json")
    args = ap.parse_args()

    proj_dir = args.project_dir
    manifest_path = proj_dir / "popups.json"
    if not manifest_path.exists():
        print(f"Error: manifest {manifest_path} not found", file=sys.stderr)
        return 1

    font_path = resolve_font_path(proj_dir)
    if font_path:
        print(f"Using font: {font_path}")
    else:
        print("Lato font not found; falling back to Arial/default", file=sys.stderr)

    char_colors = load_character_colors(resolve_meta_path(args.meta))

    with open(manifest_path, encoding="utf-8") as f:
        popups = json.load(f)

    for item in popups:
        # `source` is the raw build input; fall back to `image` (frozen re-run), then <id>.webp.
        img_name = item.get("source") or item.get("image") or f"{item.get('id')}.webp"
        va_img_path = proj_dir / img_name
        # `image` is the finished overlay that hardsub burns — write exactly there.
        card_out = proj_dir / item.get("image", f"{item.get('id', 'card')}_card.png")

        if not va_img_path.exists():
            print(f"Skip {item.get('id')}: source image {va_img_path.name} not found", file=sys.stderr)
            continue

        # RAW IS THE DEFAULT. Most popups are just "burn this image on screen" (memes,
        # reference shots, screenshots). The VA split card is the special case and must be
        # requested with "type": "card". Legacy "type": "raw" still works (it's the default).
        if item.get("type") != "card":
            save_raw_overlay(va_img_path, card_out, width=item.get("width"))
            continue

        chara_en = item.get("character", "")
        chara_art_path = proj_dir / f"{item.get('id', 'chara')}_art.png"

        fetch_character_artwork(chara_en, chara_art_path)

        color = item.get("color") or char_colors.get(chara_en.lower(), "#ddaacc")
        title_str = item.get("title", chara_en)
        subtitle_str = item.get("subtitle", f"Voice of {chara_en}")

        create_split_card(
            va_img_path,
            chara_art_path if chara_art_path.exists() else va_img_path,
            title_str,
            subtitle_str,
            color,
            card_out,
            font_path=font_path,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
