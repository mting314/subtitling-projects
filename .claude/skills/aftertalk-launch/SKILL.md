---
name: aftertalk-launch
description: >-
  Finishing pass for ProSeka AfterTalk streams (and alias for video-launch).
  Covers (1) positional styles, (2) line length QC, (3) Overlays & Popups pre-flight
  audit (popups.json), (4) watchalong segment cutting and hardsubbing, and (5) YouTube publish.
  For all general video releases (Events, Stage Dramas, Radio), use `video-launch`.
---

# AfterTalk Launch (Alias of `video-launch`)

> [!NOTE]
> This skill has been generalized to **[`video-launch`](../video-launch/SKILL.md)** to support all video formats (AfterTalks, Stage Dramas, Event streams, and Radio shows). See [`video-launch/SKILL.md`](../video-launch/SKILL.md) for the universal reference.

The finishing pass on an AfterTalk `_translated.ass`, after the four-dimension QC text review:

1. **Positional styles** — reposition subs so they clear on-screen content (PiP mid-frame, Side-Song lower-right shift).
2. **Line length** — flag + fix any line rendering to 3+ rows (`detect_long_lines.py`).
3. **Overlays & Popups pre-flight** — audit `popups.json`, verify VA card / meme assets, deconflict lines.
4. **Hardsub segments** — find host-talk ranges (`find_segments.py`) and burn with GPU acceleration (`hardsub_trim.py`).
5. **YouTube title + description** — write release copy in `notes.md`.
6. **YouTube upload** — automated upload via `scripts/youtube_upload.py`.

Refer to [`video-launch/SKILL.md`](../video-launch/SKILL.md) for full documentation and CLI flags.
