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
