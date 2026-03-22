## General yt-dlp

```
yt-dlp -vU *Bilibili link* res:1080--cookies cookies.txt
```

## yt-dlp as mkv

```
yt-dlp *link* --merge-output-format mkv
```

## Hardsubbing

```
ffmpeg -i "inputvideo" -vf "ass=subtitlename" outputvideo.mp4
```

## Trim mkv

```
ffmpeg -i "input.mkv" -ss 00:10:52 -to 00:30:00 -c copy "pre story cut.mkv"
```

## Convert mp4 to mkv

```
ffmpeg -i input.mp4 -c:v copy -c:a copy output.mkv
```

## Whisper

```
whisper input.mp4 --output_format txt --task transcribe --language Japanese
```

## Extract mp3 from mkv

```
ffmpeg -i input.mkv -vn -acodec copy output.mp3
```

## GCP Chirp 3 batch transcription (step 1: transcribe to JSON)

Project ID is loaded from `.env` automatically. Override with `--project-id` if needed.

```
uv run gcp_transcribe_batch.py \
  --input "video.mkv" \
  --output "raw_transcripts/"
```

From a GCS URI:

```
uv run gcp_transcribe_batch.py \
  --input "gs://subtitling-projects/audio-files/audio.opus" \
  --output "raw_transcripts/"
```

Skip leading silence/intro (e.g., 2 minutes):

```
uv run gcp_transcribe_batch.py \
  --input "video.mkv" \
  --output "raw_transcripts/" \
  --trim-start 120
```

Override project/region:

```
uv run gcp_transcribe_batch.py \
  --input gs://bucket/file.opus \
  --output raw_transcripts/ \
  --project-id my-project \
  --region us-central1
```

## Convert transcript JSON to ASS (step 2: generate subtitles)

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass --title "My Transcript"
```

Tune line splitting (re-run without re-transcribing):

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass --pause-threshold 0.5 --max-line-chars 100
```

Accept a directory of chunk files:

```
uv run json_to_ass.py raw_transcripts/ output.ass
```

## Upload audio to GCS for transcription

```
gsutil cp "input.opus" "gs://subtitling-projects/audio-files/input.opus"
```