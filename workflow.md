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

## Step 3: Whisper

```
whisper input.mp4 --output_format txt --task transcribe
```

Produce txt file as transcript to pick up on parts that are harder to hear or for unknown vocab words.

## Step 4: Subbing

## Step 5:
