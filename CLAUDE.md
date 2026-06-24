# Subtitling Projects

Project files for Japanese-to-English fan subtitle translations. This repo tracks subtitle files, transcripts, speaker maps, and translation outputs. The tooling lives in `mting314/autosub`.

## Projects

- **Project Sekai** — AfterTalk streams, anniversary videos, event content from the rhythm game
- **Lieraji** — Episodic radio show (Liella no Radio Japan), Love Live! Superstar!! cast
- **Liella 6th to 7th** — Love Live! Superstar!! Liella! live concert content

All projects live under `projects/`, each in a subdirectory named after the content.

## Workflow

Each subtitled video moves through these stages:

1. **Generate** — set up the project (folder, `notes.md`, video download) and run the autosub pipeline (transcribe → format → translate → postprocess) to produce `<name>_translated.ass`. New-project setup steps are in [`aftertalk_project_setup.md`](aftertalk_project_setup.md); tooling lives in the [autosub](https://github.com/mting314/autosub) repo.
2. **QC review** — human pass over `<name>_translated.ass` for consistency, grammar, spelling, and style. Follow [`subtitle_review_guide.md`](subtitle_review_guide.md).
3. **Hardsub + trim** — burn the reviewed subs into the video and trim to the subbed portion with `hardsub_trim.sh` (see [Post-Pipeline: Hardsub + Trim](#post-pipeline-hardsub--trim)).
4. **Publish** — write the YouTube description ([YouTube Video Blurbs](#youtube-video-blurbs)).

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

## QC Review

Before hardsubbing, do a human-pass review of `<name>_translated.ass`. The full checklist
is in **[`subtitle_review_guide.md`](subtitle_review_guide.md)** — read it before reviewing.

In short, review across four dimensions:

- **Consistency** — grep each recurring term (titles, song names, character names + honorifics, stylized names) and enforce one canonical form. See the Project Sekai glossary in the guide.
- **Grammar** — especially the capitalization/continuation rule (a comma-broken line → next line lowercase; a sentence-ending line → next line capitalized).
- **Spelling** — name typos and duplicated words/clauses from the STT/LLM.
- **Style** — natural casual spoken English, not academic.

Process: extract dialogue with awk (the `.ass` can be 1+ MB due to embedded `img2ass` lines), suggest edits as a table and confirm before applying, apply with a line-targeted script that dry-runs each replacement, then re-grep to verify the consistency counts.

## Post-Pipeline: Hardsub + Trim

After QC, burn subtitles into video and trim to the subbed portion. **Must hardsub before trimming** — trimming invalidates .ass timestamps.

### `hardsub_trim.sh`

Script at repo root. Handles single or multiple segments with automatic concatenation.

```bash
# Single segment
./hardsub_trim.sh <input.mkv> <subtitle.ass> <output.mp4> <start> <end>

# Multiple segments (gaps like story recaps/songs are skipped)
./hardsub_trim.sh <input.mkv> <subtitle.ass> <output.mp4> <start1> <end1> <start2> <end2> ...
```

Example (Colors of Pure Sense — 2 segments, skipping story recap):
```bash
./hardsub_trim.sh \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense.mkv" \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_final.mp4" \
  00:09:45 00:18:19 \
  00:33:35 00:55:30
```

**Notes:**
- Requires ffmpeg built with libass (`brew install libass`, then `brew reinstall --build-from-source ffmpeg`)
- The `ass=` filter doesn't handle spaces in filenames — the script creates a symlink to work around this
- Multiple segments are encoded in parallel, then concatenated with `-c copy` (no re-encode)
- Timestamps for each project are saved in `notes.md` within each project folder
- To auto-detect segments from subtitle gaps, analyze the .ass file for gaps > 30 seconds

See `snippets.md` for standalone ffmpeg commands.

## YouTube Video Blurbs

When writing YouTube descriptions for subtitled videos, follow this format:
1. VA name + character they voice + what the content covers
2. 1-2 sentences teasing highlights/fun moments
3. Link to original video
4. Credits/references if applicable

Example tone: casual, enthusiastic, highlights personality moments from the VAs.

## Git Conventions

- `project-shortname: description` for project work
- `wip: description` for work in progress
- `project-shortname: QC` for completed/reviewed
