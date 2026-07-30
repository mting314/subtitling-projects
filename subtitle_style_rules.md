# Subtitle Style Rules (Wikipedia MoS, adapted)

Grammar and style rules our English subtitles abide by, **distilled from the
[Wikipedia Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)**
and adapted for spoken-dialogue subtitles.

This is the *reference* companion to [`subtitle_review_guide.md`](subtitle_review_guide.md):
that file is the review *process*; this file is the *ruleset* the review enforces. Where the
MoS conflicts with the natural register of casual speech, we override it — those overrides are
marked and are deliberate. Each rule cites its MoS shortcut (e.g. `MOS:LQ`) for lookup.

Legend: **✅ Adopt** = follow MoS · **🔁 Override** = deliberately break MoS for subtitle
register · **⚖️ Carve-out** = adopt MoS but with named exceptions.

---

## Punctuation

### ✅ Straight quotes and apostrophes — `MOS:CURLY` / `MOS:APOSTROPHE`
Use `"straight"` and `'straight'`, never `"curly"` `'curly'`. Convert on import.

### ✅ Ellipsis is three unspaced dots — `MOS:ELLIPSIS`
`...`, not the precomposed `…` glyph and not `. . .`. Our convention uses `...` for a long
pause / trailing-off (see projects `CLAUDE.md`).

### ✅ Em dash, unspaced, for interruption — `MOS:DASH`
Interrupted / cut-off speech uses an unspaced em dash: `so you can—`. Never a hyphen or `--`
in its place. En dash (spaced) is the MoS alternative; we standardize on **em dash** to match
the projects `CLAUDE.md` pause convention. En dash `–` only for numeric ranges.

### ✅ Single space between sentences — `MOS:DOUBLESPACE`
Never double-space. Never a space *before* `, . ; : ! ?`.

### ⚖️ Quotation punctuation: **American style (inside)** — `MOS:LQ` (overridden)
MoS mandates *logical quotation* (punctuation outside the quote unless part of the original).
**We override to American convention: terminal commas and periods go INSIDE the closing quote**,
including for quoted titles. This is standard subtitle-house practice and reads cleaner.

- Correct: `they went with that take."` · `of "kitty," in the MV` · `So that was "kitty."`
- Wrong:   `that take".` · `of "kitty", in the MV`
- Exception: a trailing `...` or a `?`/`!` that belongs to the outer sentence stays **outside**:
  `Goodbye, "kitty"...` ✓ · `Kanade singing "AM 1 o'clock" is so good!` ✓

### ✅ Dialogue tags: introducing comma + capitalization — `MOS:PMC`
When a speaker quotes someone (`said`, `wrote`, `asked`, `like`...), three things depend on
whether the quote is a **full sentence** or a **fragment folded into your grammar**:

| Part | Full sentence | Fragment |
|---|---|---|
| Comma before the quote | yes | no |
| First letter | **Capital** | **lowercase** (proper nouns / `I` always capital) |
| Terminal punctuation | inside (American, per rule above) | inside |

Test: *if the quoted words could stand alone as a sentence* → comma + capital.

- Full sentence: `Someone wrote, "See you again in a year!"` · `Mizuki said, "You're merging with the white."`
- Fragment: `She called it "surprisingly white."` · `They kept saying it was "so good."`

If a clause follows the quote, use a comma **inside** the closing quote and continue lowercase:

- `He said, "You're cute," to her.`  (capital `Y` = full sentence; comma inside before `to her`)
- Wrong: `He said "you're cute" to her.` (missing introducing comma + wrong case)

### ✅ Serial (Oxford) comma — `MOS:SERIAL`
MoS allows either but demands internal consistency. **We use the serial comma**:
`red, blue, and green`.

---

## Numbers

### ⚖️ Spell out zero–nine; numerals for 10+ — `MOS:NUMERAL`
`four times slower`, not `4 times slower`. Numerals for 10 and above (`150 pulls`, `15 hours`).
Named carve-outs where numerals are **kept** because spelling out is wrong or unidiomatic:
- **Game rarity terms** — `2-star`, `4-star` (players write `2★`/`4★`).
- **Literal chat input read aloud** — `4, 7...`, `7, 7, 7...` (viewers typed digits; words destroy the meaning).
- **Designations / names** — `Episode 7`, `N25`, `2DMV`, `100%` (MoS: numerals with `%`).

