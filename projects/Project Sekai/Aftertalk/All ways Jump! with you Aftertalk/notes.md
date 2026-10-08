# All ways Jump! with you Aftertalk

> Official JP event name: **"All ways Jump! with you"** (World Link, asset bundle `event_wl_2nd_idol_2025`, `wl2-5`, series 2, part 5).

**Commit prefix**: `wl2-mmj`

## Event Details

- **Event name (JP)**: All ways Jump! with you
- **Event id**: 176  |  **Type**: world_bloom (World Link)  |  **Unit**: MORE MORE JUMP! (`more_more_jump` / idol)
- **Event dates**: 2025-08-08 → 2025-08-20
- **Stream date**: 2025-08-21 21:00 JST
- **Focus characters**: All MORE MORE JUMP! members (Chapter focuses: Minori Hanasato, Haruka Kiritani, Airi Momoi, Shizuku Hinomori)
- **Host VAs**:
  - 小倉唯 (Yui Ogura) — Voice of Minori Hanasato
  - 本泉莉奈 (Rina Honnizumi) — Voice of Shizuku Hinomori
- **Event Gacha**: Empty Teatimeガチャ
  - ★4 [夢は雑踏に紛れて] Minori Hanasato (A Dream Lost in the Crowd)
  - ★4 [出逢い育む絆] Haruka Kiritani (Bonds Nurtured by Encounters)
  - ★4 [スペシャルコラボ配信！] Airi Momoi (Special Collab Stream!)
  - ★4 [完璧な微笑] Shizuku Hinomori (A Perfect Smile)
- **Songs**:
  - **Commissioned song**: None (World Link 2 chapters do not debut an individual commissioned unit song; cf. World Link 1 MMJ commissioned song "Hug" by MIMI)
  - **AfterLive song**: "Idol Shin'eitai" (アイドル新鋭隊) by Mitchie M

