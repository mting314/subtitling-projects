# Style Guide for Subtitling

Unless otherwise stated, follow grammar, punctuation, and spelling rules set by the [BBC writing style guide](https://www.bbc.co.uk/newsstyleguide/grammar-spelling-punctuation).

More specific rules for subtitling Japanese seiyuu and anime content are below.

## AI Generated Guide Based on a Team Onibe File

## 1. Timing Guidelines

### Line Duration

| Type               | Duration    | Examples                               |
| ------------------ | ----------- | -------------------------------------- |
| Short exclamations | 0.3–1.0 sec | "Huh?" "Yeah!" "Wow!" "So cute!"       |
| Standard dialogue  | 1.5–3.0 sec | Most conversational lines              |
| Complex/expository | 4.0–8.0 sec | Reading letters, explanations, stories |

**Target average:** 1.5–2.5 seconds per line

### Gap Handling

- **Minimize gaps** between consecutive lines from the same or different speakers
- Gaps under 1 second are acceptable in fast conversation
- **Acceptable gap scenarios:**
  - Scene/topic transitions (5+ seconds)
  - Audience reactions (cheering, applause) — 1–3 seconds
  - Physical actions (standing up, moving) — 1–3 seconds
  - Reading comprehension time after long lines

### Overlapping Dialogue

- **Overlaps are expected** in multi-speaker formats (talk shows, group conversations)
- Multiple speakers can have subtitles displayed simultaneously
- Layer appropriately using Layer 0 for all standard dialogue

---

## 2. Punctuation for Pauses

### Primary Pause Indicator: Ellipsis (`…`)

Use the ellipsis (Unicode U+2026 or three periods) to indicate:

- **Speaker hesitation**
- **Trailing off**
- **Incomplete thoughts**
- **Dramatic pauses**

**Examples:**

"I won't mind… if you fall in love with me." "Nice to meet you…" "I'm so happy…" "Wait, what…?"

### Do NOT Use for Pauses

- **Commas** — Reserve for grammatical purposes only (lists, clauses)
- **Em dashes (`—`)** — Not used for hesitation in this style

### Em Dash Usage (Limited)

Use em dashes only for:

- **Interruptions** (when another speaker cuts in)
- **Abrupt changes in thought**

**Example:**

"Like, I don't know whether she's in a growth spurt or something—" (Speaker gets interrupted)

### Ellipsis Placement Rules

1. **Mid-sentence pause:** Place ellipsis where the pause occurs
   - `"I won't mind… if you fall in love with me."`

2. **Trailing off (end of line):** End with ellipsis
   - `"I'm so happy…"`

3. **Ellipsis + question:** Combine them
   - `"Wait, what…?"`

---

## 3. Formatting Conventions

### Italics

Use ASS italic tags `{\i1}text{\i0}` for:

1. **Japanese terms kept in romaji:**
   - `{\i1}kabedon{\i0}` (wall slam)
   - `{\i1}tsundere{\i0}` (character archetype)
   - Event names: `{\i1}2nd Live{\i0}`, `{\i1}Mitero!{\i0}`

2. **Emphasis on specific words:**
   - `"It {\i1}is{\i0} a sport!"`
   - `"Not the character, not the character, not Sumire."`

3. **Titles of works:**
   - `{\i1}The Scream{\i0}` by Munch
   - `{\i1}Mona Lisa{\i0}`
   - `{\i1}Girl with Balloon{\i0}`

### Capitalization

- Standard sentence case for dialogue
- ALL CAPS used sparingly for extreme emphasis:
  - `"I rEaLly wAnna eAt tAkoYaki!"` (mocking/playful intonation)

---

## 4. Conversational Authenticity

### Preserve Natural Speech Patterns

**Filler words:** Keep them for authenticity

- "Like," "Err…," "Well," "I mean,"
- Example: `"Like, I don't think I've talked to her face-to-face."`

**Repetition:** Preserve when intentional

- `"Hair bun, hair bun, hair bun."`
- `"You're so cute you're so cute you're so cute…"`
- `"Yeah, yeah, yeah."`

**Contractions:** Always use natural spoken contractions

- ✅ `"I'm"` `"they're"` `"won't"` `"can't"` `"doesn't"`
- ❌ `"I am"` `"they are"` `"will not"` (sounds unnatural)

### Interjections

Keep short, natural reactions:

- `"Huh?"` `"Wow!"` `"Oh!"` `"Yay!"`
- `"So cute!"` `"That's terrifying!"`
- `"No way!"` `"Really?!"`

---

## 5. Speaker-Specific Styling

### Multi-Speaker Format

- Each speaker gets their own **Style** in the ASS file
- Styles are color-coded by speaker (see V4+ Styles section)
- Use the Name field to identify speaker (though it may be left blank)

### Speaker Styles Used

| Style Name | Speaker         | Color (Outline)        |
| ---------- | --------------- | ---------------------- |
| Sayurin    | Date Sayuri     | Orange (#F27521)       |
| Liyuu      | Liyuu           | Gold (#6CC1E3)         |
| Paychan    | Aoyama Nagisa   | Green (#3BAE2B)        |
| Nakochan   | Konoe Nako      | Purple (#FF6E90)       |
| Nagichan   | Okuyama Nagi    | Dark Red (#000A0)      |
| Nonchan    | Suzuhara Nozomi | Cyan (#EEC400)         |
| Yabuchan   | Yabuki Akane    | Blue (#F23B4C)         |
| Kumachan   | Okuma Wakana    | Yellow-Green (#17D8BD) |
| Emorin     | Emori Aya       | Pink (#F273C4)         |

---

## 6. Translation Approach

### Quotation Marks

- Use for **reading from letters** or **quoting others**
- Example: `"If the cuckoo does not sing, then it's such a pity."`

### Cultural References

- Keep Japanese terms that lack direct equivalents
- Italicize and provide context through dialogue if possible
- Examples kept: `kabedon`, `tsundere`, song titles

### Sentence Flow

- Match the speaker's natural cadence
- Break long utterances into readable chunks (max ~10-12 words per line when possible)
- Keep related ideas together

---

## 7. Special Cases

### Reading Segments (Letters/Questions)

When speakers read from prepared materials:

- Wrap content in quotation marks
- Maintain slightly longer line durations for readability
- Example:

"If the cuckoo does not sing, bring it back to where it came from!"

### Audience/Group Lines

- Use group style (e.g., `Liella`) for unison responses
- Example: `"Yay!"` `"Welcome!"` `"Thank you very much!"`

### Sound Effects / Actions

- Not typically subtitled in dialogue tracks
- If needed, use parentheses or brackets: `(laughter)` `(applause)`

---

## 8. Quality Checklist

Before finalizing:

- [ ] No unnecessary gaps between consecutive dialogue
- [ ] Japanese terms in italics
- [ ] Natural contractions used throughout
- [ ] Filler words preserved for authenticity
- [ ] Line durations within target ranges
- [ ] Speaker styles correctly assigned
- [ ] Emphasis italics applied where needed

---

## Quick Reference

| Element          | Correct                | Incorrect               |
| ---------------- | ---------------------- | ----------------------- |
| Pause/hesitation | `I mean… it's just…`   | `I mean, it's just,`    |
| Interruption     | `But like—`            | `But like...`           |
| Japanese terms   | `{\i1}kabedon{\i0}`    | `kabedon` / `"kabedon"` |
| Emphasis         | `It {\i1}is{\i0} real` | `It IS real`            |
| Trailing off     | `So cute…`             | `So cute...`            |
| Filler words     | `Like, I guess…`       | (omitting "Like,")      |

# Human Generated Section

## Naming Convention

### Japanese People Names

- Use "Given Name" + "Family Name" (e.g. "Mizuki Akiyama", not "Akiyama Mizuki").
- Use capitalization as it appears in Fandom wikis. Otherwise, defer to regular style guides on capitalization.

### Event Names

- Should be "quoted", not italicized.
- Use the English server event names and capitalization. If not available, use the name provided in the Fandom wiki.

Examples:

- "With Our Wounded Hands", not "Kizudarake no Te de, Watashitachi wa"

### Project Sekai Terminology

- "AfterTalk" should be capitalized as "AfterTalk", not "aftertalk" or "Aftertalk".
- "AfterLive" should be written as one word (with capital "L"): "AfterLive" (singular) and "AfterLives" (plural). Do NOT write "After Lives".
- "ProSeka" should be capitalized as "ProSeka", not "proseka" or "Proseka".
- Use "MV" when referring to music videos (e.g., "the MV"). "2DMV" is also acceptable when specifically describing 2D music videos.
- Use "fan festa" for the fan event term. ("fan fes" is a common shorthand but the full form is preferred.)
- When referring to numbered sections of Project Sekai event stories, use "Episode", not "Chapter" (e.g., "Episode 1", "Episode 2"). This aligns with the game's official terminology.

## Grammar

### Spoken Pauses

Spoken pauses should be indicated with:

1. A comma, if the pause is short.
2. A dash, if the pause is long.
3. An elipsis, if the pause is very long.

### Song Titles

Should be "quoted", not italicized.

Examples:

- "Yoka ni Mitore"

Should use the same capitalization as Fandom wikis. Otherwise, defer to regular style guides on song title capitalization.

