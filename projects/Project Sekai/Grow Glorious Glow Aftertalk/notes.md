# Grow Glorious Glow Aftertalk

**Commit prefix**: `shizu5`

## Event Details

- **Event name (JP)**: Grow glorious glow
- **Focus character**: Shizuku Hinomori (MORE MORE JUMP!)
- **Commissioned song**: Hashiru! Tooku! Todoku! (走る！遠く！届く！)
- **Composer**: Usushioshisuu (薄塩指数)

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
Shizuku receives an invitation to audition for a cosmetics CM for the major brand Gran Fleur. She's up against Yuu Hagiyama, a seasoned model with an overwhelming presence. The story follows Shizuku as she confronts the gap between them, draws on her growth as an idol, and ultimately earns her place in the CM alongside Hagiyama.

## Segments

Cuts to remove (everything else is kept):
- start → 9:51 — intro delay
- 13:12 → 21:24 — story watchalong
- 34:38 → 36:31 — cut
- 39:54 → 47:44 — cut
- 1:10:06 → end — outro

Kept segments (transcribed + translated):
- 00:09:51 → 00:13:12 (post-intro host segment)
- 00:21:24 → 00:34:38 (post-story discussion)
- 00:36:31 → 00:39:54 (between cuts)
- 00:47:44 → 01:10:06 (post-MV to closing)

## Command (full pipeline)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Grow Glorious Glow Aftertalk/Grow glorious glow Aftertalk.mkv" \
  --profile proseka/mmj \
  --backend chirp_3 \
  --start 00:09:51 --end 00:13:12 \
  --start 00:21:24 --end 00:34:38 \
  --start 00:36:31 --end 00:39:54 \
  --start 00:47:44 --end 01:10:06 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

## Profile
- `proseka/mmj`

## VA
- 本泉莉奈 (Honnizumi Rina)

## Notes
TBD — fill in after editorial pass

## YouTube Title
Grow Glorious Glow Aftertalk (feat. Shizuku's VA)

## YouTube Blurb (draft)
TBD — draft after editorial pass per `~/.claude/.../youtube_blurb_style.md`
