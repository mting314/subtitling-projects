# Subtitling Projects

Project files for Japanese-to-English fan subtitle translations. This repo tracks subtitle files, transcripts, speaker maps, and translation outputs. The tooling lives in `mting314/autosub`.

## Projects

- **Project Sekai** — AfterTalk streams, anniversary videos, event content, and the Sekaraji radio show
- **Lieraji** — Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast

Projects are grouped by **franchise**, then by show type:

```
projects/
  Project Sekai/
    official_cast_photos/   shared VA press photos, given_family.webp
    character_art/          shared sekai.best art, named by character
    profiles/
    Aftertalk/     11 AfterTalk streams
    Events/        fan meetings, anniversary videos, one-offs
    Sekaraji/      Sekaraji radio show, by episode
  Lieraji/
    official_cast_photos/   Liella! press photos
    assets/                 cropped avatars + CAST.md
    Episode NNN/
  assets/fonts/    LATO-EXTRABOLD.TTF (one copy, shared by all shows)
```

**Shared assets resolve by walking up.** Anything reused across events — VA photos,
character art, the Lato font — lives once at the franchise level, not copied into each
event folder. `scripts/generate_overlays.py` searches from the event folder up to the repo
root, so a popup's `source` can be a bare filename like `minori_suzuki.webp`. A local file
always shadows the shared one.

**Asset filenames follow each franchise's own name order.** ProSeka uses **given_family**
(`minori_suzuki.webp`), matching the Western order this repo uses in subtitles. Lieraji uses
**family_given** (`date_sayuri.png`) because it follows the romanization printed on the
official Liella! cast page. Both are correct for their show — don't "fix" one to match the
other.

**Cast data itself is not stored here.** VA names, kanji, and character assignments live in
the autosub repo's `profiles/proseka/*.toml`, which is the only copy that reaches the
transcriber and translator; `Project Sekai/profiles/*.md` are derived reference tables. When
a VA's kanji is wrong, correct the `.toml` first — see `profiles/proseka/README.md` in
autosub. A fix applied only to the `.md` changes nothing about the output, which has already
happened once.

## Workflow

Each subtitled video moves through these stages:

