# 5th Anniversary 感謝祭 Day 2 — Reading Drama

| Name | Description |
| --- | --- |
| [BV1DVsAzqEiv](https://www.bilibili.com/video/BV1DVsAzqEiv/) | Clean source (the `.mkv`), 19:59 |
| [BV1nnsKz8ELd](https://www.bilibili.com/video/BV1nnsKz8ELd/) | Chinese fansub; burned-in subs OCR'd to `reference_zh.srt` (shifted +25.62s onto the clean video) |

Profile: `proseka/5th_kanshasai_drama` (extends `proseka/reading_drama`).

## Handover (2026-09-27)

**Status:** The QC review pass, speaker attribution audit, gap-elimination pass, and manual edit integrations are complete.
- All 21 low-confidence speaker attributions and 4 open questions have been audited and resolved against the Japanese dialogue and Chinese fansub reference (`reference_zh.srt`).
- Speaker corrections applied:
  - 9:19 (`cue-00000180`): Rui -> Mizuki (`ほら、類でに言われてるよ。` where ASR misheard 奏に as でに; Mizuki teases Rui: "Look, Rui, even Kanade is telling you to.").
  - 14:58 (`cue-00000339`): An -> Ichika (`これ、すごいです。` polite reaction from Ichika after roleplaying with Kanade; matches speaker 4 diarization).
  - 3:02: An -> Nene ("Maybe you're just too fired up?").
- Translation corrections applied:
  - 3:23: "True." -> "Definitely."
  - 17:09 (`cue-00000391`): "It's building up..." -> "That was so thrilling..." (Airi's beam had already fired and the audience wave was finished; this was post-beam exhilaration).
- Honorifics standardized to bare names per profile rules (dropping -san, -kun, -chan while preserving -senpai and Rui's 02:46 seiyuu slip-of-the-tongue).
- Line length QC: `detect_long_lines.py` scanned all 434 renderable lines; tightened long lines (cues 40, 63, 66, 67, 68), resulting in **0 lines flagged with > 2 rows**.
- Gap elimination: applied `_close_screen_gaps` logic extending cue end times when $0 < \text{gap} < 500\text{ms}$; closed all 63 sub-500ms gaps (**0 sub-500ms gaps remaining**).
- Manual Aegisub edits integrated: off-screen reaction laughs at 02:48-02:50 (`{\pos(320,628)}Hehehehe...` for Mizuki and `{\pos(200,284)}Oh?` for An) preserved and tracked as split cues `cue-00000032-1` and `cue-00000032-2`.
- Synchronized `_postprocessed.json` and `_translated.json` to 434 cues matching the final `.ass`.
- Clean source video downloaded and present at `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.mkv`. Ready for final verification and hardsubbing.

### Setting up on a new machine

1. **Profiles.** `profiles/` here holds copies of `reading_drama.toml` and `5th_kanshasai_drama.toml`.
   Copied to `autosub/profiles/local/proseka/`.
2. **Videos.** Both `.mkv`s are gitignored. Clean source is downloaded at `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.mkv` (1080p, audio format 30280).
   - If re-downloading: `yt-dlp -f 30080+30280 --merge-output-format mkv -o "5th Anniversary Thanksgiving Festival Day 2 Reading Drama.mkv" https://www.bilibili.com/video/BV1DVsAzqEiv/`
   - The fansub is only needed if you want to re-OCR `reference_zh_fansub.mkv`. `reference_zh.srt` already has it.
3. **Fonts.** The final `.ass` uses **Lato ExtraBold**. Installed / present in `assets/fonts/`.

### Next steps

1. **Subtitle check in Aegisub**: Open `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.ass` with `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.mkv` for final visual verification.
2. **Hardsub**: Burn the finished, restyled `.ass` with `hardsub_trim.py`.
3. **Publish**: Prepare YouTube metadata and blurb.

### Scripts (`scripts/`, copied from `/tmp` so they survive)

| Script | Description |
| --- | --- |
| `voice_attr.py` | ECAPA voice attribution. Needs `/tmp/drama16k.wav`, made with `ffmpeg -i <stem>.mkv -ac 1 -ar 16000 /tmp/drama16k.wav`. Run with `uv run --python 3.12 --with speechbrain --with torch --with torchaudio --with soundfile python scripts/voice_attr.py <formatted.json> out.json`. `ANCHORS` indexes the 412-cue **raw** formatted file (`formatted_raw_diarization.json`). |
| `apply_attr.py` | Writes the final per-cue speaker table onto `formatted_raw_diarization.json` and merges the Virtual Singer cues. It is already applied, so don't run it on the current `_formatted.json`: the cue count assert fails. It imports autosub from `/Users/michaelting/github/autosub`, so fix that path on a new machine. |
| `restyle_final_ass.py` | Post-postprocess layout pass: styles, `\N` strip, `\an8` for Virtual Singers. |
| `ocr_textboxes.py` | macOS Live Text OCR of the in-game text box, which produced `virtual_singer_scenes_ja.json`. It needs the `ocrmac` package and only runs on macOS. |
| `ocr_hardsubs.py`, `align_audio.py` | OCR of the fansub's burned-in subtitles, and audio cross-correlation for the +25.62s offset. |

## Layout

- 0:33–1:59 and 18:50–19:53: in-game Virtual Singer scenes (RIN, LUKA, KAITO). Text came from OCR of the
  game text box (`virtual_singer_scenes_ja.json`), not ASR. Subs are top-aligned (`\an8`) so they don't
  cover the text box.
- 2:07–18:36: live reading drama. The Minori handshake flashback runs 6:32–7:38.

## How the transcript was built

- **Chirp 3 dropped speech** at 8:12–9:26 and 17:38–18:35 and returned nothing for those spans.
  Those spans were re-transcribed (`transcript_gaps.json`) and merged into `_transcript.json`.
  `transcript_chirp_raw.json` is the original output.
- **Diarization was unusable**: 7 voices collapsed into overlapping labels, and `--speakers 7`
  was ignored. `formatted_raw_diarization.json` keeps the raw labels.
- **Speakers were attributed** from text anchors (names, content, who's addressed), with SpeechBrain
  ECAPA voice embeddings checked against per-character centroids. Voice agreed with text on 89% of
  anchors. Voice is unreliable for cues under 0.8s, and for the role-play scenes where cast members do kid
  voices:
  - Rui plays the kid for Mizuki.
  - Mizuki plays the kid for Rui.
  - Nene plays the kid for An.
  - Kanade plays the kid for Ichika.
- No speaker map: slot layout doesn't fit a drama. Speakers are written straight into the JSON.
  Styles follow the AfterTalk convention (Lato ExtraBold 100, white fill, character colour in the outline).

## Manual edits after translation

- 2:22.80: the opening line was reworded.
- 8:52–9:03: the kid-fan lines were corrected from the zh reference.
  - "fan of your videos": the ASR had 東雲.
  - "Bake no Hana" (化けの花): the ASR had バケモノ花. The LLM had invented a song called 'Cinema'.
- Final `.ass`: manual `\N` breaks were removed so libass balances the lines at 100px.

## Speaker attribution audit & resolutions

| Time | Line | Resolution |
| --- | --- | --- |
| 2:34–2:40 | サビで紙吹雪が舞ってたのも良かったよね… | **Nene** (confirmed). Sets up Ichika's mention of Saki & Tsukasa, prompting Rui to explain Tsukasa took confetti from his house. |
| 3:23–3:31 | 確かに、… | **Nene** (confirmed). Banter with An regarding Akito's singing before Kanade chimes in at 3:40. |
| 3:46–4:03 | あ。 奏さん大丈夫でしたか?… | **Ichika** / **Kanade** / **Ichika** / **An** (confirmed). Ichika checks in on Kanade, who answers she managed because of the music. |
| 5:43–5:46 | ああ、瑞希、そうだよ。… | **An** (greeting Mizuki & Airi) / **Kanade** (mentioning Rui fumbled) (confirmed). |
| 5:50 | 奏ちゃん。 | **Airi** (confirmed). Directly answers Kanade's question ("どこにいたの?"). |
| 7:57 | 本当に、絵面が可愛くて、笑っちゃうな | **Nene** (confirmed). Reacts to the visual of Minori with the kids. |
| 8:06 | 瑞希の出はないでしょ。 | **An** (confirmed). Classic tsukkomi to Mizuki's proud parent moment. |
| 9:05 | すごい喋る。 | **Nene** (confirmed). Deadpans at Rui's rapid-fire child-fan act. |
| 9:19 | ほら、類でに言われてるよ。 | **Mizuki** (**fixed** from Rui). ASR garbled 奏に as でに; Mizuki teases Rui that Kanade told him to do it. |
| 9:25 | いや、全然可愛くない。 | **Nene** (confirmed). Instantly shuts down Rui asking if he makes an adorable child. |
| 9:47, 10:02 | か。かっこいい声? / やっ。やってみる。 | **Rui** (confirmed). Stammers when Mizuki asks for a "cool voice", then tries it out. |
| 10:31 | 違和、違和感あった? | **Mizuki** (confirmed). Asks Kanade if their fan service felt weird. |
| 11:24–11:43 | 今、出番だんじゃ? / わかったの? / 断ってもいいんだよ。 | **Nene** (confirmed). All three lines are Nene trying to pump the brakes while An rides the hype. |
| 12:52–13:15 | Rap aftermath: An's fan service and Nene's kid role | **An** & **Nene** (confirmed). An gives Nene street fan service; Nene shyly fist-bumps. |
| 13:23 | 草薙さんやってうまいな。 | **An** (confirmed). An casually remarks to the group on Nene's rap talent. |
| 14:58 | これ、すごいです。 | **Ichika** (**fixed** from An). Ichika was the recipient of Kanade's "お姉たん" act; matches speaker 4 in diarization. |
| 15:30, 15:41 | 褒め褒めファンサ? / いや。 | **Nene** (skeptical question at 15:30) & **Rui** (stepping in at 15:41) (confirmed). |
| 16:01–16:07 | 出番かなって立ち上がったよ、類。 / みんな? | **Mizuki** (16:01) & **Airi** (16:06) (confirmed). |
| 17:03–17:10 | うわあ。 / 気持ち。 / 溜まるぞ。 | **Mizuki** (17:03) & **Airi** ("気持ちいいー！" at 17:06) & **Kanade** (**fixed translation** at 17:09 to "That was so thrilling..."). |
| 17:39–17:44 | 盛大な拍手を! / 最高です! | **Rui** ("盛大な拍手を!") / **Ichika** & **An** ("最高です!") / **Airi** (confirmed). |
| 18:18–18:28 | うん! 言葉でも… / パレードをやったら… | **An** (18:18) / **Nene** (18:23) / **Rui** (18:29) (confirmed). |

## Open questions & resolutions

- **Is the Minori flashback a pre-recorded Minori voice, or a cast member?**
  Pre-recorded Minori voice (Yoshioka Mayu was not in the live cast for Day 2). Attributing to `Minori` with her character style is correct.
- **Honorifics:**
  Standardized by dropping `-san`, `-kun`, `-chan` as bare names across all lines per `reading_drama.toml` rules, while preserving `-senpai` (`Kamishiro-senpai`) and Rui's live slip-of-the-tongue at 02:46 (`Tsukasa-san... Tsukasa-kun`).
- **ハッピー偉いぞビーム translation:**
  Kept as "Happy Airi Beam!" as explicitly prompted by `5th_kanshasai_drama.toml` (reflecting Airi's name and the えらい/あいり pun).
- **ASR-garbled lines (An and Nene raps):**
  Freestyle rap translations maintained and tightened to preserve the rhythm and internal rhymes (e.g. Wandasho / samurai spirit / future expectations).

## YouTube Title
[ENG SUB] Project SEKAI 5th Anniversary Thanksgiving Festival Day 2 — Reading Drama

## YouTube Blurb (draft)
English subtitles for the Project SEKAI Colorful Stage! 5th Anniversary Thanksgiving Festival (感謝祭) Day 2 Live Reading Drama.

Original clean video: https://www.bilibili.com/video/BV1DVsAzqEiv/
