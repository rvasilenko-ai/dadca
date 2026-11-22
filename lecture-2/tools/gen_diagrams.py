"""Generate the Lecture 2 harness / loop / attack-surface SVG diagrams.

Self-contained SVGs (white card, explicit colours) so they render in GitHub,
VS Code preview and any deck. Groups carry data-build="n" so a deck runtime
can reveal them step by step; statically everything is visible.
"""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

INK, INK2, LINE, RULE = "#1f2937", "#4b5563", "#9ca3af", "#cbd5e1"
SURF, SURF2, FRAME = "#ffffff", "#f1f5f9", "#f8fafc"
ACC, ACC_WASH, ACC_INK = "#0284c7", "#e0f2fe", "#075985"
BAD, BAD_WASH, BAD_INK = "#dc2626", "#fee2e2", "#991b1b"
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

def head(w, h, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}" font-family="{FONT}">
<title>{title}</title>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{INK2}"/></marker>
  <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{BAD}"/></marker>
</defs>
<rect x="0" y="0" width="{w}" height="{h}" fill="{SURF}"/>
'''

def text(x, y, s, size=24, weight=400, fill=INK, anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" dominant-baseline="central"{st}>{s}</text>\n'

def tile(x, y, w, h, title, subs, bad=False, title_size=25, sub_size=20):
    stroke, fill = (BAD, BAD_WASH) if bad else (RULE, SURF)
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="{4 if bad else 2.5}"/>\n'
    s += text(x + 20, y + 32, title, title_size, 700, INK)
    for i, sub in enumerate(subs):
        s += text(x + 20, y + 62 + i * 26, sub, sub_size, 500 if bad else 400, BAD_INK if bad else INK2)
    return s

def badge(cx, cy, n):
    return (f'<circle cx="{cx}" cy="{cy}" r="22" fill="{BAD}" stroke="{SURF}" stroke-width="3"/>\n'
            + text(cx, cy + 1, str(n), 24, 700, SURF, "middle"))

def edge(d, strong=False, arrow=False, red=False, dashed=False):
    stroke = BAD if red else (INK2 if strong else LINE)
    m = f' marker-end="url(#{"arrow-red" if red else "arrow"})"' if arrow else ""
    da = ' stroke-dasharray="12 9"' if dashed else ""
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{4 if (strong or red) else 3}" stroke-linecap="round"{m}{da}/>\n'

# ---------------------------------------------------------------- harness
def harness(attack: bool):
    W, H = 1800, 720
    title = ("The harness under attack: where the attacker reaches in" if attack
             else "The harness: everything around the model")
    s = head(W, H, title)
    # frame
    s += f'<g data-build="0">\n<rect x="300" y="20" width="1030" height="680" rx="26" fill="{FRAME}" stroke="{RULE}" stroke-width="2.5"/>\n'
    s += text(330, 56, "Harness", 28, 700, INK2)
    # model
    s += f'<rect x="700" y="300" width="260" height="130" rx="18" fill="{ACC_WASH}" stroke="{ACC}" stroke-width="4"/>\n'
    s += text(830, 346, "Model", 36, 700, ACC_INK, "middle")
    s += text(830, 392, "unchanged, still subverted" if attack else "chooses the next action", 20, 500 if attack else 400, ACC_INK, "middle")
    s += '</g>\n'
    # rows
    L, LW, R, RW, TH = 330, 330, 985, 320, 110
    rows = {1: 95, 2: 310, 3: 525}
    cy = {k: v + TH // 2 for k, v in rows.items()}
    # 1 objective
    s += '<g data-build="1">\n' + edge("M985 150L945 300")
    s += tile(R, rows[1], RW, TH, "Objective and instructions", ["the task and its rules"]) + '</g>\n'
    # 2 tools + tool servers
    s += '<g data-build="2">\n' + edge("M660 150L715 300") + edge("M260 150H328", arrow=True, red=attack)
    s += tile(L, rows[1], LW, TH, "Tools, skills, plugins", ["poisoned skill,", "injected tool description"] if attack else ["how it acts"], bad=attack)
    s += tile(40, rows[1], 220, TH, "Tool servers", ["compromised server,", "supply chain"] if attack else ["MCP, marketplaces"], bad=attack, title_size=24, sub_size=18)
    if attack: s += badge(L, rows[1], 1) + badge(40, rows[1], 4)
    s += '</g>\n'
    # 3 shell/network + environment
    s += '<g data-build="3">\n' + edge("M985 580L945 430")
    s += tile(R, rows[3], RW, TH, "Shell and network", ["where its actions land"])
    s += edge("M1330 255H1418", strong=True, arrow=True) + text(1374, 232, "actions", 22, 600, INK, "middle")
    s += edge("M1420 475H1332", strong=True, arrow=True) + text(1374, 500, "output", 22, 600, INK, "middle")
    s += f'<rect x="1420" y="250" width="360" height="230" rx="18" fill="none" stroke="{LINE}" stroke-width="3" stroke-dasharray="14 10"/>\n'
    s += text(1450, 290, "Environment", 28, 700, INK) + text(1450, 332, "files, systems, network:", 22) + text(1450, 362, "the target", 22)
    s += text(1600, 440, "real-world consequences", 22, 500, INK2, "middle", italic=True) + '</g>\n'
    # 4 retrieval + documents
    s += '<g data-build="4">\n' + edge("M660 365H698") + edge("M260 365H328", arrow=True, red=attack)
    s += tile(L, rows[2], LW, TH, "Retrieval", ["instructions planted", "in what it reads"] if attack else ["what it is fed: documents,", "mail, records, web pages"], bad=attack)
    s += tile(40, rows[2], 220, TH, "Documents", ["attacker-written", "content"] if attack else ["web, mail, CRM,", "tickets, files"], bad=attack, title_size=24, sub_size=18)
    if attack: s += badge(L, rows[2], 2)
    s += '</g>\n'
    # 5 memory
    s += '<g data-build="5">\n' + edge("M660 580L715 430")
    s += tile(L, rows[3], LW, TH, "Memory and context", ["malicious context persisted,", "replayed on a later task"] if attack else ["what persists between turns"], bad=attack)
    if attack: s += badge(L, rows[3], 3)
    s += '</g>\n'
    # 6 credentials
    s += '<g data-build="6">\n' + edge("M985 365H962")
    s += tile(R, rows[2], RW, TH, "Credentials and authority", ["confused or excessive", "delegated permissions"] if attack else ["whose identity it acts with"], bad=attack)
    if attack: s += badge(R, rows[2], 5)
    s += '</g>\n'
    if attack:
        # attacker, outside everything, never touching the model
        s += '<g data-build="7">\n'
        s += tile(40, 470, 220, 100, "Attacker", ["never talks", "to the model"], bad=True, title_size=24, sub_size=18)
        s += edge("M150 468V422", red=True, arrow=True) + edge("M40 520H22V150H38", red=True, arrow=True)
        s += text(1065, 672, "red: a component the attacker can write to — every arrow ends in the model's context", 21, 500, BAD_INK, "middle")
        s += '</g>\n'
    return s + '</svg>\n'

# ---------------------------------------------------------------- loop
def loop():
    W, H = 1680, 640
    s = head(W, H, "The agent loop: a model, a harness, and a loop")
    # 0 model
    s += f'<g data-build="0">\n<rect x="390" y="110" width="360" height="190" rx="18" fill="{ACC_WASH}" stroke="{ACC}" stroke-width="4"/>\n'
    s += text(570, 180, "Model", 36, 700, ACC_INK, "middle") + text(570, 240, "chooses the next action", 24, 400, ACC_INK, "middle") + '</g>\n'
    # 1 objective
    s += '<g data-build="1">\n' + tile(0, 140, 270, 130, "Objective", ["the task it was given"], title_size=28, sub_size=22)
    s += edge("M270 205H380", arrow=True) + '</g>\n'
    # 2 action into environment
    s += '<g data-build="2">\n'
    s += f'<rect x="1110" y="70" width="570" height="530" rx="22" fill="none" stroke="{LINE}" stroke-width="3" stroke-dasharray="14 10"/>\n'
    s += text(1140, 110, "Environment", 28, 700, INK)
    s += tile(1150, 180, 490, 150, "Tools", ["shell, browser, code,", "any API it is given"], title_size=28, sub_size=22)
    s += tile(1150, 360, 490, 130, "The target", ["files, systems, network"], title_size=28, sub_size=22)
    s += edge("M750 205H1100", strong=True, arrow=True) + text(925, 170, "Action: a tool call", 26, 600, INK, "middle") + '</g>\n'
    # 3 observation into context
    s += '<g data-build="3">\n' + edge("M1110 500H760", strong=True, arrow=True) + text(935, 540, "Observation: the output", 26, 600, INK, "middle")
    s += f'<rect x="390" y="400" width="360" height="200" rx="18" fill="{SURF2}" stroke="{RULE}" stroke-width="2.5"/>\n'
    s += text(420, 436, "Context", 28, 700, INK)
    s += f'<rect x="420" y="476" width="300" height="20" rx="4" fill="{RULE}"/>\n'
    s += edge("M570 400V310", arrow=True) + '</g>\n'
    # 4 context grows
    s += '<g data-build="4">\n'
    for y, w in [(506, 300), (536, 300), (566, 140)]:
        s += f'<rect x="420" y="{y}" width="{w}" height="20" rx="4" fill="{RULE}"/>\n'
    s += text(575, 576, "grows every turn", 18, 400, INK2) + '</g>\n'
    # 5 stop
    s += '<g data-build="5">\n' + edge("M390 280L225 425", arrow=True)
    s += f'<circle cx="185" cy="465" r="34" fill="none" stroke="{INK}" stroke-width="4"/><circle cx="185" cy="465" r="20" fill="{INK}"/>\n'
    s += text(185, 535, "Stop when the objective is met", 22, 600, INK, "middle") + text(185, 565, "or the budget runs out", 22, 600, INK, "middle") + '</g>\n'
    return s + '</svg>\n'

(OUT / "harness.svg").write_text(harness(False))
(OUT / "harness-attack-surface.svg").write_text(harness(True))
(OUT / "agent-loop.svg").write_text(loop())
print("wrote", [p.name for p in OUT.glob("*.svg")])
