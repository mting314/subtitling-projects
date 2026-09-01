# Unsteady, still steady step Aftertalk: AI vs Human Translation Evaluation Report

## Overview

Comparison of LLM-generated translation against human-edited final subtitles for the ProSeka AfterTalk: "Unsteady, still steady step" edition, hosted by Yuki Nakashima (voice of Shiho Hinomori from Leo/need).

- **AI translation lines**: 581
- **Human-edited lines**: 476
- **Japanese source lines**: 580
- **Unchanged lines**: 47
- **Total changes detected**: 710

> **Note on the source data**: The Chirp 3 transcription for this episode was unusually noisy — long silent runs got bundled into single multi-minute lines, the event title got mangled (transcribed as 'アンステディステディステップ' missing the 'still' syllable), and many short utterances were dropped. The human pass therefore involved heavy retiming and resegmentation in addition to translation polish. Many lines flagged as 'added' or 'deleted/merged' below reflect that resegmentation rather than truly missing/extra content.

---

## Category 4: Mistranslation Fixes

**Count: 16**

These are the most critical findings — cases where the AI translation conveyed incorrect meaning compared to the Japanese source.

### 4.1: Fan jargon
**Timestamp**: 0:12:47.82 - 0:12:49.86

| Version | Text |
|---------|------|
| AI | Hello, hello. |
| Human | _(removed/merged)_ |
| Japanese | てはこぴ、ありがとうござい。、、こんニー、こんニー。プロになったLeoNの念願の初ワンマンライブがいよいよ実現しそうでテンションが上がりまし。 |

**Analysis**: こんニー (kon-needo) is a Leo/need fan-community greeting (portmanteau of こんばんは + ニード). AI rendered it literally as 'Hello, hello', losing the in-jokey character of the host repeating viewers' greetings. Compare with the 'kon-niigo' issue from the Colors of Pure Sense report.

### 4.2: Game terminology
**Timestamp**: 0:30:18.36 - 0:30:19.72

| Version | Text |
|---------|------|
| AI | This is the pre-training version. |
| Human | This is the untrained art. |
| Japanese | 、、さっき、8話にも出てき、、カードのイラストではございます、これが特訓。 |

**Analysis**: AI used ML-style 'pre-training/post-training' for the gacha card states 特訓前/特訓後, which should be 'untrained/trained' in standard ProSeka community vocabulary.

### 4.3: Game terminology
**Timestamp**: 0:30:38.00 - 0:30:39.44

| Version | Text |
|---------|------|
| AI | And here is the post-training version. |
| Human | And here's the trained art. |
| Japanese | そして特訓後が。ん、いい。 |

**Analysis**: Same 特訓後 → 'post-training' issue. Should be 'trained'.

### 4.4: Game terminology
**Timestamp**: 0:31:28.24 - 0:31:30.60

| Version | Text |
|---------|------|
| AI | Ichika's training art. |
| Human | Ichika's trained art. |
| Japanese | いちかの特訓。これ7話でありました。 |

**Analysis**: 特訓 (tokkun) translated as 'Training' instead of 'trained'. The Japanese refers to the gacha card upgrade state, not literal training.

### 4.5: Game terminology
**Timestamp**: 0:31:41.34 - 0:31:44.36

| Version | Text |
|---------|------|
| AI | And here is the post-training version. |
| Human | And here is the trained art. |
| Japanese | 。では続いてこれが特訓。。 |

**Analysis**: 特訓後 → 'post-training version' should be 'trained art'.

### 4.6: Game terminology
**Timestamp**: 0:33:23.28 - 0:33:25.72

| Version | Text |
|---------|------|
| AI | Pre-training Rin. |
| Human | Untrained Rin. |
| Japanese | 、特訓前の鈴。 |

**Analysis**: 特訓前 → 'Pre-training' should be 'Untrained'.

### 4.7: Game terminology
**Timestamp**: 0:34:53.80 - 0:34:55.20

| Version | Text |
|---------|------|
| AI | Shiho's Training card. |
| Human | Shiho's trained art. |
| Japanese | 、志歩ちゃん行き。志歩ちゃんの特訓。これさありがとうございまし、本当。 |

**Analysis**: 特訓 → 'Training card' should be 'trained art'.

### 4.8: Game terminology
**Timestamp**: 0:36:34.68 - 0:36:36.58

| Version | Text |
|---------|------|
| AI | And that was only the Pre-Training version. |
| Human | And that was only the untrained. |
| Japanese | いやいや、ちょっと好きが溢れてしまっ。まだ特訓前だっつうの。特訓後も見ていき。 |

**Analysis**: 特訓前 → 'Pre-Training version' should be 'untrained'.

### 4.9: Game terminology
**Timestamp**: 0:36:36.58 - 0:36:38.28

| Version | Text |
|---------|------|
| AI | Let's look at the Post-Training one too. |
| Human | Let's look at the trained art too. |
| Japanese | まだ特訓前だっつうの。特訓後も見ていき。、戻っちゃっ。 |

**Analysis**: 特訓後 → 'Post-Training one' should be 'trained art'.

### 4.10: Character name
**Timestamp**: 0:37:38.16 - 0:37:40.38

| Version | Text |
|---------|------|
| AI | And finally... Saki. |
| Human | And finally... MEIKO. |
| Japanese | 、最後、、咲子。咲子さん、、こちら星2のやつです。 |

**Analysis**: AI confused 咲子 (Sakiko, the Vocaloid MEIKO's localized name) with 咲希 (Saki Tenma of Leo/need). This card section is about the Virtual Singer MEIKO, not the Leo/need member Saki.

### 4.11: Character name
**Timestamp**: 0:37:40.38 - 0:37:43.82

| Version | Text |
|---------|------|
| AI | This is Saki's 2-star card. |
| Human | This is MEIKO's 2-star card. |
| Japanese | 、最後、、咲子。咲子さん、、こちら星2のやつです。、、なん、咲子さんが着るとまたちょっと、雰囲気が変わっていう、 |

**Analysis**: Same 咲子/MEIKO ↔ 咲希/Saki confusion. Saki is a 4-star main character; this 2-star card is for Sub-Vocalist MEIKO.

### 4.12: Character name
**Timestamp**: 0:37:43.82 - 0:37:49.66

| Version | Text |
|---------|------|
| AI | When Saki wears it, the atmosphere changes, |
| Human | When MEIKO wears the varsity jacket, it's a completely different vibe, |
| Japanese | 咲子さん、、こちら星2のやつです。、、なん、咲子さんが着るとまたちょっと、雰囲気が変わっていう、大人っぽく見えるのがまたすごいですよ、これ。 |

**Analysis**: Same MEIKO/Saki confusion continued.

### 4.13: Producer name
**Timestamp**: 0:38:53.70 - 0:39:05.44

| Version | Text |
|---------|------|
| AI | Next, I'd like to talk about the song and the MV while watching the 2D MV for 'Transparent Palette,' which Akuera-san drew specifically for this event. |
| Human | Next, let's watch the 2DMV for 'Transparent Palette,' the song for this event commissioned from aqu3ra. |
| Japanese | 。、続いてはです、今回のイベントのためにアクエラさんに描き下ろしいただきました透明なパレットの2DMVを見て楽曲やMVについてのお話をしていこうと思い。、では昨日公開されました2DMV見ていき。 |

**Analysis**: アクエラ is the producer aqu3ra (official stylization with numeral '3'). AI transliterated as 'Akuera-san' rather than using the official romanization.

### 4.14: Brand capitalization
**Timestamp**: 0:45:18.68 - 0:45:22.08

| Version | Text |
|---------|------|
| AI | It's been uploaded to the official Proseka YouTube channel, |
| Human | The 2DMV is already uploaded to the official ProSeka YouTube channel, so be sure to watch it there. |
| Japanese | めちゃめちゃ可愛いDMVになっておりますの、皆、ぜひご覧。こちらの方、プロセカ公式YouTubeにアップされておりますの、よろしくお願いし。 |

**Analysis**: The official stylization is 'ProSeka' (capital S). AI used 'Proseka' which doesn't match project conventions.

### 4.15: Title preservation
**Timestamp**: 0:45:24.00 - 0:45:33.24

| Version | Text |
|---------|------|
| AI | And with that, our short time is up. This concludes the Proseka After Talk: Unsteady Steady Step edition. |
| Human | but that's all we have for the "Unsteady, still steady step" AfterTalk. |
| Japanese | ということ、短い時間でした、プロセカアフタートークアンステディステディステップ編は以上で終了となり。お。 |

**Analysis**: The official song/event title is 'Unsteady, still steady step' (with the 'still'). The Chirp transcription dropped the 'still' syllable and AI transliterated literally as 'Unsteady Steady Step', losing the official title.

### 4.16: Title preservation
**Timestamp**: 0:46:02.24 - 0:46:09.44

| Version | Text |
|---------|------|
| AI | So, for those who haven't finished the 'Unsteady Steady Step' event story yet, |
| Human | So with that, if you haven't watched the "Unsteady, still steady step" event story yet, |
| Japanese | もっと喋っていいの、ありがとうござい。、ということ、、イベントアンステディステディステップのストーリーはまだ見終わってないという方はです、次のイベントが始まっ、ストーリーのイベントストーリーから全て読むことができますの、 |

**Analysis**: Same dropped-'still' title issue.

---

## Category 3: Wording Changes

**Count: 213**

Style, naturalness, or clarity improvements where the core meaning is preserved. (Includes both wording-only and wording+timing changes.)

### 3.1
**Timestamp**: 0:10:03.28 - 0:10:03.78

- **AI**: Thank you so much
- **Human**: Ah, thank God I said it right.
- **JP**: nide)の日野守志歩役の中島裕貴。、この

### 3.2
**Timestamp**: 0:12:45.48 - 0:12:47.82

- **AI**: for this letter.
- **Human**: Thanks for all the messages, everyone.
- **JP**: てはこぴ、ありがとうござい。、、こんニー、こんニー。

### 3.3
**Timestamp**: 0:12:49.86 - 0:12:55.10

- **AI**: I am so excited that Leo/need's long-awaited first one-man live as pros is finally happening.
- **Human**: "I was really glad to see Leo/need growing more as pros in this story."
- **JP**: 、、こんニー、こんニー。プロになったLeoNの念願の初ワンマンライブがいよいよ実現しそうでテンションが上がりまし。個人的にはみんなで楽器をシャッフルするMCコーナーを本番でもやってほしいですといただきまし。

### 3.4
**Timestamp**: 0:13:00.92 - 0:13:01.64

- **AI**: Thank you very much.
- **Human**: Thank you for the message.
- **JP**: 個人的にはみんなで楽器をシャッフルするMCコーナーを本番でもやってほしいですといただきまし。ありがとうござい。

### 3.5
**Timestamp**: 0:13:02.32 - 0:13:03.72

- **AI**: I would definitely
- **Human**: Yeah. "If I could swing both, I'd definitely do it."
- **JP**: 確かに見。

### 3.6
**Timestamp**: 0:13:05.11 - 0:13:05.61

- **AI**: like to see that.
- **Human**: Hard to keep a straight face.
- **JP**: ?

### 3.7
**Timestamp**: 0:13:06.60 - 0:13:09.24

- **AI**: But she might hate it.
- **Human**: I'd just have to choose one.
- **JP**: でも、嫌か。

### 3.8
**Timestamp**: 0:13:10.36 - 0:13:15.08

- **AI**: If I were in her position, I would be incredibly nervous.
- **Human**: But if it were like the story, where I wanted to do both things...
- **JP**: もし自分がその立場だったらめっちゃ緊張しちゃうか。なんかなん?

### 3.9
**Timestamp**: 0:13:15.08 - 0:13:17.24

- **AI**: I wonder...
- **Human**: Yeah...
- **JP**: もし自分がその立場だったらめっちゃ緊張しちゃうか。なんかなん?

### 3.10
**Timestamp**: 0:13:17.88 - 0:13:27.34

- **AI**: If Shiho had to play the drums or the keyboard instead of the bass,
- **Human**: if it really were a "one or the other" situation,
- **JP**: 志歩がもしベースじゃなく、、ドラムだっ、、、キーボードってなった場合受け入れてくんの、くれるのかなってちょっと気持ちになっ。

### 3.11
**Timestamp**: 0:13:27.34 - 0:13:29.36

- **AI**: I wonder if she would actually be willing to go along with it.
- **Human**: There really are way too many "st st"s.
- **JP**: 志歩がもしベースじゃなく、、ドラムだっ、、、キーボードってなった場合受け入れてくんの、くれるのかなってちょっと気持ちになっ。この、、リハだったからやってくれたけど、音楽、、

### 3.12
**Timestamp**: 0:16:32.60 - 0:16:36.56

- **AI**: I want to see her getting all flustered.
- **Human**: Seeing her get flustered like that... that'd be really fun to see.
- **JP**: そのわたわたしてるところを見てみたいですよ。

### 3.13
**Timestamp**: 0:16:37.28 - 0:16:42.48

- **AI**: I really want to see everyone struggling and saying they can't do it.
- **Human**: "I was really excited to see Leo/need finally getting an opportunity to do their much-awaited one-man live."
- **JP**: こう、みんな、、できないと言って言ってるとこちょっと見たいですよ。

### 3.14
**Timestamp**: 0:16:43.12 - 0:16:46.85

- **AI**: I feel like I could listen to that and watch it forever.
- **Human**: I for sure could watch that forever.
- **JP**: 全然それなら聞いてられる、永遠見てられる気が。。

### 3.15
**Timestamp**: 0:16:48.60 - 0:16:49.96

- **AI**: I want them to do it.
- **Human**: If I really had to do that, I'd be so nervous.
- **JP**: やってほしい。どうするんだろう。

### 3.16
**Timestamp**: 0:16:49.96 - 0:16:51.30

- **AI**: I wonder what would happen.
- **Human**: Hope we get that one day. Curious what exactly would happen.
- **JP**: やってほしい。どうするんだろう。ちょっと今後の、ストーリーが楽しみですけど。

### 3.17
**Timestamp**: 0:16:51.30 - 0:16:54.24

- **AI**: I am looking forward to seeing how the story develops.
- **Human**: But yeah, I'm interested in where the story will go from here.
- **JP**: どうするんだろう。ちょっと今後の、ストーリーが楽しみですけど。

### 3.18
**Timestamp**: 0:16:55.16 - 0:16:57.02

- **AI**: I can't really imagine Shiho on the drums.
- **Human**: "I can't imagine Shiho-chan on the drums." Ahh, that's true.
- **JP**: 志歩ちゃんがドラムとか想像つか。、、確か。

### 3.19
**Timestamp**: 0:16:57.02 - 0:16:58.64

- **AI**: That is true.
- **Human**: That being said...
- **JP**: 志歩ちゃんがドラムとか想像つか。、、確か。でもなんかリズムキープが得意そうだからなんか卒なくこなせそうだけどこう、

### 3.20
**Timestamp**: 0:16:58.64 - 0:17:06.50

- **AI**: She seems like she would be good at keeping rhythm, so she might handle it well, but
- **Human**: Hmm, I don't know, she seems good at keeping rhythm though,
- **JP**: 、、確か。でもなんかリズムキープが得意そうだからなんか卒なくこなせそうだけどこう、手と足が別々の動きするから、結局わたわたするのか。

### 3.21
**Timestamp**: 0:17:06.50 - 0:17:11.90

- **AI**: since your hands and feet have to move differently, she might end up fumbling after all.
- **Human**: But your hands and feet are doing different things,
- **JP**: でもなんかリズムキープが得意そうだからなんか卒なくこなせそうだけどこう、手と足が別々の動きするから、結局わたわたするのか。気になる。

### 3.22
**Timestamp**: 0:17:13.56 - 0:17:15.53

- **AI**: I would like to see her on guitar too.
- **Human**: "I'd wanna see her on guitar!"
- **JP**: 、ギターは見てみたいか。。

### 3.23
**Timestamp**: 0:17:15.53 - 0:17:16.21

- **AI**: Yes.
- **Human**: Nope.
- **JP**: 、ギターは見てみたいか。。

### 3.24
**Timestamp**: 0:17:17.04 - 0:17:18.12

- **AI**: I really want to see that.
- **Human**: I, uh, I don't really think I'd like that.
- **JP**: ちょっと見てみたさある。

### 3.25
**Timestamp**: 0:17:20.16 - 0:17:21.80

- **AI**: She would definitely end up saying she can't do it.
- **Human**: so she might end up a little flustered too. I'm really curious though.
- **JP**: できないってなるの絶対。確か。

### 3.26
**Timestamp**: 0:17:27.08 - 0:17:28.80

- **AI**: I definitely want to see that.
- **Human**: I definitely would want to see that happen.
- **JP**: 確かに見たい。ちょっと、今後の、ストーリー皆さん期待していって。

### 3.27
**Timestamp**: 0:17:28.80 - 0:17:32.54

- **AI**: Everyone, please look forward to the future story.
- **Human**: So yeah, everyone, definitely look forward to the coming stories.
- **JP**: 確かに見たい。ちょっと、今後の、ストーリー皆さん期待していって。、お頼りありがとうござい。

### 3.28
**Timestamp**: 0:17:32.54 - 0:17:34.24

- **AI**: Thank you for the letter.
- **Human**: Thank you for the message.
- **JP**: ちょっと、今後の、ストーリー皆さん期待していって。、お頼りありがとうござい。

