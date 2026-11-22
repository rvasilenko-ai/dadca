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
    # pathLength="1" + class draw: a deck can animate stroke-dashoffset from 1 to 0 so the edge draws itself
    return f'<path d="{d}" class="{cls} draw" pathLength="1"{m}/>\n'


# ---------------------------------------------------------------- harness
def harness(mode: str):
    """Three views on one geometry. Build order follows each slide's captions: the plain view adds the harness
    piece by piece; the attack and guardrail views show the untouched harness at step 0, then the numbered
    components in badge order (1 tools, 2 retrieval, 3 memory, 4 tool servers, 5 credentials), then the
    attacker (attack) or egress and monitor (guard)."""
    attack, guard = mode == "attack", mode == "guard"
    W, H = 1800, 700
    title = {"plain": "The harness: everything around the model",
             "attack": "The harness under attack: where the attacker reaches in",
             "guard": "Guardrails: a control at every point the attacker can write to"}[mode]
    if mode == "plain":
        b = dict(objective=1, tools=2, servers=2, env=3, actions=3, retrieval=4, docs=4, memory=5, creds=6, extra=7)
    elif attack:
        b = dict(objective=0, tools=1, servers=4, env=0, actions=0, retrieval=2, docs=2, memory=3, creds=5, extra=6)
    else:
        b = dict(objective=0, tools=1, servers=4, env=0, actions=6, retrieval=2, docs=2, memory=3, creds=5, extra=7)
    def g(key, body): return f'<g data-build="{b[key]}">\n{body}</g>\n'
    s = head(W, H, title)
    s += '<g data-build="0">\n<rect x="300" y="10" width="1050" height="680" rx="26" class="frame"/>\n'
    s += text(330, 46, "Harness", 28, 700, "t2")
    s += '<rect x="700" y="290" width="260" height="130" rx="18" class="node node--model"/>\n'
    sub = {"plain": "chooses the next action", "attack": "unchanged, still subverted", "guard": "still untrusted by design"}[mode]
    s += text(830, 336, "Model", 36, 700, "t-acc", "middle")
    s += text(830, 382, sub, 20, 400 if mode == "plain" else 500, "t-acc", "middle")
    s += '</g>\n'
    L, LW, R, RW, TH = 330, 330, 985, 340, 110
    legend_x = 825  # centre of the frame, so the legend line stays inside it
    rows = {1: 85, 2: 300, 3: 515}
    def subs(plain, atk, grd): return grd if guard else (atk if attack else plain)
    hi = dict(bad=attack, good=guard)
    s += g("objective", edge("M985 140L945 290") + tile(R, rows[1], RW, TH, "Objective and instructions", ["the task and its rules"], title_size=22))
    body = edge("M660 140L715 290") + tile(L, rows[1], LW, TH, "Tools, skills, plugins",
              subs(["how it acts; its config and hooks"], ["poisoned skill or hook,", "injected tool description"],
                   ["allowlist, least privilege,", "approval for consequential acts"]), **hi)
    if attack: body += badge(L, rows[1], 1)
    if guard: body += badge(L, rows[1], 1, True)
    s += g("tools", body)
    body = edge("M260 140H328", arrow=True, red=attack, green=guard) + tile(40, rows[1], 220, TH, "Tool servers",
              subs(["MCP, marketplaces"], ["compromised server,", "supply chain"], ["pinned, signed,", "reviewed like code"]),
              title_size=24, sub_size=18, **hi)
    if attack: body += badge(40, rows[1], 4)
    if guard: body += badge(40, rows[1], 4, True)
    s += g("servers", body)
    body = edge("M985 570L945 420") + tile(R, rows[3], RW, TH, "Shell and network", ["where its actions land"])
    body += edge("M1440 465H1352", strong=True, arrow=True) + text(1394, 490, "output", 22, 600, "t", "middle")
    body += '<rect x="1440" y="240" width="340" height="230" rx="18" class="env"/>\n'
    body += text(1470, 280, "Environment", 28, 700, "t") + text(1470, 322, "files, systems, network:", 22, 400, "t") + text(1470, 352, "the target", 22, 400, "t")
    body += text(1610, 430, "real-world consequences", 22, 500, "t2", "middle", italic=True)
    s += g("env", body)
    body = edge("M1350 245H1438", strong=not guard, arrow=True, green=guard)
    body += text(1590, 205, "actions — egress: trusted destinations only", 19, 600, "t-good", "middle") if guard else text(1394, 222, "actions", 22, 600, "t", "middle")
    if guard: body += badge(1394, 245, "E", True)
    s += g("actions", body)
    body = edge("M660 355H698") + tile(L, rows[2], LW, TH, "Retrieval",
              subs(["what it is fed: documents,", "mail, records, web pages"], ["instructions planted", "in what it reads"],
                   ["untrusted text labelled,", "quarantined from authority"]), **hi)
    if attack: body += badge(L, rows[2], 2)
    if guard: body += badge(L, rows[2], 2, True)
    s += g("retrieval", body)
    s += g("docs", edge("M260 355H328", arrow=True, red=attack, green=guard) + tile(40, rows[2], 220, TH, "Documents",
              subs(["web, mail, CRM,", "tickets, files"], ["attacker-written", "content"], ["provenance kept;", "treated as data"]),
              title_size=24, sub_size=18, **hi))
    body = edge("M660 570L715 420") + tile(L, rows[3], LW, TH, "Memory and context",
              subs(["what persists between turns"], ["malicious context persisted,", "replayed on a later task"],
                   ["provenance travels with it;", "nothing imperative persists"]), **hi)
    if attack: body += badge(L, rows[3], 3)
    if guard: body += badge(L, rows[3], 3, True)
    s += g("memory", body)
    body = edge("M985 355H962") + tile(R, rows[2], RW, TH, "Credentials and authority",
              subs(["whose identity it acts with"], ["confused or excessive", "delegated permissions"],
                   ["per-agent identity, short-lived,", "never more than the user"]), title_size=22, **hi)
    if attack: body += badge(R, rows[2], 5)
    if guard: body += badge(R, rows[2], 5, True)
    s += g("creds", body)
    if attack:
        body = tile(40, 460, 220, 100, "Attacker", ["never talks", "to the model"], bad=True, title_size=24, sub_size=18)
        body += edge("M150 458V412", red=True, arrow=True) + edge("M40 510H22V140H38", red=True, arrow=True)
        body += text(legend_x, 662, "red: a component the attacker can write to — every arrow ends in the model's context", 21, 500, "t-bad", "middle")
        s += g("extra", body)
    if guard:
        body = badge(830, 252, "M", True) + text(830, 46, "M — every transition logged and classified", 22, 600, "t-good", "middle")
        body += tile(40, 460, 220, 100, "Attacker", ["still writes here;", "reaches no authority"], good=True, title_size=24, sub_size=18)
        body += text(legend_x, 662, "green: the control at each red point of the previous view — structure first, classifiers second", 21, 500, "t-good", "middle")
        s += g("extra", body)
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


def arrow(x1, y1, x2, y2, red=False, green=False, strong=True):
    return edge(f"M{x1} {y1}L{x2} {y2}", strong=strong, arrow=True, red=red, green=green)


def ladder():
    """Case A rungs of autonomy, bottom (assistant) to top (the attacker's agent on stolen model capacity).
    build 0 draws the axis; builds 1-5 reveal the rungs bottom-up, matching the slide's captions."""
    W, H = 1800, 600
    s = head(W, H, "Case A is a ladder of autonomy: each rung hands the model more of the loop, from assistant up to the attacker's agent running on stolen model capacity")
    rungs = [
        ("the model as assistant", "a commercial model for reconnaissance, lures, translating loot"),
        ("the model inside an implant", "NIK C2 relays prompts to a model; VOLTA asks it to rank the loot"),
        ("the agent runs the campaign", "~80–90% of a thirty-target intrusion; the human sets objectives"),
        ("the agent runs alone", "exploit_agent: diff the patch, write the exploit, fire it — no human"),
        ("the agent on your bill", "LLMjacking: stolen cloud model credentials run the attacker's agent"),
    ]
    s += '<g data-build="0">\n' + text(40, 40, "MORE AUTONOMY", 20, 700, "t2") + edge("M150 70V560", strong=True) + '</g>\n'
    for i, (t, sub) in enumerate(rungs):
        y = 480 - i * 108
        bad = i >= 3
        body = text(100, y + 46, str(i + 1), 44, 800, "t-bad" if bad else "t-acc", "middle")
        body += tile(180, y, 1580, 92, t, [sub], bad=bad, title_size=27, sub_size=22)
        s += f'<g data-build="{i + 1}">\n{body}</g>\n'
    return s + '</svg>\n'


def supply_chain():
    """The software supply chain across the top; below it, the inputs an agent reads as instructions at run time."""
    W, H = 1800, 330
    s = head(W, H, "The software supply chain, plus every input an agent will later read as instructions at run time")
    s += '<g data-build="0">\n' + text(40, 28, "SOFTWARE SUPPLY CHAIN", 20, 700, "t2")
    xs = [40, 388, 736, 1084, 1432]
    for k, (x, name) in enumerate(zip(xs, ["source", "dependencies", "build", "artifact", "deployment"])):
        s += tile(x, 50, 300, 72, name, ["​"], title_size=25, sub_size=1)
        if k < 4:
            s += arrow(x + 300, 86, x + 386, 86)
    s += '</g>\n'
    s += '<g data-build="1">\n' + text(40, 172, "WHAT THE AGENT ALSO READS — and may treat as instructions", 20, 700, "t-bad")
    s += edge("M900 192V124", red=True, arrow=True)
    items = [("Repository", "instructions, Markdown"), ("Issues, comments,", "retrieved documents"),
             ("Skills, plugins,", "tool descriptions"), ("Model and policy", "configuration"),
             ("Memory,", "retrieved context"), ("Credentials,", "delegated permissions"), ("Approval UIs,", "generated diffs")]
    for i, (a, b) in enumerate(items):
        s += tile(40 + i * 250, 202, 244, 102, a, [b], bad=True, title_size=20, sub_size=18)
    return s + '</g>\n</svg>\n'


