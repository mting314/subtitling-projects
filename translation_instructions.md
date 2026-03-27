# Translation Instructions

Translate the input JSON array of Japanese subtitle lines to English for anime fans familiar with Japanese media.

## Core Rules

- Read neighboring lines for context before translating. Distribute the English naturally across split sentences so every line has text.
- NEVER leave a translated line blank. Absorb filler-only lines (um, uh, ah) by redistributing surrounding text.
- Prioritize natural subtitle English over literal wording. Keep tone and speaker persona intact. Use contractions ("I'm", "won't", never "I am", "will not").
- End lines on natural punctuation. Move trailing connectives ("but", "and", "so") to the next line. Keep logical phrases (article + noun) on the same line.
- Keep transitional phrases ("You know,", "Well then,", "I mean,") but place them at the start of a line, not the end.

## Glossary

- Use exact translations from the project reference glossary. Allow for minor transcription variations.
- Use consistent translations for catchphrases, segment titles, and recurring terms.

## Formatting

- Double quotes only. Ellipsis `...` for hesitation/trailing off. Em dash `—` for interruptions only.
- Preserve ASS tags like `{\i1}text{\i0}`.
- Keep untranslatable Japanese terms italicized: `{\i1}tsundere{\i0}`. Keep honorifics (-san, -chan, -kun, -senpai).
- Western name order: "Given Family". Song/event titles "quoted", not italicized.

## Output

Return a JSON array of `{id, original, translated}` objects. Same count and order as input.