### 3.29
**Timestamp**: 0:17:35.12 - 0:17:41.74

- **AI**: I have picked out another scene that I personally want to talk about,
- **Human**: Alright, I've picked a scene from the story I'd like to talk about, so let's watch it together.
- **JP**: 、今回も私が個人的に語りたいシーンをピックアップさせていただいておりますの、もう早速見ていきましょうか。

### 3.30
**Timestamp**: 0:17:41.74 - 0:17:43.16

- **AI**: so let's take a look right away.
- **Human**: so I feel like she might be able to keep up.
- **JP**: 、今回も私が個人的に語りたいシーンをピックアップさせていただいておりますの、もう早速見ていきましょうか。

### 3.31
**Timestamp**: 0:17:43.68 - 0:17:45.98

- **AI**: The one I chose is from Episode 8.
- **Human**: This time, I chose Chapter 8.
- **JP**: 私が選んだのは8話になり。。

### 3.32
**Timestamp**: 0:17:45.98 - 0:17:46.56

- **AI**: Here it is.
- **Human**: Here we go!
- **JP**: 私が選んだのは8話になり。。

### 3.33
**Timestamp**: 0:17:56.60 - 0:17:58.96

- **AI**: She is giving up on both the one-man and the Fan Festa.
- **Human**: asking from the perspective of, "which one will make our fans the happiest?",
- **JP**: ワンマンとファンフェスタは諦めまし。自分なりにし調べられることは全部調べられたと。

### 3.34
**Timestamp**: 0:18:08.96 - 0:18:13.98

- **AI**: But what about Hona-chan's role as a leader?
- **Human**: Speaking of Hona-chan as a leader,
- **JP**: でもほなちゃんのこのリーダーとしてのこの何て言うん?どっちがいいのか、まだ

### 3.35
**Timestamp**: 0:18:20.68 - 0:18:25.52

- **AI**: It is great that she researches every little detail.
- **Human**: I think that's incredible. Shows her determination as a leader.
- **JP**: 私の中で答えが出て。隅々まで調べるっていうのはすごくいいですよ。

### 3.36
**Timestamp**: 0:18:52.16 - 0:18:56.60

- **AI**: It is wonderful that she feels she has to decide on her own feelings here.
- **Human**: It's impressive that she realizes she needs to decide this based on her own feelings,
- **JP**: ここで自分の気持ちを決めなくちゃって思えるのがすごいいいよ。

### 3.37
**Timestamp**: 0:18:58.44 - 0:19:01.40

- **AI**: But I also hope it doesn't become too much of a burden for her.
- **Human**: but also realizing she can't keep everyone waiting forever.
- **JP**: でもなんか負担にならないで欲しいなっていう気持ちも。

### 3.38
**Timestamp**: 0:19:23.82 - 0:19:25.14

- **AI**: Episode 7 was great too.
- **Human**: Chapter 7 was also really good.
- **JP**: 。7話も良かった。1人じゃないって思えるんだよ。

### 3.39
**Timestamp**: 0:19:25.14 - 0:19:27.28

- **AI**: It makes you feel like you aren't alone.
- **Human**: I was like "woah".
- **JP**: 7話も良かった。1人じゃないって思えるんだよ。

### 3.40
**Timestamp**: 0:19:41.80 - 0:19:43.96

- **AI**: If you think too much, you won't be able to choose.
- **Human**: Overthinking makes it tougher to choose.
- **JP**: 考えすぎると選べなくなっちゃうよ。

### 3.41
**Timestamp**: 0:20:09.32 - 0:20:10.20

- **AI**: Good work.
- **Human**: Good for them.
- **JP**: お疲れ様。

### 3.42
**Timestamp**: 0:20:14.24 - 0:20:16.00

- **AI**: There is something I need to report urgently.
- **Human**: This is an amazing opportunity for them.
- **JP**: 急ぎ報告したいことがありまし。体の良さにおおってなっ。

### 3.43
**Timestamp**: 0:20:33.44 - 0:20:35.08

- **AI**: Please, don't be alarmed.
- **Human**: Shindo-san's very large manly frame here.
- **JP**: 、、身構えないで。

### 3.44
**Timestamp**: 0:21:06.60 - 0:21:08.00

- **AI**: I see.
- **Human**: Indeed.
- **JP**: そうだったんです。

### 3.45
**Timestamp**: 0:21:09.64 - 0:21:12.44

- **AI**: But I'm glad they're feeling better.
- **Human**: Ah, it's that scene I mentioned laughing about.
- **JP**: でも元気になられて良かった。

### 3.46
**Timestamp**: 0:22:16.24 - 0:22:17.04

- **AI**: This is so realistic.
- **Human**: Super realistic scenario.
- **JP**: 本当リアルだよ。

### 3.47
**Timestamp**: 0:23:36.32 - 0:23:38.92

- **AI**: I'm just so relieved.
- **Human**: It's okay to feel relieved!
- **JP**: 私安心したん。

### 3.48
**Timestamp**: 0:24:02.92 - 0:24:04.10

- **AI**: Truly admirable.
- **Human**: That was really memorable for me.
- **JP**: すごいえらい。ほな。

### 3.49
**Timestamp**: 0:24:05.51 - 0:24:06.01

- **AI**: This isn't good.
- **Human**: Hona-chan is such a good girl...
- **JP**: ダメ。

### 3.50
**Timestamp**: 0:24:19.48 - 0:24:24.12

- **AI**: Times when I'll have to make a decision where there is no right answer.
- **Human**: I was worried that Honami-chan might panic if she really did have to make that tough decision.
- **JP**: 正解がない選択を決断しないといけない時。

### 3.51
**Timestamp**: 0:24:48.83 - 0:24:51.28

- **AI**: And that was Episode 8.
- **Human**: That was Chapter 8.
- **JP**: 。ということで8話でございまし。

### 3.52
**Timestamp**: 0:25:11.78 - 0:25:18.76

- **AI**: The scene where she resolves to lead everyone as their leader was really moving.
- **Human**: but then resolving herself to continue being a strong leader for Leo/need.
- **JP**: 選ぶって言ってたの、っていう風、、なんか少し落ち込んでいるという、、さらにリーダーとしてみんなを導いていけるよう、、決心するシーンが本当に印象的で

### 3.53
**Timestamp**: 0:25:20.28 - 0:25:24.88

- **AI**: If it were me, I'd probably be more optimistic, like 'Oh, wow!'
- **Human**: If I were in her shoes, I'd probably just blow it off like,
- **JP**: 、結構自分だったら楽観的、おやっ!みたい、

### 3.54
**Timestamp**: 0:25:24.88 - 0:25:25.38

- **AI**: That's how I'd feel.
- **Human**: but that said... how to say it...
- **JP**: 、結構自分だったら楽観的、おやっ!みたい、

### 3.55
**Timestamp**: 0:25:25.88 - 0:25:29.68

- **AI**: I've never had a job like being a leader before, so...
- **Human**: and was feeling a little disappointed in herself,
- **JP**: 思っちゃうタイプだ、、リーダーっていう、おしごこと、、やったことがないからっていうのもあるんですけどそこを、

### 3.56
**Timestamp**: 0:25:36.24 - 0:25:44.26

- **AI**: I find her strong sense of responsibility to be quite reliable,
- **Human**: I definitely feel that Honami is super dependable and responsible,
- **JP**: ちょっと責任を強く感じている部分が、頼もしいなっていう部分もあり、そんなに重くならないで欲しいなっていう気持ちもありつつ、そのまま行っちゃうと潰れちゃうか、

### 3.57
**Timestamp**: 0:25:55.70 - 0:25:58.32

- **AI**: That's why I chose this scene for today.
- **Human**: So that was our scene for today.
- **JP**: 穂波ちゃん、みたいな心配になるようなシーンでもあったの、ちょっと今回はこのシーンを選ばせていただきまし。

### 3.58
**Timestamp**: 0:26:28.16 - 0:26:33.44

- **AI**: I'm not sure how Honami will make her choices from now on, or
- **Human**: I'm not sure how Honami will make her choices from now on,
- **JP**: 何事、やっぱそういう決断をしなきゃいけない時は多々あるから。、今後どういう風に穂波が選択をしていくの、そして、Leonidが、どういう選択を取っていくの、ちょっと分からないですけれど、

### 3.59
**Timestamp**: 0:26:33.44 - 0:26:37.50

- **AI**: what kind of path Leo/need will take, but
- **Human**: or what kind of path Leo/need will take,
- **JP**: 、今後どういう風に穂波が選択をしていくの、そして、Leonidが、どういう選択を取っていくの、ちょっと分からないですけれど、我々は見守っていきたいななんて思っております、みんながどうか仲&#悪とか、

### 3.60
**Timestamp**: 0:26:37.50 - 0:26:45.94

- **AI**: I want to keep watching over them. I hope they don't end up on bad terms or
- **Human**: but I want to keep watching over them.
- **JP**: Leonidが、どういう選択を取っていくの、ちょっと分からないですけれど、我々は見守っていきたいななんて思っております、みんながどうか仲&#悪とか、メンタルが壊れちゃったりとかしないことを願い。

### 3.61
**Timestamp**: 0:26:45.94 - 0:26:50.76

- **AI**: have their mental health suffer.
- **Human**: or have their mental health suffer.
- **JP**: 我々は見守っていきたいななんて思っております、みんながどうか仲&#悪とか、メンタルが壊れちゃったりとかしないことを願い。

### 3.62
**Timestamp**: 0:26:59.08 - 0:27:05.28

- **AI**: Project Sekai event stories always leave some kind of foreshadowing.
- **Human**: Oh yeah, Project Sekai event stories always leave some kind of foreshadowing.
- **JP**: そうなんだよ。必ずなんかプロセカのイベントストーリーって何か伏線を残していきますよ。

### 3.63
**Timestamp**: 0:27:06.08 - 0:27:08.32

- **AI**: It's only natural, since the story continues.
- **Human**: I mean, of course they do, since the story'll continue.
- **JP**: 、当たり前なんだ、続いていくから。

### 3.64
**Timestamp**: 0:27:08.84 - 0:27:11.68

- **AI**: It's natural, but still...
- **Human**: Of course it'll continue, but...
- **JP**: 当たり前なんですけれど、、。

### 3.65
**Timestamp**: 0:27:22.92 - 0:27:25.96

- **AI**: I want them to worry a lot,
- **Human**: This is when they should be worrying a lot,
- **JP**: いっぱい悩んでいただいて、

### 3.66
**Timestamp**: 0:27:26.84 - 0:27:29.60

- **AI**: and learn from their failures.
- **Human**: and learning a looot from their failures.
- **JP**: 失敗もして学んで。

### 3.67
**Timestamp**: 0:27:39.64 - 0:27:44.82

- **AI**: It was in Episode 7, and it also appeared in the middle of Episode 8.
- **Human**: It was in Episode 7, and we also saw it a bit in Episode 8,
- **JP**: ということ、、個人的には、もう1個、、気になるシーンはあったんです。、7話が、、8話の途中にも、出てきたりとかもしてました、、7話で、穂波といちかが一緒にミクちゃんのライブ見に行くのすごく個人的には好きでいちかがいつも以上にテンション上がってたじゃないです。

### 3.68
**Timestamp**: 0:27:44.82 - 0:27:53.88

- **AI**: I really liked the part in Episode 7 where Honami and Ichika go to see Miku's concert. Ichika was more excited than usual.
- **Human**: but I really liked the part in Episode 7 where Honami and Ichika go to see the Miku concert.
- **JP**: 、7話が、、8話の途中にも、出てきたりとかもしてました、、7話で、穂波といちかが一緒にミクちゃんのライブ見に行くのすごく個人的には好きでいちかがいつも以上にテンション上がってたじゃないです。キャッキャっみたい。

### 3.69
**Timestamp**: 0:27:55.00 - 0:27:56.08

- **AI**: like, "It's Miku!"
- **Human**: She was all like "Yay! It's Miku!"
- **JP**: キャッキャっみたい。はミク、みたい。

### 3.70
**Timestamp**: 0:27:59.08 - 0:28:01.44

- **AI**: I thought about featuring that part too, but
- **Human**: I thought about featuring that part too,
- **JP**: 本当はそこも取り上げようかなって思ったんですけど

### 3.71
**Timestamp**: 0:28:10.64 - 0:28:11.68

- **AI**: So I decided to stick with Episode 8.
- **Human**: So I just went with Episode 8.
- **JP**: 8話だけにしまし。

### 3.72
**Timestamp**: 0:28:13.88 - 0:28:16.24

- **AI**: Episode 7 was really cute too.
- **Human**: But Episode 7 was really cute too.
- **JP**: 、可愛かったよ、7話も。

### 3.73
**Timestamp**: 0:28:17.68 - 0:28:19.12

- **AI**: It makes me want to watch it again.
- **Human**: "I kinda wanna watch it again."
- **JP**: もう1回見返したくなってき。、。

### 3.74
**Timestamp**: 0:28:20.84 - 0:28:22.26

- **AI**: You should go back and read it.
- **Human**: By all means, please go back and read it again.
- **JP**: 読み返してみて。可愛かったよ、あそこ、本当に。

### 3.75
**Timestamp**: 0:28:22.26 - 0:28:24.60

- **AI**: That part was truly adorable.
- **Human**: That Miku live part was super adorable.
- **JP**: 読み返してみて。可愛かったよ、あそこ、本当に。

### 3.76
**Timestamp**: 0:28:26.12 - 0:28:27.56

- **AI**: I want to go to a Miku concert too!
- **Human**: I want to go to a Miku live too!
- **JP**: 私もミクちゃんのライブ行きたいっ。確か、。

### 3.77
**Timestamp**: 0:28:30.56 - 0:28:36.48

- **AI**: Back when the title was still "MikuPa," I'm from Wakayama,
- **Human**: Actually, back when the title was still "MikuPa,"
- **JP**: 私は1、あのタイトルがまだミクパの時に和歌山出身なんです、和歌山でライブがあっ、もういちかと同じテンションでし。

### 3.78
**Timestamp**: 0:28:36.48 - 0:28:39.68

- **AI**: and there was a concert there. I was just as excited as Ichika.
- **Human**: I was just as excited as Ichika.
- **JP**: 私は1、あのタイトルがまだミクパの時に和歌山出身なんです、和歌山でライブがあっ、もういちかと同じテンションでし。

### 3.79
**Timestamp**: 0:28:40.20 - 0:28:41.54

- **AI**: I was like, "It's Miku!"
- **Human**: I was like, "It's Miku-chan!"
- **JP**: ミク、みたい。ミク、みたい。

### 3.80
**Timestamp**: 0:28:41.54 - 0:28:42.82

- **AI**: "It's Miku!"
- **Human**: "Miku!"
- **JP**: ミク、みたい。ミク、みたい。感じでテンション上がってたんで。

### 3.81
**Timestamp**: 0:28:42.82 - 0:28:44.96

- **AI**: I was getting all hyped up like that.
- **Human**: I was super hyped for that.
- **JP**: ミク、みたい。感じでテンション上がってたんで。

### 3.82
**Timestamp**: 0:28:46.14 - 0:28:49.30

- **AI**: I want everyone to experience that feeling too.
- **Human**: I hope everyone gets a chance to be as excited as that.
- **JP**: 。みんなにもそれを味わっていただきたいです。ということ、ちょっと脱線してしまいました、、今回もです、

### 3.83
**Timestamp**: 0:28:49.30 - 0:28:52.64

- **AI**: Anyway, I got a bit sidetracked again. This time,
- **Human**: Anyway, I got a bit sidetracked again.
- **JP**: みんなにもそれを味わっていただきたいです。ということ、ちょっと脱線してしまいました、、今回もです、カードのイラストの方も見ていければなと思い。

### 3.84
**Timestamp**: 0:28:52.64 - 0:28:55.80

- **AI**: I'd like to take a look at the card illustrations.
- **Human**: Alright, let's take a look at the card illustrations.
- **JP**: ということ、ちょっと脱線してしまいました、、今回もです、カードのイラストの方も見ていければなと思い。まず、、イラスト制作チームに衣装についてのコメントいただきましたので紹介していき。

### 3.85
**Timestamp**: 0:28:55.80 - 0:29:01.86

- **AI**: First, I'll share some comments from the illustration team regarding the outfits.
- **Human**: First, I'll share some comments from the illustration team about the outfits.
- **JP**: カードのイラストの方も見ていければなと思い。まず、、イラスト制作チームに衣装についてのコメントいただきましたので紹介していき。、今回は穂波がリーダーとして決断をすることに関しての重要性や重みを再認識するようなストーリーでし。

### 3.86
**Timestamp**: 0:29:09.02 - 0:29:22.24

- **AI**: It's an episode about a leader's struggles, but the design reflects a positive outlook on the best choice for Leo/need.
- **Human**: the illustrations reflect a positive determination to find the best path forward for Leo/need.
- **JP**: 、今回は穂波がリーダーとして決断をすることに関しての重要性や重みを再認識するようなストーリーでし。リーダーゆえの悩みを持つ回ではあります、Leonidにとって何が最善の選択かを前向きに見つめていく姿勢や楽曲のリズミカルな印象から歩みを止めない軽やかさをイメージできるような、かつLeonidとしては珍しい甘めの可愛らしさがフックになる、

### 3.87
**Timestamp**: 0:29:22.24 - 0:29:27.00

