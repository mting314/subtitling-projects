# We Escape to Survive Aftertalk

> Official Colorful Stage EN title: **"We Escape to Survive"**. JP: ボク達の生存逃走 (Cheerful Carnival, asset bundle `event_runaway_2023`).

**Commit prefix**: `mizu4`

## Event Details

- **Event name (JP)**: ボク達の生存逃走
- **Event id**: 93  |  **Type**: Cheerful Carnival  |  **Unit**: Nightcord at 25:00 (school_refusal)
- **Event dates**: 2023-04-30 → 2023-05-09
- **Stream date**: 2023-05-10 20:30 JST
- **Focus character**: Mizuki Akiyama (Nightcord at 25:00)
- **Host VA**: 佐藤日向 (Hinata Sato), solo host
- **Commissioned song**: キティ (Kitty)
- **Composer / Lyricist / Arranger**: ツミキ (Tsumiki)

### Episode Titles
1. 無意識のうちに (Without realizing it)
2. 自分らしくいられるように (So they can stay true to themselves)
3. 安心できる時間 (Time to feel at ease)
4. 迫る足音 (Approaching footsteps)
5. 向き合えないまま (Still unable to face it)
6. ボクの方法 (My way)
7. 生きるために (In order to live)
8. 怖いけど、それでも (Scared, but even so)

> Episode titles are working translations — flag for confirmation.

### Story Premise
With Mafuyu's activity in N25 increasingly restricted, Kanade and the others search for
what they can do for her. Mizuki tries to carve out time to work alongside Mafuyu so she
can find some peace of mind — but things don't go simply.

## Segments

**TBD — needs a skim of the downloaded video.** Standard AfterTalk cut pattern (mirror in the
Scoped with `scripts/scope_segments.py` (video-layout detector) and verified against its
boundary contact sheet (`..._segments.png`). Every boundary landed within ~1s of the true
transition.

Cuts to remove:
- start → 10:00 — intro/standby card (long delay)
- 15:00 → 30:04 — story recap watchalong
- 35:26 → 47:42 — song/MV watchalong
- 48:55 → 50:31 — song/MV watchalong
- 1:03:03 → end — outro card

Kept segments (transcribed + translated) — 24:07 total, ~37%:
- 10:00 → 15:00
- 30:04 → 35:26
- 47:42 → 48:55
- 50:31 → 1:03:03

> QC update: the auto-scoped pass flagged 54:46 → 1:00:11 as a "card gallery / MV
> watchalong" cut, but the human pass found it was actual discussion and kept it —
> so 50:31 → 54:46, 54:46 → 1:00:11, and 1:00:11 → 1:03:03 merged into one
> contiguous 50:31 → 1:03:03 segment. Hardsub was run against these 4 segments.

## Command (full pipeline)

Local (from the projects repo root):
```bash
uv run autosub run \
  "projects/Project Sekai/We Escape to Survive Aftertalk/We Escape to Survive Aftertalk.mkv" \
  --profile proseka/n25 --backend chirp_3 \
  --start 10:00 --end 15:00 \
  --start 30:04 --end 35:26 \
  --start 47:42 --end 48:55 \
  --start 50:31 --end 54:46 \
  --start 1:00:11 --end 1:03:03 \
  --chunk-size 30 --llm-reasoning-effort low --mark-chunks --save-log
```

Docker remote (unreliable local network — run from the autosub repo root, note the extra `projects/`):
```bash
./scripts/remote.sh \
  "projects/projects/Project Sekai/We Escape to Survive Aftertalk/We Escape to Survive Aftertalk.mkv" \
  run --profile proseka/n25 --backend chirp_3 \
  --start 10:00 --end 15:00 \
  --start 30:04 --end 35:26 \
  --start 47:42 --end 48:55 \
  --start 50:31 --end 54:46 \
  --start 1:00:11 --end 1:03:03 \
  --chunk-size 80 --llm-reasoning-effort medium --mark-chunks --save-log
```

## Profile
- `proseka/n25`

## VA
- 佐藤日向 (Hinata Sato)

## Notes
- Mizuki's focus event, solo host
- Cheerful Carnival event (event_runaway_2023)

## YouTube Title
TBD

## YouTube Blurb (draft)
TBD

## Source
- **URL**: https://www.youtube.com/watch?v=V5Gs4JghH84
- **Video**: プロセカアフタートーク ボク達の生存逃走編 (1:05:46)

### Download command (yt-dlp)
```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/Project Sekai/We Escape to Survive Aftertalk/We Escape to Survive Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=V5Gs4JghH84"
```
