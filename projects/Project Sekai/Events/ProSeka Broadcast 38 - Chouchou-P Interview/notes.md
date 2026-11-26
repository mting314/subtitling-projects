# ProSeka Broadcast #38 — Chouchou-P Interview ("The name of painting")

> Creator interview from **「プロジェクトセカイ プロセカ放送局 #38」** (*ProSeka Broadcast Station #38*), opening corner **「ボカロミュージックのセカイ」** (*Sekai of Vocalo Music*), featuring **Minori Suzuki** (voice of **Ena Shinonome**), guest Vocaloid producer **Chouchou-P** (`蝶々P`, EN-server credit `papiyon`), and MC **Ai Shimizu**.

**Commit prefix**: `ena6-interview` (canonical event nickname: `ena6`)

## Broadcast & Event Details

- **Broadcast title (JP)**: プロジェクトセカイ プロセカ放送局 #38
- **Corner**: ボカロミュージックのセカイ (*Sekai of Vocalo Music*)
- **Stream date**: 2026-11-25 19:30 JST
- **Associated event**: **Colors of Pure Sense** (Event #184, `ena6`, Marathon, asset bundle `event_colors_2025`)
  - **Event dates (JP)**: 2025-10-31 → 2025-11-08 (EN: 2026-10-31 → 2026-11-08)
  - **Unit**: Nightcord at 25:00 (`school_refusal`)
  - **Focus character**: 東雲絵名 (Ena Shinonome — 6th focus event)
  - **Side characters**: 雪平実篤 (Yukihira-sensei, art teacher), 夏野二葉 (Futaba Natsuno, classmate)
- **Commissioned song**: **「その絵の名前は」** (*"The name of painting"* — exact EN-server title, `song_id: 597`)
  - **Lyrics / Composition / Arrangement**: 蝶々P
  - **SEKAI ver.**: Kanade, Mafuyu, Ena, Mizuki + Hatsune Miku · **Virtual Singer ver.**: Hatsune Miku · **Another Vocal ver.**: Ena
  - **SEKAI 2DMV**: illustration 猫目トヲル (Nekome Toworu), video まるいち (Maruichi)
- Chouchou-P's singer-songwriter alias: **一之瀬ユウ (Yu Ichinose)** — 一之瀬, not 一瀬/一ノ瀬.
- Title wordplay: JP 「その**絵**の**名**前は」 hides 絵名 (unintentional); EN "th**E** **NA**me of painting" hides "Ena" (intentional).

## Segments

Cuts to remove:
- `00:00:00` → `00:11:42` — Standby screen + show opening, Minori's corner debut, lineup & `#プロセカ放送局` X challenge
- `00:13:06` → `00:18:55` — Billboard Japan *Niconico VOCALOID SONGS* October 2026 Top 10 + Chouchou-P's commentary on the ranking and the "My Bat" MV clip
- `00:30:44` → `01:46:00` — Song MV playout, mini-skit, and main-cast game news half

Kept segments (13m 13s total):
- **Segment 1 (`00:11:42` → `00:13:06`)** — Chouchou-P guest entrance, career profile, "practically my first time on a show like this"
- **Segment 2 (`00:18:55` → `00:30:44`)** — Guest Q&A Corner (`ゲストさんへの質問コーナー`): title origin, lyrics, Minori's recording approach, Miku "like coming home", warm songs & gratin, sign-off

## Command (Full Pipeline)

Transcription on Chirp 3; translation on local Claude Opus through autosub's `claude-cli` provider (branch `claude-cli-provider`). No Gemini calls: the profile's normalizer is exact-only and reflow is deterministic. Run from the `autosub` repo root:

```bash
P="projects/projects/Project Sekai/Events/ProSeka Broadcast 38 - Chouchou-P Interview"
S="ProSeka Broadcast 38 - Chouchou-P Interview"

uv run autosub transcribe "$P/$S.mkv" --out "$P/${S}_transcript.json" \
  --profile proseka/housoukyoku_38_chouchoup --backend chirp_3 --speakers 3 \
  --start 00:11:42 --end 00:13:06 --start 00:18:55 --end 00:30:44

uv run autosub format "$P/${S}_transcript.json" --out "$P/${S}_original.ass" \
  --json-out "$P/${S}_logs/${S}_formatted.json" \
  --profile proseka/housoukyoku_38_chouchoup --speaker-map "$P/speaker_map.toml"

# AUTOSUB_CLAUDE_CLI_ARGS="--dangerously-disable-osx-sandbox" is only needed when
# autosub itself runs inside a sandboxed agent shell (nested macOS sandbox fails).
uv run autosub translate "$P/${S}_logs/${S}_formatted.json" \
  --out "$P/${S}_translated.json" --ass-out "$P/${S}_translated.ass" \
  --profile proseka/housoukyoku_38_chouchoup --speaker-map "$P/speaker_map.toml" \
  --model claude-opus-5-5 --llm-provider claude-cli --llm-reasoning-effort medium \
  --chunk-size 30 --reflow --mark-chunks --save-log

uv run autosub postprocess "$P/${S}_translated.json" --out "$P/${S}_translated.json" \
  --ass-out "$P/${S}_translated.ass" \
  --profile proseka/housoukyoku_38_chouchoup --speaker-map "$P/speaker_map.toml"
```

(`autosub run ... --model claude-opus-5-5 --llm-provider claude-cli` does the same in one go; stages were run separately here to verify diarization labels before formatting.)

## Profile
- `proseka/housoukyoku_38_chouchoup` (`autosub/profiles/local/proseka/housoukyoku_38_chouchoup.toml`, mirrored in [`profiles/housoukyoku_38_chouchoup.toml`](profiles/housoukyoku_38_chouchoup.toml)); extends `proseka/base`.

## Cast / Speakers
Chirp 3 labels were consistent across both ranges (no reconciliation needed):
- `"0"` **清水藍 (Ai Shimizu)** — Broadcast MC, `#22AA99` (same as Broadcast #34)
- `"1"` **蝶々P (Chouchou-P)** — Guest Vocaloid producer, `#8866DD`
- `"2"` **鈴木みのり (Minori Suzuki)** — Voice of Ena Shinonome, official Ena color `#CCAA88`

## Pipeline Run Notes (2026-11-25)
- **Transcription (`chirp_3`, `--speakers 3`)**: 2,610 words. 15 Chirp misreadings fixed via `[format.normalizer.replacements]` (その音の名前は → その絵の名前は, 一ノ瀬優 → 一之瀬ユウ, 突きつけられた歌詞が → 突きつけられた現実が, 世界/配信バージョン → セカイバージョン, コメとるさん → 猫目トヲルさん, …).
- **Format**: 205 Japanese cues (Ai 90 / Chouchou-P 59 / Minori 56).
- **Translate**: 7 chunks × ≤30 via `claude-opus-5-5` (`claude-cli`, effort medium), ~2 min total, ~10k prompt / ~1k output tokens per chunk. Postprocessed to **212** English cues (248 + 2 TL notes after QC/layout splits).
- A local WhisperX large-v3 attempt was abandoned: Japanese output is unpunctuated character-level with no diarization, and wav2vec2 alignment collapses under the song bed during the Q&A (e.g. 30:07–30:17 squashed into ~2s).

## QC & Layout (applied 2026-11-25)

All finishing edits were made directly in `_translated.ass` (as with #34); `_translated.json` still holds the raw postprocess output.

**Text QC**
- `23:33` "Chouchou-san's work" → "Chouchou-P-san's work" (only non-standard form).
- `22:57`–`23:03` repeated clause → "Until now, Ena probably believed this path was, / for her, as an artist, the very best one,".
- `21:37` MC reaction + new question split into two events at a 1.04s pause ("A song received with such care!" / "Now, for the lyrics, …").
- `26:13` reworded for length: "I always record one take of just my part of the SEKAI version,".

**Visual layout**
- **Restyled** from autosub's stacked slot styles (Fontsize 70, top-left) to the canonical `DefaultOnibe` set used in #34: `Lato ExtraBold 100`, bottom-center, `MarginL/R 200, MarginV 100`, speaker color in `OutlineColour`.
- **Lower-left 2DMV window** (`x ≈ 16–596, y ≈ 736–1064`) detected from the box's dark left border: `00:19:16.25`–`00:29:54.50` (MV hidden briefly at `23:39–23:43` and `28:08–28:17`; kept one continuous window so subs don't jump). **Lower-right question banner** (`x ≈ 1160–1850, y ≈ 946–1036`) is up throughout that window.
  - All lines overlapping the window use `<Speaker> - Shifted` (`MarginL 620, MarginR 100, MarginV 150`), same as #34: text clears the MV box on the left and sits above the banner.
- **Profile slide** (`00:12:01.4`–`00:12:38.0`, full-screen "蝶々P 代表作品" card): same treatment as #34. A semi-transparent `Panel` drawing at `(72,823)` 1777×183 covers the slide's Japanese PROFILE body, with Ai's profile reading on top in `Ai Shimizu - Slide` (`Fontsize 90`, `{\an5\pos(960,908)}`). The last line is trimmed to the slide's exit at `12:38.00`, and the panel and last line fade out together. (The slide's own bullets — piano-based, rock/ballad/jazz range; 5 songs incl. "E? Aa, Sou." and "Kokoro Bakashi" past 1M plays — are covered, not translated.)
- **Guest lower-third** ("ゲスト 蝶々P", `00:11:51.75`–`00:11:57.94`): the 6 overlapping lines get `{\pos(960,840)}` so they sit above it.

**Line length** (`scripts/detect_long_lines.py`)
- 44 flagged after the restyle. Removed autosub's hard `\N` breaks (laid out for the old size-70 layout) → 36. `scripts/autosplit_long_lines.py` (spaCy `dep`, transcript pause-snapping) applied 32 splits; then hand-fixed 4 pairs it split inside a quoted title or lyric or across a sentence end (`20:44`, `22:49`, `24:20`, `24:29`), and split/reworded the 4 deferred lines (`19:33`, `26:05`, `26:13`, `26:55`).
- Result: **250 renderable lines, 0 over 2 rows**, 0 same-speaker overlaps, 0 zero-duration cues.

**Outline contrast** (`scripts/check_outline_contrast.py --frames 16`, all pass ≥1.5×)
- Ai Shimizu 2.77× (Shifted 2.81×, Slide 2.86×) · Chouchou-P 4.04× · Minori Suzuki (official Ena `#CCAA88`) 2.02× (Shifted 2.08×). No override needed.

## Overlays

No image popups planned (no memes, VA cards, or banners discussed), so there is no `popups.json`; `hardsub_trim.py` will burn subtitles only.

Two `DefaultOnibe - TL Note` lines (top-center) explain the title wordplay, with the hidden letters in Ena's color (`\c&H0088AACC&`):
- `00:20:16.36`–`00:20:24.00`: "TL Note: The Japanese title その**絵**の**名**前は hides Ena's name, **絵名**."
- `00:20:39.60`–`00:20:59.00`: "TL Note: th**E** **NA**me of painting → **ENA**"

Both contain CJK/arrow glyphs: local renders use the macOS fallback, and the Docker image ships `fonts-noto-cjk`.

Remaining before release: hardsub + trim (segments `00:11:42–00:13:06`, `00:18:55–00:30:44`), YouTube title/blurb, upload.

## Source
- **URL**: https://www.youtube.com/watch?v=frerQO72DCk
- **Video Title**: プロジェクトセカイ プロセカ放送局 #38
- YouTube Japanese auto-captions saved at [`frerQO72DCk.ja-orig.vtt`](frerQO72DCk.ja-orig.vtt).

### Download command (yt-dlp)
```bash
uv run --with "yt-dlp[default]>=2026.08.01" yt-dlp --no-update --no-playlist \
  --js-runtimes node --remote-components ejs:github \
  -f "299+251/137+251/bv*[height<=1080][vcodec^=avc]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Events/ProSeka Broadcast 38 - Chouchou-P Interview/ProSeka Broadcast 38 - Chouchou-P Interview.mkv" \
  "https://www.youtube.com/watch?v=frerQO72DCk"
```