- **AI**: Inspired by the rhythmic song, it captures a lightheartedness that keeps moving forward, with a sweet cuteness rare for the band.
- **Human**: the outfit design conveys a lighthearted "keep moving forward" attitude.
- **JP**: リーダーゆえの悩みを持つ回ではあります、Leonidにとって何が最善の選択かを前向きに見つめていく姿勢や楽曲のリズミカルな印象から歩みを止めない軽やかさをイメージできるような、かつLeonidとしては珍しい甘めの可愛らしさがフックになる、ポップで可愛いカラーリングのスターちゃんとカジュアルなスニーカーを用いたデザインにしてい。

### 3.88
**Timestamp**: 0:29:27.00 - 0:29:32.16

- **AI**: The design features pop and cute star patterns along with casual sneakers.
- **Human**: we used pop and cute design elements like colorful star patterns and sneakers as the motif for our design.
- **JP**: かつLeonidとしては珍しい甘めの可愛らしさがフックになる、ポップで可愛いカラーリングのスターちゃんとカジュアルなスニーカーを用いたデザインにしてい。

### 3.89
**Timestamp**: 0:29:32.72 - 0:29:41.06

- **AI**: To show them choosing their path, each of the three has a planisphere-like element in their outfit.
- **Human**: each of the three has a star chart-like element in their outfit.
- **JP**: 、悩みながら進んで、道を選んでいくという点、3人ともワンポイントとしての衣装のどこかに星座板のよう、、デザインのカラーパレットをコンパスに見立てたアイテムを入れ込もうと考えてい。

### 3.90
**Timestamp**: 0:29:46.40 - 0:29:51.40

- **AI**: This palette represents the choice between Leo/need's new song and Miku's song,
- **Human**: This palette represents not only the choice between Leo/need's new song and Miku's song,
- **JP**: カラーパレットは今回のLeonidの新曲かミクの曲かを選ぶというところ、、今回の2択であっ、その先の未来でも続くたくさんの選択肢という意味合いで用いていますということで、

### 3.91
**Timestamp**: 0:29:51.40 - 0:29:59.64

- **AI**: symbolizing the many choices that will continue to appear in the future.
- **Human**: but also the many choices that they will have to make in the future.
- **JP**: カラーパレットは今回のLeonidの新曲かミクの曲かを選ぶというところ、、今回の2択であっ、その先の未来でも続くたくさんの選択肢という意味合いで用いていますということで、見ていき。

### 3.92
**Timestamp**: 0:30:01.56 - 0:30:04.52

- **AI**: Now, where should we start?
- **Human**: Who should we start with?
- **JP**: 、、まずはどうしようか?

### 3.93
**Timestamp**: 0:30:12.72 - 0:30:13.70

- **AI**: Here they are.
- **Human**: Here's Honami.
- **JP**: こちら。、、さっき、8話にも出てき、、カードのイラストではございます、

### 3.94
**Timestamp**: 0:30:13.70 - 0:30:18.36

- **AI**: This is the card illustration for the scene that appeared in Episode 8.
- **Human**: This is from that scene in Episode 8.
- **JP**: こちら。、、さっき、8話にも出てき、、カードのイラストではございます、これが特訓。

### 3.95
**Timestamp**: 0:30:20.24 - 0:30:28.84

- **AI**: Honami has a bit of a surprised look on her face, but that smartphone case is so soothing.
- **Human**: but her smartphone case is super soothing.
- **JP**: 、ちょっとね、ほなちゃんの顔、はって顔してますけどこの携帯のスマホケースで癒されます。

### 3.96
**Timestamp**: 0:30:30.84 - 0:30:33.72

- **AI**: Is that a Shiba Inu on it?
- **Human**: Is that a Shiba Inu?
- **JP**: 柴犬っぽいのがいるのか?

### 3.97
**Timestamp**: 0:30:34.28 - 0:30:36.40

- **AI**: It looks like one. It's very comforting.
- **Human**: It looks like one. Very comforting.
- **JP**: そんな感じ、すごく癒されます。

### 3.98
**Timestamp**: 0:30:39.44 - 0:30:40.56

- **AI**: Oh, this is nice.
- **Human**: Very nice.
- **JP**: そして特訓後が。ん、いい。

### 3.99
**Timestamp**: 0:30:42.12 - 0:30:48.68

- **AI**: This one is in portrait orientation. It looks even better when you view it that way.
- **Human**: It looks really good if you turn it that way.
- **JP**: 今度若干縦画面になってるという、縦画面で見るとさらに良く見える感じがまたいいですよ。

### 3.100
**Timestamp**: 0:30:50.36 - 0:30:55.54

- **AI**: Leo/need hasn't really had anything this pop and cute until now.
- **Human**: Now that I think about it, Leo/need hasn't really had anything this pop and cute yet.
- **JP**: 確かに今までLeonidなかった、ここまでポップで可愛いという。。

### 3.101
**Timestamp**: 0:30:59.00 - 0:31:01.20

- **AI**: There's so much detail in it.
- **Human**: It's kind of a portrait shot, isn't it?
- **JP**: 、。いっぱい入ってて。

### 3.102
**Timestamp**: 0:31:01.84 - 0:31:04.92

- **AI**: And look, there's a dog in the building in the background.
- **Human**: And look, there's a dog on that building signboard in the background.
- **JP**: 、しかもなんか後ろの建物の、ワンちゃんいる。

### 3.103
**Timestamp**: 0:31:07.24 - 0:31:09.80

- **AI**: I love it. There's a compass on the bag too.
- **Human**: Oh yeah, and she has a compass on the bag too.
- **JP**: いい、コンパスも鞄に付いてる。。

### 3.104
**Timestamp**: 0:31:12.92 - 0:31:17.08

- **AI**: So, this is Honami's post-training art.
- **Human**: So, that was the Honami trained art.
- **JP**: 、ということ、穂波のこちらが特訓後でございまし。しかもちゃんと缶、リンゴなんだ。

### 3.105
**Timestamp**: 0:31:17.08 - 0:31:19.76

- **AI**: And the can is actually apple juice.
- **Human**: Wait, that's an apple badge, isn't it?
- **JP**: 、ということ、穂波のこちらが特訓後でございまし。しかもちゃんと缶、リンゴなんだ。

### 3.106
**Timestamp**: 0:31:21.96 - 0:31:22.72

- **AI**: It's so good.
- **Human**: So good.
- **JP**: いいよ。

### 3.107
**Timestamp**: 0:31:24.44 - 0:31:27.08

- **AI**: Moving on...
- **Human**: Moving on... to Ichika.
- **JP**: 、、続いては。

### 3.108
**Timestamp**: 0:31:30.60 - 0:31:32.28

- **AI**: This was in Episode 7.
- **Human**: This was from Episode 7.
- **JP**: いちかの特訓。これ7話でありました。

### 3.109
**Timestamp**: 0:31:32.96 - 0:31:39.36

- **AI**: Ichika was telling us not to worry too much about it.
- **Human**: Ichika was telling Honami not to sweat it too much.
- **JP**: あのあんまり気にしなくていい、みたいな感じで、いちか言ってくれてました。

### 3.110
**Timestamp**: 0:31:48.00 - 0:31:49.14

- **AI**: I'm losing my vocabulary here.
- **Human**: I'm losing my vocabulary here. All I've been saying is "so good".
- **JP**: もう語彙力なくなるです。よ、良すぎる。

### 3.111
**Timestamp**: 0:31:50.68 - 0:31:58.52

- **AI**: I can't say anything but 'it's good.' I love how the whole scene is visible in Ichika's art.
- **Human**: I love how you kind of get a full view of the scenery for Ichika's card here.
- **JP**: いいしか言わなくこれ、、いちかの時は全体がこの、見えてる感じもまたいいですよ。

### 3.112
**Timestamp**: 0:32:00.16 - 0:32:04.00

- **AI**: And the way she's sitting with her knees up with her guitar on her back is just wonderful.
- **Human**: And the way she's sitting with her knees up and her guitar on her back looks nice.
- **JP**: しかもこのギターを背負いながらこの三角座りしてるっていうのがまたいいよ。

### 3.113
**Timestamp**: 0:32:04.88 - 0:32:09.22

- **AI**: I call it 'sankaku-zuwari' (triangle sit).
- **Human**: I call it 'sankaku-zuwari' (triangle sitting).
- **JP**: なんか三角座、、三角座りって言いますよ。座りって言うの。

### 3.114
**Timestamp**: 0:32:11.68 - 0:32:13.24

- **AI**: Oh, my regional dialect is showing.
- **Human**: My regional dialect is showing.
- **JP**: 、地域のものが出てしまいまし。

### 3.115
**Timestamp**: 0:32:15.16 - 0:32:16.97

- **AI**: Is 'sankaku-zuwari' a Kansai thing?
- **Human**: Is 'sankaku-zuwari' just a Kansai thing?
- **JP**: 三角座りって関西?言う。

### 3.116
**Timestamp**: 0:32:23.20 - 0:32:23.80

- **AI**: Wait?
- **Human**: right?
- **JP**: 。、?ごめん、座り。

### 3.117
**Timestamp**: 0:32:23.80 - 0:32:25.20

- **AI**: Sorry, I meant 'taiiku-zuwari' (gym sit).
- **Human**: Sorry, I meant 'taiiku-zuwari,' then.
- **JP**: 、?ごめん、座り。

### 3.118
**Timestamp**: 0:32:29.92 - 0:32:31.08

- **AI**: Is it a dialect?
- **Human**: That was a dialect thing?
- **JP**: 方言なのか?失礼いたしまし。

### 3.119
**Timestamp**: 0:32:32.92 - 0:32:35.84

- **AI**: Doesn't sitting like that feel so 'student-like'?
- **Human**: Doesn't sitting like that feel a bit 'student-like'?
- **JP**: 座りしてるのってなんか学生感ありませ?

### 3.120
**Timestamp**: 0:32:39.36 - 0:32:41.04

- **AI**: Maybe only during a photoshoot.
- **Human**: Maybe only during photoshoots.
- **JP**: 大人になってからあんましないですよ、体育座。撮影の時にしかし、。

### 3.121
**Timestamp**: 0:32:42.08 - 0:32:47.28

- **AI**: If they tell you to sit there like a student, you might do it.
- **Human**: Like, if they tell you to sit there like a student, you might do it like this.
- **JP**: ここにちょこんと座って下さいって言われた時に体育座りするけど。

### 3.122
**Timestamp**: 0:32:53.42 - 0:32:54.32

- **AI**: I'm so sorry.
- **Human**: So good.
- **JP**: 体育座りは、言う、三角座りは関西限定って言われて。すみませんでし。失礼いたしまし。

### 3.123
**Timestamp**: 0:32:56.72 - 0:32:59.88

- **AI**: Anyway, I personally love it because it feels so much like a student.
- **Human**: Anyway, I personally really like that student vibe here.
- **JP**: 、なんか学生感あって個人的にはすごい好きです。

### 3.124
**Timestamp**: 0:33:05.25 - 0:33:05.75

- **AI**: It's like...
- **Human**: Like...
- **JP**: もうなんか

### 3.125
**Timestamp**: 0:33:27.36 - 0:33:29.36

- **AI**: She's all excited for a party.
- **Human**: She's all excited for the party.
- **JP**: もうルンルンでパーティーです。

### 3.126
**Timestamp**: 0:33:39.98 - 0:33:44.60

- **AI**: And that paper chain around her neck... she definitely made that herself.
- **Human**: And that paper necklace... she definitely made that herself.
- **JP**: 。しかもこの首につけてるこの輪っかのやつって絶対作りましたよ、学生の。

### 3.127
**Timestamp**: 0:33:45.58 - 0:33:49.32

- **AI**: When you have a party, you always put those up on the walls.
- **Human**: It's like in class, remember? You'd always put those up on the walls.
- **JP**: 学生の。パーティーすると言ったらなんか壁とかにこうやってつけ。

### 3.128
**Timestamp**: 0:33:54.84 - 0:33:56.40

- **AI**: That's another great touch.
- **Human**: THIS ART THOUGH
- **JP**: しかもルーズソックスなのか?。 っていうのがまたいいよ。ギャル感があってよ。

### 3.129
**Timestamp**: 0:33:56.40 - 0:33:57.36

- **AI**: It really adds to the gyaru feel.
- **Human**: That's another great touch. It really adds to the gyaru feel.
- **JP**: 。 っていうのがまたいいよ。ギャル感があってよ。

### 3.130
**Timestamp**: 0:33:58.64 - 0:34:00.14

- **AI**: the post-training art.
- **Human**: And here's the trained art.
- **JP**: 、間違え。特訓、。。

### 3.131
**Timestamp**: 0:34:18.32 - 0:34:21.70

- **AI**: And what do you call this part...
- **Human**: And the uhh... what do you call this again?
- **JP**: しかもこの、、ここ何て言うんです?道路の。

### 3.132
**Timestamp**: 0:34:21.70 - 0:34:22.52

- **AI**: of the road?
- **Human**: The thing on the side of the road?
- **JP**: しかもこの、、ここ何て言うんです?道路の。

### 3.133
**Timestamp**: 0:34:23.12 - 0:34:25.32

- **AI**: I love that she's walking along the curb.
- **Human**: I love that she's balancing on it.
- **JP**: ここを歩いてるのもいいよ。

### 3.134
**Timestamp**: 0:34:28.16 - 0:34:31.20

- **AI**: I want to tell her not to swing her instrument around.
- **Human**: I wanna be like "don't swing your guitar around!"
- **JP**: 楽器振り回しちゃっダメだよって言いたくなっ。

### 3.135
**Timestamp**: 0:34:35.16 - 0:34:37.12

- **AI**: Loose socks really are cute.
- **Human**: And the loose socks again are cute.
- **JP**: やっぱルーズソックスって可愛いよ。

### 3.136
**Timestamp**: 0:34:37.64 - 0:34:39.64

- **AI**: Trends always come back around eventually.
- **Human**: Trends always come back around.
- **JP**: 流行りって1周するもんですよ。

### 3.137
**Timestamp**: 0:34:49.08 - 0:34:50.72

- **AI**: That sigh... she's just too cute.
- **Human**: Ahh, so cute.
- **JP**: ため息で、なん、可愛すぎ。

### 3.138
**Timestamp**: 0:34:55.20 - 0:34:58.36

- **AI**: Thank you so much for this, really.
- **Human**: THANK YOU SO MUCH
- **JP**: 志歩ちゃんの特訓。これさありがとうございまし、本当。

### 3.139
**Timestamp**: 0:35:10.32 - 0:35:15.88

- **AI**: Looking at the YouTube comments and seeing myself spin on the lag,
- **Human**: I can see myself spinning because of the delay,
- **JP**: なんか、YouTubeのコメントを見てる、ラグで自分が回ってるの見てすごい恥ずかしくなっちゃっ。

### 3.140
**Timestamp**: 0:35:19.12 - 0:35:19.92

- **AI**: is so embarrassing.
- **Human**: Ahh, so embarrassing.
- **JP**: 恥ずかしい。

### 3.141
**Timestamp**: 0:35:22.84 - 0:35:23.96

- **AI**: Is she okay?
- **Human**: She looks a bit sleepy.
- **JP**: 良く?。

### 3.142
**Timestamp**: 0:35:25.24 - 0:35:28.84

- **AI**: She looks drowsy. Maybe she slept too much the day before.
- **Human**: Maybe she slept too much the day before.
- **JP**: うとうとして、ちょっと、前日寝寝すぎちゃったよっ。、眠いなっ。

### 3.143
**Timestamp**: 0:35:34.00 - 0:35:34.64

- **AI**: Very much so.
- **Human**: Super duper cute.
- **JP**: すごく。しかも、後ろのこの壁のところに、多分秋のシャッフルイベントでやったやつの写真か?

### 3.144
**Timestamp**: 0:35:34.64 - 0:35:41.20

- **AI**: Plus, on the wall in the back, is that a photo
- **Human**: Plus, on the wall in the back, is that a photo from the autumn shuffle event?
- **JP**: すごく。しかも、後ろのこの壁のところに、多分秋のシャッフルイベントでやったやつの写真か?あれを貼ってるのがまたいいよ。

### 3.145
**Timestamp**: 0:35:42.80 - 0:35:44.28

- **AI**: I should look at this instead of that.
- **Human**: Ah, I should be looking here.
- **JP**: あれを貼ってるのがまたいいよ。そっちじゃなくてこっちを見ればいいん。

### 3.146
**Timestamp**: 0:35:48.04 - 0:35:54.58

- **AI**: I'm happy I can see the details of Shiho's room like this,
- **Human**: I'm happy I can see so many little details of Shiho's room like this,
- **JP**: めちゃめちゃいいよ。なんか改めて志歩ちゃんの部屋の感じ、、細かく見れて嬉しい、志歩ちゃんの足の裏が見えてるのも。

### 3.147
**Timestamp**: 0:36:02.04 - 0:36:04.32

- **AI**: or you just can't see their feet at all.
- **Human**: so you don't get a chance to look at their feet.
- **JP**: あと足元見えなかったりもするじゃないです。

### 3.148
**Timestamp**: 0:36:21.00 - 0:36:22.16

- **AI**: by the devs.
- **Human**: Maybe the devs.
- **JP**: 運営さんに怒られ。そんなとこ見ないでくださいっ。