### Episode Titles
1. わたし達らしく夢に向かって (Heading Toward Our Dreams in Our Own Way) [wl_idol_02_01]
2. 憧れを目指して (Aiming for What I Admire) [wl_idol_02_02]
3. 明日はきっと (Tomorrow, Surely) [wl_idol_02_03]
4. 遠い青空 (A Distant Blue Sky) [wl_idol_02_04]
5. めぐる希望 (Circulating Hope) [wl_idol_02_05]
6. 諦められない夢 (A Dream I Can't Give Up) [wl_idol_02_06]
7. 届かないなら、届くまで (If It Won't Reach, Until It Does) [wl_idol_02_07]
8. 求められる私を (The Me Everyone Expects) [wl_idol_02_08]
9. 息のしやすい場所 (A Place Where I Can Breathe Easy) [wl_idol_02_09]
10. その手をもう一度 (Take That Hand Once Again) [wl_idol_02_10]
11. これからも、アイドルとして (From Here On, As Idols) [wl_idol_02_11]

### Story Premise
While hosting a broadcast for the LUMINA Grand Prix in the Sekai, MORE MORE JUMP! and the Virtual Singers notice the wish-granting Sekai tree wilting because of strange black fragments clinging to it. When Minori touches one, the group is pulled into a shared dream. In that dream, MORE MORE JUMP! never formed and the four girls each walk separate, lonely paths—Minori as a struggling underground idol in Pop☆Drop, Haruka as a retired idol volunteering at a children's center, Airi as a popular variety streamer ("Happy Everyday"), and Shizuku as an exhaustively "perfect" fashion model—all quietly suppressing their true selves and their wish to deliver hope. 

Their paths gradually cross again: Minori reconnects with Haruka, Airi mentors Minori, Shizuku joins them for lunch and finds people who accept her true clumsy self, and Minori invites everyone to rehearse together for her selection audition. Dancing together restores their memories, Minori pulls Haruka back onto the stage, and the four awaken to find the fragment absorbed into the thriving tree.

## Segments

Cuts to remove:
- start → 00:09:56 — intro delay (standby title screen)
- 00:55:18 → end — outro (standby card)

Kept segments (host commentary runs throughout, including live voiceover reactions over the two story scenes):
- **00:09:56 → 00:12:54** — Host Introductions & Greeting (Yui Ogura & Rina Honnizumi, fan greetings "コンモア", chat interactions)
- **00:12:54 → 00:21:02** — Fan Letter Corner:
  - Letter 1 from Miso Nikomi Udon: Minori's handshake event & how hope reached the fans
  - Letter 2 from Pochi: Overcoming nervousness, pre-stage anxiety at Kanshasai
  - **17:30 (1050s) Highlight**: Yui-chan and Hon-chan discussion on dealing with anxiety and regret. Hon-chan shares coming home alone and dwelling on shortcomings, coping via cat paws (Sally-chan), food, sleep, and taking walks hands-free ("tebura") without a phone to reset as an ordinary human rather than "Rina Honnizumi."
- **00:21:02 → 00:27:58** — Scene 1 Watchalong & Discussion (Selected by Yui Ogura):
  - Episode 5 (めぐる希望): Children's center volunteer scene where Minori encourages Haruka and they agree to call each other "Minori" and "Haruka"
  - Discussion on Minori's pure, heartfelt words reaching Haruka
- **00:27:58 → 00:41:17** — Scene 2 Watchalong & Discussion (Selected by Rina Honnizumi):
  - Episode 9 (息のしやすい場所): Lunch scene with Minori, Airi, and Shizuku
  - Discussion of Shiho (Minori's nickname "Shiku-in" / zookeeper) rescuing Shizuku when lost at the station, Shizuku's cute airheadedness vs her public model image, and MMJ being a place where she can breathe easy
- **00:41:17 → 00:54:36** — Card Illustrations Corner:
  - Illustration dev team design notes and commentary for Minori, Haruka, Airi, and Shizuku
  - Card art close-up review & reactions (expressions, "wink-pero", teacups, costumes)
- **00:54:36 → 00:55:18** — Closing announcements & farewell

## Command (full pipeline)

```bash
uv run autosub run \
  "projects/projects/Project Sekai/Aftertalk/All ways Jump! with you Aftertalk/All ways Jump! with you Aftertalk.mkv" \
  --profile proseka/mmj \
  --backend chirp_3 \
  --speakers 2 \
  --speaker-map "projects/projects/Project Sekai/Aftertalk/All ways Jump! with you Aftertalk/speaker_map.toml" \
  --start 00:09:56 --end 00:55:18 \
  --chunk-size 30 \
  --llm-reasoning-effort low \
  --mark-chunks \
  --save-log
```

## Profile
- `proseka/mmj`

## Cast / Speakers
Two hosts (similar to "With Our Wounded Hands" AfterTalk):
- **小倉唯 (Yui Ogura)** — Voice of Minori Hanasato (花里みのり), Speaker 0, color `#ffccaa`
- **本泉莉奈 (Rina Honnizumi)** — Voice of Shizuku Hinomori (日野森雫), Speaker 1, color `#99eedd`

## YouTube Transcript Reference
The raw YouTube transcript has been extracted to `youtube_transcript.txt` (and `G-YoFvF-xCI.ja.vtt`) in this directory. Consult it when resolving ambiguous ASR homophones or verifying live banter phrasing.

## YouTube Title
[ENG SUB] All ways Jump! with you Aftertalk feat. Yui Ogura & Rina Honnizumi (Minori & Shizuku's VAs)

## YouTube Blurb (draft)

This special dual-hosted episode of ProSeka AfterTalk features both Yui Ogura (voice of Minori Hanasato) and Rina Honnizumi (voice of Shizuku Hinomori) looking back on MORE MORE JUMP!'s World Link 2 event "All ways Jump! with you."

In the fan message corner, they answer questions about how they handle nerves before major concerts like the MMJ Kanshasai and open up about personal reset routines—including an intimate conversation where Hon-chan describes coming home after recordings feeling frustrated about her performance, finding peace by squishing her cat Sally-chan's paws, and taking walks completely hands-free without a smartphone just to disconnect from being "Rina Honnizumi" and feel like an ordinary human being.

The hosts then react live to their favorite story scenes: Yui-chan revisits Episode 5 where Minori's earnest words reach a retired Haruka at the children's center, while Hon-chan revisits Episode 9 to laugh over Shizuku getting hopelessly lost at the train station (and getting rescued by her little sister Shiho) before finding friends in Minori and Airi who love her for her clumsy, authentic self. Finally, they unpack developer commentary for all four ★4 card illustrations from the "Empty Teatime" gacha and admire every detail from costumes to expressions.

Original livestream: https://www.youtube.com/watch?v=G-YoFvF-xCI

## Source
- **URL**: https://www.youtube.com/watch?v=G-YoFvF-xCI
- **Video Title**: プロセカアフタートーク All ways Jump! with you編
- **Stream Date**: 2025-08-21 21:00 JST

### Download command (yt-dlp)
```bash
uv run --with "yt-dlp>=2026.08.01" yt-dlp --no-update --no-playlist \
  -f "137+251/bv*[height<=1080]+ba/b" \
  --merge-output-format mkv \
  -o "projects/projects/Project Sekai/Aftertalk/All ways Jump! with you Aftertalk/All ways Jump! with you Aftertalk.mkv" \
  "https://www.youtube.com/watch?v=G-YoFvF-xCI"
```

## QC Status
- **Status**: Completed (Human-Pass Review)
- **File**: `All ways Jump! with you Aftertalk_final.ass`
- **Key QC Actions**:
  - Remapped inverted chunk 0 speaker attributions (`Yui Ogura` and `Rina Honnizumi`) and restyled watchalong audio (`Game`).
  - Standardized ASS header styles to canonical `DefaultOnibe` bottom-centered layout (`Fontsize 100`, BGR colors).
  - Standardized unit name: resolved all 19 `Momojan` instances to `MORE MORE JUMP!` / `MMJ`.
  - Corrected Haruka's former group name to **ASRUN** (fixed STT hallucination "ASUNARO").
  - Split 8 high-density commentary lines (flower language of marigolds, ASRUN costume, light/shadow contrasts) into comfortable sequential cues preserving 100% lore at $\le 2$ rows with zero manual `\N` breaks.
  - Polished conversational flow across 17:30 coping discussion (cat paws, Sally-chan, phone-free walks, mood-maker).
