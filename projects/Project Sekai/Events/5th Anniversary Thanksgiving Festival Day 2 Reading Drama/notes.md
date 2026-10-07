# 5th Anniversary 感謝祭 Day 2 — Reading Drama

| Name | Description |
| --- | --- |
| [BV1DVsAzqEiv](https://www.bilibili.com/video/BV1DVsAzqEiv/) | Clean source (the `.mkv`), 19:59 |
| [BV1nnsKz8ELd](https://www.bilibili.com/video/BV1nnsKz8ELd/) | Chinese fansub; burned-in subs OCR'd to `reference_zh.srt` (shifted +25.62s onto the clean video) |

Profile: `proseka/5th_kanshasai_drama` (extends `proseka/reading_drama`).

## Handover (2026-09-27)

**Status:** the first full pass is done. `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.ass` is the finished, styled
subtitle file. It has not been reviewed by a human or hardsubbed yet.

### Setting up on a new machine

1. **Profiles.** `profiles/` here holds copies of `reading_drama.toml` and `5th_kanshasai_drama.toml`.
   autosub's `profiles/local/` is gitignored, so they aren't anywhere else. Copy them to
   `autosub/profiles/local/proseka/` before running any autosub stage.
2. **Videos.** Both `.mkv`s are gitignored. Re-download them with `yt-dlp` from the links above; the audio
   format used was `30280`.
   - Save the clean source as `5th Anniversary Thanksgiving Festival Day 2 Reading Drama.mkv`.
   - The fansub is only needed if you want to re-OCR `reference_zh_fansub.mkv`. `reference_zh.srt` already has it.
3. **Fonts.** The final `.ass` uses **Lato ExtraBold**. Install it, or renders fall back to another font.

### Next steps

1. **Review pass** (see the [[subtitle_review_guide]], `projects/subtitle_review_guide.md`):
   - Check the low-confidence speakers listed below, especially 9:19, which may be Mizuki rather than Rui.
   - Resolve the open questions at the bottom.
   - Edit the text in Aegisub on the final `.ass`, or in `_translated.json`.
2. **If you re-run postprocess**, it overwrites the final `.ass` with plain Arial styles. Re-apply the layout with:
   ```bash
   uv run autosub postprocess "<stem>_translated.json" --profile proseka/5th_kanshasai_drama \
     --out "<stem>_postprocessed.json" --ass-out "<stem>.ass"
   python3 scripts/restyle_final_ass.py "<stem>.ass"
   ```
   The restyle script is idempotent.
3. **If you change a speaker**, edit `speaker` in `_translated.json` (the cue and its `words[]`). Then re-run
   step 2. You only need to re-translate if you want the LLM to re-voice the line.
4. **Hardsub** only the finished, restyled `.ass`.

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

## Low-confidence speaker attributions (review these)

| Time | Line |
| --- | --- |
| 2:34–2:40 | サビで紙吹雪が舞ってたのも良かったよね… |
| 3:23–3:31 | 確かに、… |
| 3:46–4:03 | あ。 奏さん大丈夫でしたか?… |
| 5:43–5:46 | ああ、瑞希、そうだよ。… |
| 5:50 | 奏ちゃん。 |
| 7:57 | 本当に、絵面が可愛くて、笑っちゃうな |
| 8:06 | 瑞希の出はないでしょ。 |
| 9:05 | すごい喋る。 |
| 9:19 | ほら、類でに言われてるよ。 (resolved: Mizuki addressing Rui) |
| 9:25 | いや、全然可愛くない。 |
| 9:47, 10:02 | か。かっこいい声? / やっ。やってみる。 |
| 10:31 | 違和、違和感あった? |
| 11:24–11:43 | 今、出番だんじゃ? / わかったの? / 断ってもいいんだよ。 |
| 12:52–13:15 | Rap aftermath: An's fan service and Nene's kid role |
| 13:23 | 草薙さんやってうまいな。 |
| 14:58 | これ、すごいです。 |
| 15:30, 15:41 | 褒め褒めファンサ? / いや。 |
| 16:01–16:07 | 出番かなって立ち上がったよ、類。 / みんな? |
| 17:03–17:10 | うわあ。 / 気持ち。 / 溜まるぞ。 |
| 17:39–17:44 | 盛大な拍手を! / 最高です! |
| 18:18–18:28 | うん! 言葉でも… / パレードをやったら… |

## Open questions

- Is the Minori flashback a pre-recorded Minori voice, or a cast member? It's attributed to Minori.
- Honorifics: the profile says to drop さん/くん/ちゃん, but the LLM kept many of them
  ("Kanade-san", "Kusanagi-san", "Rui-kun"). The result is inconsistent: "Kusanagi" appears in some
  lines and "Kusanagi-san" in others.
- ハッピー偉いぞビーム was translated as "Happy Airi Beam". The fansub heard "happy arise beam".
  It's probably an 愛莉/偉い pun.
- ASR-garbled lines where the translation is a guess: An's rap (11:58), Nene's rap line (12:37).
