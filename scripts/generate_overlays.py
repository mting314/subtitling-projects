#!/usr/bin/env python3
"""Generate PNG popup cards (split VA photo + Character illustration) with English text.

Reads character image colors from sekai-story-indexer (`meta.json`) and downloads official
character card artwork from sekai.best CDN.

Usage:
    uv run --with pillow python scripts/generate_overlays.py "projects/projects/Project Sekai/We Escape to Survive Aftertalk"
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DEFAULT_INDEXER_META = Path("C:/Users/Michael/Documents/GitHub/sekai-story-indexer/webapp/static/meta.json")

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


def load_character_colors(meta_path: Path = DEFAULT_INDEXER_META) -> dict[str, str]:
    """Load character hex colors from sekai-story-indexer meta.json."""
    if not meta_path.exists():
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


def fetch_character_artwork(chara_name_en: str, dst_path: Path) -> bool:
    """Download character card illustration from sekai.best CDN."""
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


def create_split_card(
    va_img_path: Path,
    chara_img_path: Path,
    title_text: str,
    subtitle_text: str,
    chara_color_hex: str,
    output_path: Path,
    total_w: int = 480,
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

    # Fonts (Using subtitle font: Lato ExtraBold)
    lato_font_path = Path("C:/Users/Michael/AppData/Local/Microsoft/Windows/Fonts/LATO-EXTRABOLD.TTF")
    try:
        if lato_font_path.exists():
            title_font = ImageFont.truetype(str(lato_font_path), 32)
            sub_font = ImageFont.truetype(str(lato_font_path), 22)
        else:
            title_font = ImageFont.truetype("arialbd.ttf", 32)
            sub_font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

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
    ap.add_argument("--meta", type=Path, default=DEFAULT_INDEXER_META, help="path to sekai-story-indexer meta.json")
    args = ap.parse_args()

    proj_dir = args.project_dir
    manifest_path = proj_dir / "popups.json"
    if not manifest_path.exists():
        print(f"Error: manifest {manifest_path} not found", file=sys.stderr)
        return 1

    char_colors = load_character_colors(args.meta)

    with open(manifest_path, encoding="utf-8") as f:
        popups = json.load(f)

    for item in popups:
        img_name = item.get("image") or f"{item.get('name')}.webp"
        va_img_path = proj_dir / img_name
        card_out = proj_dir / f"{item.get('id', 'card')}_card.png"

        # If raw image popup (no card banner)
        if item.get("type") == "raw":
            if va_img_path.exists():
                # Save as clean PNG for overlay
                img = Image.open(va_img_path).convert("RGBA")
                img.save(card_out, "PNG")
                print(f"Prepared raw image overlay: {card_out.name}")
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
            card_out
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
