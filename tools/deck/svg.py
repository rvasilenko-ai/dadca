"""Shared SVG primitives for the lecture diagrams.

The SVGs carry no colour literals on their shapes: every element has a class, and a <style> block at
the top maps the classes to CSS variables with light values and a prefers-color-scheme dark block, so
the files theme themselves when viewed on their own (GitHub, an editor preview). The deck build strips
that <style> when it inlines a diagram and styles the same classes from its own tokens, so the deck's
theme toggle recolours the diagrams too. No background rectangle: the diagram sits on the page.

Groups carry data-build="n" so the deck runtime can reveal them step by step.
"""
import pathlib
import sys


def out_dir() -> pathlib.Path:
    """The figures directory a generator writes to: its first argument."""
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    return out


FONT = "Inter, Helvetica Neue, Helvetica, Arial, sans-serif"


STYLE = """<style>
svg{--surface:#ffffff;--surface-2:#eceff6;--frame:#f8fafc;--ink:#1f2937;--ink-2:#4b5563;--ink-3:#5b6580;--line:#9ca3af;--rule:#cbd5e1;--rule-3:#6c768e;
--acc:#0284c7;--acc-wash:#e0f2fe;--acc-ink:#075985;--bad:#dc2626;--bad-wash:#fee2e2;--bad-ink:#991b1b;
--good:#15803d;--good-wash:#dcfce7;--good-ink:#14532d;--on-badge:#ffffff;
--part-0:#0369a1;--part-1:#b45309;--part-2:#5b3fd0;--part-3:#b91c1c;--part-4:#0f766e}
@media (prefers-color-scheme: dark){svg{--surface:#141a2a;--surface-2:#1b2234;--frame:#10172a;--ink:#eef1f8;--ink-2:#c6cddd;--ink-3:#9aa4ba;--line:#8b96b0;--rule:#344062;--rule-3:#7f8aa6;
--acc:#7cc4ff;--acc-wash:#10304a;--acc-ink:#bfe3ff;--bad:#f87171;--bad-wash:#3b1515;--bad-ink:#fecaca;
--good:#4ade80;--good-wash:#0f2e1c;--good-ink:#bbf7d0;--on-badge:#0b0f1a;
--part-0:#7cc4ff;--part-1:#f0a04b;--part-2:#a78bfa;--part-3:#f87171;--part-4:#2dd4bf}}
.node{fill:var(--surface);stroke:var(--rule);stroke-width:2.5}.node--model{fill:var(--acc-wash);stroke:var(--acc);stroke-width:4}
.node--bad{fill:var(--bad-wash);stroke:var(--bad);stroke-width:4}.node--good{fill:var(--good-wash);stroke:var(--good);stroke-width:4}
.frame{fill:var(--frame);stroke:var(--rule);stroke-width:2.5}.env{fill:none;stroke:var(--line);stroke-width:3;stroke-dasharray:14 10}
.t{fill:var(--ink)}.t2{fill:var(--ink-2)}.t-acc{fill:var(--acc-ink)}.t-bad{fill:var(--bad-ink)}.t-good{fill:var(--good-ink)}.t-badge{fill:var(--on-badge)}
.edge{fill:none;stroke:var(--line);stroke-width:3;stroke-linecap:round}.edge--strong{stroke:var(--ink-2);stroke-width:4}
.edge--bad{stroke:var(--bad);stroke-width:4}.edge--good{stroke:var(--good);stroke-width:4}
.arrow{fill:var(--ink-2)}.arrow--bad{fill:var(--bad)}.arrow--good{fill:var(--good)}
.badge--bad{fill:var(--bad);stroke:var(--surface);stroke-width:3}.badge--good{fill:var(--good);stroke:var(--surface);stroke-width:3}
.ctx-bar{fill:var(--rule)}.ring{fill:none;stroke:var(--ink);stroke-width:4}.dot{fill:var(--ink)}
.axis{stroke:var(--rule-3);stroke-width:2}.grid{stroke:var(--rule);stroke-width:1.5}.lane{fill:var(--surface);stroke:var(--rule);stroke-width:1}
.band-1{fill:var(--part-1);fill-opacity:.11}.band-2{fill:var(--part-2);fill-opacity:.11}.band-3{fill:var(--part-3);fill-opacity:.11}.band-4{fill:var(--part-4);fill-opacity:.11}
.t-part-1{fill:var(--part-1)}.t-part-2{fill:var(--part-2)}.t-part-3{fill:var(--part-3)}.t-part-4{fill:var(--part-4)}
.dot--muted{fill:var(--rule-3)}.dot--key{fill:var(--acc)}.dot--anchor{fill:var(--bad)}
.bar{fill:var(--acc);fill-opacity:.85}.bar--muted{fill:var(--rule)}.bar--bad{fill:var(--bad);fill-opacity:.85}
.line-1{stroke:var(--part-1)}.line-2{stroke:var(--part-2)}.line-3{stroke:var(--part-0)}.line-4{stroke:var(--part-4)}
.line-1,.line-2,.line-3,.line-4{fill:none;stroke-width:4;stroke-linejoin:round;stroke-linecap:round}
.pt-1{fill:var(--part-1)}.pt-2{fill:var(--part-2)}.pt-3{fill:var(--part-0)}.pt-4{fill:var(--part-4)}
.cell{fill:var(--surface);stroke:var(--rule);stroke-width:1.5}.cell--sub{fill:var(--surface-2);stroke:var(--rule);stroke-width:1.5}
.cell--lit{fill:var(--bad-wash);stroke:var(--bad);stroke-width:3}.colhead{fill:var(--surface-2);stroke:var(--rule);stroke-width:1.5}
.marker{stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 6}.hit{fill:transparent}
</style>"""


def esc(s):
    """Escape text for an SVG text node or attribute."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def wrap(s, width):
    """Greedy word wrap to about `width` characters per line (SVG text does not wrap itself)."""
    words, lines, cur = str(s).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)
    return lines


def circle(cx, cy, r, cls, tip=None):
    """A circle; with `tip`, a larger transparent hit circle on top carries the tooltip, so small dots are easy to hover."""
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls}"/>\n'
    if tip:
        s += f'<circle cx="{cx}" cy="{cy}" r="{max(r + 6, 12)}" class="hit"><title>{esc(tip)}</title></circle>\n'
    return s


def rect(x, y, w, h, cls, rx=0, tip=None):
    """A rectangle, with a native hover tooltip when `tip` is given."""
    inner = f"<title>{esc(tip)}</title>" if tip else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}">{inner}</rect>\n'


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


def arrow(x1, y1, x2, y2, red=False, green=False, strong=True):
    return edge(f"M{x1} {y1}L{x2} {y2}", strong=strong, arrow=True, red=red, green=green)


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
