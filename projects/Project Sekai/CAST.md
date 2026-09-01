# Project Sekai cast — shared VA assets

Franchise-level assets shared by everything under `Project Sekai/` — `Aftertalk/`,
`Events/`, and `Sekaraji/`. These shows draw on the same VA pool, so a photo lives here
once instead of being copied into each event folder.

```
Project Sekai/
  official_cast_photos/   VA press photos (raw source for card popups)
  character_art/          sekai.best card illustrations, keyed by character
  CAST.md                 this file
```

## VA photos (`official_cast_photos/`)

| VA | Japanese | Voices | Asset |
| --- | --- | --- | --- |
| Rina Honnizumi | 本泉莉奈 | Shizuku Hinomori (日野森雫) | `rina_honnizumi.webp` |
| Minori Suzuki | 鈴木みのり | Ena Shinonome (東雲絵名) | `minori_suzuki.webp` |
| Rui Tanabe | 田辺留依 | Mafuyu Asahina (朝比奈まふゆ) | `rui_tanabe.webp` |

Kanji are taken from the unit profiles in `autosub/profiles/local/proseka/` (`n25.toml`,
`mmj.toml`), which were checked against the Project Sekai wiki. **Do not write VA kanji
from memory** — a past pass put two fabricated readings into live profiles. Verify against
the wiki or an existing profile before adding a row.

## Character art (`character_art/`)

Illustrations fetched from the sekai.best CDN by `scripts/generate_overlays.py`, named by
**character** (`ena_shinonome.png`), not by popup id. Keying on the character is what lets
a second event reuse a fetch instead of pulling its own copy. Present so far:
`ena_shinonome.png`, `mafuyu_asahina.png`.

## Naming convention

ProSeka assets use **given_family** (`minori_suzuki.webp`), matching the Western name order
this repo uses in subtitles (see the Style Conventions in the root `CLAUDE.md`).

This deliberately differs from `Lieraji/assets/CAST.md`, which uses **family_given**
(`date_sayuri.png`) because it follows the romanization printed on the official Liella!
cast page. Both are correct for their show — don't "fix" one to match the other.

## Adding a VA

1. Drop the press photo in `official_cast_photos/` as `given_family.webp`.
2. Add a row above, with kanji verified against a profile or the wiki.
3. Reference it from a popup's `source` by **bare filename** — `generate_overlays.py`
   walks up from the event folder to find this directory, so no relative path is needed.
