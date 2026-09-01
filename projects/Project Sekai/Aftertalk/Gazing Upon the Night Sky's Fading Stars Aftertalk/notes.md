# Gazing Upon the Night Sky's Fading Stars Aftertalk

**Commit prefix**: `saki7`

> **English title (FINAL): "Gazing Upon the Night Sky's Fading Stars"** (仰ぐ夜空に、星は紛れて).
> Confirmed 2026-07-01; folder, mkv, `.ass`, and all output files renamed to match (was
> the working title "Gazing at the Night Sky, the Stars Blend In"). In-file event-title
> mentions all synced to this form during the QC pass.

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

Determined from gaps in the rendered subtitle timeline (re-derived after human QC,
2026-07-01). Human QC added a corrected opening at 9:43 (after the OP), so the earlier
opening block at 2:45–5:26 (Block A) is a duplicate and is CUT.

Cuts to remove (everything else is kept):
- 0:00:00 → 0:09:42 — intro delay + duplicate opening (Block A) + OP/PV (silent)
- 0:27:40 → 0:36:05 — Episode 4 story watchalong (in-game story audio)
- 0:51:00 → 0:52:25 — "Hanamusubi" 2DMV viewing (song lyrics)
- 1:00:09 → end — outro

Kept segments (host's talk — hardsub these):
- 0:09:42 → 0:27:40
- 0:36:05 → 0:51:00
- 0:52:25 → 1:00:09

## Command (full pipeline — review/adjust segments before running)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Aftertalk/Gazing Upon the Night Sky's Fading Stars Aftertalk/Gazing Upon the Night Sky's Fading Stars Aftertalk.mkv" \
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
[ENG SUB] Gazing Upon the Night Sky's Fading Stars Aftertalk feat. Karin Isobe (Saki's VA)

## YouTube Blurb
This episode of ProSeka AfterTalk has Karin Isobe (voice of Saki Tenma) covering the Leo/need event "Gazing Upon the Night Sky's Fading Stars," a heavy story where Saki, on the road to the group's first one-man live, gets pulled back into the loneliness of her hospital past and quietly decides to keep her feelings to herself so she can stay by everyone's side. Hosting solo, she reads through viewer messages and rewatches Episode 4 with the audience, digging into why Saki's usual brightness makes those buried emotions land even harder.

She reflects on voicing Saki after all these years, how there's barely any friction left between her and the character now, and how genuinely painful Episodes 4 and 8 were to record. She walks through the new adventurer-themed card illustrations, noting that only Saki's cloak is a flat yellow instead of a gradient to signal her hiding her true feelings, that even her covered mouth is part of the design, and gushing over Honami's "MAMA" energy and the stars Saki cradles in the final art. She also breaks down the commissioned song "Hanamusubi" by Kuriyama Yuri and its just-released 2DMV, from the airy, no-room-to-breathe high chorus to the emotion she poured into every lyric, all while fretting that she's talking too much and fumbling the word "2DMV" one too many times.

Original video: https://www.youtube.com/watch?v=kK3aZTzvyGs

## Source
- Original video: https://www.youtube.com/watch?v=kK3aZTzvyGs
- Video ID: kK3aZTzvyGs | Duration: 1:02:48

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Aftertalk/Gazing Upon the Night Sky's Fading Stars Aftertalk/Gazing Upon the Night Sky's Fading Stars Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=kK3aZTzvyGs"
```
