# Subtitling Projects

Japanese-to-English subtitle translation for anime/game content. Primary subtitle editor is Aegisub; output format is ASS (Advanced SubStation Alpha).

## Projects

- **Project Sekai** - AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** - Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** - Love Live! Superstar!! Liella! live concert content

Each project gets a subdirectory named after the content (e.g., `Project Sekai/Colors of Pure Sense/`). Subtitle files, transcripts, and audio/video intermediates live together in each subdirectory.

## Toolchain

| Tool | Purpose |
|------|---------|
| **yt-dlp** | Download source video from YouTube/Bilibili |
| **ffmpeg** | Convert formats, trim video, extract audio, hardsub |
| **whisper** | Generate Japanese transcript from audio (`--language Japanese`) |
| **Aegisub** | Manual subtitle editing (ASS format) |
| **gcp_transcribe_batch.py** | Google Cloud Speech-to-Text (Chirp 3) batch transcription for longer audio |
| **json_to_ass.py** | Convert GCP Speech-to-Text JSON output to ASS subtitle format |

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
- Other: `project-shortname: description`

Project shortnames from commit history: `hona5` (This story continues with hope AfterTalk), `ena6` (Colors of Pure Sense).
