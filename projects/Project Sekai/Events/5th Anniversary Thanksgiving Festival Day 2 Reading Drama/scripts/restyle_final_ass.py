"""Apply the AfterTalk character styles to the postprocessed .ass, in place.

Postprocess renders plain Arial per-speaker styles, so re-run this after every
postprocess. It also strips the translate stage's manual \\N breaks (sized for
54px Arial, they leave 3-line stubs at 100px) and top-aligns Virtual Singer
cues so they clear the in-game text box.

Usage: restyle_final_ass.py FINAL.ass
"""

import re
import sys

COLORS = {
    "Ichika": "#33aaee", "Minori": "#ffccaa", "Airi": "#ffaacc", "An": "#00bbdd",
    "Nene": "#33dd99", "Rui": "#bb88ee", "Kanade": "#bb6688", "Mizuki": "#ddaacc",
    "Rin": "#ffcc11", "Luka": "#ffbbcc", "KAITO": "#3366cc", "Virtual Singers": "#000000",
}
TOP = {"Rin", "Luka", "KAITO", "Virtual Singers"}


def bgr(h: str) -> str:
    h = h.lstrip("#")
    return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}".upper()


path = sys.argv[1]
out = []
for ln in open(path, encoding="utf-8").read().split("\n"):
    if m := re.match(r"Style: ([^,]+),", ln):
        name = m.group(1)
        ln = (f"Style: {name},Lato ExtraBold,100,&H00FFFFFF,&H000000FF,{bgr(COLORS[name])},&H00000000,"
              "0,0,0,0,100,100,0,0,1,4,1.33,2,200,200,100,1")
    elif ln.startswith("Dialogue:"):
        f = ln.split(",", 9)
        text = re.sub(r"\s*\\N\s*", " ", f[9])
        if f[3] in TOP and not text.startswith(r"{\an8}"):
            text = r"{\an8}" + text
        f[9] = text
        ln = ",".join(f)
    out.append(ln)
open(path, "w", encoding="utf-8").write("\n".join(out))
