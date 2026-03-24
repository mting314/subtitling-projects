# Translation Instructions

## Target Audience

English-speaking anime fans familiar with Japanese media conventions. Viewers may know common Japanese terms, honorifics, and cultural references but need natural, readable English subtitles.

## Tone Guidelines

- Use natural spoken English — subtitles should sound like how people actually talk
- Preserve filler words for authenticity ("Like,", "Well,", "I mean,", "Err...")
- Always use contractions ("I'm", "won't", "can't", not "I am", "will not", "cannot")
- Match the speaker's energy and register — casual speech stays casual, formal stays formal

## Formatting Rules

See `style_guide.md` for complete formatting rules. Key points:

- **Pauses**: ellipsis `...` for long pauses, comma for short, em dash for interruptions
- **Japanese terms**: italicize with ASS tags `{\i1}term{\i0}`, keep terms without direct English equivalents
- **Names**: Western order ("Given Family", e.g., "Sayuri Date")
- **Song/event titles**: quoted, not italicized (e.g., "Yoka ni Mitore")

## Project-Specific Context

Always check the project-level `translation_reference.md` (passed via `--project`) for:

- **Fixed translations**: Recurring scripted lines with established English translations. Use these translations when the Japanese text matches (allow for minor transcription variations).
- **Character/speaker context**: Who the speakers are, their speaking styles, and relationships
- **Franchise terminology**: Project-specific terms and their established translations

## Honorifics and Cultural Terms

- Keep honorifics attached to names when they convey relationship context: "-san", "-chan", "-kun", "-senpai", "-sensei"
- Keep Japanese terms that lack direct English equivalents and italicize them
- Translate common expressions naturally rather than literally (e.g., "yoroshiku onegaishimasu" → context-dependent translation, not a literal rendering)

## Translation Quality

- Preserve the speaker's intent, not just literal meaning
- Keep line lengths reasonable for subtitle readability
- Maintain 1:1 line correspondence with the source — do not merge or split lines
- Each translated line corresponds to exactly one source line with the same timing
