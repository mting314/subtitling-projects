# 5周年記念ビデオメッセージ Leo/need編 (5th Anniversary Video Leo/need)

> Special 5th Anniversary video message featuring the full cast of **Leo/need**:
> - **Ruriko Noguchi** (野口瑠璃子, voice of **Ichika Hoshino**)
> - **Karin Isobe** (磯部花凛, voice of **Saki Tenma**)
> - **Reina Ueda** (上田麗奈, voice of **Honami Mochizuki**)
> - **Yuki Nakashima** (中島由貴, voice of **Shiho Hinomori**)

---

## Video Information

- **Title**: 5周年記念ビデオメッセージ Leo/need編
- **Video ID**: `fCP_qMoK7ww`
- **Duration**: 22:33 (1353.10s, 81,106 frames at 59.94 fps)
- **Resolution**: 1080p (1920x1080)

---

## Chapters / Corners

- `00:00` — Opening & Self-Introductions
- `01:08` — Looking Back on These 5 Years (5年間を振り返って)
- `16:12` — Messages to Everyone (皆さまへのメッセージ)
- `22:15` — Ending & Final Greetings

---

## Subtitle Styling & Alignment

- **Base Architecture**: Standard `1920x1080` canvas (`PlayResX: 1920`, `PlayResY: 1080`).
- **Font**: `Lato ExtraBold` at `Fontsize 75`, ensuring subtitles sit above hardsubbed Japanese telops while staying clear of the VAs' faces during close-ups.
- **Outline Colors & Contrast Overrides**:
  - **Ichika Hoshino**: `#33aaee` (`&H00EEAA33`) — 2.32x contrast vs white studio wall
  - **Saki Tenma**: `#dbb300` (`&H0000B3DB`, bright-wall override) — 1.80x contrast
  - **Honami Mochizuki**: `#ee6666` (`&H006666EE`) — 2.80x contrast
  - **Shiho Hinomori**: `#a5c31e` (`&H001EC3A5`, bright-wall override) — 1.80x contrast
  - **Leo/need Unit**: `#4455dd` (`&H00DD5544`) — 4.92x contrast
- **Vertical Tiers**:
  - `- 1Line`: `MarginV 225` (sits directly above 1-line Japanese telops)
  - `- 2Line`: `MarginV 380` (sits directly above 2-line Japanese telops)
  - `- Top`: `MarginV 75` (top-center anchor for opening self-intros over bottom nameplates)
- **Topic Banners**:
  - Mask: Color-matched rectangle (`#FBFBFA`, `x=104..576, y=28..86`) covering Japanese ribbon text
  - English text: `Lato ExtraBold` 42pt navy (`#0C4F82`) with white outline (`Looking Back on These 5 Years` and `Messages to Everyone`)

---

## YouTube Title

`[ENG SUB] Project SEKAI 5th Anniversary Video Message — Leo/need (Full Cast)`

## YouTube Blurb

To celebrate the 5th Anniversary of Project SEKAI: Colorful Stage! feat. Hatsune Miku, all four members of Leo/need's voice cast—Ruriko Noguchi (Ichika), Karin Isobe (Saki), Reina Ueda (Honami), and Yuki Nakashima (Shiho)—gather together in person for an extended special video message!

From looking back at their first auditions and how their characters have grown over the past five years (from Ichika's shy monologues to her unbridled passion for yakisoba bread and Miku!), to stories from their music recordings and live performances, the cast reflects on the bond between the childhood bandmates and shares their heartfelt gratitude and future hopes with fans around the world.

Original Video: https://www.youtube.com/watch?v=fCP_qMoK7ww
Translated & subtitled by the AutoSub team.


---

## Overlays

Defined in `popups.json` and burned in during hardsubbing (`scripts/hardsub_trim.py`):
- **Card #110 (`00:08:16.05`–`00:08:20.11`)**:
  - **Context**: Reina Ueda (voice of Honami) remarks: *"Going forward, she's going to face more and more choices to make, isn't she? ... what will she ultimately choose to do?"*
  - **Meme & Banner Joke**: Foreshadowing Event #220 **"Stars Off Orbit"** (軌道を外れた星たち, Honami's 7th focus event regarding the major label debut offer) via the classic Paul Dano Riddler **"DOES HE KNOW?"** meme paired with the official **"Stars Off Orbit"** event banner (`popup_does_she_know_stacked.png` / `popup_does_she_know_horizontal.png`).
  - **Position**: Upper-right empty wall at `pos: [1150, 70]` (stacked) or `pos: [800, 60]` (horizontal), cleanly framed between Reina Ueda and Ruriko Noguchi without obscuring any speaker or UI.
