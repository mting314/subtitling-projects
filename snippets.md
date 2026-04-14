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

## GCP Chirp 3 batch transcription (transcribe + generate ASS)

Project ID is loaded from `.env` automatically. Override with `--project-id` if needed.
ASS subtitles are generated automatically after transcription.

```
uv run transcribe.py \
  --input "video.mkv"
```

Raw JSON transcripts are saved to `raw_transcripts/` next to the input file by default.

Override transcript directory or ASS output path:

```
uv run transcribe.py \
  --input "video.mkv" \
  --transcripts-dir "custom_transcripts/" \
  --ass-output "custom_output.ass"
```

From a GCS URI:

```
uv run transcribe.py \
  --input "gs://subtitling-projects/audio-files/audio.opus" \
  --transcripts-dir "raw_transcripts/"
```

Skip leading silence/intro (e.g., 2 minutes):

```
uv run transcribe.py \
  --input "video.mkv" \
  --trim-start 120
```

Override project/region:

```
uv run transcribe.py \
  --input gs://bucket/file.opus \
  --project-id my-project \
  --region us-central1
```

## Tune ASS line splitting (re-run without re-transcribing)

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass --title "My Transcript"
```

```
uv run json_to_ass.py raw_transcripts/merged.json output.ass --pause-threshold 0.5 --max-line-chars 100
```

Accept a directory of chunk files:

```
uv run json_to_ass.py raw_transcripts/ output.ass
```

## Run tests

```
uv run python -m unittest discover -s tests -v
```

## Upload audio to GCS for transcription

```
gsutil cp "input.opus" "gs://subtitling-projects/audio-files/input.opus"
```