### 3.149
**Timestamp**: 0:36:22.16 - 0:36:23.68

- **AI**: "Please don't look at things like that!"
- **Human**: "Please don't look at that stuff!"
- **JP**: 運営さんに怒られ。そんなとこ見ないでくださいっ。

### 3.150
**Timestamp**: 0:36:41.98 - 0:36:43.00

- **AI**: This is nice.
- **Human**: That's a nice touch.
- **JP**: 特訓後。いい。

### 3.151
**Timestamp**: 0:36:46.24 - 0:36:49.04

- **AI**: That varsity jacket...
- **Human**: That varsity jacket looks so good on her.
- **JP**: 、スタジャンが。

### 3.152
**Timestamp**: 0:36:52.40 - 0:36:55.80

- **AI**: it's rare to see her with something like tea.
- **Human**: Also, I feel like you don't see her with an iced tea drink like that too much.
- **JP**: しかも珍しく、何か紅茶っぽい。

### 3.153
**Timestamp**: 0:36:56.44 - 0:36:58.54

- **AI**: Maybe it's apple tea?
- **Human**: Wait, maybe it's apple tea?
- **JP**: アップルティーなのか、、もしかし。そんな気。

### 3.154
**Timestamp**: 0:36:59.52 - 0:37:03.12

- **AI**: She's drinking that... I didn't know Shiho drank apple tea.
- **Human**: Wow... I didn't know Shiho drank stuff like apple tea.
- **JP**: そんな気。それ飲んでんの、、志保ちゃんってアップルティー飲めるん。

### 3.155
**Timestamp**: 0:37:10.96 - 0:37:18.76

- **AI**: The location looks like it's in front of a music store, which really fits her.
- **Human**: And it looks like she's in front of a music store. Fits her well.
- **JP**: 、結構なんか志保ちゃんがいる場所、もう楽器屋さんの前って感じがしてキャラ感出てていいですよ。

### 3.156
**Timestamp**: 0:37:19.60 - 0:37:26.66

- **AI**: Also, since Shiho's character color is light green,
- **Human**: Also, Shiho's character color is light green,
- **JP**: しかもなんかこのこのキャラカラー、、黄緑色じゃないです、志保ちゃんっ。だからこの、青リンゴにする、また良くないです。

### 3.157
**Timestamp**: 0:37:26.66 - 0:37:30.74

- **AI**: using a green apple like this is a great touch.
- **Human**: so her apple bag being green is a great touch.
- **JP**: しかもなんかこのこのキャラカラー、、黄緑色じゃないです、志保ちゃんっ。だからこの、青リンゴにする、また良くないです。、いい。

### 3.158
**Timestamp**: 0:37:30.74 - 0:37:31.69

- **AI**: It's so good.
- **Human**: It's so good. Oh crap—
- **JP**: だからこの、青リンゴにする、また良くないです。、いい。、。

### 3.159
**Timestamp**: 0:37:49.66 - 0:37:52.84

- **AI**: and she looks so much more mature. It's amazing.
- **Human**: She looks so much more mature. It's amazing.
- **JP**: 、、なん、咲子さんが着るとまたちょっと、雰囲気が変わっていう、大人っぽく見えるのがまたすごいですよ、これ。

### 3.160
**Timestamp**: 0:38:01.76 - 0:38:03.86

- **AI**: The Ln logo.
- **Human**: That "LN" logo.
- **JP**: Leon。Lnの。なんかグッズ化して欲しいぐらい欲しいんだ。

### 3.161
**Timestamp**: 0:38:03.86 - 0:38:06.40

- **AI**: I want it so bad, I wish they'd make it into merch.
- **Human**: It'd be cool if they'd make it into merch so I could get it.
- **JP**: Lnの。なんかグッズ化して欲しいぐらい欲しいんだ。

### 3.162
**Timestamp**: 0:38:07.84 - 0:38:09.80

- **AI**: Someone said it's okay to spin as many times as I want.
- **Human**: "Spin as many times as you like."
- **JP**: 何回回っても大丈夫ですよって言われ。恥ずかしいんで止め。

### 3.163
**Timestamp**: 0:38:09.80 - 0:38:10.72

- **AI**: But it's embarrassing, so I'll stop.
- **Human**: It's too embarrassing!
- **JP**: 何回回っても大丈夫ですよって言われ。恥ずかしいんで止め。

### 3.164
**Timestamp**: 0:38:13.08 - 0:38:17.60

- **AI**: You usually do these After Talks alone, at your own pace,
- **Human**: You usually do these AfterTalks alone, at your own pace,
- **JP**: アフタートークって1人でやる、1人のペースでやるじゃないです。なんか素でやっちゃう、なんか本当にたまに見返すと恥ずかしくなるですよ。

### 3.165
**Timestamp**: 0:38:24.88 - 0:38:33.68

- **AI**: Even though it's an official stream, I'm just going at my own pace,
- **Human**: Even though this is an official PJSK stream, I just go at my own pace,
- **JP**: 作品を生放送なのに自分1人でやっ、自分のペースでやってるからなんかこんなんで大丈夫?

### 3.166
**Timestamp**: 0:38:34.96 - 0:38:35.96

- **AI**: so I start to wonder if this is really okay.
- **Human**: so sometimes I'm like "is this really okay?"
- **JP**: 気持ちになっ。

### 3.167
**Timestamp**: 0:38:40.20 - 0:38:42.24

- **AI**: I really want that Leo/need logo.
- **Human**: But I really want that Leo/need logo though.
- **JP**: 、このLeonのロゴ欲しいよ。これなんかワッペングッズとかで出して欲しいんです。

### 3.168
**Timestamp**: 0:38:47.76 - 0:38:48.98

- **AI**: Please enjoy.
- **Human**: Please and thank you.
- **JP**: いつかよろしくお願いし、偉い。お願いし。ということ、、イラスト見ていきまし。

### 3.169
**Timestamp**: 0:38:48.98 - 0:38:51.88

- **AI**: So, let's take a look at the illustrations.
- **Human**: Anyway, that's all for the card illustrations.
- **JP**: お願いし。ということ、、イラスト見ていきまし。

### 3.170
**Timestamp**: 0:39:05.44 - 0:39:09.68

- **AI**: So, let's watch the 2D MV that was released yesterday.
- **Human**: So without further ado, released just yesterday, here's the 2DMV!
- **JP**: 、続いてはです、今回のイベントのためにアクエラさんに描き下ろしいただきました透明なパレットの2DMVを見て楽曲やMVについてのお話をしていこうと思い。、では昨日公開されました2DMV見ていき。

### 3.171
**Timestamp**: 0:42:20.16 - 0:42:21.08

- **AI**: It's good.
- **Human**: Giant one too.
- **JP**: いいよ。

### 3.172
**Timestamp**: 0:42:28.84 - 0:42:36.18

- **AI**: When we were recording this song... it's very refreshing, but
- **Human**: I remember when I recorded for this song,
- **JP**: 、今回この楽曲、、収録、レコーディングする時、、爽やかなんです、、A、Bメロとかで、、結構迷ってたりと、

### 3.173
**Timestamp**: 0:42:46.86 - 0:42:51.02

- **AI**: And for the chorus... how should I put it...
- **Human**: And then in the chorus, how to say...
- **JP**: 、戸惑いだったりとかをちょっと入れていただい、あん強いな感じで歌って欲しいって言われ、、サビの方で、、何て言うんですか、、、透明感溢れる感じで歌って欲しいですって言われ、、みんなで歌わせていただきまし。

### 3.174
**Timestamp**: 0:42:51.02 - 0:42:56.64

- **AI**: I was told to sing with a sense of transparency, and we all sang it together.
- **Human**: we were asked to sing with a much brighter and transparent feeling,
- **JP**: 、サビの方で、、何て言うんですか、、、透明感溢れる感じで歌って欲しいですって言われ、、みんなで歌わせていただきまし。

### 3.175
**Timestamp**: 0:42:57.16 - 0:43:02.88

- **AI**: Personally, I love the lyric about having apple pie on a day of celebration so much.
- **Human**: Also, I love the part of the lyrics that says "and on days of celebration, we'll have apple pies" so much.
- **JP**: 、個人的にお祝いの日にアップルパイをっていう歌詞があまりにも好きすぎ、なんか今、何、、書き下ろしていただいた歌詞の中、、

### 3.176
**Timestamp**: 0:43:02.88 - 0:43:08.32

- **AI**: In the lyrics written for us...
- **Human**: Even though it's pretty upbeat,
- **JP**: 、個人的にお祝いの日にアップルパイをっていう歌詞があまりにも好きすぎ、なんか今、何、、書き下ろしていただいた歌詞の中、、キャラクターの好きなものがダイレクトに入ってるっていうの、あんまなかったって、

### 3.177
**Timestamp**: 0:43:08.32 - 0:43:12.92

- **AI**: there haven't been many times where a character's favorite thing is mentioned so directly.
- **Human**: And seeing a character's favorite food directly mentioned like that,
- **JP**: なんか今、何、、書き下ろしていただいた歌詞の中、、キャラクターの好きなものがダイレクトに入ってるっていうの、あんまなかったって、、。

### 3.178
**Timestamp**: 0:43:15.24 - 0:43:20.72

- **AI**: I had that image... I remember it feeling quite fresh.
- **Human**: I remember that part being stuck in my head forever.
- **JP**: っていうイメージがあったん、、なんか新鮮だった、覚え。

### 3.179
**Timestamp**: 0:43:21.96 - 0:43:27.52

- **AI**: That part just keeps playing in my head. I personally really like it.
- **Human**: But a good kind of "stuck in my head". I really liked it.
- **JP**: 、ずっとなんかそこの部分だけが私の脳内で流れる、個人的にはすごく好き。

### 3.180
**Timestamp**: 0:43:28.24 - 0:43:32.00

- **AI**: And also, I think it was on the Master difficulty chart?
- **Human**: Actually, I saw that on the Master chart, there's an "apple pie" note.
- **JP**: 、しかも、多分、マスター譜面だったか?にアップルパイが出てくるんです。

### 3.181
**Timestamp**: 0:43:34.56 - 0:43:38.68

- **AI**: They worked hard to make it look like an apple pie, a really big apple pie.
- **Human**: Somehow they made an apple pie out of the hold notes.
- **JP**: 頑張ってアップルパイになってたんです、めっちゃでかくてアップル。

### 3.182
**Timestamp**: 0:43:40.68 - 0:43:43.92

- **AI**: It was like, 'Oh, it's an apple pie!' and I played it a bit.
- **Human**: When I first played it, I was like "woah, is than an apple pie?!"
- **JP**: 、、アップルパイってなり、ちょっとやったりしたん。気になった方は、マスター遊んでみて。

### 3.183
**Timestamp**: 0:43:43.92 - 0:43:47.04

- **AI**: If you're curious, please try playing the Master difficulty.
- **Human**: Definitely try out the Master chart if you wanna see it.
- **JP**: 、、アップルパイってなり、ちょっとやったりしたん。気になった方は、マスター遊んでみて。

### 3.184
**Timestamp**: 0:43:49.16 - 0:43:52.64

- **AI**: I wonder if Shiho's ramen will show up eventually? Do you think so?
- **Human**: "You think Shiho's ramen will show up one day?"
- **JP**: いずれ志保のラーメンも来るのかなっ、来るか?

### 3.185
**Timestamp**: 0:43:53.60 - 0:43:57.44

- **AI**: Would Shiho even get such a poppy song?
- **Human**: Would she get a pop song like this though?
- **JP**: 志保でそんなポップな曲来るか?

### 3.186
**Timestamp**: 0:43:59.04 - 0:44:02.20

- **AI**: But I'd certainly like to see it.
- **Human**: I mean, I'd definitely be interested in seeing that.
- **JP**: 、でも確かに見てみたさはありますけど。

### 3.187
**Timestamp**: 0:44:03.72 - 0:44:05.50

- **AI**: Try playing the Master chart.
- **Human**: Yeah, try the Master chart. It's uh...
- **JP**: 、マスター譜面やってみて。、、

### 3.188
**Timestamp**: 0:44:12.20 - 0:44:13.08

- **AI**: please give it a try.
- **Human**: Please check it out, everyone.
- **JP**: やってみて。

### 3.189
**Timestamp**: 0:44:14.44 - 0:44:16.84

- **AI**: Shiho and ramen... I can't quite imagine it.
- **Human**: I can't imagine Shiho and ramen in a song like this.
- **JP**: 志保にラーメン、ちょっと想像できない。

### 3.190
**Timestamp**: 0:44:19.00 - 0:44:19.52

- **AI**: A little...
- **Human**: If that really happened...
- **JP**: ちょっと、

### 3.191
**Timestamp**: 0:44:23.20 - 0:44:24.66

- **AI**: Or maybe they want it to be metal?
- **Human**: Like maybe she could get a metal song.
- **JP**: メタル系で行って欲しいか。ジャガジャガジャガジャガっみたい。

### 3.192
**Timestamp**: 0:44:44.48 - 0:44:46.72

- **AI**: Slap bass is impossible... true.
- **Human**: "Would have lots of slap bass." Yeah, I suppose it would.
- **JP**: スラップ不可、、確かに。

### 3.193
**Timestamp**: 0:44:48.04 - 0:44:50.28

- **AI**: The steam from the ramen would be all zigzaggy.
- **Human**: "The steam from the ramen would zig zag everywhere."
- **JP**: ラーメンの湯気がめっちゃジグザグして。なんかもう、、すごい、想像力豊かです。

### 3.194
**Timestamp**: 0:44:50.28 - 0:44:54.36

- **AI**: Wow, you have a great imagination.
- **Human**: Wow, everyone's already got so many creative ideas for this.
- **JP**: ラーメンの湯気がめっちゃジグザグして。なんかもう、、すごい、想像力豊かです。

### 3.195
**Timestamp**: 0:45:02.80 - 0:45:03.82

- **AI**: so I'm looking forward to it.
- **Human**: So do try it.
- **JP**: 、こういう感じで、キャラクターの、好きなものが、今後入ってくるかもしれないです、楽しみです。、咲希ちゃんの、、衣装姿もここで見れたのも嬉しいです。

### 3.196
**Timestamp**: 0:45:03.82 - 0:45:08.14

- **AI**: I'm also happy to see Saki-chan in her outfit here.
- **Human**: And getting to see Saki's outfit here in the MV was also really nice.
- **JP**: 楽しみです。、咲希ちゃんの、、衣装姿もここで見れたのも嬉しいです。ここ、ハートのマークも、、ロゴがあっ、それぞれ違ったんだっていう感じも認識でき。

### 3.197
**Timestamp**: 0:45:08.14 - 0:45:13.96

- **AI**: I also noticed that the heart marks and logos were different for each of them.
- **Human**: That heart mark here is actually different for everyone.
- **JP**: 、咲希ちゃんの、、衣装姿もここで見れたのも嬉しいです。ここ、ハートのマークも、、ロゴがあっ、それぞれ違ったんだっていう感じも認識でき。めちゃめちゃ可愛いDMVになっておりますの、皆、ぜひご覧。

### 3.198
**Timestamp**: 0:45:13.96 - 0:45:18.68

- **AI**: It's a very cute 2D MV, so please everyone, check it out.
- **Human**: It's a super duper cute 2DMV.
- **JP**: ここ、ハートのマークも、、ロゴがあっ、それぞれ違ったんだっていう感じも認識でき。めちゃめちゃ可愛いDMVになっておりますの、皆、ぜひご覧。こちらの方、プロセカ公式YouTubeにアップされておりますの、

### 3.199
**Timestamp**: 0:45:35.84 - 0:45:39.80

- **AI**: It went by so fast, I just realized it's already past 9:00.
- **Human**: I saw the clock when I spun around, I was like "crap, it's already 9?"
- **JP**: あっという、気づいたらもう9時回っちゃっ。で、回った時に思ったん。

### 3.200
**Timestamp**: 0:45:39.80 - 0:45:42.06

- **AI**: I thought about it when the time passed.
- **Human**: I think they should have a little fun with the idea.
- **JP**: あっという、気づいたらもう9時回っちゃっ。で、回った時に思ったん。、意外と時間経ってるって思い、、喋って。

### 3.201
**Timestamp**: 0:45:42.06 - 0:45:44.40

- **AI**: I realized quite a bit of time had passed while I was talking.
- **Human**: I'd be a bit worried. If that really did happen.
- **JP**: で、回った時に思ったん。、意外と時間経ってるって思い、、喋って。

### 3.202
**Timestamp**: 0:45:45.36 - 0:45:48.52

- **AI**: I thought, 'I shouldn't be doing this, I have to watch the MV too,'
- **Human**: I was like "I can't just be spinning here, we need to move on to watch the MV!"
- **JP**: こんなことしてる場合じゃないと思っ、MVも見なきゃいけないの、みたい。

### 3.203
**Timestamp**: 0:45:53.82 - 0:45:55.14

- **AI**: Let's do this again.
- **Human**: "Let's do this again!" Definitely.
- **JP**: あっという間でした。またやり。そうです。

### 3.204
**Timestamp**: 0:45:55.14 - 0:45:55.88

- **AI**: That's right.
- **Human**: That really did fly by.
- **JP**: またやり。そうです。

### 3.205
**Timestamp**: 0:45:57.00 - 0:45:59.68

