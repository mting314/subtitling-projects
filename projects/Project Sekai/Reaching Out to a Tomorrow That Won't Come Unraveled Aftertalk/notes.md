# Reaching Out to a Tomorrow That Won't Come Unraveled Aftertalk

**Commit prefix**: `mizu6`

## Event Details

- **Event name (JP)**: ほどけぬ明日に手を伸ばして
- **Focus character**: Mizuki Akiyama (Nightcord at 25:00)
- **Commissioned song**: 飾って (Kazatte)
- **Composer**: 大沼パセリ (Onuma Paseri)

### Episode Titles
1. 嬉しいニュース (Happy news)
2. 進む背中 (A back that pushes forward)
3. みんなみたいには (Not like everyone else)
4. 夢のきっかけ (The spark of a dream)
5. 抱く憧れ (Holding onto admiration)
6. ニーゴをご紹介！ (Introducing N25!)
7. 眩しい景色 (A dazzling view)
8. 思い描く未来 (The future they envision)

### Story Premise
With things settling down after the incident at the Asahina household, Mizuki's older sister Yuki returns to Japan for work — her brand is doing a pop-up store in Shibuya. Through catching up with Yuki and learning what sparked her sister's dream, Mizuki starts thinking about their own future and what they want to pursue.

## Segments

Cuts to remove (everything else is kept):
- start → 9:30 — intro delay
- 15:00 → 24:45 — story recap
- 35:45 → 37:55 — song watchalong
- 55:00 → end — outro

Kept segments (transcribed + translated):
- 00:09:30 → 00:15:00 (post-intro host segment)
- 00:24:45 → 00:35:45 (post-story discussion)
- 00:37:55 → 00:55:00 (post-MV to closing)

## Command (full pipeline)

```bash
./scripts/remote.sh \
  "projects/projects/Project Sekai/Reaching Out to a Tomorrow That Won't Come Unraveled Aftertalk/Reaching Out to a Tomorrow That Won't Come Unraveled.mkv" \
  run --profile proseka/n25 --backend chirp_3 \
  --start 9:30 --end 15:00 \
  --start 24:45 --end 35:45 \
  --start 37:55 --end 55:00 \
  --chunk-size 80 \
  --llm-reasoning-effort medium \
  --mark-chunks \
  --save-log
```

## Profile
- `proseka/n25`

## VA
- 佐藤日向 (Sato Hinata)

## Notes
- Mizuki's focus event, solo host
- Renewed AfterTalk format (Discord + email submissions)
- Story about Niigo members facing their futures, education/career paths
- 2026-06-02 Docker remote run: Gemini didn't engage thinking despite medium effort

## YouTube Title
TBD

## YouTube Blurb (draft)
Hinata Sato (voice of Mizuki) recaps the story, song, and illustrations for Mizuki's focus event, "Reaching Out to a Tomorrow That Won't Come Unraveled", in the ProSeka AfterTalk.

Watch her share surprisingly personal reflections on career choices and effort, get emotional about Mizuki finally finding a passion worth pursuing, and dress up to match the event illustration.

Original video: TBD
