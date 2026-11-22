"""Generate the Lecture 1 diagrams: the ladder, the original model, the timelines, the breaks, the ATT&CK
matrix with a lit path, the benign-file cards, the pipeline strips, the HTTPS chart and the exercise.

Drawing primitives and the shared theme live in tools/deck/svg.py; the data in data.py."""
import sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "deck"))
sys.path.insert(0, str(HERE))
from svg import *  # noqa: E402,F401,F403
from data import PERIODS, TRACKS, EVENTS, BREAKS, PIPELINE, HTTPS, ATTACK  # noqa: E402

OUT = out_dir()
TRACK_INDEX = {t["key"]: i for i, t in enumerate(TRACKS)}
TRACK_NAMES = ["Motive and money", "Attackers", "Operating system", "Internet", "Security products"]
STAGES = [p["label"] for p in PIPELINE]


def xscale(y0, y1, x0, x1):
    return lambda y: round(x0 + (y - y0) / (y1 - y0) * (x1 - x0), 1)


class LabelSlots:
    """Places event labels above or below a dot in one of three vertical slots, picking the first slot whose last
    label in the same lane does not overlap horizontally (text width estimated from the character count)."""
    def __init__(self, offsets, size):
        self.offsets, self.size, self.last = offsets, size, {}

    def place(self, lane, cx, label, anchor):
        w = len(label) * self.size * 0.56
        left = cx if anchor == "start" else (cx - w if anchor == "end" else cx - w / 2)
        for k, dy in enumerate(self.offsets):
            if self.last.get((lane, k), -1e9) + 10 < left:
                self.last[(lane, k)] = left + w
                return dy
        k = min(range(len(self.offsets)), key=lambda k: self.last.get((lane, k), -1e9))
        self.last[(lane, k)] = left + w
        return self.offsets[k]


def small_badge(cx, cy, label, good=False, r=14, size=15):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{"badge--good" if good else "badge--bad"}"/>\n'
            + text(cx, cy + 1, str(label), size, 700, "t-badge", "middle"))


def lines(x, y, items, size, cls="t2", weight=400, step=None):
    step = step or round(size * 1.3)
    return "".join(text(x, y + i * step, esc(it), size, weight, cls) for i, it in enumerate(items))


# ---------------------------------------------------------------- slide 3: the ladder
def ladder():
    items = ["A trojan executable is written to disk", "PowerShell downloads and runs code",
             "A Portable Executable image exists only in process memory",
             "An attacker controls a legitimate remote-management tool",
             "Repository instructions cause a coding agent to exfiltrate secrets"]
    W, H = 1800, 520
    s = head(W, H, "Five suspicious situations as a ladder, from the file at the top to no file at the bottom: " + "; ".join(items))
    for i, it in enumerate(items):
        y = 50 + i * 86
        body = tile(280, y, 1300, 70, f"{i + 1}  ·  {esc(it)}", [], title_size=27)
        if i == 0:
            body = edge("M200 62V470", strong=True, arrow=True) + text(200, 30, "the file", 22, 700, "t", "middle") + body
        if i == len(items) - 1:
            body += text(200, 500, "no file", 22, 700, "t-bad", "middle")
        s += f'<g data-build="{i}">\n{body}</g>\n'
    return s + "</svg>\n"


# ---------------------------------------------------------------- slide 6: the original mental model
def original_model():
    W, H = 1800, 170
    s = head(W, H, "The original mental model: a malicious executable, executed by a user or the system, produces malicious behavior")
    steps = [("malicious executable", "a file, written to disk", True), ("user or system executes it", "double-click, autorun, exploit", False),
             ("malicious behavior occurs", "on that host, from that file", True)]
    for i, (t, sub, bad) in enumerate(steps):
        x = 40 + i * 600
        body = tile(x, 30, 520, 110, t, [sub], bad=bad, title_size=27, sub_size=21)
        if i:
            body = edge(f"M{x - 80} 85H{x - 4}", strong=True, arrow=True) + body
        s += f'<g data-build="{i}">\n{body}</g>\n'
    return s + "</svg>\n"


# ---------------------------------------------------------------- slides 9-13: timelines
def event_tip(e):
    yr = int(e["y"])
    return f"{yr} · {e['s']}" + (f" — {e['d']}" if e.get("d") else "")