- **AI**: I think I just got word...
- **Human**: "But I just got here!" Yeah!
- **JP**: 、今来た、確か。もっと喋っていいの、ありがとうござい。

### 3.206
**Timestamp**: 0:45:59.68 - 0:46:02.24

- **AI**: I can talk more? Thank you!
- **Human**: "Don't go, keep chatting." Thank you.
- **JP**: 、今来た、確か。もっと喋っていいの、ありがとうござい。、ということ、、イベントアンステディステディステップのストーリーはまだ見終わってないという方はです、

### 3.207
**Timestamp**: 0:46:09.44 - 0:46:14.00

- **AI**: even after the next event starts, you can read it all from the Event Story archives,
- **Human**: after the next event starts, you can read it in-game in the "Event Story" section under the "Story" button, so please do so.
- **JP**: 、ということ、、イベントアンステディステディステップのストーリーはまだ見終わってないという方はです、次のイベントが始まっ、ストーリーのイベントストーリーから全て読むことができますの、ぜひ読んでみて。

### 3.208
**Timestamp**: 0:46:14.00 - 0:46:15.40

- **AI**: so please give it a read.
- **Human**: It's already 9PM.
- **JP**: 次のイベントが始まっ、ストーリーのイベントストーリーから全て読むことができますの、ぜひ読んでみて。アフタートークで、今後もおたよりを募集しており。

### 3.209
**Timestamp**: 0:46:15.40 - 0:46:18.26

- **AI**: We are still looking for messages for After Talk.
- **Human**: We'll be accepting submissions for future AfterTalks as usual.
- **JP**: ぜひ読んでみて。アフタートークで、今後もおたよりを募集しており。プロセカ公式ディスコードの募集チャンネルのアフタートークおたより、もしくはメールにて募集を受け付けており。

### 3.210
**Timestamp**: 0:46:18.26 - 0:46:25.02

- **AI**: We're accepting them via the After Talk message channel on the official Proseka Discord or via email.
- **Human**: You can submit your messages in the submissions channel on the official Project Sekai Discord, or through email.
- **JP**: アフタートークで、今後もおたよりを募集しており。プロセカ公式ディスコードの募集チャンネルのアフタートークおたより、もしくはメールにて募集を受け付けており。次回のアフタートークのイベントが開催されまし、ぜひお送り。

### 3.211
**Timestamp**: 0:46:25.02 - 0:46:28.82

- **AI**: When the next After Talk event is held, please send them in.
- **Human**: Feel free to send them in after the next AfterTalk event starts.
- **JP**: プロセカ公式ディスコードの募集チャンネルのアフタートークおたより、もしくはメールにて募集を受け付けており。次回のアフタートークのイベントが開催されまし、ぜひお送り。おたより、イベントに関する内容でよろしくお願いし。

### 3.212
**Timestamp**: 0:46:28.82 - 0:46:32.60

- **AI**: Please send in messages related to the event.
- **Human**: Please keep your messages related to the events.
- **JP**: 次回のアフタートークのイベントが開催されまし、ぜひお送り。おたより、イベントに関する内容でよろしくお願いし。ということ、とても楽しかった。

### 3.213
**Timestamp**: 0:46:35.02 - 0:46:37.12

- **AI**: I'll see you all again.
- **Human**: See you again next time!
- **JP**: ということ、とても楽しかった。皆、またお会いし。。

---

## Category 2: Structural Changes (Splits, Merges, Additions, Deletions)

**Count: 456** — 280 AI lines deleted/merged into human edit, 176 new human lines added/split out.

Given the noisy transcription baseline, the human editor performed extensive resegmentation. Listed in chronological order:

### 2.1
- **AI** [0:08:18.60 - 0:10:03.28]: the voice of Hinomori Shiho from Leo/need.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.2
- **AI**: *(no line)*
- **Human** [0:09:55.58 - 0:10:00.42]: Welcome to ProSeka AfterTalk "Unsteady, still steady step" Edition!
- **Note**: Line added in human version

### 2.3
- **AI**: *(no line)*
- **Human** [0:10:02.47 - 0:10:06.91]: This is Yuki Nakashima, voice of Shiho Hinomori from Leo/need!
- **Note**: Line added in human version

### 2.4
- **AI**: *(no line)*
- **Human** [0:10:06.91 - 0:10:12.67]: In this edition of ProSeka AfterTalk, we'll look back at this event while covering messages you, the fans, have sent in.
- **Note**: Line added in human version

### 2.5
- **AI**: *(no line)*
- **Human** [0:10:12.67 - 0:10:16.09]: This time, we'll be covering the "Unsteady, still steady step" event.
- **Note**: Line added in human version

### 2.6
- **AI**: *(no line)*
- **Human** [0:10:19.42 - 0:10:20.97]: When I first saw the script, I was like,
- **Note**: Line added in human version

### 2.7
- **AI**: *(no line)*
- **Human** [0:10:20.97 - 0:10:25.02]: "...Unsteady, still steady step.... There's way too many 'st's here."
- **Note**: Line added in human version

### 2.8
- **AI**: *(no line)*
- **Human** [0:10:25.02 - 0:10:29.06]: "Is this supposed to be a tongue-twister?"
- **Note**: Line added in human version

### 2.9
- **AI**: *(no line)*
- **Human** [0:10:29.06 - 0:10:34.14]: Right, so did you enjoy this event's story, everyone?
- **Note**: Line added in human version

### 2.10
- **AI**: *(no line)*
- **Human** [0:10:34.14 - 0:10:37.59]: Yep, I sure did read it right. Thank you.
- **Note**: Line added in human version

### 2.11
- **AI**: *(no line)*
- **Human** [0:10:37.59 - 0:10:39.88]: "Kon-needo". Kon-needo.
- **Note**: Line added in human version

### 2.12
- **AI**: *(no line)*
- **Human** [0:10:42.45 - 0:10:44.63]: It's like a "st st" party up in here.
- **Note**: Line added in human version

### 2.13
- **AI**: *(no line)*
- **Human** [0:10:46.49 - 0:10:47.77]: Yeah but like,
- **Note**: Line added in human version

### 2.14
- **AI**: *(no line)*
- **Human** [0:10:47.77 - 0:10:50.48]: talking about the story for real,
- **Note**: Line added in human version

### 2.15
- **AI**: *(no line)*
- **Human** [0:10:50.48 - 0:10:54.17]: it's not like there were any earthshattering developments or decisions here,
- **Note**: Line added in human version

### 2.16
- **AI**: *(no line)*
- **Human** [0:10:54.17 - 0:11:00.60]: Honami was just a little uncertain on this decision in front of her.
- **Note**: Line added in human version

### 2.17
- **AI**: *(no line)*
- **Human** [0:11:00.60 - 0:11:07.11]: But,
- **Note**: Line added in human version

### 2.18
- **AI**: *(no line)*
- **Human** [0:11:07.11 - 0:11:09.62]: "I liked the story!" Thank you.
- **Note**: Line added in human version

### 2.19
- **AI**: *(no line)*
- **Human** [0:11:10.49 - 0:11:11.64]: Glad to hear.
- **Note**: Line added in human version

### 2.20
- **AI**: *(no line)*
- **Human** [0:11:11.64 - 0:11:14.58]: We've had a bit of a mini-renewal for AfterTalk since April
- **Note**: Line added in human version

### 2.21
- **AI**: *(no line)*
- **Human** [0:11:14.58 - 0:11:20.22]: We've gathered the comments you sent in through email and the Discord submissions channel.
- **Note**: Line added in human version

### 2.22
- **AI**: *(no line)*
- **Human** [0:11:22.16 - 0:11:26.59]: We'd like to go over some of them in our program today, so please look forward to that!
- **Note**: Line added in human version

### 2.23
- **AI**: *(no line)*
- **Human** [0:11:26.59 - 0:11:28.79]: Also, if you have any thoughts on today's program,
- **Note**: Line added in human version

### 2.24
- **AI**: *(no line)*
- **Human** [0:11:28.79 - 0:11:31.85]: please post them on X with #ProSekaAfterTalk.
- **Note**: Line added in human version

### 2.25
- **AI**: *(no line)*
- **Human** [0:11:31.85 - 0:11:36.42]: We'll also be watching the YouTube chat, so please keep all the messages coming.
- **Note**: Line added in human version

### 2.26
- **AI**: *(no line)*
- **Human** [0:11:36.42 - 0:11:42.25]: Also, note that since the mini-renewal, we won't be watching the AfterLives. Thanks for your understanding.
- **Note**: Line added in human version

### 2.27
- **AI**: *(no line)*
- **Human** [0:11:43.50 - 0:11:47.49]: Yeah, they're going to have to start choosing now that they're pros.
- **Note**: Line added in human version

### 2.28
- **AI**: *(no line)*
- **Human** [0:11:49.53 - 0:11:52.53]: "Shindo-san helped out a ton." For sure.
- **Note**: Line added in human version

### 2.29
- **AI**: *(no line)*
- **Human** [0:11:52.53 - 0:11:56.77]: I remember that part where he's on the phone with her — how to say —
- **Note**: Line added in human version

### 2.30
- **AI**: *(no line)*
- **Human** [0:11:56.77 - 0:11:58.38]: the splitscreen part?
- **Note**: Line added in human version

### 2.31
- **AI**: *(no line)*
- **Human** [0:11:58.38 - 0:12:02.78]: When it shows Honami and Shindo-san side by side,
- **Note**: Line added in human version

### 2.32
- **AI**: *(no line)*
- **Human** [0:12:02.78 - 0:12:05.01]: it makes Shindo's frame look even bigger.
- **Note**: Line added in human version

### 2.33
- **AI**: *(no line)*
- **Human** [0:12:05.01 - 0:12:05.94]: I saw it and was like,
- **Note**: Line added in human version

### 2.34
- **AI**: *(no line)*
- **Human** [0:12:05.94 - 0:12:10.94]: "ah, that sure is a fully grown man."
- **Note**: Line added in human version

### 2.35
- **AI**: *(no line)*
- **Human** [0:12:10.94 - 0:12:12.80]: "The AfterLive was really good!" Mmm!
- **Note**: Line added in human version

### 2.36
- **AI**: *(no line)*
- **Human** [0:12:12.80 - 0:12:14.75]: Thank you!
- **Note**: Line added in human version

### 2.37
- **AI**: *(no line)*
- **Human** [0:12:14.75 - 0:12:19.88]: Alright! Let's get right into the "Unsteady, still steady step" story...
- **Note**: Line added in human version

### 2.38
- **AI**: *(no line)*
- **Human** [0:12:25.00 - 0:12:27.66]: Let's get into the story.
- **Note**: Line added in human version

### 2.39
- **AI**: *(no line)*
- **Human** [0:12:27.66 - 0:12:31.17]: Let's look back together while going over some of the messages you've sent in.
- **Note**: Line added in human version

### 2.40
- **AI**: *(no line)*
- **Human** [0:12:31.17 - 0:12:33.90]: First up, a message from "King"-san. Thank you for the message.
- **Note**: Line added in human version

### 2.41
- **AI**: *(no line)*
- **Human** [0:12:33.90 - 0:12:36.48]: "Kon-needo, Nakashima-san!" Kon-needo!
- **Note**: Line added in human version

### 2.42
- **AI**: *(no line)*
- **Human** [0:12:42.35 - 0:12:47.78]: "Both the one-man live and the fan fes were big opportunities for Leo/need to move forward."
- **Note**: Line added in human version

### 2.43
- **AI**: *(no line)*
- **Human** [0:12:47.78 - 0:12:51.82]: "There wasn't a clear right option so it was tough deciding which to write a new song for."
- **Note**: Line added in human version

### 2.44
- **AI**: *(no line)*
- **Human** [0:12:51.82 - 0:12:56.74]: "I'm pretty indecisive myself and tend to freeze from over-analysis,"
- **Note**: Line added in human version

### 2.45
- **AI** [0:12:55.10 - 0:13:00.92]: The letter says, "Personally, I would love to see an MC segment where everyone swaps instruments during the actual show."
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.46
- **AI**: *(no line)*
- **Human** [0:12:56.74 - 0:12:59.32]: so I was really able to sympathize with Honami."
- **Note**: Line added in human version

### 2.47
- **AI**: *(no line)*
- **Human** [0:12:59.32 - 0:13:04.99]: "By the way, Nakashima-san, when you're faced with important choices, how do you generally come to a decision?"
- **Note**: Line added in human version

### 2.48
- **AI**: *(no line)*
- **Human** [0:13:07.57 - 0:13:09.03]: Ehhhhhh?
- **Note**: Line added in human version

### 2.49
- **AI**: *(no line)*
- **Human** [0:13:10.04 - 0:13:12.64]: I think usually,
- **Note**: Line added in human version

### 2.50
- **AI**: *(no line)*
- **Human** [0:13:12.64 - 0:13:16.31]: I'm able to come up with a pretty clear option I favor more.
- **Note**: Line added in human version

### 2.51
- **AI**: *(no line)*
- **Human** [0:13:20.74 - 0:13:22.66]: I'd probably try to do both.
- **Note**: Line added in human version

### 2.52
- **AI**: *(no line)*
- **Human** [0:13:23.60 - 0:13:27.78]: But if it were a real scheduling conflict, like on the exact same day,
- **Note**: Line added in human version

### 2.53
- **AI**: *(no line)*
- **Human** [0:13:27.78 - 0:13:30.87]: like I had other work scheduled on the same day,
- **Note**: Line added in human version

### 2.54
- **AI** [0:13:29.36 - 0:13:35.16]: They did it because it was just a rehearsal, but when it comes to music,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.55
- **AI**: *(no line)*
- **Human** [0:13:32.75 - 0:13:35.19]: But if it were like the story,
- **Note**: Line added in human version

### 2.56
- **AI** [0:13:35.16 - 0:16:32.00]: she is so confident in her skills that her pride might make her refuse even for an MC segment, but I still want to see it.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.57
- **AI**: *(no line)*
- **Human** [0:13:35.19 - 0:13:41.34]: like if I needed to get two separate things done by the same day,
- **Note**: Line added in human version

### 2.58
- **AI**: *(no line)*
- **Human** [0:13:41.34 - 0:13:44.79]: I think I'd try to do both.
- **Note**: Line added in human version

### 2.59
- **AI**: *(no line)*
- **Human** [0:13:44.79 - 0:13:49.30]: Like, it definitely depends on what exactly I'm deciding on,
- **Note**: Line added in human version

### 2.60
- **AI**: *(no line)*
- **Human** [0:13:49.30 - 0:13:52.22]: but I tend to make decisions really impulsively like that.
- **Note**: Line added in human version

### 2.61
- **AI**: *(no line)*
- **Human** [0:13:52.22 - 0:13:54.18]: Oh yeah and of course,
- **Note**: Line added in human version

### 2.62
- **AI**: *(no line)*
- **Human** [0:13:54.18 - 0:13:55.74]: I usually just go by vibes.
- **Note**: Line added in human version

### 2.63
- **AI**: *(no line)*
- **Human** [0:13:57.66 - 0:14:00.53]: So I can't really be of much help. Sorry.
- **Note**: Line added in human version

### 2.64
- **AI**: *(no line)*
- **Human** [0:14:02.17 - 0:14:04.03]: Actually, what would you all do?
- **Note**: Line added in human version

### 2.65
- **AI**: *(no line)*
- **Human** [0:14:08.32 - 0:14:12.77]: As uh... selfish as that would be.
- **Note**: Line added in human version

### 2.66
- **AI**: *(no line)*
- **Human** [0:14:14.92 - 0:14:17.07]: Would probably try something like that.
- **Note**: Line added in human version

### 2.67
- **AI**: *(no line)*
- **Human** [0:14:18.04 - 0:14:20.81]: Leave it up to vibes. Yeah.
- **Note**: Line added in human version

### 2.68
- **AI**: *(no line)*
- **Human** [0:14:20.81 - 0:14:23.41]: "Flip a coin." Haha maybe.
- **Note**: Line added in human version

### 2.69
- **AI**: *(no line)*
- **Human** [0:14:23.41 - 0:14:27.07]: I mean if you're really stuck between the two...
- **Note**: Line added in human version

### 2.70
- **AI**: *(no line)*
- **Human** [0:14:27.07 - 0:14:29.65]: Like if you don't want to regret your decision,
- **Note**: Line added in human version

### 2.71
- **AI**: *(no line)*
- **Human** [0:14:29.65 - 0:14:34.48]: and you really can't decide on a clear favorite, maybe leaving it up to fate makes sense.
- **Note**: Line added in human version

### 2.72
- **AI**: *(no line)*
- **Human** [0:14:34.48 - 0:14:38.25]: Play "eeny, meeny, miny, moe" or something.
- **Note**: Line added in human version

### 2.73
- **AI**: *(no line)*
- **Human** [0:14:38.25 - 0:14:44.02]: That sure is one way to do it.
- **Note**: Line added in human version

### 2.74
- **AI**: *(no line)*
- **Human** [0:14:44.02 - 0:14:45.83]: But I mean, like,
- **Note**: Line added in human version

### 2.75
- **AI**: *(no line)*
- **Human** [0:14:50.40 - 0:14:53.50]: I think I'd just go with vibes...
- **Note**: Line added in human version

### 2.76
- **AI**: *(no line)*
- **Human** [0:14:53.50 - 0:14:55.93]: Like just going with whatever my gut was telling me.
- **Note**: Line added in human version

