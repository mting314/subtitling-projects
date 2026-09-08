# Sekaraji Episode 71

> Second **Sekaraji** (セカラジ) project, after Episode 72. Two hosts, still show
> cards, radio overlay. First episode run end-to-end on the reworked slot-style
> overlay pipeline (`radio-overlay-slot-styles`).

**Commit prefix**: `sekaraji71`

**Pipeline branch**: `radio-overlay-slot-styles` in `mting314/autosub`, cut from
`feature/radio-overlay`. Note that `origin/feature/radio-overlay` was force-pushed
from another machine and now holds a *different* design (it still bakes `\pos` into
event text); the two have not been reconciled. Run this episode from
`radio-overlay-slot-styles`.

## Show Details

- **Show name (JP)**: セカラジ | **Latin subtitle on card**: "Project SEKAI RADIO"
- **Format**: WEB radio, **pre-recorded** (`※『セカラジ』は事前収録です`)
- **Schedule**: biweekly, Fridays 20:00 JST
- **Episode**: #71
- **Source**: <https://www.youtube.com/watch?v=ubmtyOt0b9U>
- **Upload date**: 2026-08-14
- **Duration**: 32:24
- **Video**: 1920x1080, audio-only content over two still cards

## Hosts

The pair rotates every episode (ユニットシャッフル), so this differs entirely from
Episode 72. Taken from the description's 出演者 list, which gives them 順不同.

| Slot | VA (JP) | VA (romanized) | Character | Unit | Character colour |
| --- | --- | --- | --- | --- | --- |
| 1 | 野口瑠璃子 | Ruriko Noguchi | Ichika Hoshino (星乃一歌) | Leo/need | `#33AAEE` |
| 2 | Machico | Machico | Nene Kusanagi (草薙寧々) | Wonderlands×Showtime | `#33DD99` |

VA→character pairings verified against `profiles/proseka/leoneed.toml` and
`profiles/proseka/wxs.toml` rather than from memory. Colours from
`sekai-story-indexer` `webapp/static/meta.json`, the documented ProSeka source in
autosub's `docs/speaker_colors.md` — looked up by **character**, not by VA.

Cast photos pulled from the ProSeka fandom wiki API (`Noguchi Ruriko` and `Machico`
lead images) and converted to webp in `../../official_cast_photos/`. A bare curl
403s; the API needs a User-Agent, and page titles are Family-Given.

## Command (full pipeline, remote)

Local runs cannot complete this episode — see [60s cap](#the-60s-request-cap).

```bash
./scripts/remote.sh \
  "projects/projects/Project Sekai/Sekaraji/Episode 71/Sekaraji Ep 71.mkv" \
  run --profile proseka/sekaraji \
  --backend chirp_3 \
  --speakers 2 \
  --speaker-map profiles/local/sekaraji_ep71_speaker_map.toml \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

`remote.sh` only ships `profiles/local/` and `prompts/local/` to the VM, so the
episode's `speaker_map.toml` has to be copied into `profiles/local/` first and
referenced by that path. The container's WORKDIR is `/app`, so the relative path
resolves. (The avatar paths in the map break under that copy, which only matters
for overlay generation — do that locally.)

## The song

Unlike Episode 72, this run was **not** cut with `--start/--end`, because the
YouTube auto-captions transcribe the song lyrics rather than leaving a gap, so a
caption-gap scan finds nothing. The song is real:

- **Song corner**: 11:01.04 → 13:33.76
- **Sung portion**: 11:26.24 → 13:15.76 (16 lines)

Chirp 3's diarizer gave the singing voice its own label (`2`) — correctly, since it
is acoustically distinct from the two hosts. It is *not* a phantom third speaker and
must not be mapped to a slot.

Those 16 lines were deleted from `_final.ass`, `_translated.ass` and all three JSON
documents after the fact (`chunk_boundaries` remapped accordingly). To avoid it next
time, cut at:

```
--start 00:00:00 --end 00:11:05  --start 00:13:30 --end 00:32:24
```

## Corners detected

| Time | Corner |
| --- | --- |
| 00:00.00 | Opening Talk |
| 02:16.52 | Contact Notebook |
| 05:12.64 | Listener Mail |
| 11:01.04 | Song |
| 13:33.76 | Theme Mail |
| 29:39.80 | Ending |

## Gotchas hit on this episode

### The 60s request cap

The local network terminates any single HTTPS request at almost exactly 60s. Two
full-script classifier calls died at 59.98s and 60.00s; with 60-line windows one in
three windows still died at 60s; with 30-line windows plus three retries, window 9
failed all three attempts. Episode 72 (786 lines) squeaked under the cap, which is
why it worked locally and this one does not. **Run Sekaraji remotely.**

Consequences landed in the pipeline: `proseka/sekaraji` now windows the classifier
(`scope = "windowed"`, size 30, overlap 8), and `classify_combined` retries a failed
window instead of discarding every window already done.

### Normalizer term gap

The normalizer's approved-term list only held greeting portmanteaus for the units of
*previous* episodes' hosts, so when the pair rotated to Leo/need and WxS it had
nowhere to put listeners' greetings and failed the format stage outright. Added
`コンワンダホイ`. **Whenever the host pair comes from a new unit, check this list
first.**

Also added `drop_unusable_edits` to the proseka chain: a single hallucinated edit
used to abort the whole run, nondeterministically.

### Diarization over-segmentation

Transcription returned 3 labels for 2 speakers, as expected. Here the extra label was
the song rather than a mis-split host, so no `assign-speakers` pass was needed.

## Output state

- 817 dialogue lines, 424 Ruriko / 393 Machico
- Slot styles: `\an7`, MarginL 330, MarginR 50, MarginV 186 / 726; **no `\pos` tags** —
  position lives in the style, so retagging a speaker in Aegisub moves the line
- 0 same-slot overlaps, 0 sub-500ms lines
- 35 cues were split by line breaking and persisted into the JSON
- Speaker attribution reassigned 199 of 815 lines from the diarizer

Not yet done: human QC pass, hardsub.
