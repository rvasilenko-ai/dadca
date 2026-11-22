"""Generate the Lecture 2 diagrams: the attack map, the harness (plain, attack, guardrail) and the loop.

The SVGs carry no colour literals on their shapes: every element has a class, and a <style> block at
the top maps the classes to CSS variables with light values and a prefers-color-scheme dark block, so
the files theme themselves when viewed on their own (GitHub, an editor preview). The deck build strips
that <style> when it inlines a diagram and styles the same classes from its own tokens, so the deck's
theme toggle recolours the diagrams too. No background rectangle: the diagram sits on the page.

Groups carry data-build="n" so a deck runtime can reveal them step by step.
"""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"

STYLE = """<style>
svg{--surface:#ffffff;--frame:#f8fafc;--ink:#1f2937;--ink-2:#4b5563;--line:#9ca3af;--rule:#cbd5e1;
--acc:#0284c7;--acc-wash:#e0f2fe;--acc-ink:#075985;--bad:#dc2626;--bad-wash:#fee2e2;--bad-ink:#991b1b;
--good:#15803d;--good-wash:#dcfce7;--good-ink:#14532d;--on-badge:#ffffff}
@media (prefers-color-scheme: dark){svg{--surface:#141a2a;--frame:#10172a;--ink:#eef1f8;--ink-2:#c6cddd;--line:#8b96b0;--rule:#344062;
--acc:#7cc4ff;--acc-wash:#10304a;--acc-ink:#bfe3ff;--bad:#f87171;--bad-wash:#3b1515;--bad-ink:#fecaca;
--good:#4ade80;--good-wash:#0f2e1c;--good-ink:#bbf7d0;--on-badge:#0b0f1a}}
.node{fill:var(--surface);stroke:var(--rule);stroke-width:2.5}.node--model{fill:var(--acc-wash);stroke:var(--acc);stroke-width:4}
.node--bad{fill:var(--bad-wash);stroke:var(--bad);stroke-width:4}.node--good{fill:var(--good-wash);stroke:var(--good);stroke-width:4}
.frame{fill:var(--frame);stroke:var(--rule);stroke-width:2.5}.env{fill:none;stroke:var(--line);stroke-width:3;stroke-dasharray:14 10}
.t{fill:var(--ink)}.t2{fill:var(--ink-2)}.t-acc{fill:var(--acc-ink)}.t-bad{fill:var(--bad-ink)}.t-good{fill:var(--good-ink)}.t-badge{fill:var(--on-badge)}
.edge{fill:none;stroke:var(--line);stroke-width:3;stroke-linecap:round}.edge--strong{stroke:var(--ink-2);stroke-width:4}
.edge--bad{stroke:var(--bad);stroke-width:4}.edge--good{stroke:var(--good);stroke-width:4}
.arrow{fill:var(--ink-2)}.arrow--bad{fill:var(--bad)}.arrow--good{fill:var(--good)}
.badge--bad{fill:var(--bad);stroke:var(--surface);stroke-width:3}.badge--good{fill:var(--good);stroke:var(--surface);stroke-width:3}
.ctx-bar{fill:var(--rule)}.ring{fill:none;stroke:var(--ink);stroke-width:4}.dot{fill:var(--ink)}
</style>"""


def head(w, h, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}" font-family="{FONT}">
<title>{title}</title>
{STYLE}
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arrow"/></marker>
  <marker id="arrow-bad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arrow arrow--bad"/></marker>
  <marker id="arrow-good" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="arrow arrow--good"/></marker>
