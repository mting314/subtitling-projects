# Subtitling Projects

Japanese-to-English subtitle translation for anime/game content. Primary subtitle editor is Aegisub; output format is ASS (Advanced SubStation Alpha).

## Projects

- **Project Sekai** - AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** - Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** - Love Live! Superstar!! Liella! live concert content

All projects live under `projects/`, each in a subdirectory named after the content (e.g., `projects/Project Sekai/Colors of Pure Sense/`). Subtitle files, transcripts, and audio/video intermediates live together in each subdirectory.

See `README.md` for full project progress table.

## Toolchain

Two-script pipeline for GCP Chirp 3 transcription, with shared utilities in `utils/`:

| Tool | Purpose |
|------|---------|
| **yt-dlp** | Download source video from YouTube/Bilibili |
| **ffmpeg** | Convert formats, trim video, extract audio, hardsub |
| **whisper** | Generate Japanese transcript from audio (`--language Japanese`) |
| **Aegisub** | Manual subtitle editing (ASS format) |
| **transcribe.py** | GCP Speech-to-Text (Chirp 3) batch transcription, outputs raw JSON. Accepts local files or GCS URIs. Auto-splits audio >20 min into non-overlapping chunks. Run with `uv run` |
| **json_to_ass.py** | Convert Chirp 3 JSON transcripts to ASS subtitles. Word-level line splitting with smart comma splitting (longest pause). No GCP dependencies — re-run freely to tune parameters |
| **quality_report.py** | Quality analysis and reporting. Generates `.log` (untruncated plain text) and `.html` (interactive viewer with color-coded issues, filter buttons, optional video player with click-to-seek). Called automatically by both scripts via `write_reports()` |
| **translate.py** | Translate Japanese ASS subtitles to English using Gemini via Vertex AI. Sends lines in batches with translation context (instructions, style guide, project reference with fixed translations). Auto-generates comparison report |
| **compare_translations.py** | Generate side-by-side JP vs EN comparison HTML report. Same dark theme as quality_report.py, with char ratio warnings and optional video player |
| **utils/** | Shared utility modules: `utils/audio.py` (ffmpeg/ffprobe helpers), `utils/gcs.py` (GCS operations), `utils/time.py` (timestamp parsing/formatting), `utils/ass_parser.py` (ASS file parsing/writing) |
| **tests/** | Unit tests (`unittest`). Run with `uv run python -m unittest discover -s tests -v`. All external deps mocked — no network, GCP, or ffmpeg needed |

### Environment

Python dependencies managed with [uv](https://docs.astral.sh/uv/). Run `uv sync` to install, then use `uv run` to execute scripts.

### transcribe.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--transcripts-dir` | `raw_transcripts/` next to input | Output directory for raw JSON transcript files (optional) |
| `--ass-output` | Input stem + ` - Transcript.ass` | Override ASS output filename (optional) |
| `--trim-start` | 0.0 | Skip this many seconds of leading audio before transcribing. Timestamps are offset so they align with the original file |

### Transcription pipeline

```
uv run transcribe.py --input local_video.mkv
```

ASS subtitles are generated automatically. Re-run `json_to_ass.py` to tune splitting:

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass
```

### json_to_ass.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--pause-threshold` | 1.0s | Silence duration that always forces a line break |
| `--max-line-chars` | 50 | Hard character limit per line |
| `--comma-split-chars` | 40 | Lines over this length get split at the comma with the longest pause. 0 to disable |
| `--lead-in` | 0.125 | Lead-in padding in seconds (subtitle appears before speech). Always applies full amount; previous line's lead-out yields. 0 to disable |
| `--lead-out` | 0.5 | Lead-out padding in seconds (subtitle lingers after speech). Capped at next line's (shifted) start. 0 to disable |
| `--snap-gap` | 0.25 | Snap gaps smaller than this (seconds) between same-style lines to prevent flashing. 0 to disable |
| `--min-duration` | 0.5 | Minimum line duration in seconds. Short lines get lead-out/lead-in padding. 0 to disable |
| `--video` | None | Path to source video file. Embeds an HTML5 player in the HTML report for click-to-seek |

### Quality reports

Both scripts automatically generate quality reports next to the ASS output:
- **`.log`** — untruncated plain text with all flagged lines (console output truncates to first 3–5)
- **`.html`** — interactive viewer with color-coded rows (red=critical, orange=warning, yellow=info, blue=gaps), filter buttons, expandable issue details, and optional video player

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass --video source.mkv
# Generates: output.ass, output.log, output.html (with embedded video player)
```

`transcribe.py` auto-passes the local input file as the video source.

### Translation pipeline

```
uv run translate.py --input source_jp.ass --project projects/Lieraji/translation_reference.yaml
```

Auto-generates a comparison report. Re-run comparison separately:

```
uv run compare_translations.py --source source_jp.ass --translated source_jp_en.ass --video source.mkv
```

### translate.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--input` | required | Source ASS file (Japanese) |
| `--output` | `{input_stem}_en.ass` | Output ASS file (English) |
| `--project` | None | Path to project `translation_reference.yaml` (or legacy `.md`) |
| `--instructions` | `translation_instructions.md` | Path to top-level instructions |
| `--model` | `gemini-2.5-flash` | Gemini model to use |
| `--batch-size` | 50 | Lines per API request |
| `--video` | None | Video path for comparison report |

### compare_translations.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--source` | required | Source ASS file (Japanese) |
| `--translated` | required | Translated ASS file (English) |
| `--video` | None | Path to source video file for embedded player |
| `--title` | translated filename stem | Report title |

### Translation context files

- **`translation_instructions.md`** — self-contained Gemini system prompt. Includes all translation directives (cross-line context, no-blank-lines, filler handling, line-ending flow, phrase grouping) AND formatting rules (punctuation, italics, contractions, naming, cultural terms). This is the only style reference sent to the model — `style_guide.md` is NOT loaded
- **`style_guide.md`** — human-only reference for manual Aegisub work. Not used by `translate.py`
- **Per-project `translation_reference.yaml`** — structured YAML with separate sections for glossary, segments, fixed replacements, and project context. Speaker profiles are auto-loaded from `speakers/*.yaml` in the same directory. Legacy `.md` references are still supported for backward compatibility. Exists for `projects/Lieraji/` and `projects/Project Sekai/`
- **Per-project `speakers/*.yaml`** — individual speaker profile files keyed by voice actor name. Each file contains the VA's name, roles (characters they voice), speaking style, and optional greetings. Auto-discovered by `translate.py` when using a YAML reference

### Key translation technical notes

- **Structured output**: Uses Gemini's `response_schema` with a `TranslatedSubtitle` Pydantic model (`id`, `original`, `translated`) for reliable JSON output. No text-format parsing needed
- **Cross-line context**: Prompt instructs the model to read neighboring lines before translating, so split sentences flow naturally across subtitle lines
- **No blank lines**: Every source line produces a non-empty translation. Filler-only lines are absorbed by redistributing the surrounding sentence across them
- **Filler word handling**: Standalone fillers ("um", "uh", "ah") are not translated literally — their lines carry redistributed text instead. Transitional phrases ("Well then,", "You know,") are kept
- **Line-ending flow**: Lines end on natural punctuation; trailing connectives ("but", "and", "so") move to the next line. Logical phrases (article + noun) are kept together on the same line
- **Glossary enforcement**: Fixed translations from `translation_reference.yaml` are used verbatim for recurring scripted lines
- **Speaker profiles**: Per-speaker YAML files (`speakers/*.yaml`) provide voice/personality context to the model, but translation accuracy is prioritized over matching speaker tone

### Key technical notes

- **Non-overlapping chunks**: Overlap was removed because the API transcribes the same audio differently per chunk, making deduplication unreliable.
- **Word-level splitting**: Chirp 3 returns 1 giant result per chunk. We split using word timestamps at sentence enders (。？！), pauses ≥1s, max chars, and commas on long lines.
- **Smart comma splitting**: `_emit_line()` recursively splits lines >40 chars at the comma with the longest pause after it. Min first-part = threshold/2 to avoid tiny fragments. Falls back to splitting at the longest pause at any word boundary when no comma is found and the line exceeds `max-line-chars`.
- **Local file input**: `--input` accepts local video/audio files or `gs://` URIs. Video files are auto-detected (via ffprobe) and audio is extracted with stream copy (no re-encoding). The audio codec is probed to pick the right container extension (opus→.opus, aac→.m4a, etc.). Non-Opus audio (e.g., AAC) is automatically re-encoded to Opus before uploading — Chirp 3 returns empty results for AAC input.
- **Bogus timestamps**: Chirp 3 sometimes returns zero, negative, or absurdly large word `endOffset` values. These are clamped to `startOffset` *before* adding the chunk time offset — otherwise a bogus `0s` end becomes a plausible-looking timestamp after the offset is added (e.g., `0 + 1080 = 1080s`). Offsets exceeding the chunk duration are also clamped.
- **GCP project ID**: set via `GOOGLE_CLOUD_PROJECT` env var or `--project-id` flag.
- **Trim offset**: `--trim-start` trims leading audio (e.g., silence or intros) before sending to the API. The trim offset is added back to all word timestamps so they match the original file's timeline. Stored in `merged.json` as `trim_offset`.
- **GCS bucket**: `gs://subtitling-projects/audio-files/`. Local files are uploaded to `gs://{bucket}/tmp/` for transcription, then cleaned up. Override with `--gcs-bucket`.

See `snippets.md` for common CLI commands and `workflow.md` for the end-to-end process.

## Subtitle Format

ASS files use:
- 1920x1080 or 1280x720 play resolution
- Per-speaker color-coded styles (character name as style name)
- Layer 0 for all standard dialogue
- `{\i1}text{\i0}` for italics (Japanese terms in romaji, emphasis, work titles)

## Style Conventions

Full rules in `style_guide.md`. Key points:

- **Pauses**: ellipsis `...` for long pauses, comma for short, em dash for interruptions
- **Japanese terms**: italicize with ASS tags, keep terms without direct English equivalents
- **Names**: Western order ("Given Family", e.g., "Mizuki Akiyama")
- **Contractions**: always use natural spoken forms ("I'm", "won't", not "I am", "will not")
- **Filler words**: preserve for authenticity ("Like,", "Well,", "I mean,")
- **Song/event titles**: quoted, not italicized (e.g., "Yoka ni Mitore")
- **Project Sekai terms**: "AfterTalk" (capital T), "AfterLive" (capital L), "ProSeka" (capital S), "MV", "Episode" not "Chapter"

## Git Conventions

Commit message format:
- Work in progress: `wip: description` or `project-shortname: wip, description`
- Completed/QC: `project-shortname: QC`
- Tooling: `refactor:`, `fix:`, `docs:` prefixes
- Other: `project-shortname: description`

Project shortnames from commit history: `ena5` (With Our Wounded Hands Aftertalk), `hona5` (This story continues with hope AfterTalk), `ichi6` (Kimi to Tsunagu HeartBeat Aftertalk), `ena6` (Colors of Pure Sense), `mizu6` (Reaching Out to a Tomorrow That Won't Come Unraveled Aftertalk).

## Documentation Rules

- When updating documentation, always update **both** `README.md` and `CLAUDE.md`. They document the same toolchain from different angles (README for humans/GitHub, CLAUDE.md for AI agent context), so changes must be mirrored to keep them in sync.
