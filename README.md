# Subtitling Projects

Japanese-to-English fan subtitle translations for anime, game, and idol content. Subtitles are authored in Aegisub and output as ASS (Advanced SubStation Alpha) files.

## Projects

### Project Sekai

AfterTalk streams, anniversary videos, and event content from Project Sekai: Colorful Stage! (プロジェクトセカイ カラフルステージ！).

| Project | Status | Notes |
|---------|--------|-------|
| With Our Wounded Hands Aftertalk Part 1 | Complete | |
| With Our Wounded Hands Aftertalk Part 2 | Complete | |
| This story continues with hope Aftertalk | Complete | QC'd |
| 5th Anniversary Video LeoNeed | Complete | |
| Kimi to Tsunagu HeartBeat Aftertalk | Complete | |
| Find the dream view Aftertalk | Complete | |
| Unsteady, still steady step Aftertalk | Complete | |
| Colors of Pure Sense (ena6) | In Progress | Transcript generated via Chirp 3; translation not started |
| Reaching Out to a Tomorrow That Won't Come Unraveled Aftertalk (mizu6) | In Progress | Transcript generated via Chirp 3; translation not started |

### Lieraji (Liella no Radio Japan)

Episodic radio show featuring the Love Live! Superstar!! Liella! cast.

| Project | Status | Notes |
|---------|--------|-------|
| Episode 247 | In Progress | Draft translation in markdown |
| Episode 248 | Not Started | Whisper transcript only |
| Episode 249 | In Progress | ASS file started |

### Liella 6th to 7th

Love Live! Superstar!! Liella! live concert content.

| Project | Status | Notes |
|---------|--------|-------|
| Concert MC 1 | Complete | `1-en.ass` |

## Toolchain

| Tool | Purpose |
|------|---------|
| **yt-dlp** | Download source video from YouTube/Bilibili |
| **ffmpeg** | Convert formats, trim video, extract audio, hardsub |
| **whisper** | Generate Japanese transcript from audio (local, quick) |
| **gcp_transcribe_batch.py** | GCP Speech-to-Text (Chirp 3) batch transcription, outputs raw JSON |
| **json_to_ass.py** | Convert Chirp 3 JSON transcripts to ASS with word-level line splitting |
| **utils/** | Shared utility modules: `audio.py` (ffmpeg/ffprobe), `gcs.py` (GCS ops), `time.py` (timestamps) |
| **tests/** | Unit tests (`unittest`) for utils/ and main scripts. All external deps mocked |
| **Aegisub** | Manual subtitle editing and timing |

## Transcription Pipeline

For longer audio or when higher accuracy is needed, a two-script pipeline handles GCP Chirp 3 transcription:

```
local video/audio (or GCS URI)
  → gcp_transcribe_batch.py (extract audio, chunk, upload, transcribe, generate ASS)
  → raw JSON (per-chunk + merged.json) + Transcript.ass
  → Aegisub (manual translation and timing)
```

**Transcribe + generate ASS (single command)**

```bash
export GOOGLE_CLOUD_PROJECT=your-project-id

# From a local video file (auto-extracts audio)
uv run gcp_transcribe_batch.py --input "video.mkv"

# Or from a GCS URI
uv run gcp_transcribe_batch.py \
  --input "gs://subtitling-projects/audio-files/audio.opus" \
  --transcripts-dir "raw_transcripts/"

# Skip leading silence/intro (timestamps still align with original file)
uv run gcp_transcribe_batch.py --input "video.mkv" --trim-start 120

# Override output paths
uv run gcp_transcribe_batch.py \
  --input "video.mkv" \
  --transcripts-dir "raw_transcripts/" \
  --ass-output "custom.ass"
```

Audio longer than 20 minutes is automatically split into non-overlapping chunks (default 18 min). Video files are detected and audio is extracted (stream copy, no re-encoding).

**Tune line splitting** (re-run `json_to_ass.py` without re-transcribing):

```bash
python3 json_to_ass.py raw_transcripts/merged.json output.ass \
  --pause-threshold 0.5 \
  --max-line-chars 100 \
  --comma-split-chars 30
```

### Line Splitting Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--pause-threshold` | 1.0s | Silence duration that always forces a line break |
| `--max-line-chars` | 200 | Hard character limit per line |
| `--comma-split-chars` | 40 | Lines over this length get split at the comma with the longest pause. Set to 0 to disable |
| `--snap-gap` | 0.25 | Snap gaps smaller than this (seconds) between same-style lines to prevent flashing. Set to 0 to disable |
| `--min-duration` | 0.5 | Minimum line duration in seconds. Short lines get lead-out/lead-in padding. Set to 0 to disable |

### Setup

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/), ffmpeg, and a GCP project with Speech-to-Text API enabled.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python dependencies
uv sync

# Install ffmpeg (macOS)
brew install ffmpeg

# Authenticate with GCP
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project-id
```

Run scripts with `uv run` to use the managed environment:

```bash
uv run python3 gcp_transcribe_batch.py --input audio.opus
uv run python3 json_to_ass.py raw_transcripts/merged.json output.ass  # tune splitting only
```

`json_to_ass.py` has no external dependencies and can also be run directly with any Python 3.11+.

## Subtitle Conventions

See `style_guide.md` for full rules. Key points:

- ASS format, 1920x1080 play resolution
- Per-speaker color-coded styles
- Western name order ("Given Family")
- Natural contractions ("I'm", "won't")
- Ellipsis `...` for long pauses, em dash for interruptions
- Japanese terms in italics via `{\i1}text{\i0}`
- Song/event titles quoted, not italicized

## Testing

```bash
uv run python -m unittest discover -s tests -v
```

80 tests covering timestamp parsing, bogus value clamping, line splitting, gap snapping, min duration, ASS output, transcript loading, `transcript_to_json`, and end-to-end ASS integration. All external dependencies (ffmpeg, GCS) are mocked — no network access or credentials needed.

## TODO

### Bugs

- ~~**Chirp 3 fails on large leading silence**~~: Resolved — use `--trim-start <seconds>` to skip leading silence before transcription. Timestamps are automatically offset to align with the original file

### Enhancements

- **Intelligent audio chunking based on silence**: Currently audio is split into fixed ~18-minute chunks, which risks cutting mid-sentence. Instead, detect long silent portions in the audio and split at those boundaries.
- **Language-aware line splitting**: Line splitting currently relies on punctuation and pause duration, which is deterministic but naive. When Chirp 3 omits punctuation, lines can run on too long. Future improvements:
  - Use a pause duration threshold as a fallback when punctuation is absent
  - Use semantic/linguistic analysis to find natural break points in the Japanese text
- ~~**Fix subtitle flashing**~~: Resolved — `json_to_ass.py` now snaps near-adjacent same-style lines together via `--snap-gap` (default 0.1s). Gaps smaller than the threshold are closed by extending the earlier line's end time.
- **Overlapping speakers**: When multiple speakers talk simultaneously, Chirp 3 merges their words into a single interleaved stream, producing lines that are confusing and unreadable. Investigate whether Chirp 3's raw output can separate simultaneous speakers (e.g., via speaker diarization or multiple alternatives). If so, update `json_to_ass.py` to split overlapping speakers into separate ASS lines. If not, this is a fundamental limitation of the current approach.
- ~~**End-to-end pipeline orchestration**~~: Resolved — `gcp_transcribe_batch.py` now generates ASS subtitles automatically after transcription. Re-run `json_to_ass.py` separately to tune splitting parameters.

## References

- `workflow.md` — end-to-end subtitle creation process
- `snippets.md` — common CLI commands
- `style_guide.md` — translation and formatting rules
