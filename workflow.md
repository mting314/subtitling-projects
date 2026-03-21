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

For longer or higher-quality transcription, use `gcp_transcribe_batch.py` with Google Cloud Speech-to-Text Chirp 3. Outputs an ASS file directly with per-line timestamps.

**Setup (one-time):**

1. Install dependencies: `pip3 install google-cloud-speech google-cloud-storage`
2. Install ffmpeg: `brew install ffmpeg`
3. Authenticate: `gcloud auth application-default login`
4. Set project: `export GOOGLE_CLOUD_PROJECT=your-project-id`

**Usage:**

1. Extract audio: `ffmpeg -i input.mkv -vn -acodec copy audio.opus`
2. Upload to GCS: `gsutil cp audio.opus gs://subtitling-projects/audio-files/`
3. Run transcription:
   ```
   python3 gcp_transcribe_batch.py \
     --input "gs://subtitling-projects/audio-files/audio.opus" \
     --output "Project Name/Transcript.ass" \
     --title "Project Transcript"
   ```

Audio longer than 20 minutes is automatically split into chunks (default 18 min with 30s overlap), transcribed separately, and merged back with corrected timestamps. Use `--chunk-minutes` to adjust chunk size.

**Customizing the ASS output:**

The script generates ASS files with two built-in styles:
- **Default** — white text, for English/non-Japanese content
- **JP** — white text with blue-gray outline (`&H006381A1`), for Japanese content

The style is auto-detected from the transcription language. To customize after generation:
- Open in Aegisub to change fonts, colors, sizes, positioning
- Add per-speaker styles by changing the Style column in dialogue lines
- The header uses 1920x1080 PlayRes, Lato ExtraBold 72pt, border style 1 (outline+shadow)
- Modify `ASS_HEADER_TEMPLATE` in `gcp_transcribe_batch.py` to change defaults for all future runs

## Step 4: Subbing

## Step 5:
