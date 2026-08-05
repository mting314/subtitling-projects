# Subtitle Translation Review Guide

A repeatable checklist for the **human-pass QC review** of a `*_translated.ass` file
(the pass that happens *after* the autosub pipeline produces the translation). Covers
the four review dimensions: **Consistency, Grammar, Spelling, Style**.

This complements the style rules in [`CLAUDE.md`](CLAUDE.md) (names, pauses, ProSeka
term casing, song/title quoting) and the full ruleset in
[`subtitle_style_rules.md`](subtitle_style_rules.md) (grammar/punctuation/number/capitalization
rules distilled from the Wikipedia Manual of Style, with our deliberate overrides for spoken
register). Don't duplicate those — this file is about the *review process* and the *recurring
error patterns* to hunt for; consult `subtitle_style_rules.md` for the authoritative rule on any
punctuation/number/capitalization question.

---

## Process

### 1. Extract the dialogue (files can be huge)
If an `.ass` file contains legacy embedded `img2ass` lines, extract just the readable dialogue. Note: For new projects, use **`popups.json`** and **`scripts/generate_overlays.py`** for image overlays rather than `img2ass` vector drawing lines.

```bash
f="<name>_translated.ass"
awk 'NR>=30' "$f" | awk '{ if (length($0) > 300) print NR+29": [LONG "length($0)" chars] "substr($0,1,80); else print NR+29": "$0 }'
```

Keep the leading line numbers — you'll use them to target edits precisely.

### 2. Review against the four dimensions (below).

### 3. Suggest edits first, then apply after sign-off.
Present a table of `Line | Current | → Suggested` grouped by dimension. Flag any
judgment calls (e.g. which form to standardize a term to) and **ask before applying**.

### 4. Apply with a line-targeted, verified script — never blind global replace.
Big files + repeated phrases make naive `sed` risky. Use a dry-run that confirms every
`old` string is present on its target line *before* writing. Pattern:

```python
edits=[(lineno, old, new), ...]   # 1-indexed line numbers
lines=open(f,encoding="utf-8").read().split("\n")
miss=[ (ln,old) for ln,old,_ in edits if old not in lines[ln-1] ]
if miss: print("ABORT", miss)            # fix line numbers, re-run
else:
    for ln,old,new in edits: lines[ln-1]=lines[ln-1].replace(old,new,1)
    open(f,"w",encoding="utf-8").write("\n".join(lines))
```

If a string "misses", the line number drifted — `grep -n` the phrase to find the real line.

### 5. Verify the consistency fixes landed.
Re-grep every standardized term and confirm the counts (one canonical form, zero of the
variants). Don't trust "53 edits applied" — a missed variant on an unlisted line is the
classic failure (see the Hagiyama-san straggler on the Grow Glorious Glow pass).

---

## Dimension 1 — Consistency

The single highest-value check. Pick **one canonical form** per recurring term and grep
the whole file to enforce it.

**How to audit a term:**
```bash
grep -oE "Cheerful.Days" "$f" | sort | uniq -c     # shows every variant + count
grep -oE "Hagiyama[-a-zA-Z']*" "$f" | sort | uniq -c
```

**Recurring variant traps:**
- **Event/song titles drift mid-file.** They are the most-repeated proper nouns and the
  most likely to be wrong inconsistently. On the "Grow Glorious Glow" pass, the title was
  wrong in *all 6* instances and in *3 different ways* (`Grow Glorious Grow`,
  `grow glorious grow`, `Glow Glorious Glow`). Cross-check against the **filename** and
  internal evidence (e.g. a "tongue twister" joke confirmed Gr**o**w / Gl**o**w).
- **Stylized names lose their special characters.** `Cheerful＊Days` (fullwidth ＊, U+FF0A)
  vs `Cheerful Days`. Decide once: keep the official stylization for proper nouns, or
  plain ASCII for readability — then apply everywhere.
- **All-caps name artifacts.** `MIKU` vs `Miku` — the STT/LLM sometimes uppercases a
  name. Normalize to in-game casing (`Miku`, plus affectionate `Miku-chan` where used).
- **Romaji vs translated song titles.** Same song appears as `"Hashiru! Tooku! Todoku!"`
  in 3 places and `"Run, Deliver"` in 1. Pick romaji *or* a single English rendering and
  use it every time (default: romaji, matching in-game).
- **Honorific drift.** `Hagiyama-san` / `Hagiyama-chan` / bare `Hagiyama`. If the split
  isn't deliberate, unify (usually to the majority / the register that fits the show's
  tone). Bare-name (no honorific) is almost always an oversight.
- **Clock-time formatting.** `9:55PM` / `9:55 PM` / `10:10PM` — standardize the space.
  Also sanity-check the *numbers* against context (a room-ID reveal at `9:55` then `10:55`
  with the live at `10:00 PM` is a red flag — flag for audio verification, don't silently
  "fix" a digit you can't confirm).

**Maintain a per-show glossary** (see bottom) so the canonical forms carry across episodes.

---

## Dimension 2 — Grammar

### The capitalization / sentence-continuation rule (primary check)
When one subtitle line flows into the next, capitalization and end-punctuation must agree:

- If a line **does not end the sentence** (breaks on a comma, or trails with no terminal
  punctuation), the **next line starts lowercase**.
- If a line **ends the sentence** (`.`, `!`, `?`), the **next line starts capitalized**.

So a mismatch is one of two bugs — fix whichever side is wrong:

| Symptom | Likely fix |
|---|---|
| `...synchronized lines,` → `But get this!` | the comma is wrong; the first line is a complete thought → make it `.` |
| `...center of Cheerful＊Days.` → `almost like it was her last chance.` | the period is wrong; it's one sentence → make it `,` |

(Note: `"I..."` and proper nouns are always capitalized regardless — not violations.
Lines starting with a quotation mark or `...` continuation are usually fine.)

### Other grammar patterns that recur
- **Tense / verb-form slips after "want/said":** `wants to grown wings and taken flight`
  → `wanted to grow wings and take flight`.
- **Doubled auxiliary:** `She's was muttering` → `She was muttering`; `lucky to be have`
  → `lucky to have`.
- **Missing copula:** `Those can painful` → `Those can be painful`.
- **Dropped relative pronoun:** `you already know the lead is` → `...know who the lead is`.
- **Dropped/extra article:** `put lot of pressure` → `put a lot of pressure`;
  `a swan metaphors` → `swan metaphors`.
- **Word-order inversion (literal-from-JP):** `Shizuku since has such a mature look`
  → `since Shizuku has such a mature look`.
- **Stray possessive/pronoun:** `working her so hard all on her own` → `working so hard...`;
  `see their keep surpassing` → `see them keep surpassing`.

---

## Dimension 3 — Spelling

- **Name misspellings** are the priority — they read as obvious errors:
  `Shiuzku` → `Shizuku`. Grep each character name for near-misses.
- **Plain typos:** `relaex` → `relax`.
- **Duplicated words/phrases** from STT or LLM stutter:
  `reaction's reaction` → `reaction`; `auditions auditions` → `auditions`;
  `so so many so many` → `so many`; `previously appeared in a previous event`
  → de-duplicate. Two adjacent near-identical clauses across lines are usually a
  pipeline artifact — trim one.

```bash
# quick duplicate-word scan
grep -noE "\b(\w+) \1\b" "$f"
```

---

## Dimension 4 — Style

Target: **natural, casual, spoken English** — like a streamer talking to fans, not an
academic essay. The pipeline output is usually close; tighten the literal/stiff spots.

- Prefer everyday words over formal/literal ones: `stoic with her diet` → `strict with
  her diet`; `meals as refreshments` (差し入れ) → `snacks`; `the foundation of your
  physique` → `the foundation of your body`.
- Keep contractions and casual interjections (`yeah`, `man`, `Gotta`, `yapping`) — these
  are correct register, don't formalize them.
- **Keep deliberate fandom terms**, even niche ones, when the speaker signals them — e.g.
  `"absolute territory"` (絶対領域) where she says "so-called". Don't over-sanitize.
- Read continuation lines as one utterance — fix phrasing that only reads wrong because
  it was split (`almost like if to cheer` → `almost as if to cheer`).
- Leave the `img2ass` meme placeholder lines and `{\pos(...)}`/`{\i1}` override tags
  untouched — they're not prose.

---

## Dimension 5 — Line length (max 2 rows on screen)

3+ rows is bad subtitling practice: it forces the viewer's eyes to sweep too far and eats
screen real estate. Target **≤2 rows** for every line. Row count depends on libass's actual
wrapping under each line's *style* — `Saki - PiP` (wrap ~1020px) and `Saki - Side Song`
(~1090px) wrap narrower than the main style (~1320px), so the same text can be 2 rows in one
and 3 in another. **Measure by rendering, don't guess.**

Detect (renders each line under its real style over black, counts rows by projection):
```bash
uv run --with pillow --with numpy python3 scripts/detect_long_lines.py "<name>_translated.ass"
```
It flags every line rendering to >2 rows. Fix each one of two ways, and **re-render to
confirm the fix is ≤2 rows before applying**:

- **Split into two events** at a clause boundary (comma, `and`/`but`/`so`, `that`, or a
  sentence end) using `scripts/split_subtitle_line.py --line N --before "<clause>" --transcript
  <t.json>`. The *time* split lands on a real breath: it estimates proportionally by each
  half's length, then snaps to the largest word-gap within ±1s (rejecting a distant
  mid-sentence pause, or any snap that leaves a half under ~1s to read). Preserves exact
  wording and any `\pos`. The transcript words are source-language, so they're used only
  for *timing* (silence is language-agnostic), never to choose the text split point.
- **Reword shorter**, preserving meaning + the casual spoken style.

Prefer split when it's two real clauses/sentences or has a natural pause (`...`); reword when
it's a single breath. Re-run the detector after applying — the target is **0 flagged**.

Runs after text edits (a reword can change wrapping) and pairs with the positional pass,
since PiP/Side-Song lines are the most frequent 3-row offenders.

---

## Positional styles — PiP + song-shift (do before hardsub)

### Standardized `DefaultOnibe` Base Architecture

1. **Master Base Style (`DefaultOnibe`):**
   `Style: DefaultOnibe,Lato ExtraBold,100,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,100,1`
   - Serves as the canonical default for all subtitle events.
   - **Standard values (1080p): Fontsize 100, MarginL/R 200, MarginV 100.** Per the
     [idolactivities subtitling guide](https://idolactivities.github.io/vtuber-things/guides/subtitling.html):
     font ≥100 for 1080p, vertical margin ≥ font size, horizontal margins ≈ 2× that.
     (Was 72 / 180 / 60 before — bumped up 2026-07 for readability + margin balance.)
   - **`PlayResX: 1920` / `PlayResY: 1080` must be in `[Script Info]`.** If they're absent,
     libass assumes a **384x288** script canvas and scales it to the video frame — a ~5x
     blowup that makes almost every line wrap to 3+ rows. `pyass` (autosub's ASS writer)
     omitted these until `format/generator.py` was fixed, so older files need a backfill.
     `detect_long_lines.py` now warns when they're missing; check the header first if a
     file shows an implausible number of long lines.
2. **Master TL Note Style (`DefaultOnibe - TL Note`):**
   `Style: DefaultOnibe - TL Note,Lato ExtraBold,54,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,4,1.33,8,100,100,50,1`
   - Use for all Translator Note text across all projects.
3. **Character Styles (`<Character>`):**
   - Characters change **nothing** about `DefaultOnibe` other than their signature character color in `OutlineColour`.
   - **ASS colors are BGR, not RGB** — `&H00BBGGRR`. Derive from the character's official
     hex by swapping the outer bytes: `#RRGGBB` → `&H00BBGGRR` (e.g. Shizuku `#99eedd` →
     `&H00DDEE99`). Getting this backwards silently yields a plausible-looking but wrong
     color — always **render-verify**.

     Source of truth: the `|color=` field on each character's
     [Project Sekai Fandom](https://projectsekai.fandom.com/) page, which was cross-checked
     against `sekai-story-indexer/webapp/static/meta.json` — **all 26 agree**. Full table
     (audited corpus-wide 2026-08-04; all 65 style rows match):

     | Character | Hex | `OutlineColour` | | Character | Hex | `OutlineColour` |
     |---|---|---|---|---|---|---|
     | Ichika Hoshino | `#33aaee` | `&H00EEAA33` | | Kanade Yoisaki | `#bb6688` | `&H008866BB` |
     | Saki Tenma | `#ffdd44` | `&H0044DDFF` | | Mafuyu Asahina | `#8888cc` | `&H00CC8888` |
     | Honami Mochizuki | `#ee6666` | `&H006666EE` | | Ena Shinonome | `#ccaa88` | `&H0088AACC` |
     | Shiho Hinomori | `#bbdd22` | `&H0022DDBB` | | Mizuki Akiyama | `#ddaacc` | `&H00CCAADD` |
     | Minori Hanasato | `#ffccaa` | `&H00AACCFF` | | Hatsune Miku | `#33ccbb` | `&H00BBCC33` |
     | Haruka Kiritani | `#99ccff` | `&H00FFCC99` | | Rin Kagamine | `#ffcc11` | `&H0011CCFF` |
     | Airi Momoi | `#ffaacc` | `&H00CCAAFF` | | Len Kagamine | `#ffee11` | `&H0011EEFF` |
     | Shizuku Hinomori | `#99eedd` | `&H00DDEE99` | | Luka Megurine | `#ffbbcc` | `&H00CCBBFF` |
     | Kohane Azusawa | `#ff6699` | `&H009966FF` | | MEIKO | `#dd4444` | `&H004444DD` |
     | An Shiraishi | `#00bbdd` | `&H00DDBB00` | | KAITO | `#3366cc` | `&H00CC6633` |
     | Akito Shinonome | `#ff7722` | `&H002277FF` | | Tsukasa Tenma | `#ffbb00` | `&H0000BBFF` |
     | Toya Aoyagi | `#0077dd` | `&H00DD7700` | | Emu Otori | `#ff66bb` | `&H00BB66FF` |
     | Rui Kamishiro | `#bb88ee` | `&H00EE88BB` | | Nene Kusanagi | `#33dd99` | `&H0099DD33` |

   - **Readability override for bright backgrounds.** The official colors are the default,
     but several are very light (Shizuku, Saki, Len, Minori, Shiho, Luka, Haruka…) and the
     outline is what separates white fill from the video. On a bright background the light
     outline vanishes and the text washes out. **What matters is outline-vs-background
     contrast where the subs actually sit — not outline-vs-white-fill.** So don't blanket-
     darken; measure the episode and deviate only when it's actually needed:
       1. Sample the real luminance of the subtitle region across representative frames
          (bottom-center band for the main style, around `\pos(650,750)` for PiP).
       2. Compute WCAG contrast of the official outline against the **brightest** background
          it sits over (the 90th-percentile luminance).
       3. If that's low (roughly < ~1.5×), darken the outline — keeping the character's hue
          — until it reads, then **render-verify on a real bright frame** (burn the actual
          subs, don't trust the number). Darker backgrounds need no change.
     A drop shadow does **not** fix this (it's offset, so it can't frame the glyph), and a
     black outer halo was rejected as too heavy. Keep the fix to a hue-preserving darken.

     Per-episode overrides applied so far:

     | Episode | Character | Official | Override | Why |
     |---|---|---|---|---|
     | At The End of The Unraveled Thread (shizu3) | Shizuku | `#99eedd` (`&H00DDEE99`) | `#22ceac` (`&H00ACCE22`) | studio wall L≈0.80; official outline only 1.09× vs bg |
     | Gazing Upon the Night Sky's Fading Stars (saki7) | Saki | `#ffdd44` (`&H0044DDFF`) | `#dbb300` (`&H0000B3DB`) | near-white wall + pale-yellow-sweater host; yellow washed out (1.34× vs bg) |
     | Colors of Pure Sense (ena6) | Ena | `#ccaa88` (`&H0088AACC`) | `#ba8c5d` (`&H005D8CBA`) | pastel striped wall (L≈0.66); caramel washed out (1.47× vs bg) |
     | Unsteady, still steady step (hona5) | Shiho | `#bbdd22` (`&H0022DDBB`) | `#a5c31e` (`&H001EC3A5`) | bright song-segment + near-white backgrounds (Shifted 1.26× vs bg) |
4. **Shifted Character Styles (`<Character> - Shifted`):**
   - Inherit character colors and **Fontsize 100** exactly. Only margins change: `MarginL = 100, MarginR = 730, MarginV = 60`.
5. **PiP Character Styles (`<Character> - PiP`):**
   - Inherit character colors and **Fontsize 100** exactly. Margins: `MarginL = 100, MarginR = 800, MarginV = 50`, Alignment `8`. **Every line must have `{\pos(650,750)}`.**
   - (Was Fontsize 72 before — bumped to 100 in 2026-07 to match main style size.)

### The positional styles table

| Situation | Reference style (Colors) | Alignment | MarginL | MarginR | MarginV | Position tag on lines |
|---|---|---|---|---|---|---|
| **PiP** — host cam / card art fills most of the frame, subs sit in a fixed spot | `PiP` / `<Char> - PiP` | `8` (top-center anchor) | `100` | `800` | `50` | **`{\pos(650,750)}` on every line** |
| **Song-shift** — a 2D/3D MV plays in the **lower-right**; shift subs left to clear it | `<Char> - Shifted` (a.k.a. "Side Song") | `2` (bottom-center) | `100` | `730` | `60` | none — style margins do it |

> Only Alignment + the three margins change between these and the main style. Keep the
> character's `OutlineColour`, font (`Fontsize 100`), `Bold`, `Outline`, `Shadow` identical to the main
> style so the look is consistent.

The **PiP** case relies on `\pos`, not margins (the `\pos` overrides them; Alignment `8`
just sets the anchor point). The **song-shift** case relies purely on the asymmetric
margins (bigger `MarginR` pushes the centered box left).

### Apply

Use the script — it does both fixes deterministically (idempotent, `--dry-run`, prints a
summary), reading the canonical layout values live from the reference file. It lives in
`scripts/` (next to `hardsub_trim.sh`); run it from the projects repo root:

```bash
python3 scripts/apply_positional_styles.py "projects/Project Sekai/<event>/<name>_translated.ass" \
  --reference "projects/Project Sekai/Colors of Pure Sense/Colors of Pure Sense_translated.ass" \
  --pip   "<Char> - PiP:PiP:650,750" \
  --shift "<Char> - Side Song:DefaultOnibe - Shifted" \
  --dry-run          # inspect first, then drop --dry-run
```

Mapping: `TARGET_STYLE:REF_STYLE[:X,Y]`. It copies only Alignment + MarginL/R/V (color/font
preserved), prepends `{\pos(650,750)}` to PiP *Dialogue* lines, and skips `Comment:` lines
and any line already carrying a `\pos`. The **`aftertalk-launch` skill** wraps this
(along with hardsub segment-finding and the YouTube title/description) — it resolves
the differing style names to roles and render-verifies for you.

Then **verify by rendering** (per the `aegisub-ass` skill): retime one PiP and one
song-shift line to `0:00:00.00–0:00:05.00`, render a frame over flat gray, and confirm the
PiP text sits mid-frame and the song-shift text clears the lower-right. Don't trust the
tags; trust the render.

---

## Per-show glossary (extend over time)

Canonical forms to enforce across all episodes of a show.

### Project Sekai
| Term | Canonical form | Notes |
|---|---|---|
| Program name | `ProSeka AfterTalk` | capital T (also `AfterLive`, capital L) |
| Unit (MMJ) | `MORE MORE JUMP!` / `MMJ` | full name first use, then abbreviate |
| Shizuku's debut unit | `Cheerful＊Days` | fullwidth ＊ (U+FF0A) — official stylization |
| Rival character | `Hagiyama-chan` | unify honorific unless a -san/-chan split is intentional |
| Vocaloid | `Miku` / `Miku-chan` | never `MIKU` |
| Characters | `Minori`, `Haruka`, `Airi`, `Miku` | MMJ members; Western-order full names elsewhere |
| Brands | `Grand Fleur`, `Floraison Éclat` | keep accents |
| Composer | `Usushioshisuu-san` | as romanized in-show |
| Song (Run/Far/Reach) | `"Hashiru! Tooku! Todoku!"` | romaji, quoted, not translated |
| Host nickname | `Hon-chan` | Rina Honnizumi (VA of Shizuku) |

> When standardizing a stylized name, the fullwidth ＊ is U+FF0A (not the ASCII `*`).
> Copy it from an existing correct instance to avoid typing the wrong glyph.