### 2.77
- **AI**: *(no line)*
- **Human** [0:14:55.93 - 0:15:01.90]: Even if I were just feeling it 1-2% more, I'd probably go with that one.
- **Note**: Line added in human version

### 2.78
- **AI**: *(no line)*
- **Human** [0:15:01.90 - 0:15:02.66]: Right?
- **Note**: Line added in human version

### 2.79
- **AI**: *(no line)*
- **Human** [0:15:02.66 - 0:15:06.48]: If I were in Leo/need's specific situation in the story,
- **Note**: Line added in human version

### 2.80
- **AI**: *(no line)*
- **Human** [0:15:06.48 - 0:15:12.56]: and the request for the fan fes got withdrawn,
- **Note**: Line added in human version

### 2.81
- **AI**: *(no line)*
- **Human** [0:15:12.56 - 0:15:14.86]: I'd actually be relieved.
- **Note**: Line added in human version

### 2.82
- **AI**: *(no line)*
- **Human** [0:15:14.86 - 0:15:18.39]: I'd be like "Oh! We get to do both!"
- **Note**: Line added in human version

### 2.83
- **AI**: *(no line)*
- **Human** [0:15:18.39 - 0:15:22.81]: Probably not good to think this way but I'd be like "we got lucky!"
- **Note**: Line added in human version

### 2.84
- **AI**: *(no line)*
- **Human** [0:15:22.81 - 0:15:25.81]: Mmm. Something like that.
- **Note**: Line added in human version

### 2.85
- **AI**: *(no line)*
- **Human** [0:15:25.81 - 0:15:28.91]: Okay. Let's move on to one more message.
- **Note**: Line added in human version

### 2.86
- **AI**: *(no line)*
- **Human** [0:15:28.91 - 0:15:31.68]: Next up, from "Copy"-san. Thank you for the message.
- **Note**: Line added in human version

### 2.87
- **AI**: *(no line)*
- **Human** [0:15:31.68 - 0:15:33.74]: "Yukki, kon-needo." Kon-needo.
- **Note**: Line added in human version

### 2.88
- **AI**: *(no line)*
- **Human** [0:15:39.02 - 0:15:44.05]: "I was secretly hoping that they would do that instrument shuffle for the real thing."
- **Note**: Line added in human version

### 2.89
- **AI**: *(no line)*
- **Human** [0:15:44.05 - 0:15:46.05]: Thank you for the message.
- **Note**: Line added in human version

### 2.90
- **AI**: *(no line)*
- **Human** [0:15:46.05 - 0:15:47.96]: Oh yeah. Would definitely want to see that.
- **Note**: Line added in human version

### 2.91
- **AI**: *(no line)*
- **Human** [0:15:49.01 - 0:15:51.10]: Ehhhh? Like,
- **Note**: Line added in human version

### 2.92
- **AI**: *(no line)*
- **Human** [0:16:00.61 - 0:16:05.06]: I wonder... Shiho switched from bass,
- **Note**: Line added in human version

### 2.93
- **AI**: *(no line)*
- **Human** [0:16:05.06 - 0:16:09.84]: and had to play drums... or guitar, or keyboard...
- **Note**: Line added in human version

### 2.94
- **AI**: *(no line)*
- **Human** [0:16:09.84 - 0:16:13.68]: Would you even be able to get her to do it? That's what I'd be wondering.
- **Note**: Line added in human version

### 2.95
- **AI**: *(no line)*
- **Human** [0:16:13.68 - 0:16:16.73]: I mean, if it were for rehearsal, I think she would be okay with it.
- **Note**: Line added in human version

### 2.96
- **AI**: *(no line)*
- **Human** [0:16:16.73 - 0:16:23.02]: As someone so talented and self-confident in her music,
- **Note**: Line added in human version

### 2.97
- **AI**: *(no line)*
- **Human** [0:16:23.02 - 0:16:27.58]: I think she'd have some pride on the line! Even if it were just for an MC, she'd be like "I'm not giving you my bass."
- **Note**: Line added in human version

### 2.98
- **AI**: *(no line)*
- **Human** [0:16:37.20 - 0:16:43.06]: But yeah, I kind of wanna see everyone go "how do you play this?"
- **Note**: Line added in human version

### 2.99
- **AI** [0:16:46.85 - 0:16:47.45]: Yes.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.100
- **AI** [0:17:11.90 - 0:17:12.56]: I am curious.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.101
- **AI**: *(no line)*
- **Human** [0:17:15.81 - 0:17:17.06]: Mmmmm.
- **Note**: Line added in human version

### 2.102
- **AI**: *(no line)*
- **Human** [0:17:17.06 - 0:17:19.07]: That would be cool to see.
- **Note**: Line added in human version

### 2.103
- **AI**: *(no line)*
- **Human** [0:17:20.11 - 0:17:24.67]: "Everyone going 'how do you play this?' would be so cute." Oh yeah. 100%.
- **Note**: Line added in human version

### 2.104
- **AI** [0:17:21.80 - 0:17:22.52]: True.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.105
- **AI** [0:17:23.36 - 0:17:24.00]: Exactly.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.106
- **AI**: *(no line)*
- **Human** [0:17:27.00 - 0:17:29.05]: Ah, that would be so great to see.
- **Note**: Line added in human version

### 2.107
- **AI**: *(no line)*
- **Human** [0:17:52.54 - 0:17:55.10]: Nakashima-san, could you play guitar when you started learning bass?
- **Note**: Line added in human version

### 2.108
- **AI** [0:17:52.56 - 0:17:55.08]: Can you play the guitar as well as the bass, Nakashima-san?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.109
- **AI** [0:17:55.08 - 0:17:55.59]: No, I can't.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.110
- **AI**: *(no line)*
- **Human** [0:17:57.26 - 0:17:59.24]: I gave up on guitar pretty quick.
- **Note**: Line added in human version

### 2.111
- **AI** [0:17:58.96 - 0:18:03.24]: She said she looked into everything she possibly could on her own.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.112
- **AI** [0:18:13.98 - 0:18:15.88]: She still hasn't found
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.113
- **AI** [0:18:17.72 - 0:18:20.68]: the answer within herself as to which is better.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.114
- **AI**: *(no line)*
- **Human** [0:18:20.75 - 0:18:24.64]: and actually going out of her way to understand everyone's perspective,
- **Note**: Line added in human version

### 2.115
- **AI** [0:18:26.12 - 0:18:43.04]: She wants to show the way. Ichika-chan told her not to take it all on herself, and it is something for everyone to decide, but if she stays indecisive, it might just lead everyone astray.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.116
- **AI** [0:18:44.47 - 0:18:44.97]: That is why
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.117
- **AI** [0:18:47.48 - 0:18:50.64]: she needs to make up her mind.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.118
- **AI** [0:19:03.23 - 0:19:03.73]: Look.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.119
- **AI** [0:19:04.28 - 0:19:08.72]: The fans will definitely be happy with a new song for the one-man.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.120
- **AI** [0:19:09.56 - 0:19:14.68]: And she thinks Saki-chan and Shiho-chan would surely want to do that too.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.121
- **AI** [0:19:15.87 - 0:19:16.37]: However,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.122
- **AI** [0:19:19.32 - 0:19:22.04]: I really love this song.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.123
- **AI** [0:19:23.08 - 0:19:23.82]: Yes.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.124
- **AI** [0:19:31.44 - 0:19:36.40]: She wants people who love Virtual Singers to hear their music too.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.125
- **AI** [0:19:38.28 - 0:19:41.04]: Ichika-chan surely feels the same way.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.126
- **AI** [0:19:44.92 - 0:19:46.88]: If I have to choose one,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.127
- **AI** [0:19:48.72 - 0:19:49.24]: then I...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.128
- **AI** [0:19:52.64 - 0:19:54.56]: What I choose is...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.129
- **AI** [0:20:00.89 - 0:20:01.39]: Wait?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.130
- **AI** [0:20:02.12 - 0:20:03.04]: Shindo-san?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.131
- **AI** [0:20:06.36 - 0:20:08.08]: Good work today.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.132
- **AI** [0:20:10.92 - 0:20:11.72]: I am sorry
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.133
- **AI** [0:20:11.72 - 0:20:13.12]: for calling so late.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.134
- **AI** [0:20:16.00 - 0:20:18.52]: The timing was so perfect, it really surprised me.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.135
- **AI** [0:20:20.81 - 0:20:21.31]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.136
- **AI** [0:20:21.88 - 0:20:22.44]: Actually,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.137
- **AI** [0:20:24.40 - 0:20:28.12]: the request for the new song for the Fan Festa has been withdrawn.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.138
- **AI** [0:20:30.13 - 0:20:30.63]: ?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.139
- **AI** [0:20:36.00 - 0:20:38.56]: It wasn't due to any fault on our part.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.140
- **AI** [0:20:39.80 - 0:20:41.84]: The representative just contacted me.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.141
- **AI** [0:20:42.76 - 0:20:45.68]: It seems they heard back from the creator who was ill.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.142
- **AI** [0:20:46.55 - 0:20:47.05]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.143
- **AI** [0:20:47.60 - 0:20:51.24]: So you mean the person who was originally in charge of the song?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.144
- **AI** [0:20:51.24 - 0:20:51.99]: Yes.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.145
- **AI** [0:20:52.68 - 0:21:00.16]: They said they'll be able to finish all three songs as planned, and they were very apologetic.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.146
- **AI** [0:21:01.04 - 0:21:04.88]: It sounded like they were ready to prostrate themselves over the phone.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.147
- **AI** [0:21:05.59 - 0:21:06.09]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.148
- **AI** [0:21:13.56 - 0:21:17.28]: It is a bit disappointing that the offer fell through, though.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.149
- **AI** [0:21:18.92 - 0:21:19.64]: True.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.150
- **AI** [0:21:20.68 - 0:21:23.32]: However, we actually received a new request.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.151
- **AI** [0:21:24.04 - 0:21:25.04]: A new one?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.152
- **AI** [0:21:27.48 - 0:21:34.96]: The rep said they'd love to have Leo/need perform in the 'Freshman Slot' at the next Fan Festa.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.153
- **AI** [0:21:35.80 - 0:21:37.36]: It's partly to make up for this time.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.154
- **AI** [0:21:39.53 - 0:21:40.03]: ?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.155
- **AI** [0:21:42.96 - 0:21:47.48]: It's a bit further out, but I think we should consider it positively.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.156
- **AI** [0:21:48.24 - 0:21:51.48]: Since it's in the future, there shouldn't be any scheduling issues.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.157
- **AI** [0:21:53.04 - 0:21:53.64]: I understand.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.158
- **AI** [0:21:54.52 - 0:21:58.44]: I'll talk to the rest of the members about it.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.159
- **AI** [0:21:59.48 - 0:22:00.16]: Please do.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.160
- **AI** [0:22:00.92 - 0:22:05.08]: There's no rush, so feel free to take your time deciding.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.161
- **AI** [0:22:06.76 - 0:22:13.84]: I'm truly sorry for causing so much confusion in the end.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.162
- **AI**: *(no line)*
- **Human** [0:22:13.24 - 0:22:14.47]: This happens, doesn't it?
- **Note**: Line added in human version

### 2.163
- **AI** [0:22:18.79 - 0:22:19.29]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.164
- **AI** [0:22:20.24 - 0:22:22.16]: I think it couldn't be helped.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.165
- **AI** [0:22:23.40 - 0:22:26.68]: Besides, I'm glad we found out before we officially accepted.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.166
- **AI** [0:22:28.08 - 0:22:30.36]: I'm relieved to hear you say that.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.167
- **AI** [0:22:31.80 - 0:22:39.48]: I'll do my best to support you so you can focus on the one-man live and the new songs.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.168
- **AI** [0:22:41.88 - 0:22:42.48]: We're counting on you.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.169
- **AI** [0:22:45.56 - 0:22:46.20]: That's good.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.170
- **AI** [0:22:50.92 - 0:22:52.32]: Right now, I...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.171
- **AI** [0:22:54.40 - 0:22:58.16]: Well then, I'll leave contacting the other members to you.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.172
- **AI** [0:22:59.92 - 0:23:02.92]: I'll get in touch with the staff for the one-man live.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.173
- **AI** [0:23:03.96 - 0:23:06.12]: I want to proceed with the setlist that includes the new song.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.174
- **AI** [0:23:07.53 - 0:23:08.03]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.175
- **AI** [0:23:08.54 - 0:23:09.04]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.176
- **AI** [0:23:09.04 - 0:23:10.00]: I'll let them know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.177
- **AI** [0:23:11.36 - 0:23:12.36]: Thank you very much.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.178
- **AI** [0:23:13.24 - 0:23:14.88]: I'll be going now.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.179
- **AI** [0:23:20.72 - 0:23:21.40]: I...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.180
- **AI** [0:23:28.08 - 0:23:31.52]: I feel so relieved right now.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.181
- **AI** [0:23:32.37 - 0:23:32.87]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.182
- **AI** [0:23:35.08 - 0:23:35.64]: Yeah.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.183
- **AI** [0:23:44.20 - 0:23:54.36]: I thought I had to make a choice, that I had to pick one over the other, but now that I don't have to...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.184
- **AI** [0:23:56.32 - 0:23:57.32]: I'm just glad.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.185
- **AI** [0:23:58.12 - 0:23:59.04]: I'm relieved.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.186
- **AI** [0:23:59.04 - 0:23:59.64]: She's so admirable.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.187
- **AI** [0:24:04.10 - 0:24:05.00]: But...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.188
- **AI** [0:24:07.80 - 0:24:17.05]: This time I happened to avoid it, but there will surely be times in the future when I have to choose.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.189
- **AI** [0:24:17.05 - 0:24:17.69]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.190
- **AI** [0:24:24.84 - 0:24:25.36]: That's why...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.191
- **AI** [0:24:28.40 - 0:24:30.08]: I need to become someone who can make those choices.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.192
- **AI** [0:24:31.09 - 0:24:31.73]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.193
- **AI** [0:24:31.73 - 0:24:33.48]: So that I can lead everyone.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.194
- **AI** [0:24:35.56 - 0:24:37.20]: She's leading herself.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.195
- **AI**: *(no line)*
- **Human** [0:24:35.56 - 0:24:38.32]: You're already such a good leader!
- **Note**: Line added in human version

### 2.196
- **AI** [0:24:37.20 - 0:24:40.16]: As the leader of Leo/need.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.197
- **AI** [0:24:44.79 - 0:24:45.29]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.198
- **AI** [0:24:48.17 - 0:24:48.83]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.199
- **AI**: *(no line)*
- **Human** [0:24:52.05 - 0:25:00.83]: So my favorite, or most memorable part was that part just before,
- **Note**: Line added in human version

### 2.200
- **AI** [0:24:52.12 - 0:24:57.22]: Personally, the scene that caught my attention...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.201
- **AI** [0:24:57.22 - 0:25:06.00]: The part that left an impression was when Honami-chan said she would definitely choose...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.202
- **AI**: *(no line)*
- **Human** [0:25:00.83 - 0:25:03.46]: when Honami was thinking,
- **Note**: Line added in human version

### 2.203
- **AI**: *(no line)*
- **Human** [0:25:03.46 - 0:25:09.28]: "I thought for sure I'd be able to come to a decision,"
- **Note**: Line added in human version

### 2.204
- **AI** [0:25:06.00 - 0:25:11.78]: She seemed a bit down, but...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.205
- **AI**: *(no line)*
- **Human** [0:25:24.21 - 0:25:27.55]: "oh, yay!~"
- **Note**: Line added in human version

### 2.206
- **AI**: *(no line)*
- **Human** [0:25:27.55 - 0:25:32.59]: A lot of that has to do with the fact that I've never really worked as a leader myself,
- **Note**: Line added in human version

### 2.207
- **AI** [0:25:29.68 - 0:25:33.78]: I wonder about that part.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.208
- **AI** [0:25:33.78 - 0:25:35.56]: How should I put it?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.209
- **AI** [0:25:44.26 - 0:25:51.92]: but I also don't want her to take things too heavily. If she keeps going like that, she might break,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.210
- **AI**: *(no line)*
- **Human** [0:25:44.31 - 0:25:49.12]: but at the same time, I kept hoping that things wouldn't get too serious.
- **Note**: Line added in human version

### 2.211
- **AI** [0:25:51.92 - 0:25:55.70]: so it was a scene that made me worry about Honami-chan.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.212
- **AI**: *(no line)*
- **Human** [0:26:41.75 - 0:26:43.64]: And I pray...
- **Note**: Line added in human version

### 2.213
- **AI**: *(no line)*
- **Human** [0:26:43.64 - 0:26:45.94]: I pray they don't end up on bad terms,
- **Note**: Line added in human version

### 2.214
- **AI** [0:26:57.04 - 0:26:57.56]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.215
- **AI** [0:26:58.36 - 0:26:59.08]: That's just how it is.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.216
- **AI** [0:27:13.00 - 0:27:15.16]: I wish she could share some of Yukki's lightheartedness.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.217
- **AI**: *(no line)*
- **Human** [0:27:13.00 - 0:27:15.16]: Yukki, give some of that chill energy to them!
- **Note**: Line added in human version

### 2.218
- **AI** [0:27:16.04 - 0:27:19.04]: Well, maybe it's still too early for that.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.219
- **AI**: *(no line)*
- **Human** [0:27:16.04 - 0:27:19.51]: Well, hold on a sec, guys.
- **Note**: Line added in human version

