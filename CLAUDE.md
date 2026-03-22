# Subtitling Projects

Japanese-to-English subtitle translation for anime/game content. Primary subtitle editor is Aegisub; output format is ASS (Advanced SubStation Alpha).

## Projects

- **Project Sekai** - AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** - Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** - Love Live! Superstar!! Liella! live concert content

Each project gets a subdirectory named after the content (e.g., `Project Sekai/Colors of Pure Sense/`). Subtitle files, transcripts, and audio/video intermediates live together in each subdirectory.

See `README.md` for full project progress table.

## Toolchain

Two-script pipeline for GCP Chirp 3 transcription, with shared utilities in `utils/`:

| Tool | Purpose |
|------|---------|
| **yt-dlp** | Download source video from YouTube/Bilibili |
| **ffmpeg** | Convert formats, trim video, extract audio, hardsub |
| **whisper** | Generate Japanese transcript from audio (`--language Japanese`) |
| **Aegisub** | Manual subtitle editing (ASS format) |
| **gcp_transcribe_batch.py** | GCP Speech-to-Text (Chirp 3) batch transcription, outputs raw JSON. Accepts local files or GCS URIs. Auto-splits audio >20 min into non-overlapping chunks. Run with `uv run` |
| **json_to_ass.py** | Convert Chirp 3 JSON transcripts to ASS subtitles. Word-level line splitting with smart comma splitting (longest pause). No GCP dependencies — re-run freely to tune parameters |
| **utils/** | Shared utility modules: `utils/audio.py` (ffmpeg/ffprobe helpers), `utils/gcs.py` (GCS operations), `utils/time.py` (timestamp parsing/formatting) |
| **tests/** | Unit tests (`unittest`). Run with `uv run python -m unittest discover -s tests -v`. All external deps mocked — no network, GCP, or ffmpeg needed |

### Environment

Python dependencies managed with [uv](https://docs.astral.sh/uv/). Run `uv sync` to install, then use `uv run` to execute scripts.

### gcp_transcribe_batch.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--trim-start` | 0.0 | Skip this many seconds of leading audio before transcribing. Timestamps are offset so they align with the original file |

### Transcription pipeline

```
uv run gcp_transcribe_batch.py --input local_video.mkv --output raw_transcripts/
uv run json_to_ass.py raw_transcripts/merged.json output.ass
```

### json_to_ass.py parameters

| Flag | Default | Purpose |
|------|---------|---------|
| `--pause-threshold` | 1.0s | Silence duration that always forces a line break |
| `--max-line-chars` | 200 | Hard character limit per line |
| `--comma-split-chars` | 40 | Lines over this length get split at the comma with the longest pause. 0 to disable |

### Key technical notes

- **Non-overlapping chunks**: Overlap was removed because the API transcribes the same audio differently per chunk, making deduplication unreliable.
- **Word-level splitting**: Chirp 3 returns 1 giant result per chunk. We split using word timestamps at sentence enders (。？！), pauses ≥1s, max chars, and commas on long lines.
- **Smart comma splitting**: `_emit_line()` recursively splits lines >40 chars at the comma with the longest pause after it. Min first-part = threshold/2 to avoid tiny fragments.
- **Local file input**: `--input` accepts local video/audio files or `gs://` URIs. Video files are auto-detected (via ffprobe) and audio is extracted with stream copy (no re-encoding). The audio codec is probed to pick the right container extension (opus→.opus, aac→.m4a, etc.).
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

Project shortnames from commit history: `hona5` (This story continues with hope AfterTalk), `ena6` (Colors of Pure Sense), `ichi6` (Unsteady, still steady step), `mizu6` (Reaching Out to a Tomorrow That Won't Come Unraveled Aftertalk).
