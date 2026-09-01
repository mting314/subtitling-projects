# Sekaraji Episode 72

> First **Sekaraji** (セカラジ) project. This is a Project Sekai *radio show*, not an
> AfterTalk — two hosts, still show cards, no story/MV watchalongs. It is the first
> ProSeka project that will use the **radio overlay** tech built for Lieraji.

**Commit prefix**: `sekaraji72`

**Pipeline branch**: `sekaraji`, cut from `feature/radio-overlay` (which already contains
`dev` + `hardsub-pipeline`). Isolated worktree at `/private/tmp/asub-sekaraji`.

Run everything from the worktree with **absolute paths** to files under `projects/`. The
main checkout is on `hardsub-pipeline`, which has neither `generate-overlay` nor
`multi_seiyuu_radio`, so it cannot run this show. And `projects` is registered in
autosub's index as a gitlink (mode 160000, no `.gitmodules`), so symlinking it into a
worktree makes every git command fail with *"expected submodule path 'projects' not to be
a symbolic link"* — the worktree keeps an empty `projects/` instead.

## Show Details

- **Show name (JP)**: セカラジ  |  **Latin subtitle on card**: "Project SEKAI RADIO"
- **Format**: WEB radio, **pre-recorded** (`※『セカラジ』は事前収録です`)
- **Schedule**: biweekly, Fridays 20:00 JST
- **Premise (from description)**: covers the appeal of *Project Sekai: Colorful Stage!
  feat. Hatsune Miku* and runs corners tied to each unit
