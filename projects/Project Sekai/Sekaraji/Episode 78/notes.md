# Sekaraji Episode 78

> **Sekaraji** (セカラジ) #78 with Vivid BAD SQUAD pair: Tomomi Jiena Sumi (An) and Kent Ito (Toya).

**Commit prefix**: `sekaraji78`

## Show Details

- **Show name (JP)**: セカラジ | **Latin subtitle on card**: "Project SEKAI RADIO"
- **Format**: WEB radio, **pre-recorded** (`※『セカラジ』は事前収録です`)
- **Schedule**: biweekly, Fridays 20:00 JST
- **Episode**: #78
- **Source**: <https://www.youtube.com/watch?v=MTAKEOzS5Ac>
- **Upload date**: 2026-11-20
- **Duration**: 34:37 (2077s)
- **Theme corner**: 「これで仲直りしました」

## Hosts

| Slot | VA (JP) | VA (romanized) | Character | Unit | Character colour |
| --- | --- | --- | --- | --- | --- |
| 1 | 鷲見友美ジェナ | Tomomi Jiena Sumi | An Shiraishi (白石杏) | Vivid BAD SQUAD | `#00BBDD` |
| 2 | 伊東健人 | Kent Ito | Toya Aoyagi (青柳冬弥) | Vivid BAD SQUAD | `#0077DD` |

Character colours from `sekai-story-indexer` `webapp/static/meta.json`.

## Corners

| From | Corner | What happens |
| --- | --- | --- |
| 00:00:05 | Opening Talk | Greetings, self-intros, bumping into each other on the train |
| 00:06:10 | Exchange Notebook | Answering Episode 77 MMJ hosts' year-end question |
| 00:10:01 | Listener Mail | General mail (`ふつおた`) |
| 00:19:23 | Song | VBS song |
| 00:22:22 | Theme Mail | Theme: これで仲直りしました ("How we made up") |
| 00:32:20 | Ending | Submissions info, next episode's relay question, sign-off |

## Transcription Command (`gemini-4-carbon`)

```bash
EP="projects/projects/Project Sekai/Sekaraji/Episode 78"
uv run autosub transcribe "$EP/Sekaraji Ep 78.mkv" \
  --profile proseka/sekaraji \
  --backend gemini \
  --gemini-model gemini-4-carbon \
  --speaker-map "$EP/speaker_map.toml" \
  --speakers 2 \
  -o "$EP/Sekaraji Ep 78_transcript.json"
```

## Source

- **URL**: https://www.youtube.com/watch?v=MTAKEOzS5Ac
- **Video ID**: `MTAKEOzS5Ac`

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Sekaraji/Episode 78/Sekaraji Ep 78.mkv" \
  "https://www.youtube.com/watch?v=MTAKEOzS5Ac"
```
