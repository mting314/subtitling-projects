# scripts/

Local finishing + utility scripts for the subtitling workflow. **Run them from the
projects repo root** (they take/emit `projects/...` paths and, for `find_segments.py`,
print a `./scripts/hardsub_trim.sh` command). The autosub transcribe→format→translate→
postprocess pipeline lives in a separate repo ([mting314/autosub](https://github.com/mting314/autosub)).

The `aftertalk-launch` skill (`.claude/skills/aftertalk-launch/`) drives most of these;
`subtitle_review_guide.md` (repo root) documents the QC-time ones in depth.

| Script | Purpose | Stage |
|---|---|---|
| `apply_positional_styles.py` | Copy Alignment + margins from a reference style onto PiP / song-shift lines (deterministic; caller resolves which styles play which role). | QC / layout |
| `detect_long_lines.py` | Render each Dialogue line under its real style and flag any wrapping to 3+ rows. Needs `uv run --with pillow --with numpy`. | QC / layout |
| `split_subtitle_line.py` | Split a flagged line into two events at a clause boundary, snapping the time split to a real breath (`--before`, `--transcript`). Fixes 3-row lines from `detect_long_lines.py`. | QC / layout |
| `scope_segments.py` | **Pre-pipeline** keep-segment scoping from the *raw* mkv (no STT): classifies each second as standby/watchalong/talk by video layout (right-panel template + stillness), plus an audio pass that catches full-screen songs (continuous-music low-energy-rate) the panel misses on newer layouts. Emits `--start/--end` for `autosub run` + a boundary contact-sheet PNG. Needs `uv run --with opencv-python-headless --with numpy --with librosa` (librosa optional — audio pass skipped without it). Always confirm via the contact sheet. | Setup / scoping |
| `find_segments.py` | **Post-pipeline** sibling of `scope_segments.py`: finds keep-segments between watchalong gaps in the *rendered* `.ass` timeline; `--transcript` classifies each gap silent vs audio, `--hardsub` emits a ready-to-run `hardsub_trim.sh` command. | Hardsub |
| `hardsub_trim.sh` | Burn subs into video and trim/concat to the kept segments (parallel encode + `-c copy` concat; blackdetect warnings). Requires ffmpeg built with libass. | Hardsub |
| `fetch_event.py` | Fetch Project Sekai event story data from the sekai-world master DB + asset CDN. | Setup / reference |

## Typical order (per episode)

0. `scope_segments.py <mkv> --profile proseka/<unit>` — scope keep-segments from the raw video (setup, before the pipeline); confirm against its contact sheet, then run `autosub run` with the emitted `--start/--end`
1. `apply_positional_styles.py` — reposition PiP / song-shift subs
2. `detect_long_lines.py` → `split_subtitle_line.py` — fix 3-row lines (loop until 0 flagged)
3. `find_segments.py --transcript --hardsub …` — get the cut plan + hardsub command
4. `./scripts/hardsub_trim.sh …` — render the final mp4
