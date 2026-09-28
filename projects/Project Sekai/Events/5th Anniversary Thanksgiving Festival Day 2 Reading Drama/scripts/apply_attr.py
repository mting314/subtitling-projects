import json, sys
D = ""  # run from the project directory
S = "5th Anniversary Thanksgiving Festival Day 2 Reading Drama"
T = """0-1 DROP
2-5 An
6-9 Kanade
10-12 Ichika
13-14 Nene
15-16 Ichika
17-20 Rui
21 Nene
22-24 An
25-27 Rui
28-29 An
30-33 Nene
34-35 An
36-37 Kanade
38-40 Ichika
41-42 Kanade
43-45 Ichika
46-49 An
50 Ichika
51-52 Kanade
53-56 Rui
57-58 Kanade
59-60 Nene
61-63 An
64-68 Nene
69-71 Ichika
72-75 An
76-77 Kanade
78-79 Mizuki
80 Airi
81 Rui
82-83 An
84-86 Kanade
87-88 Airi
89 Nene
90-93 Mizuki
94-96 An
97-98 Airi
99 Ichika
100-102 Airi
103-132 Minori
133 Airi
134-135 Kanade
136 Nene
137 Mizuki
138 An
139-140 Rui
141-143 Mizuki
144 Kanade
145-146 Mizuki
147 Rui
148 Mizuki
149 Rui
150 Mizuki
151 Rui
152 Mizuki
153-160 Rui
161 Nene
162-163 Mizuki
164 Rui
165 Mizuki
166 Kanade
167-169 Rui
170 Nene
171-175 Rui
176-179 Mizuki
180-181 Rui
182-185 Mizuki
186-187 Rui
188-189 Mizuki
190-194 Rui
195-198 Mizuki
199-201 Kanade
202-203 Mizuki
204 Nene
205-206 Airi
207-209 Mizuki
210-213 An
214-217 Nene
218 Rui
219 Nene
220 Rui
221 Nene
222 Rui
223-226 An
227 Nene
228 Rui
229 An
230 Nene
231-241 An
242-244 Nene
245 Rui
246-259 Nene
260 Rui
261 An
262-264 Nene
265 An
266 Nene
267-269 An
270-271 Nene
272-273 An
274 Nene
275-276 Kanade
277 An
278 Mizuki
279-280 Kanade
281 Rui
282-283 Nene
284-286 Rui
287 Airi
288 Nene
289-290 Airi
291-294 An
295-298 Ichika
299 Airi
300-303 Mizuki
304 Kanade
305 Mizuki
306 Rui
307 Mizuki
308 Kanade
309 Rui
310 Kanade
311-312 Ichika
313 Rui
314-317 Kanade
318-321 Ichika
322-324 Kanade
325 Airi
326 An
327 Rui
328-329 Mizuki
330 Kanade
331-332 Mizuki
333 Rui
334 Kanade
335-338 Airi
339 Nene
340-341 Mizuki
342 Airi
343 Rui
344 Airi
345-346 Rui
347 Airi
348 Rui
349-351 Airi
352 Rui
353 Airi
354 Rui
355 Airi
356 Mizuki
357 Rui
358-359 Airi
360-361 Mizuki
362-369 Airi
370 Rui
371-374 Airi
375-376 Mizuki
377 Airi
378-379 Kanade
380-381 Airi
382 Rui
383-384 Airi
385 Rui
386 Mizuki
387-388 Airi
389 Rui
390-391 Airi
392 DROP
393 Rui
394 Ichika
395 An
396-398 Airi
399-400 Mizuki
401-403 Kanade
404-405 Ichika
406-407 An
408 Nene
409-410 Rui
411 DROP"""
attr = {}
for line in T.splitlines():
    rng, who = line.split()
    a, _, b = rng.partition("-")
    for i in range(int(a), int(b or a) + 1):
        assert i not in attr, i
        attr[i] = who
path = D + S + "_formatted.json"
doc = json.load(open(path, encoding="utf-8"))
cues = doc["cues"]
assert sorted(attr) == list(range(len(cues))), (len(cues), len(attr))
out = []
for i, c in enumerate(cues):
    who = attr[i]
    if who == "DROP":
        print("drop", i, c["start_time"], c["normalized_source_text"])
        continue
    c["speaker"] = who
    for w in c["words"]:
        w["speaker"] = who
    out.append(c)
VS = {"RIN": "Rin", "LUKA": "Luka", "KAITO": "KAITO", "RIN, LUKA & KAITO": "Rin, Luka & KAITO"}
for v in json.load(open(D + "virtual_singer_scenes_ja.json", encoding="utf-8")):
    who = VS[v["speaker"]]
    out.append({"start_time": v["start"], "end_time": v["end"], "speaker": who, "role": None, "corner": None,
                "words": [], "replacement_spans": [], "id": "", "source_text": v["text"],
                "normalized_source_text": v["text"], "translated_text": None, "final_text": None})
out.sort(key=lambda c: c["start_time"])
for n, c in enumerate(out, 1):
    c["id"] = f"cue-{n:08d}"
doc["cues"] = out
sys.path.insert(0, "/Users/michaelting/github/autosub")
from autosub.core.schemas import SubtitleDocument
SubtitleDocument.model_validate(doc)
json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
from collections import Counter
print(len(out), Counter(c["speaker"] for c in out))
