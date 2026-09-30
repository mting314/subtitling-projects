"""Attribute cues to characters by voice: ECAPA embeddings + centroids from text-certain anchors."""

import json
import sys

import numpy as np
import soundfile as sf
import torch
from speechbrain.inference.speaker import EncoderClassifier

FORMATTED = sys.argv[1]
OUT = sys.argv[2]


def r(a, b):
    return list(range(a, b + 1))


# Cue indices whose speaker is certain from content alone (see attribution notes).
ANCHORS = {
    "An": r(28, 29) + r(34, 35) + r(38, 49) + r(210, 213) + r(223, 226) + r(231, 241) + r(291, 292),
    "Kanade": r(6, 9) + r(41, 42) + [310] + r(314, 317) + r(322, 324) + [330],
    "Ichika": r(10, 12) + [50] + r(295, 296) + r(311, 312) + r(318, 321),
    "Nene": r(57, 60) + r(64, 68) + [204] + r(214, 217) + [219] + r(242, 244) + r(246, 259) + r(282, 283),
    "Rui": r(17, 20) + r(25, 27) + r(53, 56) + [81, 245, 370, 190, 191, 192, 193, 194, 220, 222, 228, 281, 285, 286,
                                                  313, 327, 343, 348, 352, 354, 357, 382, 385],
    "Airi": [80, 97, 98, 100, 101, 102, 133, 205, 206, 289, 290] + r(335, 338) + r(364, 369) + r(371, 374)
    + [383, 384, 387, 388] + r(396, 398),
    "Mizuki": [78, 79] + r(90, 93) + [137] + r(141, 143) + r(207, 209) + [360, 361, 399, 400],
    "Minori": r(103, 132),
}

cues = json.load(open(FORMATTED, encoding="utf-8"))["cues"]
audio, sr = sf.read("/tmp/drama16k.wav", dtype="float32")
model = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="/tmp/ecapa")

emb = {}
for i, c in enumerate(cues):
    s, e = c["start_time"], c["end_time"]
    if e - s < 0.3:
        continue
    seg = audio[int(s * sr): int(e * sr)]
    with torch.no_grad():
        v = model.encode_batch(torch.from_numpy(seg)[None]).squeeze().numpy()
    emb[i] = v / np.linalg.norm(v)


def centroids(exclude=None):
    out = {}
    for name, idx in ANCHORS.items():
        vs = [emb[i] for i in idx if i in emb and i != exclude and cues[i]["end_time"] - cues[i]["start_time"] >= 1.0]
        if vs:
            m = np.mean(vs, axis=0)
            out[name] = m / np.linalg.norm(m)
    return out


def rank(v, cents):
    return sorted(((float(v @ m), n) for n, m in cents.items()), reverse=True)


# Leave-one-out check on anchors >= 1s: does voice agree with content?
truth = {i: n for n, idx in ANCHORS.items() for i in idx}
hits = total = 0
confusions = []
for i, n in truth.items():
    if i not in emb or cues[i]["end_time"] - cues[i]["start_time"] < 1.0:
        continue
    pred = rank(emb[i], centroids(exclude=i))[0][1]
    total += 1
    hits += pred == n
    if pred != n:
        confusions.append((i, n, pred))
print(f"anchor LOO accuracy: {hits}/{total} = {hits / total:.0%}", file=sys.stderr)
for i, n, p in confusions:
    print(f"  cue {i}: text says {n}, voice says {p}", file=sys.stderr)

cents = centroids()
result = []
for i, c in enumerate(cues):
    ranked = rank(emb[i], cents) if i in emb else []
    result.append({
        "i": i,
        "start": c["start_time"],
        "dur": round(c["end_time"] - c["start_time"], 2),
        "text": c["normalized_source_text"],
        "anchor": truth.get(i),
        "voice": ranked[0][1] if ranked else None,
        "score": round(ranked[0][0], 3) if ranked else None,
        "margin": round(ranked[0][0] - ranked[1][0], 3) if len(ranked) > 1 else None,
        "second": ranked[1][1] if len(ranked) > 1 else None,
    })
json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=1)