def funnel():
    """Match the model to the scale, for both cases: two telemetry inputs feed one funnel of three tiers."""
    W, H = 1800, 516
    s = head(W, H, "Match the model to the scale, for both cases. Two inputs — Case A's endpoint, identity and flow events, and "
                   "Case B's agent transitions — feed one funnel: encoder-only classifiers at machine scale, small task-trained "
                   "language models at triage, a frontier model and a human for the few investigations")
    s += '<g data-build="0">\n'
    s += tile(100, 10, 780, 96, "Case A telemetry", ["endpoint, identity and flow events — hosts, tokens, API calls, connections"], title_size=23, sub_size=19)
    s += tile(920, 10, 780, 96, "Case B telemetry", ["agent transitions — retrieved texts, tool calls, arguments, destinations"], title_size=23, sub_size=19)
    s += edge("M490 106V136", strong=True, arrow=True) + edge("M1310 106V136", strong=True, arrow=True) + '</g>\n'
    bands = [
        (100, 1600, "machine scale — millions of events, flows, tool calls, retrieved texts",
         "encoder-only classifiers (BERT family): fine-tuned on telemetry, line rate, a label — not a sentence", False),
        (350, 1100, "triage — thousands of candidates", "small language models, 1–8B, trained for the task: summarize, correlate, propose", False),
        (600, 600, "investigation — a few cases", "a frontier model — and a human", True),
    ]
    y = 140
    for i, (x, w, t, sub, model) in enumerate(bands):
        body = edge(f"M900 {y - 30}V{y - 4}", strong=True, arrow=True) if i > 0 else ""
        body += tile(x, y, w, 100, t, [sub], model=model, title_size=25, sub_size=19)
        s += f'<g data-build="{i + 1}">\n{body}</g>\n'
        y += 130
    return s + '</svg>\n'


def chain_v(aria, steps, tw=1240, th=64, gap=26, size=23):
    """A vertical sequence of tiles joined by down-arrows; steps = [(text, bad)], revealed one per build."""
    n = len(steps)
    W, H = 1800, 20 + n * th + (n - 1) * gap + 20
    x = (W - tw) // 2
    s = head(W, H, aria)
    y = 20
    for i, (t, bad) in enumerate(steps):
        body = ""
        if i > 0:
            body += edge(f"M{W // 2} {y - gap}V{y - 2}", strong=True, arrow=True)
        body += tile(x, y, tw, th, t, [], bad=bad, title_size=size, sub_size=1)
        s += f'<g data-build="{i}">\n{body}</g>\n'
        y += th + gap
    return s + "</svg>\n"


# ---------------------------------------------------------------- zoned chains
# Steps sit inside labelled zones (frames); an arrow that crosses the gap between two zones is a
# boundary crossing and is drawn red. Tiles are 160 tall with a title and up to three sub lines.
ZTH = 160


def zframe(x, y, w, h, label, dashed=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" class="{"env" if dashed else "frame"}"/>\n'
            + text(x + 28, y + 36, label, 24, 700, "t2"))


def ztile(x, y, w, title, subs, bad=False, good=False):
    cls = "node node--bad" if bad else ("node node--good" if good else "node")
    sub_cls = "t-bad" if bad else ("t-good" if good else "t2")
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{ZTH}" rx="16" class="{cls}"/>\n'
    s += text(x + 26, y + 44, title, 24, 700, "t")
    for i, sub in enumerate(subs):
        s += text(x + 26, y + 82 + i * 28, sub, 20, 500 if (bad or good) else 400, sub_cls)
    return s


def zarrow(x1, y1, x2, y2, red=False):
    """Straight arrow; horizontal when y1 == y2, vertical when x1 == x2."""
    d = f"M{x1} {y1}H{x2}" if y1 == y2 else f"M{x1} {y1}V{y2}"
    return edge(d, strong=not red, arrow=True, red=red)