### ✅ Time of day: `8:55 p.m.` — `MOS:TIME`
12-hour with lowercase `a.m.`/`p.m.` (periods) and a space; or 24-hour `20:55`. Not `8:55 PM`,
not `8:55PM`. (The lyric reading `AM 1 o'clock` is quoted content, not a clock time — leave it.)

---

## Capitalization & emphasis

### 🔁 Emphasis via italics — `MOS:ALLCAPS` / `MOS:EMPHASIS` (partially overridden)
MoS: emphasize with italics (`{\i1}word{\i0}`), never caps. **We adopt italics for ordinary
emphasis** (`where {\i1}is{\i0} my kitty?`) **but allow ALL-CAPS as a deliberate
shouting / excited-reaction device** (`WAIT but the next part is so good`, `THE END.`) — this
is idiomatic in fansubs. Keep officially all-caps proper nouns as-is (`LINE`, `N25`).

### ✅ Song / work titles in quotation marks — `MOS:TITLES`
Songs, episodes, event stories → **double quotation marks, not italics**
(`"kitty"`, `"Non-Breath Oblige"`, `"We Escape to Survive"`). Albums/films/series/games would
be italic, but those rarely appear as titles in dialogue. **Casing:** default is title case,
**but keep an official lowercase stylization** when the work uses one (`"kitty"`, cf.
`Cheerful＊Days`). Whatever you pick, enforce **one** casing across the whole file
(a Consistency-dimension check).

### ✅ Scare quotes / words-as-words — `MOS:WORDSASWORDS`
Quoting a word being *discussed* is fine (`see "running away" literally`). Don't add quotes
merely for emphasis (that's italics' job).

---

## Foreign terms

### 🔁 Honorifics & romaji stay plain / quoted — `MOS:FOREIGN` (overridden)
MoS italicizes non-English words. **We override for fansub convention:**
- **Honorifics** (`-chan`, `-kun`, `-san`) — plain, hyphenated, never italic.
- **Romanized lyrics / phrases** — in double quotes as words-as-words
  (`"ajike no nai"`, `"jigetsu sae mo kodoku na tenge de"`), not italic.
- **Coined catchphrases** (`kon-niigo`, `Otsu-niigo`) — plain.
- Proper nouns (`Heisei`, `Zundamochi`) — plain (MoS agrees: proper names aren't italicized).

---

## Register (wholesale overrides — do NOT "correct" these)

These MoS rules exist for encyclopedic voice and are **inherently wrong for verbatim dialogue**.
Listed so nobody re-formalizes casual speech:

- **Contractions** — `MOS:CONTRACTION` says avoid; **subtitles must use them** (`don't`, `I'm`, `gonna`).
- **First / second person** — `MOS:I`, `MOS:YOU`; dialogue is nothing but `I`/`you`/`we`.
- **Present tense** — `MOS:TENSE`; speech uses whatever tense the speaker used.
- **Slang, interjections, stylized spelling** — `gonna`, `wanna`, `gotta`, `yapping`,
  `suuuuuper`, intentional `cyute` — correct register; keep.
- **Emoji / kaomoji** — MoS bars them; **we keep them as a tone device in reaction lines**
  (`So cyute 🤌`, `¯\_(ツ)_/¯`).

### ✅ Grammatical prose otherwise — `MOS:GRAMMAR`
Register is casual, but the prose must still be grammatical: no doubled copulas
(`she's can be` → `she can be`), no dropped verbs (`does Tomori-chan?` → `...have?`), no comma
splices, correct possessives (`MOS:POSS`: `the boss's office`). These overlap the Grammar
dimension in the review guide.

---

## Change log

- **2026-07-29** — Initial distillation from the Wikipedia MoS; first applied to *We Escape to
  Survive Aftertalk* (mizu4). Override decisions locked: American quote punctuation, ALL-CAPS
  shouting allowed, emoji/kaomoji kept, official lowercase song stylization.
