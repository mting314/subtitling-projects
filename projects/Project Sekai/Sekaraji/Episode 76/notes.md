# Sekaraji Episode 76

> **Sekaraji** (セカラジ) #76 with Leo/need pair: Ruriko Noguchi (Ichika) and Yuki Nakashima (Shiho).

**Commit prefix**: `sekaraji76`

## Show Details

- **Show name (JP)**: セカラジ | **Latin subtitle on card**: "Project SEKAI RADIO"
- **Format**: WEB radio, **pre-recorded** (`※『セカラジ』は事前収録です`)
- **Schedule**: biweekly, Fridays 20:00 JST
- **Episode**: #76
- **Source**: <https://www.youtube.com/watch?v=aktf-pUL2Cw>
- **Upload date**: 2026-10-23
- **Duration**: 33:51 (2031s)
- **Theme corner**: 「天秤にかけたもの」

## Hosts

| Slot | VA (JP) | VA (romanized) | Character | Unit | Character colour |
| --- | --- | --- | --- | --- | --- |
| 1 | 野口瑠璃子 | Ruriko Noguchi | Ichika Hoshino (星乃一歌) | Leo/need | `#33AAEE` |
| 2 | 中島由貴 | Yuki Nakashima | Shiho Hinomori (日野森志歩) | Leo/need | `#22DDBB` |

Character colours from `sekai-story-indexer` `webapp/static/meta.json`.

## Corners

| From | Corner | What happens |
| --- | --- | --- |
| 00:00:05 | Opening Talk | Greetings (`コンニード` / `kon-needo`), self-intros, Leo/need pair talk |
| 00:03:56 | Exchange Notebook | Answering Episode 75 hosts Fumiya Imai & Rui Tanabe's Halloween costume (`仮装`) question |
| 00:07:14 | Listener Mail | General mail (`ふつおた`), bass practice song recs, `"Pentatonic"`, Thanks Festival (`感謝祭`) `"needLe"` live |
| 00:18:05 | Song | Leo/need song `"Sono Oto ga Naru Nara"` (`その音が鳴るなら`) |
| 00:20:17 | Theme Mail | Theme: 天秤にかけたもの ("Things weighed on the scales / tough choices") |
| 00:31:34 | Ending | Submissions info, next episode's relay question for Ep 77 MMJ hosts, sign-off |

## Transcription Command (`gemini-4-carbon`)

```bash
EP="projects/projects/Project Sekai/Sekaraji/Episode 76"
uv run autosub transcribe "$EP/Sekaraji Ep 76.mkv" \
  --profile proseka/sekaraji \
  --backend gemini \
  --gemini-model gemini-4-carbon \
  --speaker-map "$EP/speaker_map.toml" \
  --speakers 2 \
  -o "$EP/Sekaraji Ep 76_transcript.json"
```

## Source

- **URL**: https://www.youtube.com/watch?v=aktf-pUL2Cw
- **Video ID**: `aktf-pUL2Cw`

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Sekaraji/Episode 76/Sekaraji Ep 76.%(ext)s" \
  "https://www.youtube.com/watch?v=aktf-pUL2Cw"
```
