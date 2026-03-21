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

## GCP Chirp 3 batch transcription

Short audio (under 20 min):

```
python3 gcp_transcribe_batch.py \
  --input gs://subtitling-projects/audio-files/short.opus \
  --output "output.ass"
```

Long audio (auto-splits into chunks):

```
python3 gcp_transcribe_batch.py \
  --input "gs://subtitling-projects/audio-files/Colors of Pure Sense.opus" \
  --output "Project Sekai/Colors of Pure Sense/Colors of Pure Sense - Transcript.ass" \
  --title "Colors of Pure Sense Transcript"
```

Override project/region:

```
python3 gcp_transcribe_batch.py \
  --input gs://bucket/file.opus \
  --output output.ass \
  --project-id my-project \
  --region us-central1
```

## Upload audio to GCS for transcription

```
gsutil cp "input.opus" "gs://subtitling-projects/audio-files/input.opus"
```