# Subtitling Projects

Project files for Japanese-to-English fan subtitle translations. This repo tracks subtitle files, transcripts, speaker maps, and translation outputs. The tooling lives in `mting314/autosub`.

## Projects

- **Project Sekai** — AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** — Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** — Love Live! Superstar!! Liella! live concert content

All projects live under `projects/`, each in a subdirectory named after the content.

## Tooling

The transcription and translation pipeline is in a separate repo: [mting314/autosub](https://github.com/mting314/autosub). The legacy pipeline scripts are preserved on the `ai-sub` branch of this repo.

## File Types

| Extension | Purpose |
|-----------|---------|
| `.ass` | Subtitle files (Aegisub / Advanced SubStation Alpha) |
| `.json` | Transcripts from speech-to-text |
| `.toml` | Speaker maps (speaker_map.toml, speaker_assignments.toml) |
| `.log` | Autosub pipeline logs |
| `_logs/` | Structured per-chunk translation logs |
| `.md` | Translation references with character context and glossaries |

## Style Conventions

- **Pauses**: ellipsis `...` for long pauses, comma for short, em dash for interruptions
- **Japanese terms**: italicize with ASS tags
- **Names**: Western order ("Given Family", e.g., "Mizuki Akiyama")
- **Contractions**: always use natural spoken forms
- **Song/event titles**: quoted, not italicized
- **Project Sekai terms**: "AfterTalk" (capital T), "AfterLive" (capital L), "ProSeka" (capital S)

## Git Conventions

- `project-shortname: description` for project work
- `wip: description` for work in progress
- `project-shortname: QC` for completed/reviewed
