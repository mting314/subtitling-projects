# Kimi to Tsunagu Heart Beat Aftertalk

> JP: **君と繋ぐHeart Beat** (marathon event, asset bundle `event_heartbeat_2025`).
> No official Colorful Stage EN title yet (JP event ran 2025-10, EN server is roughly a year
> behind), so the romanized JP title is the working title.
>
> **Note the space: "Heart Beat", not "HeartBeat".** The official title and the finished
> `.ass` both use two words; the folder and the legacy transcript files use one. See
> [Filename inconsistency](#filename-inconsistency).

**Commit prefix**: `ichi6`

## Event Details

- **Event name (JP)**: 君と繋ぐHeart Beat
- **Event id**: 182  |  **Type**: Marathon  |  **Unit**: Leo/need (`light_sound`)
- **Event dates**: 2025-10-11 → 2025-10-19
- **Stream date**: TBD — she mentions the Thanks Festival was "the day before yesterday"
  and a movie Stage Greeting is "this coming weekend", so it pins to a couple of days after
  the Thanks Festival. Confirm before publishing.
- **Focus character**: Ichika Hoshino (Leo/need)
- **Host VA**: 野口瑠璃子 (Ruriko Noguchi), solo host
- **Commissioned song**: スター (Star)
- **Composer / Lyricist / Arranger**: 大漠波新 (romanization unconfirmed — verify before
  putting it in a blurb)

### Episode Titles
1. 新曲お披露目！ (Unveiling the new song!)
2. 芽生える気持ち (A budding feeling)
3. あふれるアイディア (Overflowing ideas)
4. 音に込めた想い (The feelings poured into the sound)
5. 驚きの通知 (A surprising notification)
6. 届く、繋がる (It reaches, it connects)
7. 連鎖 (Chain reaction)
8. 連なりの中心で (At the center of the chain)

> Episode titles are working translations — flag for confirmation.

### Story Premise
Leo/need have finished the new song for their solo show and preparations are moving along
steadily. Then Ichika sees an ad for the Virtual Singer Fan Festa, and her wish to write a
song for Miku starts to grow.

## Segments

Video runs **43:28**. Subtitles run 9:56 → 41:17, so both ends are card/standby padding.
Gaps below were derived from the finished `.ass` (any gap > 45s), then matched against what
she says on either side of each one.

Cuts to remove:
- `0:00 → 9:56` — intro/standby card (long pre-show delay)
- `16:44 → 25:06` — story watchalong. Two clips back to back: favourite-scene reel
  (16:44 → 22:39), then Chapter 8 (22:44 → 25:06)
- `34:19 → 36:09` — "Star" 3DMV watchalong
- `41:17 → end` — outro card

Kept segments (21:09 of 43:28, 48.7%):
- `9:56 → 16:44`
- `25:06 → 34:19`
- `36:09 → 41:17`

> **One judgment call.** A single 4-second line sits marooned between the two story clips at
> `22:39 → 22:44` ("that's a very Ichika way of thinking"). The kept list above drops it to
> keep the cut clean. Splice it back in as its own segment if you'd rather not lose the line.

## Pipeline status

**This is a legacy-pipeline project.** It predates the current autosub stage layout, so the
files here don't match the `_transcript.json` / `_original.ass` / `_translated.ass` naming
the other events use:

| File | What it is |
| --- | --- |
| `Kimi to Tsunagu Heart Beat Aftertalk.ass` | **The finished product.** 396 lines, styled, layout pass done |
| `... - Transcript.ass` | JA transcript (legacy). The Japanese of record for this event |
| `... - Transcript_en_comparison.html` | AI-vs-edited comparison report |
| `.srt` / `.vtt` / `.tsv` / `.txt` / `.json` | Legacy transcript exports |
| `raw_transcripts/` | Chirp 3 per-chunk JSON + merged |

> Two `.ass` files were removed in the trial-file sweep: the pre-edit
> `... - Transcript_en.ass`, superseded by the finished file, and
> `Kimi to Tsunagu HeartBeat Aftertalk.ass`, a 927-byte stub with zero dialogue lines whose
> own log read "No dialogue lines generated!". Both recoverable from git history. Watch the
> spacing when referring to what's left: the survivor is "Heart Beat", two words.

Done so far: transcript, translation, grammar/spelling pass, story cuts removed, undefined
styles fixed, positional layout pass (`31b175b`), editing in progress (`7e5e1b6`).

Not done: final QC, hardsub, upload. There is no `_hardsubbed.mp4` yet.

### If re-running on the current pipeline

```bash
uv run autosub run \
  "projects/Project Sekai/Aftertalk/Kimi to Tsunagu HeartBeat Aftertalk/Kimi to Tsunagu HeartBeat Aftertalk.mkv" \
  --profile proseka/leoneed --backend chirp_3 \
  --start 9:56 --end 16:44 \
  --start 25:06 --end 34:19 \
  --start 36:09 --end 41:17 \
  --chunk-size 80 --llm-reasoning-effort medium --mark-chunks --save-log
```

> Re-running would overwrite the hand-edited `.ass`. The finished file is the edited one, so
> only re-run into a scratch copy.

## Profile
- `proseka/leoneed`

## VA
- 野口瑠璃子 (Ruriko Noguchi) — Ichika Hoshino

## Styles

Character styles are `Ichika`, `Ichika - Shifted`, `Ichika - PiP` (223 / 62 / 111 lines).
Outline `&H00EEAA33` = Ichika's `#33AAEE`, taken from the indexer's `meta.json`.

These were originally defined as Shiho styles, copied from a Shiho episode and never
renamed, so all 396 lines silently fell back to Arial 48 with no colour or positioning.
Fixed in `31b175b` — worth checking for the same copy-paste error on any new episode.

## Filename inconsistency

The folder and the legacy files say "HeartBeat"; the official title and the finished `.ass`
say "Heart Beat". Renaming the folder would touch the `.mkv`, every legacy export, and the
Aegisub Project Garbage block's `Audio File` / `Video File` pointers, so it isn't a pure
rename. Left alone for now; decide before publishing, since the YouTube title should match
the official spelling.

## Notes

- Ichika's focus event, solo host. She notes it's her first AfterTalk in a long while, her
  first since the format's mini-renewal, and her first solo one in a while (the previous
  Ichika focus event had Shiho's VA on too).
- Marathon event, not Cheerful Carnival, so the team-name segment is her marathon team.

## YouTube Title
[ENG SUB] Kimi to Tsunagu Heart Beat AfterTalk ft. Ruriko Noguchi (Ichika's VA)

## YouTube Blurb
This episode of ProSeka AfterTalk has Ruriko Noguchi (voice of Ichika Hoshino) going through the story, card art, and new song for Leo/need's event, "Kimi to Tsunagu Heart Beat."

She follows Ichika's growing wish to write a song for Miku and wonders aloud where it leads, reads listener messages about the things that feel satisfying purely for their own sake, and answers one with a long detour about cooking far too many portions for herself, discovering her apartment no longer contains a knife, and cutting carrots with scissors instead. She loses her place entirely by the end of it. Then it's the card art one by one, starting with her marathon team named "Ichi", plus the 3DMV team's own notes before the "star" MV. She signs off on a busy stretch of ProSeka, with the Thanks Festival two days behind her and a movie stage greeting that weekend.

Original video: https://www.youtube.com/watch?v=UjWYMT969nE

## Source
- **URL**: https://www.youtube.com/watch?v=UjWYMT969nE
- **Video ID**: UjWYMT969nE
- **Video**: `Kimi to Tsunagu HeartBeat Aftertalk.mkv`, 43:28

### Download command (yt-dlp)
```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/Project Sekai/Aftertalk/Kimi to Tsunagu HeartBeat Aftertalk/Kimi to Tsunagu HeartBeat Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=UjWYMT969nE"
```
