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
    """Match the model to the scale: a static funnel of three tiers, each band narrower, with the model that can afford it."""
    W, H = 1800, 350
    s = head(W, H, "Match the model to the scale: cheap encoder classifiers at machine scale, small task-trained models at triage, a frontier model and a human for the few investigations")
    cx = 560
    rows = [
        ("machine", "millions of events, flows, tool calls, retrieved texts", "encoder-only classifiers (BERT family)", "fine-tuned on telemetry; line rate; a label, not a sentence", 1040),
        ("triage", "thousands of candidates", "small language models, 1–8B", "trained for the task: summarize, correlate, propose", 760),
        ("investigation", "a few consequential cases", "a frontier model — and a human", "for the few cases the funnel selects", 480),
    ]
    y, prev = 10, None
    for i, (name, vol, mt, ms, w) in enumerate(rows):
        x = cx - w // 2
        s += tile(x, y, w, 96, name, [vol], title_size=25, sub_size=19)
        s += tile(1240, y, 520, 96, mt, [ms], model=(i == 2), title_size=21, sub_size=18)
        if prev is not None:
            s += edge(f"M{cx} {prev}V{y}", strong=True, arrow=True)
        prev = y + 96
        y += 116
    return s + '</svg>\n'


def chain_v(aria, steps, tw=1240, th=64, gap=26):
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
        body += tile(x, y, tw, th, t, [], bad=bad, title_size=23, sub_size=1)
        s += f'<g data-build="{i}">\n{body}</g>\n'
        y += th + gap
    return s + "</svg>\n"


def forcedleak_path():
    steps = [
        ("Attacker submits a public Web-to-Lead form", True),
        ("Concealed instructions persist in the CRM record", True),
        ("An employee later asks Agentforce about the lead", False),
        ("The agent retrieves the attacker-controlled record", False),
        ("The record's data is interpreted as instructions", True),
        ("The agent reaches more CRM data with its authority", False),
        ("Sensitive data leaves through crafted image requests", True),
    ]
    return chain_v("ForcedLeak attack path: instructions an attacker planted in a CRM record are later retrieved by the trusted agent and interpreted as commands, so data leaves with the organization's own authority", steps)


def poisoned_harness():
    steps = [
        ("Fake recruiter profile, model-generated photo", True),
        ('Fake meeting page with a "ClickFix" lure: run this script', True),
        ("Foothold, then pivot into the internal code repositories", True),
        ("Edit .claude/settings.json: a hook that runs on startup", True),
        ("A developer starts the coding agent, as on any morning", False),
        ("The hook downloads the SOMBERMEME backdoor", True),
        ("GitHub tokens named after Copilot hide the lateral movement", True),
    ]
    return chain_v("MIDNIGHT NEPTUNE path: social engineering gains a foothold, the attacker edits the agent's committed configuration so startup downloads a backdoor, and a developer starting the agent on an ordinary morning runs it", steps)


def glyph(x, y, ch, cls="t2"):
    return text(x, y, ch, 46, 300, cls, "middle")


def equation():
    """Dormant instructions, live authority: four ingredients summed into attacker-desired capability."""
    W, H = 1200, 560
    terms = [
        ("attacker-controlled data", True),
        ("trusted agent: model and harness", False),
        ("organizational identity and tools", False),
        ("permitted outbound channel", False),
    ]
    s = head(W, H, "Dormant instructions, live authority: attacker-controlled data plus a trusted agent plus organizational identity plus a permitted outbound channel equals attacker-desired capability")
    tw, th, gap = 980, 66, 56
    x = (W - tw) // 2
    y = 10
    for i, (t, bad) in enumerate(terms):
        body = glyph(W // 2, y - gap // 2, "+") if i > 0 else ""
        body += tile(x, y, tw, th, t, [], bad=bad, title_size=25, sub_size=1)
        s += f'<g data-build="{i}">\n{body}</g>\n'
        y += th + gap
    body = glyph(W // 2, y - gap // 2, "=") + tile(x, y, tw, th + 4, "attacker-desired capability", [], bad=True, title_size=27, sub_size=1)
    s += f'<g data-build="{len(terms)}">\n{body}</g>\n'
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
    """The attacker's agent acts only through tools, so existing sensors already see it; what must change is the tempo."""
    W, H = 1800, 340
    s = head(W, H, "The attacker's agent acts only through tools, so every action lands on an endpoint, an identity or a network flow that EDR, XDR, NDR and identity logs already record; what must change is the tempo, not the sensor")
    s += '<g data-build="0">\n'
    s += tile(40, 50, 380, 130, "The attacker's agent", ["acts only through tools"], bad=True, title_size=24, sub_size=20)
    s += arrow(420, 115, 518, 115)
    s += tile(520, 50, 470, 130, "Endpoint · identity · flow", ["every action lands here"], title_size=23, sub_size=20)
    s += arrow(990, 115, 1088, 115, green=True)
    s += tile(1090, 50, 670, 130, "EDR / XDR / NDR", ["identity logs, flow metadata —", "the sensors we already deploy"], good=True, title_size=26, sub_size=20)
    s += '</g>\n'
    s += '<g data-build="1">\n'
    s += tile(40, 220, 1720, 96, "What changes is the tempo, not the sensor", ["thousands of ambiguous events · several telemetry systems · changing identities · a few consequential transitions   →   a correlation problem, at machine speed"], title_size=24, sub_size=20)
    s += '</g>\n'
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
(OUT / "poisoned-harness.svg").write_text(poisoned_harness())
(OUT / "forcedleak-path.svg").write_text(forcedleak_path())
(OUT / "supply-chain.svg").write_text(supply_chain())
(OUT / "funnel.svg").write_text(funnel())
(OUT / "ladder.svg").write_text(ladder())
(OUT / "harness.svg").write_text(harness("plain"))
(OUT / "harness-attack-surface.svg").write_text(harness("attack"))
(OUT / "harness-guardrails.svg").write_text(harness("guard"))
(OUT / "agent-loop.svg").write_text(loop())
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
