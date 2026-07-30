# Grow Glorious Glow Aftertalk

> Official Colorful Stage EN title: **"Grow glorious glow"**. JP: Grow glorious glow (Marathon, asset bundle `event_grow_2024`).

**Commit prefix**: `shizu5`

## Event Details

- **Event name (JP)**: Grow glorious glow
- **Event id**: 151  |  **Type**: Marathon  |  **Unit**: MORE MORE JUMP! (idol)
- **Event dates**: 2024-12-11 → 2024-12-19
- **Stream date**: 2024-12-20 JST
- **Focus character**: Shizuku Hinomori (MORE MORE JUMP!)
- **Host VA**: 本泉莉奈 (Rina Honnizumi), solo host
- **Commissioned song**: はしる! とおく! とどく! (Hashiru! Tooku! Todoku!)
- **Composer / Lyricist / Arranger**: 薄塩指数 (Usushioshisuu)

### Episode Titles
1. 舞い込んだチャンス (A chance lands in her lap)
2. 圧倒的な光 (Overwhelming radiance)
3. 大きな差 (A vast gap)
4. 高みの覚悟 (Resolve for the summit)
5. あの頃の私は (The me from back then)
6. かつての面影 (Traces of the past)
7. オーラ (Aura)
8. たしかな一歩 (A sure step forward)

### Story Premise
MORE MORE JUMP! receives an invitation to audition for a cosmetics commercial for the major brand Gran Fleur. Shizuku is up against Yuu Hagiyama, a seasoned model with an overwhelming presence. The story follows Shizuku as she confronts the gap between them, draws on her growth as an idol, and ultimately earns her place in the CM alongside Hagiyama.

## Segments

Cuts to remove (everything else is kept):
- start → 00:09:54 — intro delay
- 00:13:09 → 00:21:36 — story watchalong
- 00:34:38 → 00:36:32 — cut
- 00:39:54 → 00:47:43 — cut
- 01:10:03 → end — outro

Kept segments (transcribed + translated) — fade-aware trimming (0.4s audio/video fade transitions):
- 00:09:54.52 → 00:13:09.88 (post-intro host segment)
- 00:21:36.40 → 00:34:38.56 (post-story discussion)
- 00:36:32.38 → 00:39:54.52 (discussion segment)
- 00:47:43.00 → 01:10:03.00 (card artwork breakdown to closing)

## Command (full pipeline)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Grow Glorious Glow Aftertalk/Grow glorious glow Aftertalk.mkv" \
  --profile proseka/mmj \
  --backend chirp_3 \
  --start 00:09:54 --end 00:13:10 \
  --start 00:21:36 --end 00:34:38 \
  --start 00:36:32 --end 00:39:54 \
  --start 00:47:43 --end 01:10:03 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

## Profile
- `proseka/mmj`

## VA
- 本泉莉奈 (Rina Honnizumi) — Voice of Shizuku Hinomori

## Notes
- Shizuku's 5th focus event, solo host
- Hardsub pipeline configured with Fontsize 100 / Margins 200/200/100, 3-row long line detection fix pass, and 0.4s fade-in/fade-out segment transitions.

## YouTube Title
[ENG SUB] Grow Glorious Glow Aftertalk feat. Rina Honnizumi (Shizuku's VA)

## YouTube Blurb (draft)

This episode of ProSeka AfterTalk has Rina Honnizumi (voice of Shizuku Hinomori) covering the MORE MORE JUMP! event "Grow Glorious Glow," where Shizuku auditions for a Gran Fleur cosmetics commercial and goes head to head with the seasoned model Yuu Hagiyama. Hosting solo this time, she watches Episode 7 with viewers and unpacks how Shizuku closes the gap with her rival by drawing on her Cheerful＊Days past.

She walks through the new card illustrations, pointing out the wings hidden in Shizuku's banner art and the swan metaphor behind the trained version, and admits she could stare at the artwork forever. She breaks down recording the "Gran Fleur" commercial, including the moment her and Hagiyama's lines synced perfectly on the first take without either of them hearing the other, and gushes over the commissioned song "Hashiru! Tooku! Todoku!" by Usushioshisuu. The episode closes on a heartfelt stretch about facing your own shortcomings and trusting that the light you're searching for will eventually reach you, right before she completely tangles herself up trying to say "2DMV" and "3DMV."

Original video: https://www.youtube.com/watch?v=XqkMAWc8y5w

## Source
- **URL**: https://www.youtube.com/watch?v=XqkMAWc8y5w
- **Video**: プロセカアフタートーク Grow glorious glow編

### Download command (yt-dlp)
```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Grow Glorious Glow Aftertalk/Grow glorious glow Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=XqkMAWc8y5w"
```
