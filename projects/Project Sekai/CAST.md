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

**This is an asset index, not a cast list.** It maps a VA to their photo file and nothing
else. Names, kanji, and which character they voice live in the unit profiles — see
[Where cast data lives](#where-cast-data-lives) below. Deliberately no kanji column here.

| VA | Asset |
| --- | --- |
| Rina Honnizumi | `rina_honnizumi.webp` |
| Minori Suzuki | `minori_suzuki.webp` |
| Rui Tanabe | `rui_tanabe.webp` |

## Where cast data lives

Three layers, only one of which is authoritative:

| Layer | Holds | Authority |
| --- | --- | --- |
| `autosub/profiles/local/proseka/*.toml` | VA name + kanji, character, personality, `[replacements]` vocabulary | **Source of truth.** The only copy that changes output: it feeds the translation prompt and Chirp 3 TranscriptNormalization |
| `Project Sekai/profiles/*.md` | Same cast, plus speaking style, greetings, relationships | Human reference. Derived — must follow the `.toml` |
| `Project Sekai/CAST.md` (this file) | VA → photo filename | Asset index only |

**When you correct a VA's kanji, fix the `.toml` first.** A correction that lands only in
the `.md` changes nothing about the output: the wrong reading keeps going to the transcriber
and the translator. That has already happened once — two fabricated readings (吉岡真優,
澄利冴那) were corrected in `mmj.md`/`vbs.md` while the `.toml` kept feeding the bad kanji to
the pipeline until it was caught in an audit.

**Do not write VA kanji from memory.** Three fabricated readings have reached live profiles
so far. Verify against the Project Sekai wiki or an existing `.toml` before adding one.

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