def timeline_overview():
    W, H = 1800, 580
    x0, x1, top, lane_h = 250, 1780, 70, 86
    X = xscale(2000, 2027, x0, x1)
    s = head(W, H, "Four periods, 2000 to 2026, across five tracks: motive and money, attackers, operating system, internet, "
                   "security products. Every event is a dot with its date on hover; the anchor events are labelled; "
                   "the four period bands light up one at a time")
    s += '<g data-build="0">\n'
    for i, name in enumerate(TRACK_NAMES):
        y = top + i * lane_h
        s += rect(x0, y, x1 - x0, lane_h, "lane") + text(x0 - 16, y + lane_h // 2, name, 20, 700, "t2", "end")
    bottom = top + 5 * lane_h
    for yr in range(2000, 2028):
        x = X(yr)
        if yr % 5 == 0:
            s += f'<path d="M{x} {bottom}V{bottom + 10}" class="axis"/>\n' + text(x, bottom + 28, str(yr), 18, 500, "t2", "middle")
    for p in PERIODS[1:]:
        s += f'<path d="M{X(p["from"])} {top}V{bottom}" class="marker"/>\n'
    s += f'<path d="M{x0} {bottom}H{x1}" class="axis"/>\n'
    slots = LabelSlots((-22, 26, -40), 16)
    for e in sorted(EVENTS, key=lambda e: e["y"]):
        lane = TRACK_INDEX[e["t"]]
        cx, cy = X(e["y"]), top + lane * lane_h + lane_h // 2
        if e.get("h"):
            s += circle(cx, cy, 9, "dot--anchor", event_tip(e))
            anchor = "start" if cx < x0 + 120 else ("end" if cx > x1 - 120 else "middle")
            s += text(cx, cy + slots.place(lane, cx, e["s"], anchor), esc(e["s"]), 16, 600, "t", anchor)
        elif e.get("k"):
            s += circle(cx, cy, 6, "dot--key", event_tip(e))
        else:
            s += circle(cx, cy, 4.5, "dot--muted", event_tip(e))
    s += '</g>\n'
    for k, p in enumerate(PERIODS):
        xa, xb = X(p["from"]), X(min(p["to"], 2027))
        label = f'{p["label"].split(" · ")[0]} · {p["short"]}'
        last = k == len(PERIODS) - 1   # the narrow last band: its label hangs from the right edge, one line up
        s += (f'<g data-build="{k + 1}">\n' + rect(xa, top, xb - xa, 5 * lane_h, f"band-{k + 1}")
              + text(xb - 6 if last else (xa + xb) / 2, top - (48 if last else 24), esc(label), 21, 700, f"t-part-{k + 1}", "end" if last else "middle") + '</g>\n')
    return s + "</svg>\n"


def period_timeline(k):
    p = PERIODS[k]
    y0, y1 = p["from"], p["to"]
    W, H = 1800, 540
    x0, x1, top, lane_h = 250, 1780, 70, 82
    X = xscale(y0, y1, x0, x1)
    s = head(W, H, f'{p["label"]}: the five tracks for these years, key events labelled, every dot with its date on hover; '
                   "the tracks light up one at a time")
    s += '<g data-build="0">\n'
    # context strip: the whole span with this period marked
    C = xscale(2000, 2027, x0, x1)
    s += rect(x0, 18, x1 - x0, 12, "lane", rx=6) + rect(C(y0), 16, C(min(y1, 2027)) - C(y0), 16, f"band-{k + 1}", rx=6)
    s += text(x0 - 16, 24, "2000–2026", 15, 500, "t2", "end")
    for i, name in enumerate(TRACK_NAMES):
        y = top + i * lane_h
        s += rect(x0, y, x1 - x0, lane_h, "lane") + text(x0 - 16, y + lane_h // 2, name, 20, 700, "t2", "end")
    bottom = top + 5 * lane_h
    for yr in range(int(y0), int(y1) + 1):
        x = X(yr)
        if yr < 2027:
            s += f'<path d="M{x} {bottom}V{bottom + 8}" class="axis"/>\n' + text(x, bottom + 26, str(yr), 17, 500, "t2", "middle")
    s += f'<path d="M{x0} {bottom}H{x1}" class="axis"/>\n'
    slots = LabelSlots((-20, 24, -38), 16)
    for e in sorted(EVENTS, key=lambda e: e["y"]):
        if not (y0 <= e["y"] < y1):
            continue
        lane = TRACK_INDEX[e["t"]]
        cx, cy = X(e["y"]), top + lane * lane_h + lane_h // 2
        if e.get("k"):
            s += circle(cx, cy, 8, "dot--key", event_tip(e))
            anchor = "start" if cx < x0 + 150 else ("end" if cx > x1 - 150 else "middle")
            s += text(cx, cy + slots.place(lane, cx, e["s"], anchor), esc(e["s"]), 16, 600, "t", anchor)
        else:
            s += circle(cx, cy, 5, "dot--muted", event_tip(e))
    s += '</g>\n'
    for i in range(5):
        y = top + i * lane_h
        s += f'<g data-build="{i + 1}">\n' + rect(x0, y, x1 - x0, lane_h, f"band-{k + 1}") + '</g>\n'
    return s + "</svg>\n"


# ---------------------------------------------------------------- slide 14: what broke, and when
def breaks_timeline():
    W, H = 1800, 420
    x0, x1, top, row = 540, 1780, 46, 54
    X = xscale(2000, 2027, x0, x1)
    s = head(W, H, "What broke the file-centric model, and when: six breaks as bars on the 2000 to 2027 axis — " +
             "; ".join(b["s"] for b in BREAKS) + " — and, as an inset, the malware-free share of CrowdStrike detections, "
             "40 percent in 2018, 51 in 2019, 62 in 2021, 79 in 2024")
    axis_y = top + len(BREAKS) * row + 6
    s += '<g data-build="0">\n'
    for yr in range(2000, 2028, 5):
        s += f'<path d="M{X(yr)} {top - 8}V{axis_y}" class="grid"/>\n' + text(X(yr), axis_y + 22, str(yr), 18, 500, "t2", "middle")
    s += f'<path d="M{x0} {axis_y}H{x1}" class="axis"/>\n</g>\n'
    for i, b in enumerate(BREAKS):
        y = top + i * row
        body = text(x0 - 18, y + 24, esc(b["short"]), 21, 700, "t", "end")
        body += rect(X(b["from"]), y + 8, X(min(b["to"], 2027)) - X(b["from"]), 32, "bar", rx=8, tip=f'{b["s"]}: {b["from"]} onward')
        if b.get("dom"):
            body += f'<path d="M{X(b["dom"])} {y + 4}l-8 -10h16z" class="arrow arrow--bad"/>\n'
        s += f'<g data-build="{i}">\n{body}</g>\n'
    # inset: the malware-free share of detections, in the empty left half of the lower rows (those breaks start in 2017)
    share = [(2018, 40), (2019, 51), (2021, 62), (2024, 79)]
    ix, iy = 600, top + 3 * row + 2
    body = text(ix, iy + 8, "Malware-free share of CrowdStrike detections", 17, 700, "t2")
    for j, (yr, v) in enumerate(share):
        bx, bh = ix + j * 120, round(v * 1.1)
        body += rect(bx, iy + 116 - bh, 56, bh, "bar--bad", rx=5, tip=f"{yr}: {v} percent of detections were malware-free")
        body += text(bx + 28, iy + 116 - bh - 12, f"{v}%", 16, 700, "t", "middle") + text(bx + 28, iy + 130, str(yr), 15, 500, "t2", "middle")
    s += f'<g data-build="{len(BREAKS)}">\n{body}</g>\n'
    return s + "</svg>\n"


# ---------------------------------------------------------------- slides 16 and 18: the ATT&CK matrix
def attack_matrix(aria, path, lead):
    """The schematic Enterprise matrix; `path` is a list of steps, each a list of (technique id, tactic id)
    cells that light together, in order."""
    tactics = ATTACK["tactics"]
    W = 1800
    col_w, x0, top, head_h, row_h = 116, 24, 44, 50, 30
    cols = []
    for t in tactics:
        rows = []
        for tech in t["techniques"]:
            rows.append((tech["id"], tech["name"], False))
            for sub in tech.get("subs", []):
                rows.append((sub["id"], sub["name"], True))
        cols.append(rows)
    max_rows = max(len(r) for r in cols)
    H = top + head_h + max_rows * row_h + 56
    s = head(W, H, aria)
    s += '<g data-build="0">\n' + text(x0, 18, esc(lead), 17, 500, "t2")
    centers = {}
    for c, (t, rows) in enumerate(zip(tactics, cols)):
        x = x0 + c * col_w + 4
        s += rect(x, top, col_w - 8, head_h, "colhead", rx=6, tip=f'{t["name"]} ({t["id"]}): {t["count"]} techniques')
        short = t["short"].split(" ")
        if len(t["short"]) > 12 and len(short) > 1:
            cut = len(short) // 2
            s += text(x + (col_w - 8) / 2, top + 16, esc(" ".join(short[:cut])), 14, 700, "t", "middle")
            s += text(x + (col_w - 8) / 2, top + 34, esc(" ".join(short[cut:])), 14, 700, "t", "middle")
        else:
            s += text(x + (col_w - 8) / 2, top + head_h / 2, esc(t["short"]), 14, 700, "t", "middle")
        for r, (tid, name, is_sub) in enumerate(rows):
            y = top + head_h + 4 + r * row_h
            cx = x + (10 if is_sub else 0)
            s += rect(cx, y, col_w - 8 - (10 if is_sub else 0), row_h - 4, "cell--sub" if is_sub else "cell", rx=4, tip=f"{tid} {name}")
            s += text(cx + 6, y + (row_h - 4) / 2, tid, 13 if is_sub else 14, 600 if not is_sub else 500, "t" if not is_sub else "t2")
            centers[(tid, t["id"])] = (cx + (col_w - 8 - (10 if is_sub else 0)) / 2, y + (row_h - 4) / 2, cx, y, col_w - 8 - (10 if is_sub else 0))
        more = t["count"] - len(t["techniques"])
        s += text(x + (col_w - 8) / 2, top + head_h + 4 + len(rows) * row_h + 12, f"+{more} more", 13, 500, "t2", "middle")
    s += '</g>\n'
    prev = None
    for k, step in enumerate(path, start=1):
        body = ""
        first = None
        for tid, tac in step:
            if (tid, tac) not in centers:
                sys.exit(f"path cell {tid} in {tac} is not in the curated matrix")
            cx, cy, x, y, w = centers[(tid, tac)]
            body += rect(x, y, w, row_h - 4, "cell--lit", rx=4, tip=f"step {k}: {tid}") + text(x + 6, cy, tid, 14, 700, "t-bad")
            if first is None:
                first = (cx, cy, x, y)
        if prev is not None:
            body = edge(f"M{prev[0]} {prev[1]}L{first[0]} {first[1]}", red=True) + body
        body += small_badge(first[2] + 2, first[3] + 2, k, r=11, size=13)
        s += f'<g data-build="{k}">\n{body}</g>\n'
        prev = first
    return s + "</svg>\n"


TROJAN_PATH = [[("T1566.001", "TA0001")], [("T1204.002", "TA0002")], [("T1027.002", "TA0005")], [("T1055", "TA0005")],
               [("T1547.001", "TA0003")], [("T1071.001", "TA0011")], [("T1486", "TA0040")]]
FILELESS_PATH = [[("T1078", "TA0001")], [("T1059.001", "TA0002"), ("T1027.010", "TA0005")], [("T1068", "TA0004")],
                 [("T1685", "TA0112")], [("T1105", "TA0011")], [("T1055", "TA0005"), ("T1055", "TA0004"), ("T1620", "TA0005")],
                 [("T1083", "TA0007"), ("T1005", "TA0009"), ("T1560", "TA0009")], [("T1071.001", "TA0011"), ("T1041", "TA0010")]]


# ---------------------------------------------------------------- slide 17: benign files
def benign_files():
    W, H = 1800, 470
    s = head(W, H, "Two capabilities delivered through benign files: a remote-management tool abused, and a vulnerable signed driver; "
                   "as files both are identical to their legitimate copies, and what makes them malicious lives outside the file")
    cards = [
        ("Remote-management tool abused", "T1219 Remote Access Tools — an ATT&CK tool, not malware", [
            ("What it is", "Legitimate remote-access software, installed as designed; the same binary and hash as every other install"),
            ("What differs from legitimate use", "Who operates the session, and whose objective it serves"),
            ("Where “malicious” sits", "Control and objective; the software works exactly as designed"),
            ("What a file classifier sees", "A clean, signed, known program")]),
        ("Vulnerable signed driver", "T1068 Exploitation for Privilege Escalation", [
            ("What it is", "A legitimate kernel driver with a valid signature and an exploitable flaw; the same binary and hash the vendor shipped"),
            ("What differs from legitimate use", "Who loads it, and that its flaw is used beyond the driver's intended design"),
            ("Where “malicious” sits", "Control and objective, and also capability: what it can be made to do"),
            ("What a file classifier sees", "A clean, signed, known driver")]),
    ]
    for i, (title, sub, rows) in enumerate(cards):
        x = 30 + i * 890
        body = rect(x, 16, 850, 384, "node", rx=16) + text(x + 26, 48, esc(title), 25, 700, "t") + text(x + 26, 78, esc(sub), 18, 500, "t-acc")
        y = 110
        for label, val in rows:
            body += text(x + 26, y, esc(label), 17, 700, "t2")
            for j, ln in enumerate(wrap(val, 78)):
                body += text(x + 26, y + 24 + j * 23, esc(ln), 19, 400, "t")
            y += 24 + 23 * max(1, len(wrap(val, 78))) + 14
        s += f'<g data-build="{i}">\n{body}</g>\n'
    s += ('<g data-build="2">\n' + text(900, 432, "As files, both are identical to their legitimate copies.", 24, 700, "t-bad", "middle")
          + text(900, 460, "What makes them malicious lives outside the file: who is in control and to what end — and, for the driver, what its flaw lets them do.", 21, 500, "t-bad", "middle") + '</g>\n')
    return s + "</svg>\n"


# ---------------------------------------------------------------- slides 20-26: the pipeline strip
TILE_H = 92


def strip_tile(i, y, kind=""):
    x = 16 + i * 224
    cls = {"": "node", "lit": "node node--model", "bad": "node node--bad"}[kind]
    tcls = {"": "t", "lit": "t-acc", "bad": "t-bad"}[kind]
    return rect(x, y, 200, TILE_H, cls, rx=14) + text(x + 100, y + TILE_H // 2, STAGES[i], 25, 700, tcls, "middle")


def strip(y):
    s = "".join(strip_tile(i, y) for i in range(8))
    for i in range(7):
        s += text(16 + i * 224 + 212, y + TILE_H // 2, "›", 30, 400, "t2", "middle")
    return s


def pipeline_figure(aria, steps):
    """A strip of the eight stages and one build per step. A step is a dict: lit (stages in accent), bad (stages in red),
    badge (a number on the first bad stage), bracket ((label, bad, "above" | "below") around the whole strip)."""
    brackets = any(st.get("bracket") for st in steps)
    y = 70 if brackets else 24
    W, H = 1800, (y + TILE_H + 110) if brackets else (y + TILE_H + 24)
    s = head(W, H, aria)
    for k, st in enumerate(steps):
        body = strip(y) if k == 0 else ""
        for i in st.get("lit", []):
            body += strip_tile(i, y, "lit")
        for i in st.get("bad", []):
            body += strip_tile(i, y, "bad")
        if st.get("badge") is not None and st.get("bad"):
            body += small_badge(16 + st["bad"][0] * 224 + 4, y + 4, st["badge"], r=16, size=17)
        if st.get("bracket"):
            label, bad, pos = st["bracket"]
            ly = y - 36 if pos == "above" else y + TILE_H + 42
            body += rect(6, y - 16, 1788, TILE_H + 32, "env", rx=18) + text(900, ly, esc(label), 23, 700, "t-bad" if bad else "t2", "middle")
        s += f'<g data-build="{k}">\n{body}</g>\n'
    return s + "</svg>\n"


def pipeline():
    return pipeline_figure("The complete detection pipeline: sensor, acquisition, extraction, representation, detection, investigation, "
                           "decision, response — each stage lit in turn", [{"lit": [i]} for i in range(8)])


def pipeline_host():
    steps = [{"bracket": ("built for: what each generation was bought to solve", False, "above")}] + [{"lit": [i]} for i in range(8)] + \
            [{"bracket": ("starved by: what moved out of each generation's field of view", True, "below")}]
    return pipeline_figure("Host and file lineage — antivirus, sandbox, EDR — stage by stage: what each generation was built for, "
                           "its sensor, acquisition, extraction, representation, detection, investigation, decision and response, "
                           "and what starved it", steps)


def pipeline_network():
    steps = [{"lit": [i]} for i in range(6)] + [{"lit": [6, 7]}] + [{"bracket": ("the challenge: what changed, and what remains observable", True, "below")}]
    return pipeline_figure("Network lineage — IDS on the plaintext web, then after HTTPS, TLS 1.3, DoH and ECH — stage by stage, "
                           "decision and response together, and the challenge", steps)


def pipeline_breaks():
    broke = [[2, 4], [0, 2], [0, 1], [2], [0], [3, 4], [0]]
    steps = [{"bad": b, "badge": k + 1} for k, b in enumerate(broke)]
    return pipeline_figure("Where each change broke the pipeline: seven changes, each lighting the stage that broke — packing broke "
                           "extraction and detection; file diversity the sensor and extraction; memory and living off the land the "
                           "sensor and acquisition; encryption extraction; stolen identities the sensor; trusted channels representation "
                           "and detection; instructions in data the sensor", steps)


def pipeline_options():
    return pipeline_figure("Options at each stage: the eight stages lit in turn, each with its menu of options", [{"lit": [i]} for i in range(8)])


def exercise():
    cases = [("A", "A memory-resident payload is missed by an on-write file scanner.", [0, 1]),
             ("B", "An HTTPS transfer is missed by a plaintext content signature.", [0]),
             ("C", "A retained PE file is parsed successfully but receives a benign score.", [3, 4]),
             ("D", "Three low-severity alerts fire on three systems over two days: an unusual sign-in, a PowerShell process, a proxy connection. Each is closed as noise.", [5]),
             ("E", "The alert is correct and investigated, but isolating the server requires an approval that is unreachable overnight. The upload completes.", [6]),
             ("F", "Isolation is ordered, but the laptop is off the VPN and the EDR cannot reach it for six hours.", [7])]
    W, H = 1800, 400 + TILE_H + 20
    s = head(W, H, "Diagnostic exercise: six misses as cards — " + " ".join(f"Case {c}: {t}" for c, t, _ in cases) +
             " — and the pipeline strip below; each answer lights the stage that failed")
    def card(i, kind=""):
        c, t, _ = cases[i]
        x, y = 20 + (i % 3) * 590, 16 + (i // 3) * 168
        cls = "node node--bad" if kind == "bad" else "node"
        body = rect(x, y, 560, 150, cls, rx=14) + text(x + 22, y + 32, f"Case {c}", 22, 700, "t-bad" if kind else "t")
        for j, ln in enumerate(wrap(t, 54)):
            body += text(x + 22, y + 64 + j * 24, esc(ln), 19, 400, "t-bad" if kind else "t2")
        return body
    s += '<g data-build="0">\n' + "".join(card(i) for i in range(6)) + strip(400) + '</g>\n'
    for i, (c, _, stages) in enumerate(cases):
        body = card(i, "bad") + "".join(strip_tile(j, 400, "bad") for j in stages)
        body += small_badge(16 + stages[0] * 224 + 4, 404, c, r=16, size=17)
        s += f'<g data-build="{i + 1}">\n{body}</g>\n'
    return s + "</svg>\n"


# ---------------------------------------------------------------- slide 22: the HTTPS chart
def https_chart():
    W, H = 1800, 560
    px0, px1, py0, py1 = 150, 1720, 56, 470
    X = xscale(2015.5, 2027.2, px0, px1)
    Y = lambda v: round(py1 - v / 100 * (py1 - py0), 1)
    s = head(W, H, "Share of page loads over HTTPS, late 2015 to 2026, for Firefox globally and in the United States and for Chrome on "
                   "Windows and on Mac: from about 40 percent to above 90; with the four protocol steps that removed fields from the "
                   "network sensor — HTTPS by default, TLS 1.3, DNS over HTTPS, Encrypted Client Hello")
    s += '<g data-build="0">\n'
    for v in (0, 25, 50, 75, 100):
        s += f'<path d="M{px0} {Y(v)}H{px1}" class="{"axis" if v == 0 else "grid"}"/>\n' + text(px0 - 14, Y(v), f"{v}%", 17, 500, "t2", "end")
    for yr in range(2016, 2028):
        s += text(X(yr), py1 + 24, str(yr), 17, 500, "t2", "middle")
    ends = []
    for n, ser in enumerate(HTTPS["series"], start=1):
        pts = ser["points"]
        s += f'<polyline points="{" ".join(f"{X(y)},{Y(v)}" for y, v in pts)}" class="line-{n}"/>\n'
        for y, v in pts:
            s += circle(X(y), Y(v), 5, f"pt-{n}", f'{ser["label"]}, {y:.1f}: {v}%')
        ends.append([Y(pts[-1][1]), X(pts[-1][0]) + 12, n, ser["short"]])
        s += rect(px0 + 20 + (n - 1) * 230, 22, 18, 18, f"pt-{n}", rx=4) + text(px0 + 46 + (n - 1) * 230, 31, esc(ser["label"]), 17, 500, "t2")
    # direct labels at the line ends, pushed apart so they never overlap
    ends.sort()
    for j in range(1, len(ends)):
        ends[j][0] = max(ends[j][0], ends[j - 1][0] + 22)
    for ly, lx, n, short in ends:
        s += text(lx, ly, esc(short), 17, 700, {1: "t-part-1", 2: "t-part-2", 3: "t-acc", 4: "t-part-4"}[n])
    s += '</g>\n'
    # the four protocol steps: markers labelled low in the plot, where no series runs
    steps = [(2015.92, "HTTPS by default · Let's Encrypt, 2015"), (2018.62, "TLS 1.3 · 2018"), (2018.8, "DNS over HTTPS · 2018"), (2023.72, "Encrypted Client Hello · 2023")]
    for k, (yr, label) in enumerate(steps, start=1):
        x = X(yr)
        ly = py1 - 22 - ((k - 1) % 2) * 28
        s += (f'<g data-build="{k}">\n<path d="M{x} {py0}V{py1}" class="marker"/>\n'
              + text(x + 8, ly, esc(label), 17, 700, "t-bad") + '</g>\n')
    return s + "</svg>\n"


# ---------------------------------------------------------------- write everything
(OUT / "ladder.svg").write_text(ladder())
(OUT / "original-model.svg").write_text(original_model())
(OUT / "timeline-overview.svg").write_text(timeline_overview())
for k in range(4):
    (OUT / f"period-{k + 1}.svg").write_text(period_timeline(k))
(OUT / "breaks.svg").write_text(breaks_timeline())
(OUT / "attack-matrix.svg").write_text(attack_matrix(
    "The Enterprise ATT&CK matrix, schematic: 15 tactic columns with a few real techniques each and the true per-tactic counts; "
    "a classic trojan lit as a path of seven techniques across seven tactics", TROJAN_PATH,
    ATTACK["version"] + " · hover a cell for its name"))
(OUT / "attack-fileless.svg").write_text(attack_matrix(
    "The Enterprise ATT&CK matrix with the recurring scenario lit step by step: valid accounts, PowerShell with command obfuscation, "
    "exploitation for privilege escalation, disable or modify tools, ingress tool transfer, process injection and reflective code "
    "loading, discovery and collection, web protocols and exfiltration over the C2 channel", FILELESS_PATH,
    ATTACK["version"] + " · hover a cell for its name"))
(OUT / "benign-files.svg").write_text(benign_files())
(OUT / "pipeline.svg").write_text(pipeline())
(OUT / "pipeline-host.svg").write_text(pipeline_host())
(OUT / "pipeline-network.svg").write_text(pipeline_network())
(OUT / "pipeline-breaks.svg").write_text(pipeline_breaks())
(OUT / "pipeline-options.svg").write_text(pipeline_options())
(OUT / "exercise.svg").write_text(exercise())
(OUT / "https-chart.svg").write_text(https_chart())
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