- **Episode**: #72
- **Upload date**: 2026-08-28
- **Duration**: 36:25 (2185.26s)
- **Video**: 1920x1080 h264 / opus, 30fps. Audio-only content over **two** still cards —
  see [Background](#background--overlay)

## Hosts

| Slot | VA (JP) | VA (romanized) | Character | Unit | Character colour |
| --- | --- | --- | --- | --- | --- |
| 1 | 本泉莉奈 | Rina Honnizumi | Shizuku Hinomori (日野森雫) | MORE MORE JUMP! | `#99EEDD` |
| 2 | 鈴木みのり | Minori Suzuki | Ena Shinonome (東雲絵名) | Nightcord at 25:00 | `#CCAA88` |

Cast order on the card is Shizuku (left) / Ena (right); the description lists them
`順不同` (no particular order).

Both VAs are already covered by existing profiles — Rina Honnizumi in `proseka/mmj`,
Minori Suzuki in `proseka/n25` — but neither profile is right on its own here (see
[Profile](#profile--done)).

### Colour source + one discrepancy to settle

Colours above come from `meta.json` in `sekai-story-indexer`
(`~/github/sekai-story-indexer/webapp/static/meta.json`), which is the documented
ProSeka source in `docs/speaker_colors.md`. They also match the name-banner tints on
the show card itself (mint for Shizuku, tan for Ena).

**But the shipped AfterTalk `.ass` files disagree for Ena:**

| Character | `meta.json` | Existing `.ass` outline | Match? |
| --- | --- | --- | --- |
| Shizuku | `#99EEDD` | `&H00DDEE99` → `#99EEDD` | yes |
| Ena | `#CCAA88` | `&H005D8CBA` → `#BA8C5D` | **no** — the `.ass` uses a darkened variant |

Settled on `#CCAA88`, for consistency with the card art. It is a light tan, and the
convention in `docs/speaker_colors.md` puts the colour in the **outline** over a white
fill, which reads fine — but see the bar-contrast problem below, which affects both
hosts.

## Background / Overlay

Measured by sampling a frame every 5s across the whole episode and diffing: the video is
**exactly two still cards**, with a ~1.25s crossfade between them. Nothing else moves.

| From | To | Card |
| --- | --- | --- |
| 00:00:00 | 00:21:15 | Main show card — chibi Shizuku left, chibi Ena right, big "72", VA headshots + name banners along the bottom |
| 00:21:15 | 00:32:25 | **お便り募集!** ("Send us your mail!") card — show logo + `sekairadio@pjsekai.jp` |
| 00:32:25 | 00:36:25 | Main show card |

Crossfade centres: 21:15.4 and 32:25.5.

That 11-minute mail card turned out to bracket the **Theme Mail** corner exactly — see
[Corners](#corners--recovered).

Because the background is not a single still, don't reuse Lieraji Ep 277's
`still_background.png` → `radio_background_with_overlay.png` route. Composite the
generated overlay straight onto the source video instead — same result, keeps the card
change, and no extra assets:

```
speaker_map.toml  →  autosub generate-overlay  →  overlay.png (VA cards + subtitle bars)
ffmpeg: mkv + overlay.png (ffmpeg `overlay` filter) + ass=<translated.ass>  →  hardsub
```

### Overlay render — done, one problem

`overlay.png` is generated and composites correctly: 2 slots stacked vertically, cards
down the left edge, face crops framed right, name banners in the correct character
colours, Lato ExtraBold throughout.

```bash
uv run autosub generate-overlay -s "$EP/speaker_map.toml" -o "$EP/overlay.png"
```

The map's `avatar` paths are relative to the map itself (`../official_cast_photos/...`).
That needed a small fix in `load_speaker_map`: it now falls back to resolving an avatar
beside the map when the path doesn't resolve from the working directory. Previously every
avatar path was cwd-relative, so a map only worked when run from the repo root — which
silently produces blank cards anywhere else, including on a remote box.

Two things to decide:

1. **The subtitle bars barely darken this background.** The bars are `rgba(10,10,14,120)`,
   designed against Lieraji's dark wooden studio art. Sekaraji's card is near-white, so
   the composited bar lands at about `#8C8B8E` — **3.39:1 against white text**. That
   scrapes past the WCAG 3.0:1 large-text floor and no further, and the coloured outline
   can't rescue it (same argument as `docs/speaker_colors.md` makes for Aoyama's navy).
   Raising the bar alpha for this show is the obvious fix; needs a number picking.
2. **The cards cover the chibi Shizuku art** on the left, as expected. Lieraji does the
   same and reads fine. The source card *also* has its own VA headshots along the bottom,
   so the overlay duplicates them — arguably fine (ours are labelled in English), arguably
   worth moving the cards right.

### Avatars

Both sourced, in `projects/Project Sekai/official_cast_photos/`. The generator face-crops raw
portraits automatically (anything narrower than the card's aspect ratio gets reframed), so
these are referenced directly — no pre-cropped `avatars/` needed yet.

| VA | Source | Size |
| --- | --- | --- |
| Rina Honnizumi | `rina_honnizumi.webp` — Project Sekai wiki press photo | 850x1142 |
| Minori Suzuki | `minori_suzuki.webp` — Project Sekai wiki press photo | 1000x1500 |

> **Updated.** These photos were promoted out of this episode folder to the franchise-level
> `Project Sekai/official_cast_photos/`, since Sekaraji and the AfterTalks share one VA pool.
> `minori_suzuki.webp` was previously duplicated in We Escape to Survive Aftertalk as
> `Minori.webp`; that byte-identical copy is gone and the event now resolves the shared one.
> The `CAST.md` suggested below now exists at `Project Sekai/CAST.md`.
> `LATO-EXTRABOLD.TTF` no longer ships per-folder either — one copy lives at
> `assets/fonts/`, found by walking up from the project dir.

## Profile — done

None of the existing profiles fit: `proseka/aftertalk` has the right ProSeka vocabulary
but `extends = ["solo_seiyuu_radio"]` with AfterTalk-only prompt and corners;
`multi_seiyuu_radio` has the two-host framing but no game knowledge. So the game knowledge
was split out:

```
proseka/base       game vocab + glossary + ProSeka style rules + LLM normalizer
 ├── proseka/aftertalk  = extends ["solo_seiyuu_radio", "proseka/base"]
 └── proseka/sekaraji   = extends ["multi_seiyuu_radio", "proseka/base"]   (new)
```

`proseka/sekaraji` carries the show framing, Sekaraji's own conventions, the **full
20-character cast roster** (any unit may host, and hosts discuss other units), and the six
corners. It deliberately has **no `[[speakers.cast]]`** — the host pair rotates every
episode, so who's on mic comes from this folder's `speaker_map.toml`, same as Lieraji.

### Careful: `profiles/local/` shadows the tracked profiles

`profiles/local/proseka/*` is where the real accumulated show knowledge lives, and
`_profile_search_dirs()` searches `local` first — so it wins at runtime. It is also
gitignored, so none of it is in git. The tracked `profiles/proseka/*` is a much thinner
older copy (n25: 22 lines tracked vs 69 local; leoneed 26 vs 79). **The split was done in
`local/`**, because that is what actually runs.

### Verified behaviour-neutral for AfterTalk

Resolved `proseka/aftertalk` and `proseka/mmj` before and after the split:

| | Result |
| --- | --- |
| vocab | identical sets (42 / 51) |
| glossary | identical |
| corners | identical |
| prompt | same rules, reorganized headers — no rule text lost |
| normalizer | **one deliberate change**, below |

The normalizer model was `gemini-3.1-flash-lite-preview`, which now 404s and takes the
format step down with it. `proseka/base` sets `gemini-2.5-flash-lite`, which is what this
branch defaults classification and normalizer extensions to. This affects AfterTalk too —
it's a fix, not a side effect, but it is a real change.

`tests/test_profile_extensions.py::test_profile_extending_two_bases_accumulates_both`
pins the two-base merge contract the split depends on. Full suite: 477 passed.

### Corners — recovered

Not listed in the YouTube description, and `pjsekai.sega.jp/sekaraji/` 404s. Recovered
instead from **YouTube's `ja-orig` auto-captions**, which this video has (`--write-auto-subs
--sub-langs ja-orig`). That's a free discovery pass — no STT spend, no API calls. Six
corners are now written into `proseka/sekaraji.toml`.

| From | Corner | What happens |
| --- | --- | --- |
| 00:00:05 | Opening Talk | Greetings + self-intros, then free chat (summer homework, holiday trips). Ends `それではセカラジ今回もよろしくお願いします` at 03:16 |
| 00:03:26 | Contact Notebook (連絡ノート) | Sponsor credit, second self-intro, then they answer the question the *previous* episode's hosts left them |
| 00:08:44 | Listener Mail | Untimed general mail. Radio names 4B, つき |
| 00:18:24 | **Song** | `ここで1曲お届けします` → `それではお聞きください`. A Shizuku-focused song, sung in full |
| 00:21:11 | Theme Mail | Theme: 秋に楽しみなこと ("what you're looking forward to this autumn") — matches the お便り募集 card |
| 00:32:33 | Ending | Address, `次回もユニットシャッフル`, they leave a new notebook question ("人生最大の忘れ物は何ですか?"), sign-off, sponsor outro |

Two things worth knowing beyond this episode:

- **連絡ノート is the show's running relay.** Each pair answers the previous pair's question
  and leaves one for the next. It bookends the episode — the answering half is its own
  corner, the asking half sits inside the Ending.
- **`次回もユニットシャッフル`** — the hosts confirm on air that the pairing rotates by unit
  every episode. That's why the profile carries the whole cast roster and no fixed cast.

The corners are written from one episode only. Verify against a second before treating
them as settled.

## Segments

**One cut: the song at ~18:48–21:05.** The auto-caption pass found `ここで1曲お届けします`
/ `それではお聞きください` at 18:24–18:46, sung lyrics from 18:48 to 20:32, a `セカラジ`
jingle at 21:05, and talk resuming at 21:11. Nothing to translate there, and burning a
full song into a reupload is asking for a copyright claim.

Everything else is talk — no cold open (hosts greet at 00:05), no watchalong.

```bash
--start 00:00:00 --end 00:18:47 \
--start 00:21:06 --end 00:36:25
```

Boundaries are from caption timings and need a listen to confirm before hardsub —
particularly the song's tail, since the last caption cue is at 20:32 but the music likely
runs to ~20:45 under the jingle.

## Speaker map

Written to `speaker_map.toml` in this folder, with labels 0 and 1 mapped to slots 1 and 2.
This is also what tells the translator who is hosting — `build_speaker_prompt()` turns it
into a "Speakers in this recording" fragment:

```
Speakers in this recording:
- Rina Honnizumi (voice of Shizuku Hinomori)
- Minori Suzuki (voice of Ena Shinonome)
```

**Cross-chunk re-ID is the main risk.** Chirp 3 splits audio into 18-minute chunks and
diarizes each independently, so labels are only consistent *within* a chunk, and it
over-segments. Expect more raw labels than hosts; run `assign-speakers` after the first
pass and add the extras here, all pointing at slot 1 or 2. Two clearly different voices
makes this tractable. Spot-check around the chunk boundary (~18:00).

## Command (full pipeline)

Run from `/private/tmp/asub-sekaraji`:

```bash
EP="/Users/michaelting/github/autosub/projects/projects/Project Sekai/Sekaraji/Episode 72"
uv run autosub run "$EP/Sekaraji Ep 72.mkv" \
  --profile proseka/sekaraji \
  --backend chirp_3 \
  --speakers 2 \
  --speaker-map "$EP/speaker_map.toml" \
  --start 00:00:00 --end 00:18:47 \
  --start 00:21:06 --end 00:36:25 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

Cutting the song also drops the episode to ~33 min of audio, which is still 2 Chirp 3
chunks rather than 3 — one less diarization label set to reconcile.

## Pipeline run 1 — done

786 dialogue lines in `Sekaraji Ep 72_translated.ass`. Styles came out right:
`Rina Honnizumi` outline `&H00DDEE99` = `#99EEDD`, `Minori Suzuki` `&H0088AACC` =
`#CCAA88`.

**It died once mid-translate** at chunk 19/30 — `ProxyError` / `RemoteDisconnected` on
`oauth2.googleapis.com`, i.e. the known unstable local proxy, not a pipeline fault. Use
`scripts/remote.sh` for the next run.

**Resuming from the checkpoint has a trap.** `run` writes `<stem>_translated.ass`, so its
checkpoint is `<stem>_translated.checkpoint.json`. Bare `autosub translate` defaults its
output to literally `translated.ass`, so it looks for `translated.checkpoint.json`, finds
nothing, and silently re-translates from chunk 1 — the 18 completed chunks were thrown
away with no warning. **Always pass `--out "<stem>_translated.ass"` when resuming.**
Worth making `translate` default to `<stem>_translated.ass` to match `run`.

### The normalizer earned its keep

| ASR output | corrected to |
| --- | --- |
| `せかラジ` | `セカラジ` |
| `こんばこ` | `コンニーゴ` |
| `こんもは` | `コンモア` |

`コンモア` firing is a small vindication of carrying every unit's greeting rather than
just the hosts'.

### QC findings

1. **`感謝祭` → "Thanksgiving"**, 4 times. It's ProSeka's fan appreciation event. **Fixed**
   — added to the `proseka/base` glossary as `Kanshasai (ProSeka fan appreciation
   festival)`.
2. **`ニーゴ` → "Niigo"**, contradicting `sekaraji.toml`'s own prompt line telling it to
   use "N25". Cause: `proseka/base`'s glossary inherited `"ニーゴ" = "Niigo"` from the old
   aftertalk profile while `proseka/n25` overrode it to `"N25"`, so the same term resolved
   two ways and the glossary beat the prompt. **Fixed** — see
   [Unit abbreviations](#unit-abbreviations).
3. **Corners over-detected**: 6 real, 4 spurious re-entries. All caused by cues of mine
   that recur outside their corner — bare `ラジオネーム` (every Theme Mail letter starts
   with one, and the Ending says `ラジオネームもお忘れなく`) and bare `連絡ノート` (the
   hosts mention it in passing at 08:52). **Fixed** — both removed, only distinctive
   phrases kept.
4. **Dangling line splits**, e.g. `The next episode will also be a unit` / `shuffle.` —
   the 1:1 JA→EN line lock. Re-run with `--reflow`.
5. **44 lines left over-length** ("No safe line break"), including the sponsor credit
   splitting mid-title. Needs the `detect_long_lines.py` pass.
6. **35:35 is mistranslated**: `こういうお姉ちゃんがいてもいいじゃない` ("there's room for
   a big sister like this") became "It's perfectly fine to have a '-chan' in there."

Items 1, 2 and 3 are fixed in the profiles, and 1 and 2 were also applied to the existing
`.ass` by scripted replacement (dry-run first, dialogue-line count and `kon-niigo`
occurrences verified unchanged). Run 2 needs `--reflow` for item 4.

## Unit abbreviations

Codified 2026-08-29 after run 1 exposed the inconsistency. The Japanese colloquial short
form maps to the **English community short form**, not to a transliteration of the
Japanese:

| JP | English | was |
| --- | --- | --- |
| `レオニ` | `Leo/need` | Leoni |
| `モモジャン` | `MMJ` | Momojan |
| `ビビバス` | `VBS` | Vivibasu |
| `ワンダショ` | `WxS` | Wandasho |
| `ニーゴ` | `N25` | Niigo |
| `バーチャルシンガー` | `Virtual Singer` | unchanged |

**Fan greetings are the exception** and stay transliterated and lowercase — `kon-needo`,
`kon-more`, `kon-niigo`, `Wonderhoi!` — because `subtitle_style_rules.md` classes them as
coined catchphrases. So `ニーゴ` is `N25` but `コンニーゴ` is still `kon-niigo`.

They had been scattered across four places that disagreed: the `proseka/base` glossary
(transliterations), `proseka/n25` (overrode `ニーゴ` to N25), `subtitle_review_guide.md`
(MMJ), and `aftertalk_project_setup.md` (MMJ/VBS/WxS/N25). Now they live in exactly two,
by design — `profiles/proseka/base.toml` for translation and the Project Sekai glossary in
`subtitle_review_guide.md` for the QC pass. Change both together.

Also removed while doing this: `proseka/mmj` had `"コンモア" = "Kon-more"` with a capital
K, disagreeing with lowercase `kon-niigo`/`kon-needo`. All seven ProSeka profiles now
resolve every one of these terms identically.

Episodes published before 2026-08-29 use the old forms.

### How a JP abbreviation actually becomes an EN one

Traced against this episode, because the obvious mental model (JP abbreviation sits in
`vocab`, glossary swaps it for the EN one) is **not** what happens:

| Lever | Stage | Status |
| --- | --- | --- |
| `vocab` | transcribe — SpeechAdaptation PhraseSet | **inert on both backends.** See [Why vocab does nothing](#why-vocab-does-nothing). |
| `[format.replacements]` | format — literal string swap | works, but **mutually exclusive** with the normalizer (`format_subtitles` raises if given both), and ProSeka uses the normalizer |
| `[format.normalizer.terms]` | format — LLM repair | **works**, and is the migration target (`d36f6e8` moved Liella off `[replacements]` onto this) |
| `[glossary]` | translate — prompt | works, and **generalizes** — it does not need the canonical Japanese to be present (measured below) |

So the JP abbreviations in `vocab` do nothing at all. What carries the load is the
glossary — and it turns out to carry more than expected.

`モモジャン` came through cleanly (ASR produced it 10×, output `MMJ`). `ニーゴ` did not:
ASR heard the homophone **`2号`** ("No. 2") every time — `2号はあんまり踊らない`,
`2号も4人揃うんだよね`.

**But the glossary handled `2号` anyway.** Translating those lines with the `ニーゴ`
glossary entry set to three different values, source text unchanged at `2号`:

| glossary `ニーゴ` → | output |
| --- | --- |
| `N25` | "All four members of **N25** will be together this year" |
| `Niigo` | "All four members of **Niigo** will be together this year" |
| `Nightcord` | "All four members of **Nightcord** will be together this year" |

Three for three. The glossary is a prompt instruction the model applies **semantically**,
not a lookup table — it does not need the canonical Japanese to appear. (This also
explains why the original run said "Niigo": the glossary said Niigo at the time. It was
the glossary all along, not context-guessing.)

A `ニーゴ` normalizer term is still in `proseka/base`, but for a narrower reason — see
below.

Not yet re-run, so this episode's `_original.ass` still says `2号` in those five lines —
the translated `.ass` was corrected by hand. A re-run of format would fix the source too.

### Why vocab does nothing

`vocab` is a list of Japanese phrase hints sent to Google Speech-to-Text v2 as a
`SpeechAdaptation` inline `PhraseSet`, to bias the recognizer toward domain terms it would
otherwise mishear. Exactly the `ニーゴ` case.

The code skipped it on chirp_3 with the comment "incompatible with
enable_word_time_offsets ... Chirp 2 does not have this conflict", recorded 2026-04-12 as
observed behaviour. Retested 2026-08-29 on a 12s clip of this episode where a host says
ニーゴ, 3 runs per cell:

| model | hints | timings | result |
| --- | --- | --- | --- |
| chirp_2 | yes | yes | accepted, **silently ignored** → `25` |
| chirp_2 | yes | no | applied → **`ニーゴ`** |
| chirp_3 | yes | yes | **404 NotFound**, no explanation |
| chirp_3 | yes | no | applied → **`ニーゴ`** |

Three things follow.

1. **The conflict is real and still current** — adaptation and word timings are mutually
   exclusive. Subtitles need the timings (that's where every line's start/end comes from),
   so the hints always lose.
2. **The old comment was wrong about chirp_2.** It doesn't error, but the adaptation has no
   effect while timings are on — and autosub hardcodes `enable_word_time_offsets=True`. So
   vocab has never worked in a subtitle run, on *either* backend, not just chirp_3.
3. **The hints would have fixed this exact bug.** With adaptation applied, the recognizer
   returns `ニーゴ` instead of `25`/`2号`, 3 times out of 3. The capability is real and
   currently unreachable.

`api.py`'s comment now carries this matrix, and the warning fires for both models and says
what to use instead.

**So `[format.normalizer.terms]` is the only working lever for ASR misreadings**, which is
also where `d36f6e8` moved Liella.

### How much do normalizer terms actually buy? (measured)

The obvious next move is to feed all ~88 vocab terms into the normalizer. Measured first,
and the answer is **don't**.

ASR mangled plenty in this episode:

| ASR produced | should be | note |
| --- | --- | --- |
| `本泉莉那` | `本泉莉奈` | host, wrong kanji |
| `本泉梨花` | `本泉莉奈` | same host, sign-off — a *different person's name* |
| `日野守雫` | `日野森雫` | character, wrong kanji |
| `暁絵名` | `東雲絵名` | character, wrong surname entirely |
| `2号` ×5 | `ニーゴ` | homophone |
| `ももジャンプ` | `モモジャン` | |

Translated those 8 lines as-is vs repaired, same prompt, same model:

- **raw vs repaired: 6/8 byte-identical.** The 2 that differed were incidental wording
  ("songs"→"music", "MORE MORE JUMP!"→"MMJ") — not names.
- **control, raw vs raw: 0/8 different.** So the translator is deterministic here and
  those 2 are real signal, not sampling noise.
- **every proper noun came out correct from the mangled Japanese** — Rina Honnizumi ×3,
  Ena Shinonome, Shizuku Hinomori, N25 ×4, MMJ. Nothing leaked: no "Rika", no "No. 2".

The speaker map plus the cast roster in the prompt are simply enough to recover them.

**Conclusion: expanding the normalizer to the full vocab list is cost with no measured
benefit to the English.** Keep the list short. A term earns its place when:

1. **The Japanese artifact matters.** `_original.ass` is committed and drives the
   bilingual view and the HTML review report — nobody wants a host's name rendered as a
   different person there. This is why the `ニーゴ` term stays.
2. **Context can't rescue it** — a song title, a one-off place name, a guest who isn't in
   the speaker map or the roster.

Caveat on scope: 8 lines, one episode, all terms with strong contextual support. A guest
appearance or an unfamiliar song title is exactly the case this sample does not cover.

## Discovery transcript

The corner structure was mapped *before* running anything, from YouTube's own
auto-captions:

```bash
yt-dlp --no-update --no-playlist --js-runtimes node --skip-download \
  --write-auto-subs --sub-langs ja-orig --sub-format vtt \
  -o "/tmp/sekaraji72" "https://www.youtube.com/watch?v=gm8pmYsG2uU"
```

Quality is rough — `セカラジ` comes out as `セラじ`, `本泉莉奈` as `ホイズミリナ`,
`日野森` as `日の森` — so it is only good enough for structure and cue phrases, not for
translation. But it makes corner discovery free on any future episode, and the misreads
it produces are themselves a good source of normalizer terms.

## YouTube Title

TODO

## YouTube Blurb (draft)

TODO — write after translation. Material from the discovery pass: the staff paired these
two as "the two big sisters" (お姉ちゃんの2人) and neither had noticed they had that in
common; Rina turns out to be a real-life older sister too; the episode closes on Rina
listing the things she left behind on a Hokkaido trip, including realising on the
shinkansen out of Tokyo that she had no wallet, and the question she leaves the next hosts
is "what's the biggest thing you've ever forgotten?"

## Source

- **URL**: https://www.youtube.com/watch?v=gm8pmYsG2uU
- **Video id**: `gm8pmYsG2uU`
- **Title**: プロジェクトセカイ WEBラジオ番組『セカラジ』#72
- **Channel**: プロジェクトセカイ カラフルステージ! feat. 初音ミク

### Download command (yt-dlp)

```bash
yt-dlp --no-update --no-playlist --js-runtimes node \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Sekaraji/Episode 72/Sekaraji Ep 72.mkv" \
  "https://www.youtube.com/watch?v=gm8pmYsG2uU"
```

> `--js-runtimes node` is new and required: yt-dlp now needs a JS runtime to solve
> YouTube's signature/n challenges. Without it every format 403s. yt-dlp was also
> updated `2026.07.04 → 2026.08.19` to get this working.

## Decisions

1. **Ena's colour** → `#CCAA88`, the meta.json / show-card value. Diverges from the
   darkened `#BA8C5D` used in the published AfterTalk `.ass` files; that's accepted.
2. **Profile structure** → split `proseka/base` out; both `aftertalk` and `sekaraji`
   extend it. Verified behaviour-neutral apart from the normalizer model fix.
3. **Rina Honnizumi headshot** → supplied from the Project Sekai wiki, in
   `official_cast_photos/`.
4. **Project location** → originally `projects/Sekaraji/Episode 72/`, top-level, mirroring
   Lieraji, since it's a recurring show rather than a one-off event.
   **Superseded:** now `projects/Project Sekai/Sekaraji/Episode 72/`. Sekaraji is a ProSeka
   show sharing the AfterTalks' VA pool, and keeping it top-level stranded the shared cast
   photos inside a sibling folder. The franchise dir (`Project Sekai/`) is now the level
   that owns `official_cast_photos/`, `character_art/`, and `CAST.md`; `Aftertalk/`,
   `Events/`, and `Sekaraji/` sit under it. Lieraji is a different franchise and is
   unchanged.

## Open questions

1. **Subtitle bar alpha.** 3.39:1 on this near-white background is too thin. What alpha
   (or a per-show override) do you want?
2. **Card placement.** Leave the cards over chibi Shizuku, or move them?
3. **`連絡ノート` in English.** Currently "contact notebook". It's the school-style
   home↔teacher notebook, used here as a host-to-host relay. Alternatives: "message
   book", "relay notebook", or leave it as *renraku note*.
4. **Song cut boundaries.** 18:47 / 21:06 come from caption timings — confirm by ear.
   Run 1 put the Song corner at 18:25 and Theme Mail at 21:10, consistent with these.
5. **Tracked vs local profiles.** The tracked `profiles/proseka/*` is now well behind
   `profiles/local/proseka/*`. Worth reconciling separately; not touched here.