### 2.220
- **AI** [0:27:34.77 - 0:27:35.29]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.221
- **AI**: *(no line)*
- **Human** [0:27:34.77 - 0:27:35.29]: Alright.
- **Note**: Line added in human version

### 2.222
- **AI**: *(no line)*
- **Human** [0:27:51.42 - 0:27:53.88]: Ichika was more excited than usual.
- **Note**: Line added in human version

### 2.223
- **AI** [0:27:53.88 - 0:27:55.00]: She was all giddy,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.224
- **AI** [0:28:03.40 - 0:28:09.40]: if I did, I'd just end up saying "how cute" the whole time, just like the audience.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.225
- **AI**: *(no line)*
- **Human** [0:28:03.40 - 0:28:09.40]: but if I did, I'd just be like "wow, Ichi cute. Hona cute. Crowd members cute."
- **Note**: Line added in human version

### 2.226
- **AI** [0:28:19.12 - 0:28:19.72]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.227
- **AI** [0:28:27.56 - 0:28:28.92]: Actually...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.228
- **AI**: *(no line)*
- **Human** [0:28:27.56 - 0:28:28.92]: 100%.
- **Note**: Line added in human version

### 2.229
- **AI** [0:28:29.47 - 0:28:29.97]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.230
- **AI**: *(no line)*
- **Human** [0:28:34.92 - 0:28:38.05]: I'm originally from Wakayama, and there happened to be a live there.
- **Note**: Line added in human version

### 2.231
- **AI** [0:28:45.55 - 0:28:46.14]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.232
- **AI**: *(no line)*
- **Human** [0:29:09.20 - 0:29:12.02]: While the story showed her struggling with the weight of her decision,
- **Note**: Line added in human version

### 2.233
- **AI**: *(no line)*
- **Human** [0:29:16.95 - 0:29:19.02]: Combining that with the event song's rhythmic energy,
- **Note**: Line added in human version

### 2.234
- **AI**: *(no line)*
- **Human** [0:29:22.24 - 0:29:27.00]: And since this song features a sweet cuteness we don't always see from Leo/need,
- **Note**: Line added in human version

### 2.235
- **AI**: *(no line)*
- **Human** [0:29:32.72 - 0:29:36.78]: Also, to symbolize Leo/need choosing their path as a band,
- **Note**: Line added in human version

### 2.236
- **AI**: *(no line)*
- **Human** [0:30:01.56 - 0:30:04.02]: Alright, so...
- **Note**: Line added in human version

### 2.237
- **AI** [0:30:05.56 - 0:30:06.64]: From where?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.238
- **AI**: *(no line)*
- **Human** [0:30:05.56 - 0:30:07.44]: Who should we look at first?
- **Note**: Line added in human version

### 2.239
- **AI**: *(no line)*
- **Human** [0:30:20.24 - 0:30:25.42]: Hmm. Honami has a bit of a stunned look here,
- **Note**: Line added in human version

### 2.240
- **AI** [0:30:55.54 - 0:30:56.23]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.241
- **AI** [0:30:57.80 - 0:30:59.00]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.242
- **AI**: *(no line)*
- **Human** [0:30:57.80 - 0:30:59.00]: Oh yeah, and the stars.
- **Note**: Line added in human version

### 2.243
- **AI**: *(no line)*
- **Human** [0:30:59.00 - 0:31:01.20]: So many stars all over the art.
- **Note**: Line added in human version

### 2.244
- **AI** [0:31:09.80 - 0:31:10.96]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.245
- **AI**: *(no line)*
- **Human** [0:31:09.80 - 0:31:10.96]: So stylish!
- **Note**: Line added in human version

### 2.246
- **AI** [0:31:20.32 - 0:31:20.96]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.247
- **AI**: *(no line)*
- **Human** [0:31:20.32 - 0:31:20.96]: Cute~
- **Note**: Line added in human version

### 2.248
- **AI** [0:31:40.71 - 0:31:41.34]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.249
- **AI** [0:31:44.36 - 0:31:44.86]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.250
- **AI**: *(no line)*
- **Human** [0:31:44.46 - 0:31:45.86]: Wow~
- **Note**: Line added in human version

### 2.251
- **AI** [0:31:49.14 - 0:31:49.96]: It's just too good.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.252
- **AI** [0:32:09.22 - 0:32:10.45]: Is that what it's called?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.253
- **AI**: *(no line)*
- **Human** [0:32:09.22 - 0:32:11.09]: It's called 'taiiku-zuwari (gym sitting)?' Ah.
- **Note**: Line added in human version

### 2.254
- **AI** [0:32:10.45 - 0:32:11.09]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.255
- **AI** [0:32:16.97 - 0:32:17.61]: People say it, right?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.256
- **AI** [0:32:22.62 - 0:32:23.20]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.257
- **AI**: *(no line)*
- **Human** [0:32:22.62 - 0:32:23.80]: 'Sankaku-zuwari'—you haven't?
- **Note**: Line added in human version

### 2.258
- **AI** [0:32:26.39 - 0:32:26.89]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.259
- **AI** [0:32:28.87 - 0:32:29.37]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.260
- **AI**: *(no line)*
- **Human** [0:32:53.42 - 0:32:54.32]: Apologies.
- **Note**: Line added in human version

### 2.261
- **AI** [0:33:07.28 - 0:33:08.08]: there are so many, right?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.262
- **AI** [0:33:16.62 - 0:33:18.54]: It's amazing.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.263
- **AI**: *(no line)*
- **Human** [0:33:16.62 - 0:33:18.23]: Super cute.
- **Note**: Line added in human version

### 2.264
- **AI** [0:33:18.54 - 0:33:19.35]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.265
- **AI** [0:33:38.72 - 0:33:39.98]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.266
- **AI**: *(no line)*
- **Human** [0:33:38.72 - 0:33:39.98]: Wow~
- **Note**: Line added in human version

### 2.267
- **AI** [0:33:44.60 - 0:33:45.58]: Like a student would.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.268
- **AI** [0:33:50.44 - 0:33:51.76]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.269
- **AI**: *(no line)*
- **Human** [0:33:50.44 - 0:33:51.76]: Good times.
- **Note**: Line added in human version

### 2.270
- **AI** [0:33:57.96 - 0:33:58.64]: Wait, I mean...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.271
- **AI** [0:34:00.14 - 0:34:00.76]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.272
- **AI**: *(no line)*
- **Human** [0:34:00.14 - 0:34:00.76]: Wow!
- **Note**: Line added in human version

### 2.273
- **AI** [0:34:04.64 - 0:34:05.50]: It's wonderful.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.274
- **AI** [0:34:31.80 - 0:34:33.84]: I want to tell her not to get hurt.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.275
- **AI**: *(no line)*
- **Human** [0:34:31.80 - 0:34:33.84]: "You're gonna get hurt!"
- **Note**: Line added in human version

### 2.276
- **AI** [0:34:41.44 - 0:34:42.64]: They really do.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.277
- **AI**: *(no line)*
- **Human** [0:34:41.44 - 0:34:42.64]: Super cute.
- **Note**: Line added in human version

### 2.278
- **AI** [0:34:47.43 - 0:34:47.93]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.279
- **AI**: *(no line)*
- **Human** [0:34:49.08 - 0:34:50.72]: Ah... So cute I can't help but just sigh.
- **Note**: Line added in human version

### 2.280
- **AI** [0:35:08.61 - 0:35:09.11]: Wait a second.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.281
- **AI**: *(no line)*
- **Human** [0:35:08.61 - 0:35:09.37]: Hold on—
- **Note**: Line added in human version

### 2.282
- **AI** [0:35:20.60 - 0:35:21.24]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.283
- **AI**: *(no line)*
- **Human** [0:35:20.60 - 0:35:21.24]: Crap.
- **Note**: Line added in human version

### 2.284
- **AI**: *(no line)*
- **Human** [0:35:22.84 - 0:35:25.24]: But isn't this so good though?
- **Note**: Line added in human version

### 2.285
- **AI** [0:35:23.96 - 0:35:24.46]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.286
- **AI** [0:35:30.88 - 0:35:31.80]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.287
- **AI** [0:35:41.20 - 0:35:42.80]: from the autumn shuffle event? Having that there is a nice touch.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.288
- **AI** [0:36:19.16 - 0:36:20.36]: I'm going to get scolded,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.289
- **AI**: *(no line)*
- **Human** [0:36:19.16 - 0:36:20.36]: Someone's gonna chew me out.
- **Note**: Line added in human version

### 2.290
- **AI** [0:36:41.12 - 0:36:41.98]: Post-Training.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.291
- **AI**: *(no line)*
- **Human** [0:36:41.12 - 0:36:43.35]: Here's the trained. Very nice~
- **Note**: Line added in human version

### 2.292
- **AI** [0:36:49.80 - 0:36:50.88]: And...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.293
- **AI** [0:37:31.69 - 0:37:32.20]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.294
- **AI**: *(no line)*
- **Human** [0:37:43.82 - 0:37:45.02]: Wow~
- **Note**: Line added in human version

### 2.295
- **AI**: *(no line)*
- **Human** [0:37:59.12 - 0:38:00.82]: And that logo— I need it.
- **Note**: Line added in human version

### 2.296
- **AI** [0:38:37.19 - 0:38:37.88]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.297
- **AI** [0:38:52.72 - 0:38:53.70]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.298
- **AI**: *(no line)*
- **Human** [0:39:01.95 - 0:39:05.44]: Then, we'll talk a bit about the song itself and the MV.
- **Note**: Line added in human version

### 2.299
- **AI**: *(no line)*
- **Human** [0:39:09.90 - 0:39:10.71]: Let's go!
- **Note**: Line added in human version

### 2.300
- **AI** [0:42:15.00 - 0:42:19.08]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.301
- **AI**: *(no line)*
- **Human** [0:42:17.27 - 0:42:19.55]: Waaah~
- **Note**: Line added in human version

### 2.302
- **AI**: *(no line)*
- **Human** [0:42:20.03 - 0:42:21.55]: Great MV.
- **Note**: Line added in human version

### 2.303
- **AI**: *(no line)*
- **Human** [0:42:21.55 - 0:42:24.92]: It has a feeling of, how to say, lightness and transparency,
- **Note**: Line added in human version

### 2.304
- **AI** [0:42:21.60 - 0:42:28.04]: This MV is really great, it has a sense of transparency but it's also poppy.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.305
- **AI**: *(no line)*
- **Human** [0:42:24.92 - 0:42:26.82]: while also keeping a pop vibe.
- **Note**: Line added in human version

### 2.306
- **AI**: *(no line)*
- **Human** [0:42:26.82 - 0:42:28.75]: Really nice.
- **Note**: Line added in human version

### 2.307
- **AI** [0:42:36.18 - 0:42:39.68]: in the A and B sections, there's a lot of hesitation.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.308
- **AI**: *(no line)*
- **Human** [0:42:36.38 - 0:42:43.64]: I remember being asked to sing with a bit of hesitation in the verse and prechorus.
- **Note**: Line added in human version

### 2.309
- **AI** [0:42:39.68 - 0:42:46.86]: I was told to convey a sense of bewilderment and not to sing it too strongly.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.310
- **AI**: *(no line)*
- **Human** [0:42:43.64 - 0:42:46.94]: Almost like I was a bit worn out.
- **Note**: Line added in human version

### 2.311
- **AI**: *(no line)*
- **Human** [0:42:54.37 - 0:42:57.06]: so that's how the song turned out.
- **Note**: Line added in human version

### 2.312
- **AI**: *(no line)*
- **Human** [0:43:02.90 - 0:43:08.34]: Actually, as far as commissioned song lyrics go,
- **Note**: Line added in human version

### 2.313
- **AI**: *(no line)*
- **Human** [0:43:11.78 - 0:43:15.14]: I don't remember if that's happened yet. Is this the first time?
- **Note**: Line added in human version

### 2.314
- **AI** [0:43:12.92 - 0:43:13.88]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.315
- **AI** [0:43:13.88 - 0:43:14.68]: Does it feel like her?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.316
- **AI**: *(no line)*
- **Human** [0:43:15.14 - 0:43:17.44]: That's what immediately stood out to me.
- **Note**: Line added in human version

### 2.317
- **AI**: *(no line)*
- **Human** [0:43:17.44 - 0:43:21.76]: Yeah. It's a pretty new feeling. And makes it easy to remember.
- **Note**: Line added in human version

### 2.318
- **AI**: *(no line)*
- **Human** [0:43:28.05 - 0:43:29.13]: Yeah.
- **Note**: Line added in human version

### 2.319
- **AI**: *(no line)*
- **Human** [0:43:29.13 - 0:43:34.52]: m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 76 1 76 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 40 1 40 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 54 1 54 0m 0 0 l 0 1 43 1 43 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 58 1 58 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 79 1 79 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 90 1 90 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 81 1 81 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 81 1 81 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 80 1 80 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 78 1 78 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 57 1 57 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 72 1 72 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 57 1 57 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0
- **Note**: Line added in human version

### 2.320
- **AI** [0:43:32.00 - 0:43:33.60]: An apple pie appears in it.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.321
- **AI**: *(no line)*
- **Human** [0:43:34.52 - 0:43:38.29]: m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 76 1 76 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 40 1 40 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 54 1 54 0m 0 0 l 0 1 43 1 43 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 53 1 53 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 44 1 44 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 58 1 58 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 48 1 48 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 51 1 51 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 56 1 56 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 79 1 79 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 90 1 90 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 52 1 52 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 81 1 81 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 46 1 46 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 81 1 81 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 45 1 45 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 80 1 80 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 78 1 78 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 57 1 57 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 72 1 72 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 50 1 50 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 49 1 49 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 35 1 35 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 36 1 36 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 31 1 31 0m 0 0 l 0 1 33 1 33 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 38 1 38 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 40 1 40 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 39 1 39 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 37 1 37 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 47 1 47 0m 0 0 l 0 1 32 1 32 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 57 1 57 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 41 1 41 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 6 1 6 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 30 1 30 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 22 1 22 0m 0 0 l 0 1 23 1 23 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 29 1 29 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 25 1 25 0m 0 0 l 0 1 19 1 19 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 2 1 2 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 26 1 26 0m 0 0 l 0 1 11 1 11 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 9 1 9 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 20 1 20 0m 0 0 l 0 1 6 1 6 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 13 1 13 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 14 1 14 0m 0 0 l 0 1 34 1 34 0m 0 0 l 0 1 28 1 28 0m 0 0 l 0 1 16 1 16 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 8 1 8 0\Nm 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 5 1 5 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 12 1 12 0m 0 0 l 0 1 18 1 18 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 15 1 15 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 21 1 21 0m 0 0 l 0 1 24 1 24 0m 0 0 l 0 1 42 1 42 0m 0 0 l 0 1 27 1 27 0m 0 0 l 0 1 17 1 17 0m 0 0 l 0 1 4 1 4 0m 0 0 l 0 1 7 1 7 0m 0 0 l 0 1 9 1 9 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 1 1 1 0m 0 0 l 0 1 2 1 2 0m 0 0 l 0 1 8 1 8 0m 0 0 l 0 1 3 1 3 0m 0 0 l 0 1 10 1 10 0m 0 0 l 0 1 7 1 7 0
- **Note**: Line added in human version

### 2.322
- **AI**: *(no line)*
- **Human** [0:43:51.59 - 0:43:53.36]: Would it?
- **Note**: Line added in human version

### 2.323
- **AI**: *(no line)*
- **Human** [0:43:53.36 - 0:43:55.74]: Would Shiho get...
- **Note**: Line added in human version

### 2.324
- **AI** [0:44:05.50 - 0:44:07.04]: ...
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.325
- **AI**: *(no line)*
- **Human** [0:44:07.56 - 0:44:12.13]: You can, uh... they made it so you can play Master mode immediately now.
- **Note**: Line added in human version

### 2.326
- **AI** [0:44:07.68 - 0:44:11.44]: The Master chart should be available to play right away, so
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.327
- **AI** [0:44:20.32 - 0:44:21.76]: Do they want us to play it that much?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.328
- **AI** [0:44:24.66 - 0:44:25.88]: Like 'chugga-chugga-chugga-chugga.'
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.329
- **AI**: *(no line)*
- **Human** [0:44:24.80 - 0:44:25.99]: Kind of like "JYA JYA JYA",
- **Note**: Line added in human version

### 2.330
- **AI** [0:44:25.88 - 0:44:39.92]: D-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d!
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.331
- **AI**: *(no line)*
- **Human** [0:44:25.99 - 0:44:28.55]: or like "DA DO DO DAN DO" hahaha!
- **Note**: Line added in human version

### 2.332
- **AI**: *(no line)*
- **Human** [0:44:36.22 - 0:44:39.57]: just make it an April Fool's song if you're really gonna do it.
- **Note**: Line added in human version

### 2.333
- **AI**: *(no line)*
- **Human** [0:44:57.12 - 0:45:03.85]: Really though, I'm excited for any potential favorite food inclusions in upcoming songs like this.
- **Note**: Line added in human version

### 2.334
- **AI** [0:44:57.20 - 0:45:02.80]: In this way, characters' favorite things might be included in the future,
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.335
- **AI** [0:45:22.08 - 0:45:23.24]: so please take a look.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.336
- **AI**: *(no line)*
- **Human** [0:45:23.90 - 0:45:27.42]: Well then, it was just a short episode this time,
- **Note**: Line added in human version

