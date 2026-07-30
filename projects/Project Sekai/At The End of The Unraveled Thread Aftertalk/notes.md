# At The End of The Unraveled Thread Aftertalk

> Official Colorful Stage EN title: **"At The End of The Unraveled Thread"**. JP: ほどかれた糸のその先に (Marathon, asset bundle `event_thread_2023`).

**Commit prefix**: `shizu3`

## Event Details

- **Event name (JP)**: ほどかれた糸のその先に
- **Event id**: 85  |  **Type**: Marathon  |  **Unit**: MORE MORE JUMP! (idol)
- **Event dates**: 2023-02-10 → 2023-02-17
- **Stream date**: 2023-02-18 JST
- **Focus character**: Shizuku Hinomori (MORE MORE JUMP!)
- **Host VA**: 本泉莉奈 (Rina Honnizumi), solo host
- **Commissioned song**: 私は、私達は (Watashi wa, Watashitachi wa)
- **Composer / Lyricist / Arranger**: Guiano

### Episode Titles
1. 波乱の予感 (Premonition of trouble)
2. 過去と対峙する勇気 (Courage to face the past)
3. FutureにFeature！ (Feature on the Future!)
4. あの時のこと (Back then)
5. Cheerful＊Daysとして (As Cheerful＊Days)
6. アイドル大戦争！ (The Great Idol War!)
7. からまった糸 (Tangled thread)
8. 私が私でいること (Me being me)

### Story Premise
MORE MORE JUMP! secures their very first TV appearance. However, the MC for the program turns out to be Cheerful＊Days, the idol group Shizuku used to belong to. Facing an unexpected reunion and unresolved tension with Arisa, Shizuku finds the strength to face her past head-on and define what it means to be herself as an idol.

## Segments

Cuts to remove (everything else is kept):
- start → 00:09:53 — intro delay
- 00:14:21 → 00:27:44 — story review watchalong
- 00:29:33 → 00:48:30 — 3DMV viewing
- 01:11:23 → end — outro

Kept segments (transcribed + translated) — fade-aware trimming (0.4s audio/video fade transitions):
- 00:09:53.00 → 00:14:21.31 (post-intro host segment)
- 00:27:44.75 → 00:29:33.86 (transition between story review and 3DMV)
- 00:48:30.13 → 01:11:23.04 (post-MV: card discussion + song talk)

## Command (full pipeline)

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

## Profile
- `proseka/mmj`

## MMJ Cast
- 小倉唯 (Ogura Yui) — 花里みのり (Minori Hanasato)
- 吉岡真優 (Yoshioka Mayu) — 桐谷遥 (Haruka Kiritani)
- 降幡愛 (Furihata Ai) — 桃井愛莉 (Airi Momoi)
- 本泉莉奈 (Honnizumi Rina) — 日野森雫 (Shizuku Hinomori)

## VA
- 本泉莉奈 (Rina Honnizumi) — Voice of Shizuku Hinomori

## Notes
- Shizuku's focus event, solo host
- Hardsub pipeline configured with Fontsize 100 / Margins 200/200/100, 3-row long line detection fix pass, and 0.4s fade-in/fade-out segment transitions.

## YouTube Title
[ENG SUB] At The End of The Unraveled Thread Aftertalk feat. Rina Honnizumi (Shizuku's VA)

## YouTube Blurb (draft)

This episode of ProSeka AfterTalk has Rina Honnizumi (voice of Shizuku Hinomori) covering the MORE MORE JUMP! event "At The End of The Unraveled Thread", where Shizuku confronts her past with Cheerful＊Days and faces Arisa head-on during a joint filming for MMJ's first TV appearance.

She walks through the new card illustrations, including Shizuku's stained-glass trained art and a viewer's observation that the costumes might be based on Thumbelina (swallows, frogs, and all). She also gives an extended, heartfelt take on Arisa's character, the complexities of jealousy in competitive idol life, and how pulling your perspective up "like a drone camera" helps you understand people better. Solo hosting today, and she's pretty proud of how put together she was.

Original video: https://www.youtube.com/watch?v=fHymS-ZEr9w

## Source
- **URL**: https://www.youtube.com/watch?v=fHymS-ZEr9w
- **Video**: プロセカアフタートーク ほどかれた糸のその先に編

### Download command (yt-dlp)
```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/At The End of The Unraveled Thread Aftertalk/At The End of The Unraveled Thread Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=fHymS-ZEr9w"
```
