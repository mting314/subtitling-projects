# Standard Workflow

General steps in case I forgot how to do this or forget some about some tripping points

Also maybe I can feed this into AI and get a script to automate the first and last steps

## Step 1: yt-dlp

Download original video as mp4.

Example:

```
yt-dlp https://www.youtube.com/watch?v=cbvTtSsc4e4 --merge-output-format mkv
```

- Might run into yt-dlp breaking, usually just need to update.
- ([Reference](https://github.com/yt-dlp/yt-dlp/issues/14707))

## Step 2: Directory setup

Create directory with name of project, video in and convert to mkv for subbing

## Step 3: Transcription

### Option A: Whisper (local, quick)

```
whisper input.mp4 --output_format txt --task transcribe --language Japanese
```

Produce txt file as transcript to pick up on parts that are harder to hear or for unknown vocab words.

### Option B: GCP Chirp 3 (cloud, better accuracy)

For longer or higher-quality transcription, use GCP Speech-to-Text Chirp 3. Two scripts:

- `gcp_transcribe_batch.py` — transcribes audio, outputs raw JSON (expensive, run once)
- `json_to_ass.py` — converts JSON to ASS subtitles (cheap, iterate freely)

**Setup (one-time):**

1. Install dependencies: `uv sync`
2. Install ffmpeg: `brew install ffmpeg`
3. Authenticate: `gcloud auth application-default login`
4. Set project ID in `.env`: `GOOGLE_CLOUD_PROJECT=your-project-id`

**Usage:**

1. Transcribe to JSON (auto-extracts audio from video, uploads to GCS, chunks if needed):
   ```
   uv run gcp_transcribe_batch.py \
     --input "Project Name/video.mkv" \
     --output "Project Name/raw_transcripts"
   ```
2. Convert JSON to ASS:
   ```
   uv run json_to_ass.py \
     "Project Name/raw_transcripts/merged.json" \
     "Project Name/Transcript.ass" \
     --title "Project Transcript"
   ```

Audio longer than 20 minutes is automatically split into non-overlapping chunks (default 18 min), transcribed separately, and merged. Use `--chunk-minutes` to adjust chunk size.

If the audio has a long silent intro that causes Chirp 3 to produce bad timestamps, use `--trim-start <seconds>` to skip it. The trim offset is added back to all timestamps so they align with the original file.

**Tuning ASS line splitting** (re-run json_to_ass.py without re-transcribing):

- `--pause-threshold 0.5` — shorter pauses trigger line breaks (default: 1.0s)
- `--max-line-chars 100` — shorter lines (default: 200)
- Accepts a single JSON file or a directory of chunk files

**Customizing ASS styles:**

The script generates ASS files with two built-in styles:
- **Default** — white text, for English/non-Japanese content
- **JP** — white text with blue-gray outline (`&H006381A1`), for Japanese content

The style is auto-detected from the transcription language. To customize after generation:
- Open in Aegisub to change fonts, colors, sizes, positioning
- Add per-speaker styles by changing the Style column in dialogue lines
- The header uses 1920x1080 PlayRes, Lato ExtraBold 72pt, border style 1 (outline+shadow)
- Modify `ASS_HEADER_TEMPLATE` in `json_to_ass.py` to change defaults for all future runs

## Step 4: Subbing

## Step 5:
