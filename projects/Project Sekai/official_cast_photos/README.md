# Official cast photos

**Source of truth:** the official ProSeka 6th Anniversary Thanks Festival page,
<https://pjsekai.sega.jp/6thanniversarythanksfestival/index.html>.

Always take new cast photos from that page. Do **not** use MyAnimeList, ANN,
agency sites, or image search: same-name voice actors get mixed up there
(this happened once with Yuki Nakashima).

## How to fetch

Images live at
`https://pjsekai.sega.jp/6thanniversarythanksfestival/assets/img/common/actor/img_<name>.webp`
(410×410 webp). Save them here as `<given>_<family>.webp` in romanized,
lowercase form (e.g. `yuki_nakashima.webp`), then point the episode's
`speaker_map.toml` `avatar` at `../../official_cast_photos/<file>`.

Each page image is a **split composite**: the VA photo is on the left half and
the character art is on the right half. Crop to the VA's face on the left half
at the overlay card's aspect ratio (~1.07:1, e.g. 205×192). Then the overlay
uses the asset as-is instead of center-cropping it, which would cut through the
face. Adjust the vertical offset per photo so the whole head is in frame.

```bash
curl -sL -A "Mozilla/5.0" -o /tmp/img_nakashima.webp \
  "https://pjsekai.sega.jp/6thanniversarythanksfestival/assets/img/common/actor/img_nakashima.webp"
.venv/bin/python3 -c 'from PIL import Image; Image.open("/tmp/img_nakashima.webp").convert("RGB").crop((0,80,205,272)).save("yuki_nakashima.webp","WEBP",quality=95)'
```

## Filename map (from the page's `alt` text)

| Page file | VA |
| --- | --- |
| `img_noguchi.webp` | 野口 瑠璃子 (Ruriko Noguchi) |
| `img_isobe.webp` | 礒部 花凜 (Karin Isobe) |
| `img_nakashima.webp` | 中島 由貴 (Yuki Nakashima) |
| `img_yoshioka.webp` | 吉岡 茉祐 (Mayu Yoshioka) |
| `img_hurihata.webp` | 降幡 愛 (Ai Furihata) |
| `img_honizumi.webp` | 本泉 莉奈 (Rina Honnizumi) |
| `img_ogura.webp` | 小倉 唯 (Yui Ogura) |
| `img_sumi.webp` | 鷲見 友美ジェナ (Tomomi Jiena Sumi) |
| `img_akina.webp` | 秋奈 (Akina) |
| `img_suzuki.webp` | 鈴木 みのり (Minori Suzuki) |
| `img_sato.webp` | 佐藤 日向 (Hinata Sato) |
| `img_machiko.webp` | Machico |
| `img_tanabe.webp` | 田辺 留依 (Rui Tanabe) |
| `img_imai.webp` | 今井 文也 (Fumiya Imai) |
| `img_toki.webp` | 土岐 隼一 (Shunichi Toki) |
| `img_kusunoki.webp` | 楠木 ともり (Tomori Kusunoki) |
| `img_hirose.webp` | 廣瀬 大介 (Daisuke Hirose) |

If a VA isn't on this page, ask before pulling a photo from anywhere else.
