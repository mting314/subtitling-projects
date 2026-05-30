# At The End of The Unraveled Thread Aftertalk

**Commit prefix**: `shizu3` (TBD — confirm when first commit lands)

## Segments

Cuts to remove (everything else is kept):
- start → 9:54 — intro delay
- 14:21 → 27:42 — story review
- 29:22 → 48:31 — 3DMV viewing
- 1:11:24 → end — outro

Kept segments (transcribed + translated):
- 00:09:54 → 00:14:21 (post-intro host segment)
- 00:27:42 → 00:29:22 (transition between story review and 3DMV)
- 00:48:31 → 01:11:24 (post-MV: card discussion + song talk)

## Command (full pipeline — preferred for reproducibility)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/At The End of The Unraveled Thread Aftertalk/At The End of The Unraveled Thread Aftertalk.mkv" \
  --profile proseka/mmj \
  --backend chirp_3 \
  --start 00:09:54 --end 00:14:21 \
  --start 00:27:42 --end 00:29:22 \
  --start 00:48:31 --end 01:11:24 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

## Run history (this episode)

The first attempt used `--profile mmj` which silently fell through (subdir prefix required — see `~/.claude/.../autosub_profile_naming.md`). Format ran without the profile, so corners and the LLM normalizer never executed. Translation also failed initially with `httpx.ReadError` at the 60s OD-proxy timeout.

What was actually run, in order:

1. `autosub run ... --profile mmj` — transcribe + format succeeded (without profile), translate failed at chunk 1 (60s timeout)
2. `autosub translate <formatted.json> --profile mmj --chunk-size 30 --mark-chunks --save-log` — failed same way
3. Cherry-picked timeout fix `6cf5454` (300s HTTP timeout) onto report branch — didn't help (60s limit comes from OD proxy, not our client)
4. `autosub translate <formatted.json> --profile proseka/mmj --chunk-size 30 --llm-reasoning-effort low --mark-chunks --save-log` — succeeded (low reasoning kept individual chunks under 60s)
5. Renamed `translated.{json,ass,llm_trace.jsonl}` → prefixed with project stem
6. `autosub postprocess <translated.json> --profile proseka/mmj --out <prefixed>.json --ass-out <prefixed>_final.ass`
7. Manually re-injected chunk-boundary Comment markers into `_final.ass` from `_translated.ass` (PR #15 regression — see https://github.com/ahuei123456/autosub/pull/15#issuecomment-4427654543)

## Known gaps in current outputs

- **No corner segment markers** — would have come from format step with the proper profile. Skipping for now; can be added manually during review pass.
- **No LLM normalizer applied at format** — character names from STT may need manual cleanup during review (e.g., 雫 / Shizuku for the MMJ member).

To regenerate cleanly, re-run from scratch with the full command above. ~5 min wall + a fresh translate API charge.

## Profile
- `proseka/mmj`

## MMJ Cast
- 小倉唯 (Ogura Yui) — 花里みのり (Minori Hanasato)
- 吉岡真優 (Yoshioka Mayu) — 桐谷遥 (Haruka Kiritani)
- 降幡愛 (Furihata Ai) — 桃井愛莉 (Airi Momoi)
- 本泉莉奈 (Honnizumi Rina) — 日野森雫 (Shizuku Hinomori)

## VA
TBD — confirm host VA after watching opener

## Notes
TBD — fill in after editorial pass

## YouTube Title
TBD

## YouTube Blurb (draft)

This episode of ProSeka AfterTalk has Rina Honnizumi (voice of Shizuku Hinomori) covering the MORE MORE JUMP! event "At The End of The Unraveled Thread", where Shizuku confronts her past with Cheerful＊Days and faces Arisa head-on during a joint iHaz filming.

She walks through the new card illustrations, including Shizuku's stained-glass trained art and a viewer's observation that the costumes might be based on Thumbelina (swallows, frogs, and all). She also gives an extended, heartfelt take on Arisa's character, the complexity of jealousy in competitive idol life, and how pulling your perspective up "like a drone" helps you understand people better. Solo hosting today, and she's pretty proud of how put together she was.

Original video: TODO