</defs>
'''

def text(x, y, s, size=24, weight=400, cls="t", anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="central"{st}>{s}</text>\n'

def tile(x, y, w, h, title, subs, bad=False, good=False, title_size=25, sub_size=20, model=False):
    cls = "node node--bad" if bad else ("node node--good" if good else ("node node--model" if model else "node"))
    sub_cls = "t-bad" if bad else ("t-good" if good else ("t-acc" if model else "t2"))
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="{cls}"/>\n'
    s += text(x + 20, y + 32, title, title_size, 700, "t-acc" if model else "t")
    for i, sub in enumerate(subs):
        s += text(x + 20, y + 62 + i * 26, sub, sub_size, 500 if (bad or good) else 400, sub_cls)
    return s

def badge(cx, cy, n, good=False):
    return (f'<circle cx="{cx}" cy="{cy}" r="22" class="{"badge--good" if good else "badge--bad"}"/>\n'
            + text(cx, cy + 1, str(n), 24, 700, "t-badge", "middle"))

def edge(d, strong=False, arrow=False, red=False, green=False):
    cls = "edge edge--bad" if red else ("edge edge--good" if green else ("edge edge--strong" if strong else "edge"))
    mk = "arrow-bad" if red else ("arrow-good" if green else "arrow")
    m = f' marker-end="url(#{mk})"' if arrow else ""
    return f'<path d="{d}" class="{cls}"{m}/>\n'


# ---------------------------------------------------------------- harness
def harness(mode: str):
    attack, guard = mode == "attack", mode == "guard"
    W, H = 1800, 700
    title = {"plain": "The harness: everything around the model",
             "attack": "The harness under attack: where the attacker reaches in",
             "guard": "Guardrails: a control at every point the attacker can write to"}[mode]
    s = head(W, H, title)
    s += '<g data-build="0">\n<rect x="300" y="10" width="1030" height="680" rx="26" class="frame"/>\n'
    s += text(330, 46, "Harness", 28, 700, "t2")
    s += '<rect x="700" y="290" width="260" height="130" rx="18" class="node node--model"/>\n'
    sub = {"plain": "chooses the next action", "attack": "unchanged, still subverted", "guard": "still untrusted by design"}[mode]
    s += text(830, 336, "Model", 36, 700, "t-acc", "middle")
    s += text(830, 382, sub, 20, 400 if mode == "plain" else 500, "t-acc", "middle")
    s += '</g>\n'
    L, LW, R, RW, TH = 330, 330, 985, 320, 110
    rows = {1: 85, 2: 300, 3: 515}
    def subs(plain, atk, grd): return grd if guard else (atk if attack else plain)
    hi = dict(bad=attack, good=guard)
    s += '<g data-build="1">\n' + edge("M985 140L945 290")
    s += tile(R, rows[1], RW, TH, "Objective and instructions", ["the task and its rules"]) + '</g>\n'
    s += '<g data-build="2">\n' + edge("M660 140L715 290") + edge("M260 140H328", arrow=True, red=attack, green=guard)
    s += tile(L, rows[1], LW, TH, "Tools, skills, plugins",
              subs(["how it acts; its config and hooks"], ["poisoned skill or hook,", "injected tool description"],
                   ["allowlist, least privilege,", "approval for consequential acts"]), **hi)
    s += tile(40, rows[1], 220, TH, "Tool servers",
              subs(["MCP, marketplaces"], ["compromised server,", "supply chain"], ["pinned, signed,", "reviewed like code"]),
              title_size=24, sub_size=18, **hi)
    if attack: s += badge(L, rows[1], 1) + badge(40, rows[1], 4)
    if guard: s += badge(L, rows[1], 1, True) + badge(40, rows[1], 4, True)
    s += '</g>\n'
    s += '<g data-build="3">\n' + edge("M985 570L945 420")
    s += tile(R, rows[3], RW, TH, "Shell and network", ["where its actions land"])
    s += edge("M1330 245H1418", strong=not guard, arrow=True, green=guard)
    s += text(1600, 205, "actions — egress: trusted destinations only", 19, 600, "t-good", "middle") if guard else text(1374, 222, "actions", 22, 600, "t", "middle")
    s += edge("M1420 465H1332", strong=True, arrow=True) + text(1374, 490, "output", 22, 600, "t", "middle")
    s += '<rect x="1420" y="240" width="360" height="230" rx="18" class="env"/>\n'
    s += text(1450, 280, "Environment", 28, 700, "t") + text(1450, 322, "files, systems, network:", 22, 400, "t") + text(1450, 352, "the target", 22, 400, "t")
    s += text(1600, 430, "real-world consequences", 22, 500, "t2", "middle", italic=True) + '</g>\n'
    s += '<g data-build="4">\n' + edge("M660 355H698") + edge("M260 355H328", arrow=True, red=attack, green=guard)
    s += tile(L, rows[2], LW, TH, "Retrieval",
              subs(["what it is fed: documents,", "mail, records, web pages"], ["instructions planted", "in what it reads"],
                   ["untrusted text labelled,", "quarantined from authority"]), **hi)
    s += tile(40, rows[2], 220, TH, "Documents",
              subs(["web, mail, CRM,", "tickets, files"], ["attacker-written", "content"], ["provenance kept;", "treated as data"]),
              title_size=24, sub_size=18, **hi)
    if attack: s += badge(L, rows[2], 2)
    if guard: s += badge(L, rows[2], 2, True)
    s += '</g>\n'
    s += '<g data-build="5">\n' + edge("M660 570L715 420")
    s += tile(L, rows[3], LW, TH, "Memory and context",
              subs(["what persists between turns"], ["malicious context persisted,", "replayed on a later task"],
                   ["provenance travels with it;", "nothing imperative persists"]), **hi)
    if attack: s += badge(L, rows[3], 3)
    if guard: s += badge(L, rows[3], 3, True)
    s += '</g>\n'
    s += '<g data-build="6">\n' + edge("M985 355H962")
    s += tile(R, rows[2], RW, TH, "Credentials and authority",
              subs(["whose identity it acts with"], ["confused or excessive", "delegated permissions"],
                   ["per-agent identity, short-lived,", "never more than the user"]), **hi)
    if attack: s += badge(R, rows[2], 5)
    if guard: s += badge(R, rows[2], 5, True)
    s += '</g>\n'
    if attack:
        s += '<g data-build="7">\n'
        s += tile(40, 460, 220, 100, "Attacker", ["never talks", "to the model"], bad=True, title_size=24, sub_size=18)
        s += edge("M150 458V412", red=True, arrow=True) + edge("M40 510H22V140H38", red=True, arrow=True)
        s += text(1065, 662, "red: a component the attacker can write to — every arrow ends in the model's context", 21, 500, "t-bad", "middle")
        s += '</g>\n'
    if guard:
        s += '<g data-build="7">\n'
        s += badge(1374, 245, "E", True)
        s += badge(830, 252, "M", True) + text(830, 46, "M — every transition logged and classified", 22, 600, "t-good", "middle")
        s += tile(40, 460, 220, 100, "Attacker", ["still writes here;", "reaches no authority"], good=True, title_size=24, sub_size=18)
        s += text(1065, 662, "green: the control at each red point of the previous view — structure first, classifiers second", 21, 500, "t-good", "middle")
        s += '</g>\n'
    return s + '</svg>\n'


# ---------------------------------------------------------------- loop
def loop():
    W, H = 1680, 620
    s = head(W, H, "The agent loop: a model, a harness, and a loop")
    s += '<g data-build="0">\n<rect x="390" y="100" width="360" height="190" rx="18" class="node node--model"/>\n'
    s += text(570, 170, "Model", 36, 700, "t-acc", "middle") + text(570, 230, "chooses the next action", 24, 400, "t-acc", "middle") + '</g>\n'
    s += '<g data-build="1">\n' + tile(0, 130, 270, 130, "Objective", ["the task it was given"], title_size=28, sub_size=22)
    s += edge("M270 195H380", arrow=True) + '</g>\n'
    s += '<g data-build="2">\n<rect x="1110" y="60" width="570" height="530" rx="22" class="env"/>\n'
    s += text(1140, 100, "Environment", 28, 700, "t")
    s += tile(1150, 170, 490, 150, "Tools", ["shell, browser, code,", "any API it is given"], title_size=28, sub_size=22)
    s += tile(1150, 350, 490, 130, "The target", ["files, systems, network"], title_size=28, sub_size=22)
    s += edge("M750 195H1100", strong=True, arrow=True) + text(925, 160, "Action: a tool call", 26, 600, "t", "middle") + '</g>\n'
    s += '<g data-build="3">\n' + edge("M1110 490H760", strong=True, arrow=True) + text(935, 530, "Observation: the output", 26, 600, "t", "middle")
    s += '<rect x="390" y="390" width="360" height="200" rx="18" class="node"/>\n'
    s += text(420, 426, "Context", 28, 700, "t")
    s += '<rect x="420" y="466" width="300" height="20" rx="4" class="ctx-bar"/>\n'
    s += edge("M570 390V300", arrow=True) + '</g>\n'
    s += '<g data-build="4">\n'
    for y, w in [(496, 300), (526, 300), (556, 140)]:
        s += f'<rect x="420" y="{y}" width="{w}" height="20" rx="4" class="ctx-bar"/>\n'
    s += text(575, 566, "grows every turn", 18, 400, "t2") + '</g>\n'
    s += '<g data-build="5">\n' + edge("M390 270L225 415", arrow=True)
    s += '<circle cx="185" cy="455" r="34" class="ring"/><circle cx="185" cy="455" r="20" class="dot"/>\n'
    s += text(185, 525, "Stop when the objective is met", 22, 600, "t", "middle") + text(185, 555, "or the budget runs out", 22, 600, "t", "middle") + '</g>\n'
    return s + '</svg>\n'


# ---------------------------------------------------------------- the attack map (slide 2)
def attack_map():
    W, H = 1800, 600
    s = head(W, H, "Where the classic attacks enter a learned model: poisoning and evasion write into the pipeline, extraction and inference read its answers")
    s += '<g data-build="0">\n'
    for x, title, sub, model in [(80, "training data", "what it learns from", False), (520, "TRAINING", "fits the function", False),
                                 (960, "MODEL", "the learned function", True), (1400, "predictions", "its answers", False)]:
        s += f'<rect x="{x}" y="240" width="300" height="110" rx="{18 if model else 14}" class="{"node node--model" if model else "node"}"/>\n'
        s += text(x + 150, 280, title, 30 if model else 28, 700, "t-acc" if model else "t", "middle")
        s += text(x + 150, 318, sub, 20, 400, "t-acc" if model else "t2", "middle")
    for x1, x2 in [(380, 518), (820, 958), (1260, 1398)]:
        s += edge(f"M{x1} 295H{x2}", strong=True, arrow=True)
    s += '</g>\n'
    TH = 136
    s += '<g data-build="1">\n' + text(80, 24, "ATTACKER WRITES: into the data it learns from, or into the input it reads", 20, 600, "t-bad")
    s += tile(960, 44, 340, TH, "Evasion", ["perturb the input", "2004 → 2014", "malware detectors 2013 → 2018"], bad=True, title_size=26, sub_size=19)
    s += edge("M1130 180V236", red=True, arrow=True) + '</g>\n'
    s += '<g data-build="2">\n' + text(80, 578, "ATTACKER READS: what the model answers, and learns the model or its data from it", 20, 600, "t-bad")
    s += tile(1040, 420, 340, TH, "Extraction", ["copy the model from its answers", "2005 → 2016"], bad=True, title_size=26, sub_size=19)
    s += edge("M1500 350L1240 416", red=True, arrow=True) + '</g>\n'
    s += '<g data-build="3">\n' + tile(80, 44, 340, TH, "Poisoning, backdoors", ["corrupt what it learns", "2008 → 2017"], bad=True, title_size=26, sub_size=19)
    s += edge("M250 180V236", red=True, arrow=True) + '</g>\n'
    s += '<g data-build="4">\n' + tile(1420, 420, 340, TH, "Inference, inversion", ["learn the training data", "from its answers · 2014 → 2017"], bad=True, title_size=26, sub_size=19)
    s += edge("M1600 350V416", red=True, arrow=True) + '</g>\n'
    return s + '</svg>\n'


(OUT / "attack-map.svg").write_text(attack_map())
(OUT / "harness.svg").write_text(harness("plain"))
(OUT / "harness-attack-surface.svg").write_text(harness("attack"))
(OUT / "harness-guardrails.svg").write_text(harness("guard"))
(OUT / "agent-loop.svg").write_text(loop())
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
