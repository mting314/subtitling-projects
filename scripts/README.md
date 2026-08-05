# scripts/

Local finishing + utility scripts for the subtitling workflow. **Run them from the
projects repo root** (they take/emit `projects/...` paths and, for `find_segments.py`,
print a `./scripts/hardsub_trim.sh` command). The autosub transcribe→format→translate→
postprocess pipeline lives in a separate repo ([mting314/autosub](https://github.com/mting314/autosub)).

The `aftertalk-launch` skill (`.claude/skills/aftertalk-launch/`) drives most of these;
`subtitle_review_guide.md` (repo root) documents the QC-time ones in depth.

| Script | Purpose | Stage |
|---|---|---|
| `apply_positional_styles.py` | Copy Alignment + margins from a reference style onto PiP / song-shift lines (deterministic; caller resolves which styles play which role). | QC / layout |
| `detect_long_lines.py` | Render each Dialogue line under its real style and flag any wrapping to 3+ rows. Needs `uv run --with pillow --with numpy`. | QC / layout |
| `check_outline_contrast.py` | Measure each character style's **outline-vs-background** contrast against the real video (readability = max(white-fill/bg, outline/bg)). Flags episodes where a light outline washes out on a bright background, so you can apply a per-episode outline override (see "Readability override for bright backgrounds" in `subtitle_review_guide.md`). Needs `uv run --with pillow --with numpy` + ffmpeg. | QC / layout |
| `split_subtitle_line.py` | Split ONE flagged line into two events at a clause boundary, snapping the time split to a real breath (`--before`, `--transcript`). Fixes 3-row lines from `detect_long_lines.py`. | QC / layout |
| `autosplit_long_lines.py` | Batch-fix all 3-row lines: drives `detect_long_lines.py` + `split_subtitle_line.py`, picking a safe clause boundary near each midpoint. Encodes the **Netflix line-break rules** (break after punctuation / before conjunctions / before prepositions; never separate article-noun, verb-subject, prep-verb, verb-aux). Default **`dep` engine** uses a spaCy dependency parse (only breaks between sibling subtrees — the "syntactically aware segmentation" the research recommends); falls back to a **`regex`** engine if spaCy isn't installed. Defers unsafe lines to a REWORD list and audits the result. `--apply` to write. Dep engine needs: `uv run --with pillow --with numpy --with spacy --with click --with "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl"`. | QC / layout |
| `scope_segments.py` | **Pre-pipeline** keep-segment scoping from the *raw* mkv (no STT): classifies each second as standby/watchalong/talk by video layout (right-panel template + stillness), plus an audio pass that catches full-screen songs (continuous-music low-energy-rate) the panel misses on newer layouts. Emits `--start/--end` for `autosub run` + a boundary contact-sheet PNG. Needs `uv run --with opencv-python-headless --with numpy --with librosa` (librosa optional — audio pass skipped without it). Always confirm via the contact sheet. | Setup / scoping |
| `find_segments.py` | **Post-pipeline** sibling of `scope_segments.py`: finds keep-segments between watchalong gaps in the *rendered* `.ass` timeline; `--transcript` classifies each gap silent vs audio, `--hardsub` emits a ready-to-run `hardsub_trim.sh` command. | Hardsub |
| `generate_overlays.py` | Build overlay PNGs from `popups.json`. **Raw burn-in is the default** (meme/screenshot, optional `width`); `"type": "card"` opts into the VA-photo + character-art card with Lato banner. Reads each entry's `source` (raw input), writes `image` (what hardsub burns). See the `source` vs `image` contract in the root [`CLAUDE.md`](../CLAUDE.md) "Image Popups & Overlays". Needs `uv run --with pillow`. | Hardsub |
| `img2ass_extract.py` | **One-off migration** off the legacy `img2ass` flow: decodes `\p` vector drawings embedded in an `.ass` back to PNGs, converts `\pos`/`\an`/`\fscx` into ffmpeg overlay top-left coords, writes `popups.json`, and strips the drawing lines (`--write-popups --strip`, `--dry-run` to inspect). Shrinks 1MB+ files to <100K. Needs `uv run --with pillow`. | Hardsub / migration |
| `hardsub_trim.py` / `hardsub_trim.sh` | Burn subs into video and trim/concat to the kept segments (parallel encode + `-c copy` concat; blackdetect warnings). Auto-overlays `popups.json` cards (the `image` field) at each `pos`/time. Requires ffmpeg built with libass. | Hardsub |
| `fetch_event.py` | Fetch Project Sekai event story data from the sekai-world master DB + asset CDN. | Setup / reference |
| `youtube_upload.py` | Upload the hardsubbed mp4 to YouTube (PRIVATE by default), pulling title/description from `notes.md`. Self-contained: `uv run scripts/youtube_upload.py`. Needs a one-time Desktop OAuth client (`scripts/client_secret.json`, gitignored) — see the script docstring. | Publish |

## Typical order (per episode)

0. `scope_segments.py <mkv> --profile proseka/<unit>` — scope keep-segments from the raw video (setup, before the pipeline); confirm against its contact sheet, then run `autosub run` with the emitted `--start/--end`
1. `apply_positional_styles.py` — reposition PiP / song-shift subs
2. `detect_long_lines.py` → `split_subtitle_line.py` — fix 3-row lines (loop until 0 flagged)
3. `find_segments.py --transcript --hardsub …` — get the cut plan + hardsub command
3b. `generate_overlays.py "<project_folder>"` — (re)build any `popups.json` cards before hardsub
4. `./scripts/hardsub_trim.sh …` — render the final mp4
5. `youtube_upload.py --video <mp4> --notes <notes.md>` — publish to YouTube (private by default)
