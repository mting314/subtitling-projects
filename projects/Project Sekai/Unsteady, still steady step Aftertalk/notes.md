# Unsteady, still steady step Aftertalk

> Official Colorful Stage EN title: **"Unsteady, still steady step"**. JP: Unsteady, still steady step (Marathon, asset bundle `event_unsteady_2025`).

**Commit prefix**: `hona5`

## Event Details

- **Event name (JP)**: Unsteady, still steady step
- **Event id**: 173  |  **Type**: Marathon  |  **Unit**: Leo/need (light_sound)
- **Event dates**: 2025-07-15 → 2025-07-21
- **Stream date**: 2025-07-22 JST
- **Focus character**: Honami Mochizuki (Leo/need)
- **Host VA**: 中島由貴 (Yuki Nakashima), solo host
- **Commissioned song**: 透明なパレット (Transparent Palette)
- **Composer / Lyricist / Arranger**: Aqu3ra

### Episode Titles
1. 嬉しい知らせ (Happy news)
2. おめでとうパーティー (Congratulations party)
3. 新たな知らせ (New news)
4. 天秤 (Balance scale)
5. 後悔しないように (So as not to regret)
6. 動いて、知って (Act and learn)
7. 熱気と迷い (Heat and hesitation)
8. 決意 (Determination)

### Story Premise
Leo/need's professional career is building momentum with media interviews and their long-awaited first one-man live confirmed. However, just as preparation gets underway, an unexpected invitation to participate in a large-scale fan festival presents a dilemma. Honami and the band must carefully weigh their choices to find the path forward without regrets.

## Segments

Cuts to remove (everything else is kept):
- 00:39:10 → 00:42:15 — song watchalong (no dialogue)
- 00:49:14 → end — outro

Kept segments (transcribed + translated) — fade-aware trimming (0.4s audio/video fade transitions):
- 00:00:00.00 → 00:39:10.00 (main episode talk & story breakdown)
- 00:42:15.00 → 00:49:14.00 (card artwork discussion & closing)

## Command (full pipeline)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Unsteady, still steady step Aftertalk/Unsteady, still steady step Aftertalk.mkv" \
  --profile proseka/leoneed \
  --backend chirp_3 \
  --start 00:00:00 --end 00:39:10 \
  --start 00:42:15 --end 00:49:14 \
  --chunk-size 80 \
  --mark-chunks \
  --save-log
```

## Profile
- `proseka/leoneed`

## Leo/need Cast
- 野口瑠璃子 (Noguchi Ruriko) — 星乃一歌 (Ichika Hoshino)
- 磯部花凛 (Isobe Karin) — 天馬咲希 (Saki Tenma)
- 上田麗奈 (Ueda Reina) — 望月穂波 (Honami Mochizuki)
- 中島由貴 (Nakashima Yuki) — 日野森志歩 (Shiho Hinomori)

## VA
- 中島由貴 (Yuki Nakashima) — Voice of Shiho Hinomori (Leo/need)

## Notes
- Honami's focus event, solo host (Yuki Nakashima)
- Covers story (Chapter 8 watchalong), card illustrations, and the 2DMV for "Transparent Palette"
- Hardsub pipeline configured with Fontsize 100 / Margins 200/200/100, 3-row long line detection fix pass, and 0.4s fade-in/fade-out segment transitions.

## YouTube Title
[ENG SUB] Unsteady, still steady step Aftertalk feat. Yuki Nakashima (Shiho's VA)

## YouTube Blurb (draft)

This episode of ProSeka AfterTalk has Yuki Nakashima (voice of Shiho Hinomori) covering Honami's focus event "Unsteady, still steady step", where Leo/need has to choose between their long-awaited one-man live and an unexpected fan fes opportunity.

She walks through how she'd approach a decision like Honami's ("I just go by vibes"), shares her thoughts on the new card illustrations along with a wish for an LN logo merch patch, and breaks down "Transparent Palette" including the hidden apple pie note someone snuck into the Master chart.

Original video: https://www.youtube.com/watch?v=cbvTtSsc4e4

## Source
- **URL**: https://www.youtube.com/watch?v=cbvTtSsc4e4
- **Video**: プロセカアフタートーク Unsteady, still steady step編

### Download command (yt-dlp)
```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Unsteady, still steady step Aftertalk/Unsteady, still steady step Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=cbvTtSsc4e4"
```