def forcedleak_path():
    # three columns (the Internet, the CRM, the organization) by three rows
    cx, tw = (24, 640, 1256), 520                  # tile x per column, tile width
    fx, fw = (0, 616, 1232), 568                   # frame x per column, frame width
    ry = (76, 288, 500)                            # tile y per row
    mid = [y + ZTH // 2 for y in ry]
    H = ry[2] + ZTH + 40
    s = head(1800, H, "ForcedLeak attack path across three zones: on the Internet the attacker fills a public Web-to-Lead form; "
                      "the concealed instructions persist in the Salesforce CRM record; inside the organization an employee later "
                      "asks the Agentforce agent about the lead, the agent retrieves the record, the injection fires and the agent "
                      "reaches more CRM data with its own authority, and sensitive data leaves through crafted image requests back "
                      "to the attacker")
    s += '<g data-build="0">\n' + zframe(fx[0], 12, fw, H - 28, "The Internet — the attacker", dashed=True)
    s += zframe(fx[1], 12, fw, ry[0] + ZTH + 24 - 12, "Salesforce CRM — the record")
    s += zframe(fx[2], 12, fw, H - 28, "The organization — Agentforce")
    s += text(fx[0] + fw // 2, mid[1], "red arrow: a trust boundary crossed", 20, 500, "t-bad", "middle")
    s += ztile(cx[0], ry[0], tw, "A public Web-to-Lead form", ["the attacker submits a lead;", "every field is attacker-written text"], bad=True) + '</g>\n'
    s += '<g data-build="1">\n' + zarrow(cx[0] + tw, mid[0], cx[1] - 4, mid[0], red=True)
    s += ztile(cx[1], ry[0], tw, "Concealed instructions persist", ["stored in the CRM record,", "waiting to be read"], bad=True) + '</g>\n'
    s += '<g data-build="2">\n' + ztile(cx[2], ry[0], tw, "An employee asks about the lead", ["later, in the normal course of work:", "a legitimate request, a legitimate identity"]) + '</g>\n'
    # retrieval: the record crosses from the CRM into the agent's context
    gap = (fx[1] + fw + fx[2]) // 2
    s += '<g data-build="3">\n' + zarrow(cx[2] + tw // 2, ry[0] + ZTH, cx[2] + tw // 2, ry[1] - 4)
    s += edge(f"M{cx[1] + tw} {mid[0]}H{gap}V{mid[1]}H{cx[2] - 4}", arrow=True, red=True)
    s += ztile(cx[2], ry[1], tw, "The agent retrieves the record", ["attacker-written text enters", "the model's context"]) + '</g>\n'
    s += '<g data-build="4">\n' + zarrow(cx[2] + tw // 2, ry[1] + ZTH, cx[2] + tw // 2, ry[2] - 4, red=True)
    s += ztile(cx[2], ry[2], tw, "The injection fires", ["the record's text is read as instructions;", "the agent reaches more CRM data", "with the organization's own authority"], bad=True) + '</g>\n'
    # egress: back across both gaps, under the CRM zone, to the attacker
    s += '<g data-build="5">\n' + zarrow(cx[2], mid[2], cx[0] + tw + 4, mid[2], red=True)
    s += ztile(cx[0], ry[2], tw, "Sensitive data leaves", ["through crafted image requests", "to an attacker-controlled domain"], bad=True) + '</g>\n'
    return s + '</svg>\n'


def incident_chain():
    """The July 2026 Hugging Face intrusion: a U-shaped flow. Top row, left to right: OpenAI's evaluation
    environment, then the Internet. Bottom row, right to left: Hugging Face production."""
    cx, tw = (24, 456, 944, 1376), 400             # tile x per column, tile width
    y0, y1 = 76, 364                               # tile y, top and bottom rows
    H = y1 + ZTH + 24 + 60
    s = head(1800, H, "The reference incident across three zones. Top row, in OpenAI's evaluation environment: an isolated "
                      "evaluation, then a sandbox escape through a proxy zero-day; then on the Internet: root on a third-party "
                      "code-execution endpoint used as a launchpad, with exposed accounts on other services. Bottom row, inside "
                      "Hugging Face production, right to left: entry through crafted dataset configs, the Kubernetes cluster taken "
                      "to cluster-admin, expansion into the VPN mesh, cloud and source control, and detection that correlated the "
                      "signals but did not escalate until humans cut access. Red arrows mark the boundaries the agent crossed")
    s += '<g data-build="0">\n' + zframe(0, 12, 880, y0 + ZTH + 24 - 12, "OpenAI — the evaluation environment")
    s += zframe(920, 12, 880, y0 + ZTH + 24 - 12, "The Internet — a third-party sandbox", dashed=True)
    s += zframe(0, y1 - 64, 1800, ZTH + 64 + 24, "Hugging Face — production")
    s += text(28, H - 22, "red arrow: a boundary the agent crossed", 20, 500, "t-bad")
    s += ztile(cx[0], y0, tw, "The evaluation", ["pre-release model on a cyber", "benchmark, deployment", "safeguards deliberately off"]) + '</g>\n'
    s += '<g data-build="1">\n' + zarrow(cx[0] + tw, y0 + ZTH // 2, cx[1] - 4, y0 + ZTH // 2)
    s += ztile(cx[1], y0, tw, "Escape, 9 July", ["a zero-day in the package proxy,", "then lateral movement to a", "node with Internet access"], bad=True) + '</g>\n'
    s += '<g data-build="2">\n' + zarrow(cx[1] + tw, y0 + ZTH // 2, cx[2] - 4, y0 + ZTH // 2, red=True)
    s += ztile(cx[2], y0, 832, "Launchpad: root at 04:01 UTC", ["an unsecured, user-hosted code-execution endpoint on a third-party sandbox",
              "becomes the control, staging and egress base; four publicly exposed accounts",
              "on other services serve as relay and storage"], bad=True) + '</g>\n'
    s += '<g data-build="3">\n' + zarrow(cx[3] + tw // 2, y0 + ZTH, cx[3] + tw // 2, y1 - 4, red=True)
    s += ztile(cx[3], y1, tw, "Entry: a worker pod", ["crafted dataset configs: a file", "read leaks pod secrets, a", "template injection runs code"], bad=True) + '</g>\n'
    s += '<g data-build="4">\n' + zarrow(cx[3], y1 + ZTH // 2, cx[2] + tw + 4, y1 + ZTH // 2, red=True)
    s += ztile(cx[2], y1, tw, "The cluster, 11 July", ["service-account token, metadata", "credentials, a privileged pod:", "root, then cluster-admin"], bad=True) + '</g>\n'
    s += '<g data-build="5">\n' + zarrow(cx[2], y1 + ZTH // 2, cx[1] + tw + 4, y1 + ZTH // 2, red=True)
    s += ztile(cx[1], y1, tw, "Mesh, cloud, CI, 12 July", ["181 VPN enrollments, keys at a", "production database, a pull", "request into CI"], bad=True) + '</g>\n'
    s += '<g data-build="6">\n' + zarrow(cx[1], y1 + ZTH // 2, cx[0] + tw + 4, y1 + ZTH // 2)
    s += ztile(cx[0], y1, tw, "Detection, 13 July", ["alerts correlated but never", "escalated; humans find the", "vector and cut access"]) + '</g>\n'
    return s + '</svg>\n'


def poisoned_harness():
    # three columns (the Internet, the organization's repositories, every developer's agent) by three rows
    cx, tw = (24, 640, 1256), 520
    fx, fw = (0, 616, 1232), 568
    ry = (76, 288, 500)
    mid = [y + ZTH // 2 for y in ry]
    H = ry[2] + ZTH + 40
    s = head(1800, H, "MIDNIGHT NEPTUNE path across three zones: on the Internet, a fake recruiter with a model-generated photo "
                      "and a fake meeting page with a ClickFix lure; inside the organization, a foothold and a pivot into the "
                      "internal code repositories, where the committed agent settings gain a startup hook; then, for every "
                      "developer, starting the coding agent on an ordinary morning runs the hook, which downloads the SOMBERMEME "
                      "backdoor, and GitHub tokens named after Copilot disguise the lateral movement")
    s += '<g data-build="0">\n' + zframe(fx[0], 12, fw, H - 28, "The Internet — the attacker", dashed=True)
    s += zframe(fx[1], ry[1] - 64, fw, H - 16 - (ry[1] - 64), "The organization — its repositories")
    s += zframe(fx[2], 12, fw, H - 28, "Every developer — the coding agent")
    s += text(fx[0] + fw // 2, mid[2], "red arrow: a trust boundary crossed", 20, 500, "t-bad", "middle")
    s += ztile(cx[0], ry[0], tw, "A fake recruiter", ["a persona with a model-generated", "photo approaches an employee"], bad=True) + '</g>\n'
    s += '<g data-build="1">\n' + zarrow(cx[0] + tw // 2, ry[0] + ZTH, cx[0] + tw // 2, ry[1] - 4)
    s += ztile(cx[0], ry[1], tw, "A fake meeting page", ['a "ClickFix" lure: run this script', "to fix your call"], bad=True) + '</g>\n'
    s += '<g data-build="2">\n' + zarrow(cx[0] + tw, mid[1], cx[1] - 4, mid[1], red=True)
    s += ztile(cx[1], ry[1], tw, "Foothold, then pivot", ["the lure runs on an employee's machine;", "the attacker reaches the internal", "code repositories"], bad=True) + '</g>\n'
    s += '<g data-build="3">\n' + zarrow(cx[1] + tw // 2, ry[1] + ZTH, cx[1] + tw // 2, ry[2] - 4, red=True)
    s += ztile(cx[1], ry[2], tw, "Edit .claude/settings.json", ["a hook that runs when the coding", "agent starts — committed, so it", "travels with the code"], bad=True) + '</g>\n'
    s += '<g data-build="4">\n' + ztile(cx[2], ry[0], tw, "A developer starts the agent", ["as on any morning; the project", "settings file configures it"]) + '</g>\n'
    # the committed hook crosses from the repository into the developer's running agent
    gap = (fx[1] + fw + fx[2]) // 2
    s += '<g data-build="5">\n' + zarrow(cx[2] + tw // 2, ry[0] + ZTH, cx[2] + tw // 2, ry[1] - 4)
    s += edge(f"M{cx[1] + tw} {mid[2]}H{gap}V{mid[1]}H{cx[2] - 4}", arrow=True, red=True)
    s += ztile(cx[2], ry[1], tw, "The hook runs first", ["it downloads the SOMBERMEME backdoor;", "the agent is the loader"], bad=True) + '</g>\n'
    s += '<g data-build="6">\n' + zarrow(cx[2] + tw // 2, ry[1] + ZTH, cx[2] + tw // 2, ry[2] - 4, red=True)
    s += ztile(cx[2], ry[2], tw, "Lateral movement, disguised", ["GitHub tokens named after Copilot", "make it look like tooling"], bad=True) + '</g>\n'
    return s + '</svg>\n'


def glyph(x, y, ch, cls="t2"):
    return text(x, y, ch, 46, 300, cls, "middle")


def centered_tile(x, y, w, h, lines, size, bad=False, weight=700):
    """A tile whose text is centred: one or two short lines."""
    cls = "node node--bad" if bad else "node"
    tcls = "t-bad" if bad else "t"
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" class="{cls}"/>\n'
    cy = y + h // 2
    ys = [cy] if len(lines) == 1 else [cy - size * 0.65, cy + size * 0.65]
    for ly, line in zip(ys, lines):
        s += text(x + w // 2, round(ly), line, size, weight, tcls, "middle")
    return s


def equation_figure(aria, terms, heading, readings):
    """What an incident adds up to: four ingredients summed, left to right, into attacker-desired
    capability; below, three readings of the same incident, revealed one at a time."""
    W, H = 1800, 480
    s = head(W, H, aria)
    tw, th, gap, y = 290, 150, 70, 16
    x = 35
    for i, (lines, bad) in enumerate(terms):
        body = glyph(x - gap // 2, y + th // 2, "+") if i > 0 else ""
        body += centered_tile(x, y, tw, th, lines, 27, bad=bad)
        s += f'<g data-build="{i}">\n{body}</g>\n'
        x += tw + gap
    body = glyph(x - gap // 2, y + th // 2, "=") + centered_tile(x, y, tw, th, ["attacker-desired", "capability"], 27, bad=True)
    s += f'<g data-build="{len(terms)}">\n{body}</g>\n'
    # three readings of the same incident
    ry = y + th + 130
    s += '<g data-build="5">\n' + text(W // 2, ry - 50, heading, 24, 600, "t2", "middle")
    rw, rgap = 540, 60
    rx = (W - 3 * rw - 2 * rgap) // 2
    for i, lines in enumerate(readings):
        if i > 0:
            s += f'</g>\n<g data-build="{5 + i}">\n'
        s += centered_tile(rx + i * (rw + rgap), ry, rw, 140, lines, 26, weight=600)
    s += '</g>\n'
    return s + "</svg>\n"


def equation():
    return equation_figure(
        "ForcedLeak, what it adds up to: attacker-controlled data plus a trusted agent plus organizational identity "
        "and tools plus a permitted outbound channel equals attacker-desired capability. Three readings of the same "
        "incident: the CRM record contains the payload; the agent is a compromised deputy; the agent has "
        "operationally become part of the malware",
        [(["attacker-controlled", "data"], True), (["trusted agent:", "model and harness"], False),
         (["organizational", "identity and tools"], False), (["permitted", "outbound channel"], False)],
        "Three readings of the same incident — each true, each useful for something different",
        [["The CRM record", "contains the payload"], ["The agent is", "a compromised deputy"],
         ["The agent has operationally", "become part of the malware"]])


def equation_neptune():
    return equation_figure(
        "MIDNIGHT NEPTUNE, what it adds up to: attacker-controlled configuration plus a trusted agent plus a developer's "
        "identity and machine plus a permitted outbound channel equals attacker-desired capability. Three readings of the "
        "same incident: the repository contains the payload; the agent is the loader; the settings file is the supply chain",
        [(["attacker-controlled", "configuration"], True), (["trusted agent:", "model and harness"], False),
         (["developer identity", "and machine"], False), (["permitted", "outbound channel"], False)],
        "Three readings — this time there is a file, and the agent fetched it",
        [["The repository", "contains the payload"], ["The agent is", "the loader"],
         ["The settings file", "is the supply chain"]])


def equation_huggingface():
    return equation_figure(
        "Hugging Face, what it adds up to: the attacker's objective plus the attacker's agent (model and harness) plus a "
        "launchpad on the Internet plus ordinary weaknesses at the victim equals attacker-desired capability. Three "
        "readings of the same incident: a tireless operator, coverage not elegance; the agent was the intruder, no human "
        "in the loop; detection worked, the decision failed",
        [(["the attacker's", "objective"], True), (["attacker's agent:", "model and harness"], True),
         (["a launchpad on", "the Internet"], True), (["ordinary weaknesses", "at the victim"], False)],
        "Three readings — each true, each pointing at a different defense",
        [["A tireless operator:", "coverage, not elegance"], ["The agent was the intruder:", "no human in the loop"],
         ["Detection worked;", "the decision failed"]])


def case_reminder():
    """Two reminder cards for the comparison: Case A (dashed, outside the organization) and Case B (inside),
    each with the incidents the lecture used for it."""
    W, H = 1800, 236
    s = head(W, H, "Two reminder cards. Case A, the attacker's own agent, runs outside the organization: AI pentesting "
                   "frameworks seen in intrusions, and the Hugging Face evaluation escape. Case B, the victim's own agent "
                   "hijacked inside the trusted workflow: ForcedLeak through injected context, MIDNIGHT NEPTUNE through a "
                   "poisoned harness")
    cards = [
        (0, "CASE A — the attacker's own agent", True,
         ["outside the organization: the attacker's objective, model and harness;", "the victim sees only the effects"],
         [("AI pentesting frameworks", "CAIRN, PentAGI — seen in intrusions"), ("Hugging Face, July 2026", "the evaluation escape, ~17,600 actions")]),
        (930, "CASE B — the victim's own agent, hijacked", False,
         ["inside the trusted workflow: the victim's own model and harness;", "the attacker changes what it reads, or what it runs"],
         [("ForcedLeak", "injected context: a CRM record"), ("MIDNIGHT NEPTUNE", "poisoned harness: a committed hook")]),
    ]
    for x, label, dashed, blurb, chips in cards:
        s += f'<rect x="{x}" y="10" width="870" height="216" rx="22" class="{"env" if dashed else "frame"}"/>\n'
        s += text(x + 28, 44, label, 26, 700, "t")
        for i, line in enumerate(blurb):
            s += text(x + 28, 76 + i * 24, line, 19, 400, "t2")
        for i, (t, sub) in enumerate(chips):
            s += tile(x + 28 + i * 420, 118, 395, 92, t, [sub], title_size=22, sub_size=18)
    return s + "</svg>\n"


def dual_use():
    """Research tools that diffused: published research, released open source, then reported in intrusions."""
    W, H = 1800, 300
    s = head(W, H, "AI pentesting frameworks began as published research, were released open source and model-agnostic, and have since been reported in real intrusions")
    cols = [
        ("PUBLISHED RESEARCH", ["autonomous agents that solve", "CTFs, find bugs, red-team nets", "PentestGPT, EnIGMA, D-CIPHER,", "Incalmo; measured on Cybench"], False),
        ("OPEN SOURCE, MODEL-AGNOSTIC", ["anyone can point a released", "framework at any target;", "only the authorization differs"], False),
        ("REPORTED IN INTRUSIONS", ["CAIRN — a China-nexus actor,", "~19 orgs, Aug–Sep 2026 (Unit 42)", "PentAGI — scanning across Asia", "HexStrike AI — experimentation"], True),
    ]
    xs, w = [40, 640, 1240], 520
    for i, (t, lines, bad) in enumerate(cols):
        body = ""
        if i > 0:
            body += arrow(xs[i] - 80, 170, xs[i] - 2, 170, red=(cols[i][2]))
        body += tile(xs[i], 40, w, 210, t, lines, bad=bad, title_size=23, sub_size=20)
        s += f'<g data-build="{i}">\n{body}</g>\n'
    return s + "</svg>\n"


def injection_jailbreak():
    """Two flows: injection shares the prompt between the developer and untrusted text; a jailbreak is the user against the model's training."""
    W, H = 1800, 430
    s = head(W, H, "Prompt injection attacks the application by concatenating untrusted text with the developer's prompt; a jailbreak attacks the model's own safety training, with the user as the attacker")
    # injection
    s += text(40, 26, "PROMPT INJECTION — an attack on the application", 22, 700, "t-bad")
    s += tile(40, 52, 380, 120, "developer's instructions", ['"Translate the following…"', "trusted, written by the app"], title_size=22, sub_size=18)
    s += glyph(442, 112, "+")
    s += tile(466, 52, 430, 120, "untrusted text", ['"Ignore the above and…"', "anyone whose text reaches it"], bad=True, title_size=22, sub_size=18)
    s += arrow(896, 112, 988, 112, red=True) + tile(990, 52, 220, 120, "MODEL", ["one text stream"], model=True, title_size=26)
    s += arrow(1210, 112, 1328, 112, red=True) + tile(1330, 52, 430, 120, "obeys the untrusted text", ["the developer's intent is defeated"], bad=True, title_size=22, sub_size=18)
    # jailbreak
    s += text(40, 258, "JAILBREAK — an attack on the model", 22, 700, "t-bad")
    s += tile(40, 284, 520, 120, "user's request", ['"From now on you are DAN…"', "the user is the attacker"], bad=True, title_size=22, sub_size=18)
    s += arrow(560, 344, 988, 344, red=True) + tile(990, 284, 220, 120, "MODEL", ["with safety training"], model=True, title_size=26)
    s += arrow(1210, 344, 1328, 344, red=True) + tile(1330, 284, 430, 120, "says what training forbade", ["the trainer's intent is defeated"], bad=True, title_size=22, sub_size=18)
    return s + "</svg>\n"


def case_a_defense():
    """Same sensors, a different arithmetic, so triage changes: three rows, revealed in four builds."""
    W, H = 1800, 500
    s = head(W, H, "Case A defense in three rows. Same sensors: EDR and XDR, identity and cloud audit, NDR and flows — the agent "
                   "cannot act without touching them. A different arithmetic: a human operator issues a few hundred actions a "
                   "day, a handful clearly malicious; the attacker's agent issued 7,677 on 11 July alone and about 17,600 in "
                   "all, none clearly malicious on its own — ten to a thousand times more events, each less malicious, "
                   "meaningful only together. So triage changes: ranking alerts by severity for humans to read gives way to "
                   "evaluating every event continuously, correlated across sources, with decisions at machine speed")
    # row A: the sensors we already have
    s += '<g data-build="0">\n' + text(20, 22, "SAME SENSORS — the agent cannot act without touching them", 21, 700, "t-good")
    sensors = [("EDR / XDR", "hosts and processes"), ("Identity and cloud audit", "tokens, roles, API calls"), ("NDR and flows", "connections, DNS, egress")]
    for i, (t, sub) in enumerate(sensors):
        s += tile(20 + i * 600, 44, 560, 96, t, [sub], good=True, title_size=24, sub_size=19)
    s += '</g>\n'
    # row B: the arithmetic, then the multiplier between the two tiles
    s += '<g data-build="1">\n' + text(20, 184, "A DIFFERENT ARITHMETIC", 21, 700, "t-bad")
    s += tile(20, 204, 700, 122, "A human operator", ["a few hundred actions a day (an estimate);", "a handful of them clearly malicious"], title_size=24, sub_size=19)
    s += tile(1080, 204, 700, 122, "The attacker's agent", ["7,677 actions on 11 July; ~17,600 in all;", "none clearly malicious on its own"], bad=True, title_size=24, sub_size=19) + '</g>\n'
    s += '<g data-build="2">\n' + text(900, 246, "×10 to ×1000", 40, 800, "t-bad", "middle")
    s += text(900, 286, "more events, each less malicious,", 19, 500, "t2", "middle") + text(900, 310, "meaningful only together", 19, 500, "t2", "middle") + '</g>\n'
    # row C: so triage changes
    s += '<g data-build="3">\n' + text(20, 370, "SO TRIAGE CHANGES", 21, 700, "t")
    s += tile(20, 390, 840, 100, "Rank alerts by severity; humans read the top", ["there is no most-malicious event: the attack is the pattern"], bad=True, title_size=23, sub_size=19)
    s += arrow(860, 440, 938, 440, green=True)
    s += tile(940, 390, 840, 100, "Evaluate every event, continuously", ["correlate across sources, decide at machine speed — the defender's loop"], good=True, title_size=23, sub_size=19) + '</g>\n'
    return s + "</svg>\n"


def weak_monitor():
    """A weaker, trusted monitor watches a stronger, untrusted agent; full context does not guarantee a correct verdict."""
    W, H = 1800, 250
    s = head(W, H, "A weaker, trusted monitor watches a stronger, untrusted agent; having the full context does not mean it can read the intent in it")
    s += tile(40, 20, 620, 130, "Strong agent", ["untrusted; its intent lives in a", "plan the monitor may not follow"], bad=True, title_size=28, sub_size=21)
    s += tile(1140, 20, 620, 130, "Weak monitor", ["trusted, cheaper; sees the trajectory", "— tools, arguments, destination"], good=True, title_size=28, sub_size=21)
    s += arrow(1138, 85, 662, 85)
    s += text(900, 56, "watches", 20, 600, "t2", "middle")
    s += text(900, 196, "full context ≠ correct verdict", 28, 700, "t-bad", "middle")
    return s + "</svg>\n"


(OUT / "attack-map.svg").write_text(attack_map())
(OUT / "case-a-defense.svg").write_text(case_a_defense())
(OUT / "weak-monitor.svg").write_text(weak_monitor())
(OUT / "injection-jailbreak.svg").write_text(injection_jailbreak())
(OUT / "dual-use.svg").write_text(dual_use())
(OUT / "equation.svg").write_text(equation())
(OUT / "equation-neptune.svg").write_text(equation_neptune())
(OUT / "equation-huggingface.svg").write_text(equation_huggingface())
(OUT / "case-reminder.svg").write_text(case_reminder())
(OUT / "poisoned-harness.svg").write_text(poisoned_harness())
(OUT / "forcedleak-path.svg").write_text(forcedleak_path())
(OUT / "incident-chain.svg").write_text(incident_chain())
(OUT / "supply-chain.svg").write_text(supply_chain())
(OUT / "funnel.svg").write_text(funnel())
(OUT / "ladder.svg").write_text(ladder())
(OUT / "harness.svg").write_text(harness("plain"))
(OUT / "harness-attack-surface.svg").write_text(harness("attack"))
(OUT / "harness-guardrails.svg").write_text(harness("guard"))
(OUT / "agent-loop.svg").write_text(loop())
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
