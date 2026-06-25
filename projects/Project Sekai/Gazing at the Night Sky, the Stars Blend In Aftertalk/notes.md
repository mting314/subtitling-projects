# Gazing Upon the Night Sky's Fading Stars Aftertalk

**Commit prefix**: `saki7`

> **English title is a working translation** of 仰ぐ夜空に、星は紛れて — confirm/adjust before publishing.
> The folder, mkv, and output files are named after it, so renaming later means renaming those too.

## Event Details

- **Event name (JP)**: 仰ぐ夜空に、星は紛れて (event id 188)
- **Event name (EN)**: Gazing Upon the Night Sky's Fading Stars
- **Unit**: Leo/need (レオニード)
- **Focus character**: Saki Tenma (天馬咲希)
- **Host VA**: Karin Isobe (礒部花凜) — VA of Saki Tenma
- **Event run (in-game)**: 2025-11-30 → 2025-12-08 (marathon event)
- **Stream date**: 2025-12-08 (Mon) 21:30 JST (right after event end)
- **Commissioned song**: 花結び (Hanamusubi)
- **Composer / lyricist**: 栗山夕璃 (Kuriyama Yuuri)

### Episode Titles
1. ワンマン決起会！ (One-Man Live Kickoff!)
2. 心繋がる音 (The Sound That Connects Hearts)
3. 微かな違和感 (A Faint Unease)
4. あの頃の記憶 (Memories of Those Days)
5. ワンマン当日 (The Day of the One-Man Live)
6. Leo/needの音楽を (Leo/need's Music)
7. 熱狂、そして (The Frenzy, and Then)
8. 気づいた想いは (The Feelings She Realized)

> Episode-title English renderings are working translations — confirm before publishing.

### Story Premise
Leo/need works toward their first solo ("one-man") live. Saki Tenma confronts a faint
unease and memories from "those days" on the way to the show. (TBD — flesh out after
scoping the video / reading the event story.)

> Source: sekai-world master DB (events / eventMusics / musics / eventStories.json),
> pulled via `curl` — see `aftertalk_project_setup.md`. sekai.best itself is a JS app and
> WebFetch is gated off, so use the raw master-db JSON instead.

## Segments

> Scope these by skimming the video: cut the intro delay, the in-stream story
> watchalong(s), and the MV viewing(s); keep the host's talking segments.
> Fill in the kept ranges below, then mirror them into the autosub command.

Cuts to remove (everything else is kept):
- start → TBD — intro delay
- TBD → TBD — story watchalong
- TBD → TBD — MV viewing
- TBD → end — outro

Kept segments (transcribed + translated):
- TBD → TBD
- TBD → TBD

## Command (full pipeline — review/adjust segments before running)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Gazing at the Night Sky, the Stars Blend In Aftertalk/Gazing at the Night Sky, the Stars Blend In Aftertalk.mkv" \
  --profile proseka/leoneed \
  --backend chirp_3 \
  --start 00:00:00 --end 00:00:00 \
  --start 00:00:00 --end 00:00:00 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

> Replace the `--start/--end` pairs with the kept segments above (repeatable, one pair
> per kept range). For Docker remote execution, prefix with `./scripts/remote.sh "<mkv>"`.

## Profile
- `proseka/leoneed` (extends `proseka/aftertalk`; Leo/need cast preconfigured)

## Leo/need Cast
- 野口瑠璃子 (Noguchi Ruriko) — 星乃一歌 (Ichika Hoshino)
- 礒部花凜 (Isobe Karin) — 天馬咲希 (Saki Tenma) ← host
- 上田麗奈 (Ueda Reina) — 望月穂波 (Honami Mochizuki)
- 中島由貴 (Nakashima Yuki) — 日野森志歩 (Shiho Hinomori)

## VA
- 礒部花凜 (Isobe Karin)

## Notes
TBD — fill in after editorial pass

## YouTube Title
[ENG SUB] Gazing Upon the Night Sky's Fading Stars Aftertalk (feat. Saki's VA)

## YouTube Blurb (draft)
TBD — draft after editorial pass per `~/.claude/.../youtube_blurb_style.md`

## Source
- Original video: https://www.youtube.com/watch?v=kK3aZTzvyGs
- Video ID: kK3aZTzvyGs | Duration: 1:02:48

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Gazing at the Night Sky, the Stars Blend In Aftertalk/Gazing at the Night Sky, the Stars Blend In Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=kK3aZTzvyGs"
```
