# Subtitling Projects

Project files for Japanese-to-English fan subtitle translations. This repo tracks subtitle files, transcripts, speaker maps, and translation outputs. The tooling lives in `mting314/autosub`.

## Projects

- **Project Sekai** — AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** — Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** — Love Live! Superstar!! Liella! live concert content

All projects live under `projects/`, each in a subdirectory named after the content.

## Workflow

Each subtitled video moves through these stages:

1. **Generate** — set up the project (folder, `notes.md`, video download) and run the autosub pipeline (transcribe → format → translate → postprocess) to produce `<name>_translated.ass`. New-project setup steps are in [`aftertalk_project_setup.md`](aftertalk_project_setup.md); tooling lives in the [autosub](https://github.com/mting314/autosub) repo.
2. **QC review** — human pass over `<name>_translated.ass` for consistency, grammar, spelling, and style. Follow [`subtitle_review_guide.md`](subtitle_review_guide.md).
3. **Hardsub + trim** — burn the reviewed subs into the video and trim to the subbed portion with `scripts/hardsub_trim.sh` (see [Post-Pipeline: Hardsub + Trim](#post-pipeline-hardsub--trim)).
4. **Publish** — write the YouTube description ([YouTube Video Blurbs](#youtube-video-blurbs)).

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
2. **Define popups in `popups.json`** inside the project folder:
   ```json
   [
     {
       "id": "rui",
       "image": "Rui.webp",
       "title": "Tanabe Rui",
       "subtitle": "Voice of Mafuyu Yoisaki",
       "character": "Mafuyu Asahina",
       "start": "00:13:50.72",
       "end": "00:13:54.92"
     }
   ]
   ```
3. **Generate PNG Popup Cards:** Run `uv run --with pillow python scripts/generate_overlays.py <project_folder>`. This reads character image colors from `sekai-story-indexer` (`meta.json`) and generates styled card PNGs (`Rui_card.png`).
4. **Hardsub Overlay:** Apply overlays via FFmpeg `overlay=x=main_w-overlay_w-15:y=70:enable='between(t,START,END)'` synchronized directly to the dialogue line start/end timestamps.

### `scripts/hardsub_trim.sh`

Script in `scripts/` (run from repo root). Handles single or multiple segments with automatic concatenation.

```bash
# Single segment
./scripts/hardsub_trim.sh <input.mkv> <subtitle.ass> <output.mp4> <start> <end>

# Multiple segments (gaps like story recaps/songs are skipped)
./scripts/hardsub_trim.sh <input.mkv> <subtitle.ass> <output.mp4> <start1> <end1> <start2> <end2> ...
```

Example (Colors of Pure Sense — 2 segments, skipping story recap):
```bash
./scripts/hardsub_trim.sh \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense.mkv" \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_final.mp4" \
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

## YouTube Video Blurbs

When writing YouTube descriptions for subtitled videos, follow this format:
1. VA name + character they voice + what the content covers
2. 1-2 sentences teasing highlights/fun moments
3. Link to original video
4. Credits/references if applicable

Example tone: casual, enthusiastic, highlights personality moments from the VAs.

## Git Conventions

- `project-shortname: description` for project work
- `wip: description` for work in progress
- `project-shortname: QC` for completed/reviewed
