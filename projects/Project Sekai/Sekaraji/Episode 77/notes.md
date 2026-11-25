# Sekaraji Episode 77

> **Sekaraji** (セカラジ) #77 with MORE MORE JUMP! pair: Yui Ogura (Minori) and Rina Honnizumi (Shizuku).

**Commit prefix**: `sekaraji77`

## Show Details

- **Show name (JP)**: セカラジ | **Latin subtitle on card**: "Project SEKAI RADIO"
- **Format**: WEB radio, **pre-recorded** (`※『セカラジ』は事前収録です`)
- **Schedule**: biweekly, Fridays 20:00 JST
- **Episode**: #77
- **Source**: <https://www.youtube.com/watch?v=BpeH9Dhw338>
- **Upload date**: 2026-11-06
- **Duration**: ~33:35

## Hosts

| Slot | VA (JP) | VA (romanized) | Character | Unit | Character colour |
| --- | --- | --- | --- | --- | --- |
| 1 | 本泉莉奈 | Rina Honnizumi | Shizuku Hinomori (日野森雫) | MORE MORE JUMP! | `#99EEDD` |
| 2 | 小倉唯 | Yui Ogura | Minori Hanasato (花里みのり) | MORE MORE JUMP! | `#FFCCAA` |

Character colours from `sekai-story-indexer` `webapp/static/meta.json`.

## Corners

| From | Corner | What happens |
| --- | --- | --- |
| 00:00:05 | Opening Talk | Greetings + self-intros |
| 00:07:46 | Listener Mail | General mail |
| 00:16:21 | Song | MMJ song |
| 00:18:59 | Theme Mail | Theme: 理想のお仕事 ("Ideal job") |
| 00:28:57 | Ending | Exchange notebook (relay question for VBS cast), followed by "How was today? / Thanks Festival Setlog story" (30:51–33:07) and sign-off |

## YouTube Title
[ENG SUB] SekaRaji #77 (Setlog Clip) ft. Rina Honnizumi & Yui Ogura (Shizuku & Minori VAs)

## YouTube Blurb
This clipped ending segment from Project SEKAI WEB Radio "SekaRaji" #77 features MORE MORE JUMP! cast members Rina Honnizumi (voice of Shizuku Hinomori) and Yui Ogura (voice of Minori Hanasato).

After leaving a year-end question in the exchange notebook for the next Vivid BAD SQUAD cast pair, the two reminisce about the ProSeka Anniversary Thanks Festival — including the viral Setlog vlog where Rina didn't realize she was supposed to record every hour, got walked through the app by Mayu Yoshioka (Haruka's VA), and ended up posting nothing all day except a single photo of her morning banana.

Original video: https://www.youtube.com/watch?v=BpeH9Dhw338
Clipped segment: 28:55–33:20

## Final Segment (Target)

Focusing on the final segment (Ending / Setlog story):
- `--start 00:28:55 --end 00:33:20` (Full Ending block: ~4m 25s)
- Core Setlog story: `00:30:51` – `00:33:07` (Rina sharing her story about downloading the Setlog app for the Thanks Festival, not understanding how it worked, and ending up only posting a photo of a morning banana)

## Command (Final segment run)

```bash
EP="projects/projects/Project Sekai/Sekaraji/Episode 77"
uv run autosub run "$EP/Sekaraji Ep 77.mkv" \
  --profile proseka/sekaraji \
  --backend chirp_3 \
  --speakers 2 \
  --speaker-map "$EP/speaker_map.toml" \
  --start 00:28:50 --end 00:33:20 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

## Source

- **URL**: https://www.youtube.com/watch?v=BpeH9Dhw338
- **Video ID**: `BpeH9Dhw338`

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Sekaraji/Episode 77/Sekaraji Ep 77.mkv" \
  "https://www.youtube.com/watch?v=BpeH9Dhw338"
```