1. **Generate** — set up the project (folder, `notes.md`, video download) and run the autosub pipeline (transcribe → format → translate → postprocess) to produce `<name>_translated.ass`. New-project setup steps are in [`aftertalk_project_setup.md`](aftertalk_project_setup.md); tooling lives in the [autosub](https://github.com/mting314/autosub) repo.
2. **QC review** — human pass over `<name>_translated.ass` for consistency, grammar, spelling, and style. Follow [`subtitle_review_guide.md`](subtitle_review_guide.md).
3. **Hardsub + trim** — burn the reviewed subs into the video and trim to the subbed portion with `scripts/hardsub_trim.sh` (see [Post-Pipeline: Hardsub + Trim](#post-pipeline-hardsub--trim)).
4. **Publish** — write the YouTube title + description in `notes.md` and upload the hardsubbed video to YouTube with `scripts/youtube_upload.py` (see [YouTube Upload & Blurbs](#youtube-upload--blurbs)).

## Tooling

The transcription and translation pipeline is in a separate repo: [mting314/autosub](https://github.com/mting314/autosub). The legacy pipeline scripts are preserved on the `ai-sub` branch of this repo.

Local finishing/utility scripts live in [`scripts/`](scripts/) (run from the repo root) — see [`scripts/README.md`](scripts/README.md) for the index. Reference guides (`subtitle_review_guide.md`, `aftertalk_project_setup.md`, `snippets.md`) stay at the repo root.

## File Types

| Extension | Purpose |
|-----------|---------|
| `.ass` | Subtitle files (Aegisub / Advanced SubStation Alpha) |
| `.json` | Transcripts from speech-to-text |
| `.toml` | Speaker maps (speaker_map.toml, speaker_assignments.toml) |
| `.log` | Autosub pipeline logs |
| `_logs/` | Structured per-chunk translation logs |
| `.md` | Translation references with character context and glossaries |

## Style Conventions

- **Pauses**: ellipsis `...` for long pauses, comma for short, em dash for interruptions
- **Japanese terms**: italicize with ASS tags
- **Names**: Western order ("Given Family", e.g., "Mizuki Akiyama")
- **Contractions**: always use natural spoken forms
- **Song/event titles**: quoted, not italicized
- **Project Sekai terms**: "AfterTalk" (capital T), "AfterLive" (capital L), "ProSeka" (capital S)

## QC Review

Before hardsubbing, do a human-pass review of `<name>_translated.ass`. The full checklist
is in **[`subtitle_review_guide.md`](subtitle_review_guide.md)** — read it before reviewing.

In short, review across four dimensions:

- **Consistency** — grep each recurring term (titles, song names, character names + honorifics, stylized names) and enforce one canonical form. See the Project Sekai glossary in the guide.
- **Grammar** — especially the capitalization/continuation rule (a comma-broken line → next line lowercase; a sentence-ending line → next line capitalized).
- **Spelling** — name typos and duplicated words/clauses from the STT/LLM.
- **Style** — natural casual spoken English, not academic.

Process: extract dialogue with awk (the `.ass` can be 1+ MB due to embedded `img2ass` lines), suggest edits as a table and confirm before applying, apply with a line-targeted script that dry-runs each replacement, then re-grep to verify the consistency counts.

**Positional styles (PiP / song-shift):** a layout pass, also before hardsub, so subs clear on-screen content. Run `scripts/apply_positional_styles.py` (from repo root). See the "Positional styles" section of [`subtitle_review_guide.md`](subtitle_review_guide.md).

**Line length (max 2 rows):** 3+ rows is bad practice. Detect by rendering with `scripts/detect_long_lines.py` (via `uv run --with pillow --with numpy`); fix each flagged line by splitting into two events or rewording, then re-run to confirm 0 flagged. See "Dimension 5" in [`subtitle_review_guide.md`](subtitle_review_guide.md).

**Launch workflow:** the **`aftertalk-launch`** skill (`.claude/skills/`) is the self-contained finishing guide covering positional styles, line-length QC (`scripts/detect_long_lines.py`), hardsub segment-finding (`scripts/find_segments.py`), and the YouTube title + description in one place.

## Post-Pipeline: Hardsub + Trim

After QC, burn subtitles into video and trim to the subbed portion. **Must hardsub before trimming** — trimming invalidates .ass timestamps.

### Image Popups & Overlays (FFmpeg Overlay Protocol)

For reference images, VA photos, or meme popups (e.g., Gachapin, VA cards):

1. **Never use `img2ass` bitmap drawings** (causes 1000s of lines, file bloat, and subpixel rendering lag).

2. **Add the raw source image.** Memes and one-off reference shots go in the project folder —
   commit them, they're the archival source a card is (re)built from. **VA photos instead go
   in the franchise `official_cast_photos/`** (`given_family.webp`), because the same VA
   recurs across events; reference them by bare filename.

3. **Define popups in `popups.json`** inside the project folder. **Raw burn-in is the
   default** — most popups are just "put this image on screen". The VA split card is the
   special case and must be asked for with `"type": "card"`.

   **Raw (default, most common)** — a meme, screenshot, or reference shot:
   ```json
   {
     "id": "that-damn-smile",
     "source": "that_damn_smile.jpeg",   // optional raw input; generate_overlays READS it
     "image": "that-damn-smile.png",     // what generate_overlays WRITES and hardsub BURNS
     "width": 720,                       // optional; omit to keep native size
     "start": "0:54:15.78", "end": "0:54:20.56",
     "pos": [1159, 130]                  // overlay TOP-LEFT x,y — used by hardsub_trim.py
   }
   ```

   **Card (opt-in)** — the VA photo + character art + name banner:
   ```json
   {
     "id": "minori",
     "type": "card",                     // REQUIRED for a card; without it you get a raw burn
     "source": "minori_suzuki.webp",     // bare filename; found in official_cast_photos/
     "image": "minori_card.png",         // written next to popups.json, in the event folder
     "title": "Minori Suzuki",
     "subtitle": "Voice of Ena Shinonome",
     "character": "Ena Shinonome",       // drives the fetched art + banner tint
     "color": "#ccaa88",
     "start": "00:14:12.68", "end": "00:14:16.28",
     "pos": [1380, 160]
   }
   ```

4. **Generate the overlay PNGs:** `uv run --with pillow python scripts/generate_overlays.py "<project_folder>"`.
   - **raw** (no `type`, or `"type": "raw"`): copies `source` → `image`, resized only if
     `width` is given. No banner, no network, no character metadata needed.
   - **`"type": "card"`**: VA photo (`source`, left) + character art (right, fetched from
     sekai.best into the shared `character_art/<character>.png` and cached) + Lato banner
     → writes `image`.
   - Cross-platform: finds `LATO-EXTRABOLD.TTF` in the project folder, then the shared
     `assets/fonts/`, and `meta.json` under `~/github/sekai-story-indexer/`. No network
     needed once the character art is cached.
   - Idempotent: an entry with no `source` reads its own `image` and rewrites it unchanged.

5. **Hardsub Overlay:** `hardsub_trim.py` overlays the `image` file at `pos` for `start`–`end`
   (`overlay=x:y:enable='between(t,START,END)'`), auto-loaded from `popups.json`.

> **`source` vs `image` — the key gotcha.** `image` is what hardsub burns into the video, so it
> **must** point at the generated overlay PNG, never at an unsized raw — otherwise the full-res
> raw gets burned in. `source` is the input the overlay is built from. To rebuild from a new raw:
> set/point `source`, run `generate_overlays.py`, render-verify the PNG, commit. (Raw sources are
> archived — memes in the event folder, VA photos in the franchise `official_cast_photos/` — even
> though hardsub never reads them directly.)
>
> **Case matters.** Keep `image` byte-identical to the filename on disk. macOS is
> case-insensitive so a mismatch works locally and then fails in the Linux Docker remote.

### Migrating legacy `img2ass` projects

Older projects embedded the image **into the `.ass`** as a `\p` vector drawing (one 1px-tall
rectangle per pixel run). It renders, but a single small image balloons the file to 1MB+ and
libass re-rasterizes thousands of shapes every frame. Convert with:

```bash
# inspect first — prints id, decoded size, scale, anchor, resulting overlay pos
uv run --with pillow python3 scripts/img2ass_extract.py "projects/Project Sekai/Aftertalk/<event>/<name>_translated.ass" --dry-run

# decode to PNGs, write popups.json entries, remove the drawing lines
uv run --with pillow python3 scripts/img2ass_extract.py "projects/Project Sekai/Aftertalk/<event>/<name>_translated.ass" \
  --write-popups --strip
```

It decodes the RLE pixel runs back to a PNG and converts the ASS anchor (`\pos` + `\an`/style
Alignment) and `\fscx/\fscy` scaling into the ffmpeg overlay's **top-left** `pos`. Then:

1. If the **original source image** is still in the project folder, prefer it — point `source`
   at it and set `width` to the size the drawing rendered at (the embedded copy was usually
   downscaled, so the original is sharper). Re-run `generate_overlays.py`.
2. **Render-verify**: burn one frame with the old `.ass` and one with the new overlay and diff
   them — the changed region should match the overlay's `pos`/size.

Measured on the two migrated events: `1.3M → 72K` and `760K → 56K`.

### `scripts/hardsub_trim.py`

Python tool in `scripts/` (run from repo root). Handles single or multiple segments with parallel GPU encoding, automatic `popups.json` card overlays, smooth 0.4s video/audio fade transitions at boundaries, and seamless concatenation.

```bash
uv run python scripts/hardsub_trim.py \
  "projects/Project Sekai/Aftertalk/<event>/<name>.mkv" \
  "projects/Project Sekai/Aftertalk/<event>/<name>_translated.ass" \
  "projects/Project Sekai/Aftertalk/<event>/<name>_hardsubbed.mp4" \
  10:00 15:00  30:04 35:26  47:35 48:55  50:29 1:03:03
```

Example (Colors of Pure Sense — 2 segments, skipping story recap):
```bash
./scripts/hardsub_trim.sh \
  "projects/Project Sekai/Events/Colors of Pure Sense/Colors of Pure Sense.mkv" \
  "projects/Project Sekai/Events/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  "projects/Project Sekai/Events/Colors of Pure Sense/Colors of Pure Sense_final.mp4" \
  00:09:45 00:18:19 \
  00:33:35 00:55:30
```

**Notes:**
- Requires ffmpeg built with libass (`brew install libass`, then `brew reinstall --build-from-source ffmpeg`)
- The `ass=` filter doesn't handle spaces in filenames — the script creates a symlink to work around this
- Multiple segments are encoded in parallel, then concatenated with `-c copy` (no re-encode)
- Timestamps for each project are saved in `notes.md` within each project folder
- To auto-detect keep-segments, run `scripts/find_segments.py <translated.ass> --transcript <transcript.json> --hardsub <mkv>:<out.mp4>` — it finds gaps in the rendered timeline, classifies each (silent vs watchalong audio) against the transcript, and prints a ready-to-run `scripts/hardsub_trim.sh` command. With `--mkv`/`--hardsub` it's **fade-aware**: runs `blackdetect` near each boundary and pulls cuts clear of source fades (avoids black flashes at joins). `hardsub_trim.sh` also runs a post-render `blackdetect` and warns if any black remains.

See `snippets.md` for standalone ffmpeg commands.

## YouTube Upload & Blurbs

When writing YouTube descriptions for subtitled videos, follow this format:
1. VA name + character they voice + what the content covers
2. 1-2 sentences teasing highlights/fun moments
3. Link to original video
4. Credits/references if applicable

Example tone: casual, enthusiastic, highlights personality moments from the VAs.

### Automated YouTube Upload (`scripts/youtube_upload.py`)
After hardsubbing and writing the title/description in `notes.md`, run:
```bash
uv run --script scripts/youtube_upload.py \
  --video "projects/Project Sekai/Aftertalk/<event>/<name>_hardsubbed.mp4" \
  --notes "projects/Project Sekai/Aftertalk/<event>/notes.md"
```

## Git Conventions

- `project-shortname: description` for project work
- `wip: description` for work in progress
- `project-shortname: QC` for completed/reviewed