### 2.337
- **AI**: *(no line)*
- **Human** [0:45:33.20 - 0:45:34.53]: So quick!
- **Note**: Line added in human version

### 2.338
- **AI** [0:45:33.24 - 0:45:34.44]: Oh.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.339
- **AI**: *(no line)*
- **Human** [0:45:35.73 - 0:45:38.16]: That just flew by so quick.
- **Note**: Line added in human version

### 2.340
- **AI** [0:45:48.52 - 0:45:49.02]: or something like that.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.341
- **AI** [0:45:51.37 - 0:45:51.87]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.342
- **AI** [0:45:52.56 - 0:45:53.82]: It went by in a flash.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.343
- **AI**: *(no line)*
- **Human** [0:46:32.54 - 0:46:35.02]: With that, thanks so much for a fun AfterTalk today!
- **Note**: Line added in human version

### 2.344
- **AI** [0:46:32.60 - 0:46:35.02]: Anyway, I had a lot of fun.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.345
- **AI** [0:46:37.12 - 0:46:37.80]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.346
- **AI**: *(no line)*
- **Human** [0:46:37.18 - 0:46:41.33]: Bye bye!
- **Note**: Line added in human version

### 2.347
- **AI** [0:46:37.80 - 0:46:38.30]: .
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.348
- **AI** [0:47:41.68 - 0:47:42.60]: What do you mean?
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.349
- **AI** [0:47:42.60 - 0:47:43.10]: I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.350
- **AI** [0:47:43.10 - 0:47:44.09]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.351
- **AI** [0:47:44.09 - 0:47:45.06]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.352
- **AI** [0:47:45.06 - 0:47:45.94]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.353
- **AI** [0:47:45.94 - 0:47:46.82]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.354
- **AI** [0:47:46.82 - 0:47:47.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.355
- **AI** [0:47:47.70 - 0:47:48.58]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.356
- **AI** [0:47:48.58 - 0:47:49.50]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.357
- **AI** [0:47:49.50 - 0:47:50.42]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.358
- **AI** [0:47:50.42 - 0:47:51.38]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.359
- **AI** [0:47:51.38 - 0:47:52.30]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.360
- **AI** [0:47:52.30 - 0:47:53.22]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.361
- **AI** [0:47:53.22 - 0:47:54.14]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.362
- **AI** [0:47:54.14 - 0:47:54.98]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.363
- **AI** [0:47:54.98 - 0:47:55.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.364
- **AI** [0:47:55.86 - 0:47:56.76]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.365
- **AI** [0:47:56.76 - 0:47:57.60]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.366
- **AI** [0:47:57.60 - 0:47:58.44]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.367
- **AI** [0:47:58.44 - 0:47:59.36]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.368
- **AI** [0:47:59.36 - 0:48:00.12]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.369
- **AI** [0:48:00.12 - 0:48:00.92]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.370
- **AI** [0:48:00.92 - 0:48:01.72]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.371
- **AI** [0:48:01.72 - 0:48:02.56]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.372
- **AI** [0:48:02.56 - 0:48:03.44]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.373
- **AI** [0:48:03.44 - 0:48:04.36]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.374
- **AI** [0:48:04.36 - 0:48:05.20]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.375
- **AI** [0:48:05.20 - 0:48:06.08]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.376
- **AI** [0:48:06.08 - 0:48:06.96]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.377
- **AI** [0:48:06.96 - 0:48:07.84]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.378
- **AI** [0:48:07.84 - 0:48:08.72]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.379
- **AI** [0:48:08.72 - 0:48:09.68]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.380
- **AI** [0:48:09.68 - 0:48:10.52]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.381
- **AI** [0:48:10.52 - 0:48:11.34]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.382
- **AI** [0:48:11.34 - 0:48:12.12]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.383
- **AI** [0:48:12.12 - 0:48:12.92]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.384
- **AI** [0:48:12.92 - 0:48:13.82]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.385
- **AI** [0:48:13.82 - 0:48:14.68]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.386
- **AI** [0:48:14.68 - 0:48:15.50]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.387
- **AI** [0:48:15.50 - 0:48:16.38]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.388
- **AI** [0:48:16.38 - 0:48:17.26]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.389
- **AI** [0:48:17.26 - 0:48:18.02]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.390
- **AI** [0:48:18.02 - 0:48:18.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.391
- **AI** [0:48:18.86 - 0:48:19.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.392
- **AI** [0:48:19.70 - 0:48:20.54]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.393
- **AI** [0:48:20.54 - 0:48:21.38]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.394
- **AI** [0:48:21.38 - 0:48:21.92]: I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.395
- **AI** [0:48:21.92 - 0:48:22.74]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.396
- **AI** [0:48:22.74 - 0:48:23.62]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.397
- **AI** [0:48:23.62 - 0:48:24.50]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.398
- **AI** [0:48:24.50 - 0:48:25.30]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.399
- **AI** [0:48:25.30 - 0:48:26.14]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.400
- **AI** [0:48:26.14 - 0:48:27.02]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.401
- **AI** [0:48:27.02 - 0:48:27.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.402
- **AI** [0:48:27.86 - 0:48:28.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.403
- **AI** [0:48:28.70 - 0:48:29.58]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.404
- **AI** [0:48:29.58 - 0:48:30.42]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.405
- **AI** [0:48:30.42 - 0:48:31.26]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.406
- **AI** [0:48:31.26 - 0:48:32.18]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.407
- **AI** [0:48:32.18 - 0:48:32.98]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.408
- **AI** [0:48:32.98 - 0:48:33.78]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.409
- **AI** [0:48:33.78 - 0:48:34.62]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.410
- **AI** [0:48:34.62 - 0:48:35.50]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.411
- **AI** [0:48:35.50 - 0:48:36.38]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.412
- **AI** [0:48:36.38 - 0:48:37.22]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.413
- **AI** [0:48:37.22 - 0:48:37.75]: I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.414
- **AI** [0:48:37.75 - 0:48:38.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.415
- **AI** [0:48:38.70 - 0:48:39.54]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.416
- **AI** [0:48:39.54 - 0:48:40.34]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.417
- **AI** [0:48:40.34 - 0:48:41.22]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.418
- **AI** [0:48:41.22 - 0:48:42.16]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.419
- **AI** [0:48:42.16 - 0:48:43.44]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.420
- **AI** [0:48:43.44 - 0:48:44.26]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.421
- **AI** [0:48:44.26 - 0:48:45.06]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.422
- **AI** [0:48:45.06 - 0:48:45.82]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.423
- **AI** [0:48:45.82 - 0:48:46.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.424
- **AI** [0:48:46.70 - 0:48:47.54]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.425
- **AI** [0:48:47.54 - 0:48:48.34]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.426
- **AI** [0:48:48.34 - 0:48:49.22]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.427
- **AI** [0:48:49.22 - 0:48:50.14]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.428
- **AI** [0:48:50.14 - 0:48:50.90]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.429
- **AI** [0:48:50.90 - 0:48:51.72]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.430
- **AI** [0:48:51.72 - 0:48:52.32]: I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.431
- **AI** [0:48:52.32 - 0:48:53.14]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.432
- **AI** [0:48:53.14 - 0:48:53.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.433
- **AI** [0:48:53.86 - 0:48:54.66]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.434
- **AI** [0:48:54.66 - 0:48:55.17]: I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.435
- **AI** [0:48:55.17 - 0:48:56.06]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.436
- **AI** [0:48:56.06 - 0:48:56.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.437
- **AI** [0:48:56.86 - 0:48:57.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.438
- **AI** [0:48:57.70 - 0:48:58.50]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.439
- **AI** [0:48:58.50 - 0:48:59.46]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.440
- **AI** [0:48:59.46 - 0:49:00.34]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.441
- **AI** [0:49:00.34 - 0:49:01.14]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.442
- **AI** [0:49:01.14 - 0:49:01.98]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.443
- **AI** [0:49:01.98 - 0:49:02.86]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.444
- **AI** [0:49:02.86 - 0:49:03.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.445
- **AI** [0:49:03.70 - 0:49:04.58]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.446
- **AI** [0:49:04.58 - 0:49:05.46]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.447
- **AI** [0:49:05.46 - 0:49:06.26]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.448
- **AI** [0:49:06.26 - 0:49:07.10]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.449
- **AI** [0:49:07.10 - 0:49:07.90]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.450
- **AI** [0:49:07.90 - 0:49:08.70]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.451
- **AI** [0:49:08.70 - 0:49:09.58]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.452
- **AI** [0:49:09.58 - 0:49:10.42]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.453
- **AI** [0:49:10.42 - 0:49:11.30]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.454
- **AI** [0:49:11.30 - 0:49:12.18]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.455
- **AI** [0:49:12.18 - 0:49:13.10]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

### 2.456
- **AI** [0:49:13.10 - 0:49:14.04]: I don't know. I don't know.
- **Human**: *(removed/merged into adjacent line)*
- **Note**: Line removed in human version

---

## Category 1: Timing-Only Adjustments

**Count: 25**

Lines where the text was unchanged but the AI start/end times were nudged.

| # | AI Start | AI End | Human Start | Human End | Text (excerpt) |
|---|----------|--------|-------------|-----------|----------------|
| 1 | 0:27:20.44 | 0:27:22.32 | 0:27:20.44 | 0:27:22.92 | They're still high school students, after all. |
| 2 | 0:27:32.92 | 0:27:34.20 | 0:27:32.92 | 0:27:34.77 | It'll be okay. |
| 3 | 0:27:56.80 | 0:27:57.60 | 0:27:56.80 | 0:27:58.15 | I thought it was so cute. |
| 4 | 0:29:01.86 | 0:29:09.02 | 0:29:02.06 | 0:29:09.20 | This story was about Honami realizing the importance and weight of making dec... |
| 5 | 0:29:59.64 | 0:30:00.32 | 0:29:59.46 | 0:30:00.32 | Let's take a look. |
| 6 | 0:30:07.44 | 0:30:09.72 | 0:30:07.44 | 0:30:10.48 | Do we usually start with the 4-stars? |
| 7 | 0:30:10.48 | 0:30:12.12 | 0:30:10.48 | 0:30:12.31 | Let's start with the 4-stars then. |
| 8 | 0:32:18.20 | 0:32:19.30 | 0:32:18.20 | 0:32:19.44 | You've never heard it? |
| 9 | 0:32:19.30 | 0:32:20.54 | 0:32:19.44 | 0:32:20.72 | No? |
| 10 | 0:32:20.54 | 0:32:21.27 | 0:32:20.72 | 0:32:21.88 | Really? |
| 11 | 0:32:31.08 | 0:32:32.12 | 0:32:31.15 | 0:32:32.47 | My apologies. |
| 12 | 0:33:01.36 | 0:33:04.24 | 0:33:01.36 | 0:33:04.59 | Also, the background... there are so many instruments! |
| 13 | 0:33:08.72 | 0:33:13.00 | 0:33:08.72 | 0:33:13.56 | There's a guitar, a bass, an acoustic guitar... |
| 14 | 0:33:52.84 | 0:33:54.84 | 0:33:52.84 | 0:33:55.26 | And are those loose socks? |
| 15 | 0:34:12.80 | 0:34:15.56 | 0:34:12.80 | 0:34:16.24 | I love that she's wearing a sleeveless top underneath. |
| 16 | 0:34:26.12 | 0:34:27.40 | 0:34:26.12 | 0:34:28.16 | It's so like Rin. |
| 17 | 0:34:44.48 | 0:34:45.32 | 0:34:44.48 | 0:34:46.14 | It suits her so well. |
| 18 | 0:35:54.58 | 0:35:56.52 | 0:35:54.58 | 0:35:56.81 | and even the soles of her feet. |
| 19 | 0:36:17.40 | 0:36:18.16 | 0:36:17.40 | 0:36:18.40 | Am I a creep? |
| 20 | 0:36:24.28 | 0:36:26.40 | 0:36:24.28 | 0:36:26.75 | Then don't draw it in the first place, honestly! |
| 21 | 0:36:29.68 | 0:36:31.04 | 0:36:29.68 | 0:36:31.39 | They'll ask me what's wrong with me. |
| 22 | 0:36:44.20 | 0:36:45.64 | 0:36:44.20 | 0:36:45.76 | So cute. |
| 23 | 0:37:32.20 | 0:37:33.16 | 0:37:32.20 | 0:37:33.51 | I almost spun around again. |
| 24 | 0:37:53.56 | 0:37:54.40 | 0:37:53.56 | 0:37:54.50 | Really amazing. |
| 25 | 0:37:55.04 | 0:38:00.82 | 0:37:55.04 | 0:37:59.12 | The logo on the sleeve is great too. I want that logo. |

---

## Summary

### Change Counts

| Category | Count | % of Changes |
|----------|-------|-------------|
| (1) Timing only | 25 | 3% |
| (2) Line redistribution | 456 | 64% |
| (3) Wording changes | 213 | 30% |
| (4) Mistranslation fixes | 16 | 2% |
| **Total changes** | **710** | |
| Unchanged lines | 47 | |

### Patterns in LLM Translation Errors

#### 1. Game/Fandom Terminology Failures
Repeating the dominant pattern from the Colors of Pure Sense evaluation:

- **"Pre-training/post-training" / "Training"** for 特訓前/特訓後 — used ML terminology instead of the standard gacha-game terms "untrained/trained." This recurred 8 times across the card-illustration segment, making it the most visible repeated error.
- **"Hello, hello"** for こんニー (kon-needo) — fabricated a literal greeting for a Leo/need fan-community portmanteau (こんばんは + ニード). Same failure mode as Colors' "Little Niigo" for コニーゴ, just with a different unit's portmanteau.
- **"Unsteady Steady Step"** for the official event title — the Chirp transcription dropped the 'still' syllable and the AI faithfully transliterated the corrupted version, losing the actual song/event title "Unsteady, still steady step."

#### 2. Proper Noun Mishandling

- **咲子 (MEIKO) → "Saki"** — the AI conflated MEIKO's Japanese kanji name 咲子 (Sakiko) with the Leo/need member 咲希 (Saki Tenma). Disastrous for a card-illustration segment where MEIKO's varsity-jacket card was being discussed; a viewer would think the host was talking about the wrong character.
- **アクエラ → "Akuera-san"** for the producer aqu3ra. Same as the Colors-era issue with song titles — official romanizations matter and direct transliteration breaks them.
- **"Proseka"** vs the official stylization "ProSeka" — minor but visible casing inconsistency.

#### 3. Transcription Quality Bleed-Through

This episode's transcription was much noisier than Colors. The AI translator dutifully translated the noise:

- Multi-minute single "lines" with no actual content (e.g., the 0:08:18–0:10:03 line collapsed nearly two minutes of intro into one subtitle).
- Word fragments like "Leon," "Lnの," or "テンション" with no surrounding context produced disconnected translation snippets that the human editor had to discard wholesale.
- The corrupted event title in the transcription propagated directly into the AI output without recognition.

This is partly why the Category 2 (added/deleted) count is so much higher than in Colors — the human had to retime and rewrite from the audio rather than polish a structurally-sound AI baseline.

#### 4. Register and Tone Miscalibration

Same patterns as Colors: the AI skewed toward formal/written English in a casual livestream context. The human edit consistently relaxed register, used contractions, and matched the host's chatty self-talk pattern ("I was like…", "Like…", "Yeah…").

### Most Notable Mistranslations

| Rank | Issue | Impact |
|------|-------|--------|
| 1 | 咲子 "Saki" (instead of MEIKO) | Wrong character identified during a card-illustration walkthrough |
| 2 | "Pre-training/Post-training" for 特訓前/特訓後 (×8) | Wrong domain jargon repeated throughout the card section |
| 3 | "Unsteady Steady Step" missing the official 'still' | Mangled official event/song title in opening and outro |
| 4 | "Hello, hello" for こんニー (kon-needo) | Lost the unit-specific fan greeting |
| 5 | "Akuera-san" for aqu3ra | Producer credit using transliterated rather than official romanization |

### Overall Assessment

The AI translation kept 47 of 581 lines unchanged — substantially fewer than Colors of Pure Sense (32%) — and that delta is largely attributable to a noisier transcription baseline that the human editor had to retime and resegment from scratch.

The mistranslation patterns mirror Colors almost exactly: domain-specific gacha terminology (特訓前/後), unit-specific fan jargon (kon-needo as a sibling of kon-niigo), proper-noun confusion (咲子/MEIKO mistaken for 咲希/Saki), and official-title preservation (the dropped 'still' in "Unsteady, still steady step"). These are the same systematic gaps a domain glossary and explicit proper-noun preservation rules would address.

**Recommendations for the LLM pipeline** (carrying forward from the Colors recommendations):

- A domain glossary covering 特訓前/後 → untrained/trained, character kanji disambiguation (especially Vocaloid-name vs Leo/need-member overlaps like 咲子 vs 咲希), and producer name romanizations (aqu3ra, etc.)
- Per-event title injection so the translator knows the official event title even when the transcription mangles it
- Pre-translation transcription QA: flag unusually long single-segment 'lines' (>30s) for resegmentation before translation runs
- Few-shot examples of unit-specific fan greetings (kon-niigo, kon-needo, etc.) so the translator stops guessing at literal renderings
