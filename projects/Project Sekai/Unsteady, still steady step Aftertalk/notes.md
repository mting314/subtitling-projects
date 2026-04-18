# Unsteady, still steady step Aftertalk

**Commit prefix**: `hona5`

## Segments
- Song watchalong at 39:10 - 42:15 — cut this segment (no dialogue)
- Total duration: ~49:14

## Command

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Unsteady, still steady step Aftertalk/Unsteady, still steady step Aftertalk.mkv" \
  --profile proseka/leoneed \
  --backend chirp_3 \
  --start 00:00:00 --end 00:39:10 \
  --start 00:42:15 --end 00:49:14 \
  --chunk-size 80 \
  --save-log \
  --mark-chunks
```

## Profile
- `proseka/leoneed`

## Leo/need Cast
- 野口瑠璃子 (Noguchi Ruriko) — 星乃一歌 (Ichika Hoshino)
- 磯部花凛 (Isobe Karin) — 天馬咲希 (Saki Tenma)
- 上田麗奈 (Ueda Reina) — 望月穂波 (Honami Mochizuki)
- 中島由貴 (Nakashima Yuki) — 日野森志歩 (Shiho Hinomori)
