#!/usr/bin/env python3
"""Build lecture-2/deck/index.html from lecture-2/slides/*.md.

The markdown slide files stay the source of truth. This script:
  * parses each slide's title, timing, module, on-slide content, speaker notes,
    interaction, transition and sources;
  * splits the on-slide content into the body, the "Build, one step per click" captions
    (rendered as stepped captions, one visible at a time) and the figures;
  * inlines the lecture's SVG diagrams so their data-build groups can be stepped, and
    links the paper figures from ../figures/;
  * picks a layout per slide: title, diagram (SVG + captions), figure (two columns) or text;
  * emits a part divider where the part changes, a sources panel per slide (the
    Lecture 1 button that opens a panel) and an aside with the speaker notes.

Run:  python3 lecture-2/deck/build.py
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LECTURE = HERE.parent
SLIDES = LECTURE / "slides"
FIGURES = LECTURE / "figures"
OUT = HERE / "index.html"

SECTION_NAMES = ["On-slide content", "Speaker notes", "Interaction", "Transition", "Sources"]
DECK_URL = "rvasilenko-ai.github.io/malware-and-ai/lecture-2/deck"

# module -> part number; the first module of a part names its divider
PART_OF = {
    "Opening": 0,
    "From adversarial ML to attacks on LLMs": 1,
    "From model to agent": 2,
    "The agent becomes an attacker": 3,
    "Case A: an agent the attacker owns": 3,
    "Case B: a trusted agent hijacked": 3,
    "The two cases compared": 3,
    "Defense and research": 4,
}
PART_TITLES = {
    1: ("Attacking the model", "Adversarial machine learning, then the failure that LLMs add"),
    2: ("From model to agent", "The harness, the loop, the attack surface, the supply chain"),
    3: ("The agent becomes an attacker", "Two cases: an agent the attacker owns, and a trusted agent hijacked"),
    4: ("Defense and research", "Case A and Case B defenses, the cheap-model funnel, the weak watching the strong"),
}
SERIES_LINE = "Malware and AI · Lecture 2"


# --------------------------------------------------------------------------- inline markdown
def inline(text: str) -> str:
    s = html.escape(text, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"(?<![\w*])\*([^*]+?)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def pre_block(lines: list[str]) -> str:
    cols = max((len(l) for l in lines), default=40)
    body = html.escape("\n".join(lines), quote=False)
    return f'<pre class="schematic" style="--cols:{cols}"><code>{body}</code></pre>'


# --------------------------------------------------------------------------- block markdown
def md_to_html(md: str) -> str:
    out: list[str] = []
    lines = md.strip("\n").split("\n")
    i = 0
    para: list[str] = []

    def flush() -> None:
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        msvg = re.match(r"^!\[(.*?)\]\((\.\./figures/[^)]+\.svg)\)$", s)
        if msvg:
            flush()
            out.append(f'<figure class="flow-diagram">{inline_svg(msvg.group(2))}</figure>')
            i += 1
            continue
        if s.startswith("```"):
            flush(); i += 1; buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append(pre_block(buf)); continue
        if s.startswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", c) for c in rows[1]):
                head, body = rows[0], rows[2:]
            else:
                head, body = [], rows
            t = ['<table class="data">']
            if head:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table>")
            out.append("".join(t)); continue
        if s.startswith("- "):
            flush(); items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if re.match(r"^\d+\. ", s):
            flush(); items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        if s.startswith(">"):
            flush(); qs = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                qs.append(lines[i].strip()[1:].strip()); i += 1
            out.append('<blockquote class="callout">' + "".join(f"<p>{inline(q)}</p>" for q in qs if q) + "</blockquote>"); continue
        m = re.match(r"^(#{1,3}) (.+)$", s)
        if m:
            flush(); level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>"); i += 1; continue
        if not s:
            flush(); i += 1; continue
        para.append(line); i += 1
    flush()
    return "\n".join(out)


# --------------------------------------------------------------------------- slide files
def parse_slide(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^# Slide (\d+) — (.+)$", text, flags=re.M)
    if not m:
        sys.exit(f"{path.name}: missing slide heading")
    number, title = int(m.group(1)), m.group(2).strip()
    timing = re.search(r"^\*\*Timing:\*\* (.+?)\s*$", text, flags=re.M).group(1).strip()
    module = re.search(r"^\*\*Module:\*\* (.+?)\s*$", text, flags=re.M).group(1).strip()
    pattern = re.compile(r"^## (" + "|".join(re.escape(n) for n in SECTION_NAMES) + r")(?: \([^)]*\))?\s*$", flags=re.M)
    marks = list(pattern.finditer(text))
    sections: dict[str, str] = {}
    for idx, mk in enumerate(marks):
        end = marks[idx + 1].start() if idx + 1 < len(marks) else len(text)
        sections[mk.group(1)] = text[mk.end():end].strip("\n")
    return {"number": number, "title": title, "timing": timing, "module": module, "part": PART_OF.get(module, 0),
            "file": path.name, "id": f"s{number}",
            **{k.lower().replace(" ", "_"): v for k, v in sections.items()}}


def split_content(md: str) -> tuple[str, list[str], list[dict]]:
    """Separate the body from the build captions and the figures."""
    lines = md.split("\n")
    body: list[str] = []
    captions: list[str] = []
    figures: list[dict] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("Build, one step per click"):
            i += 1
            while i < len(lines) and (not lines[i].strip() or re.match(r"^\d+\. ", lines[i].strip())):
                if lines[i].strip():
                    captions.append(re.sub(r"^\d+\. ", "", lines[i].strip()))
                i += 1
            continue
        m = re.match(r"^!\[(.*?)\]\(([^)]+)\)$", s)
        if m and m.group(2).endswith(".svg"):
            # an SVG renders inline in the body flow; its following *caption* line is dropped (the diagram carries its own label)
            body.append(lines[i]); i += 1
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.fullmatch(r"\*(.+)\*", lines[j].strip()):
                i = j + 1
            continue
        if m:
            fig = {"alt": m.group(1), "src": m.group(2), "caption": ""}
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.fullmatch(r"\*(.+)\*", lines[j].strip()):
                fig["caption"] = lines[j].strip()[1:-1]
                j += 1
            figures.append(fig); i = j; continue
        body.append(lines[i]); i += 1
    return "\n".join(body), captions, figures


def inline_svg(src: str) -> str:
    svg = (FIGURES / Path(src).name).read_text(encoding="utf-8")
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
    svg = re.sub(r'<svg([^>]*?)\swidth="\d+"\sheight="\d+"', r"<svg\1", svg, count=1)
    svg = svg.replace("<svg ", '<svg class="diagram" ', 1)
    # the file's own <style> is for standalone viewing; in the deck the classes take the deck's tokens
    svg = re.sub(r"<style>.*?</style>\s*", "", svg, count=1, flags=re.S)
    # every figure defines the same marker ids; inlined into one document, url(#arrow) would resolve to
    # the first figure's copy, which is hidden on every other slide, so suffix the ids per figure
    stem = re.sub(r"[^a-z0-9]+", "-", Path(src).stem.lower())
    svg = re.sub(r'\bid="(arrow(?:-bad|-good)?)"', lambda m: f'id="{m.group(1)}-{stem}"', svg)
    return re.sub(r"url\(#(arrow(?:-bad|-good)?)\)", lambda m: f"url(#{m.group(1)}-{stem})", svg)


def max_build(svg: str) -> int:
    builds = [int(x) for x in re.findall(r'data-build="(\d+)"', svg)]
    return max(builds) if builds else 0


# --------------------------------------------------------------------------- rendering
def captions_html(captions: list[str], static: bool = False) -> str:
    if not captions:
        return ""
    if static:
        # nothing else on the slide steps, so clicking through one line at a time is friction: show the list at once
        return '<div class="step-captions step-captions--static">' + "".join(f"<p>{inline(c)}</p>" for c in captions) + "</div>"
    return '<div class="step-captions">' + "".join(f'<p data-build="{k}">{inline(c)}</p>' for k, c in enumerate(captions)) + "</div>"


def sources_html(md: str | None) -> str:
    if not md:
        return ""
    items = [l.strip()[2:] for l in md.split("\n") if l.strip().startswith("- ")]
    if not items:
        return ""
    return (f'<details class="srcs"><summary>Sources ({len(items)})</summary><div class="panel"><ul>'
            + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul></div></details>")


def notes_html(slide: dict) -> str:
    parts = [f'<p class="meta"><b>Slide {slide["number"]}</b> · {html.escape(slide["timing"])} · {html.escape(slide["module"])}</p>']
    if slide.get("speaker_notes"):
        parts.append(md_to_html(slide["speaker_notes"]))
    if slide.get("interaction"):
        parts.append("<h4>Interaction</h4>" + md_to_html(slide["interaction"]))
    if slide.get("transition"):
        parts.append('<p class="transition">' + inline(slide["transition"].strip()) + "</p>")
    return '<aside class="notes">' + "\n".join(parts) + "</aside>"


def footer_html(slide: dict, total: int) -> str:
    return (f'<footer class="slide-foot"><span class="eyebrow">{html.escape(slide["module"])}</span>'
            f'<span class="count">{slide["number"]} / {total} · {html.escape(slide["timing"])}</span></footer>')


def section(slide: dict, sid: str, kind: str, inner: str, steps: int, total: int, extra_cls: str = "") -> str:
    cls = f"slide slide--{kind} {extra_cls}".strip()
    return (f'<section class="{cls}" id="{sid}" data-id="{sid}" data-part="{slide["part"]}" data-steps="{steps}" '
            f'data-number="{slide["number"]}">\n{inner}\n{sources_html(slide.get("sources"))}\n{footer_html(slide, total)}\n{notes_html(slide)}\n</section>')


def render_title(slide: dict, total: int) -> str:
    content = slide["on-slide_content"]
    display = re.search(r"^# (.+)$", content, flags=re.M).group(1)
    lead = re.search(r"^> (.+)$", content, flags=re.M).group(1)
    inner = (f'<div class="title-block"><p class="eyebrow">{SERIES_LINE}</p>'
             f'<h1 class="display">{inline(display)}</h1><p class="lead">{inline(lead)}</p>'
             f'<p class="follow">Follow along on your laptop or phone: <span class="url">{DECK_URL}</span></p></div>')
    return section(slide, "s1", "title", inner, 0, total)


def render_divider(part: int, slides_in: list[dict], total: int) -> str:
    title, sub = PART_TITLES[part]
    modules = []
    for s in slides_in:
        if s["module"] not in modules:
            modules.append(s["module"])
    first, last = slides_in[0]["number"], slides_in[-1]["number"]
    items = "".join(f"<li>{html.escape(m)}</li>" for m in modules)
    inner = (f'<div class="divider-num">{part}</div><div class="divider-body"><p class="eyebrow">Part {part}</p>'
             f'<h2 class="divider-title">{html.escape(title)}</h2><p class="lead">{html.escape(sub)}</p>'
             f'<ul class="divider-list">{items}</ul></div>')
    return (f'<section class="slide slide--divider" id="p{part}" data-id="p{part}" data-part="{part}" data-steps="0" data-number="">\n{inner}\n'
            f'<footer class="slide-foot"><span class="eyebrow">Part {part}</span><span class="count">slides {first}–{last}</span></footer>\n</section>')


def render_slide(slide: dict, total: int) -> str:
    body_md, captions, figures = split_content(slide["on-slide_content"])
    pngs = [f for f in figures if not f["src"].endswith(".svg")]
    body_html = md_to_html(body_md)
    h2 = f'<h2 class="slide-title">{inline(slide["title"])}</h2>'
    has_diagram = 'class="flow-diagram"' in body_html
    if has_diagram:
        # a text schematic in the same slide is redundant once the diagram is present
        body_html = re.sub(r'<pre class="schematic".*?</pre>\s*', "", body_html, flags=re.S)
    static_caps = bool(captions) and max_build(body_html) == 0
    steps = 0 if static_caps else max(len(captions) - 1, max_build(body_html))

    if has_diagram and not pngs:
        tables = re.findall(r"<table.*?</table>", body_html, flags=re.S)
        has_list = "<ul>" in body_html or "<ol>" in body_html
        if not has_list and len(tables) <= 1:
            # centerpiece diagram: a big diagram, then captions; a table (if any) moves to a continuation slide
            if tables:
                callouts = re.findall(r"<blockquote.*?</blockquote>", body_html, flags=re.S)
                main = re.sub(r"<blockquote.*?</blockquote>", "", re.sub(r"<table.*?</table>", "", body_html, flags=re.S), flags=re.S)
                inner = h2 + main + captions_html(captions, static_caps)
                out = [section(slide, slide["id"], "diagram", inner, steps, total)]
                inner2 = h2.replace("</h2>", ' <span class="cont">continued</span></h2>') + "".join(tables) + "".join(callouts)
                out.append(section(slide, slide["id"] + "b", "text", inner2, 0, total, "slide--cont"))
                return "\n".join(out)
            inner = h2 + body_html + captions_html(captions, static_caps)
            return section(slide, slide["id"], "diagram", inner, steps, total)
        # inline diagram among lists or several tables: everything stays in the flow, the diagram is smaller
        inner = h2 + f'<div class="body">{body_html}</div>' + captions_html(captions, static_caps)
        return section(slide, slide["id"], "has-diagram", inner, steps, total, density_class(estimate_height(body_html, bool(captions))))

    if pngs:
        # the paper figures are the real diagram on these slides; drop a redundant text schematic
        figs = "".join(f'<figure><img src="../figures/{html.escape(Path(f["src"]).name)}" alt="{html.escape(f["alt"])}">'
                       f'<figcaption>{inline(f["caption"] or f["alt"])}</figcaption></figure>' for f in pngs)
        rest = re.sub(r'<pre class="schematic".*?</pre>\s*', "", body_html, flags=re.S)
        inner = (h2 + f'<div class="cols"><div class="col-text">{rest}</div><div class="col-fig{" one" if len(pngs) == 1 else ""}">{figs}</div></div>'
                 + captions_html(captions, static_caps))
        est = 100 + max(estimate_height(rest, False) - 100, len(pngs) * 320) + (38 * len(captions) if static_caps else 80)
        return section(slide, slide["id"], "figure", inner, steps, total, density_class(est))

    inner = h2 + f'<div class="body">{body_html}</div>' + captions_html(captions, static_caps)
    return section(slide, slide["id"], "text", inner, steps, total, density_class(estimate_height(body_html, bool(captions)) + (38 * len(captions) if static_caps else 0)))


def estimate_height(body_html: str, has_captions: bool) -> int:
    """Rough stage-pixel height of a body at the normal type scale; drives the density class."""
    h = 100
    for m in re.finditer(r'<pre class="schematic"[^>]*>(.*?)</pre>', body_html, flags=re.S):
        h += (m.group(1).count("\n") + 1) * 35 + 42
    for m in re.finditer(r"<table.*?</table>", body_html, flags=re.S):
        h += m.group(0).count("<tr") * 54 + 22
    text_only = lambda s: len(re.sub(r"<[^>]+>", "", s))
    for m in re.finditer(r"<blockquote.*?</blockquote>", body_html, flags=re.S):
        h += (text_only(m.group(0)) // 115 + 1) * 40 + 36
    no_quotes = re.sub(r"<blockquote.*?</blockquote>", "", body_html, flags=re.S)
    for m in re.finditer(r"<p>(.*?)</p>", no_quotes, flags=re.S):
        h += (text_only(m.group(1)) // 135 + 1) * 40 + 16
    for m in re.finditer(r"<li>(.*?)</li>", body_html, flags=re.S):
        h += (text_only(m.group(1)) // 135 + 1) * 38
    h += 46 * body_html.count("<h3")
    h += 400 * body_html.count('class="flow-diagram"')
    if has_captions:
        h += 80
    return h


def density_class(est: int) -> str:
    return "slide--denser" if est > 965 else ("slide--dense" if est > 850 else "")


# --------------------------------------------------------------------------- page
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>When the Attacker Is an Agent</title>
<meta name="description" content="Lecture 2 of the Malware and AI series: adversarial ML, attacks on LLMs, the agent as a system, and what happens when the agent is the attacker.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%277%27 fill=%27%230369a1%27/%3E%3Ccircle cx=%2716%27 cy=%2716%27 r=%277%27 fill=%27none%27 stroke=%27%23fff%27 stroke-width=%273%27/%3E%3C/svg%3E">
<link rel="stylesheet" href="deck.css">
<script>try{var t=localStorage.getItem('deck2-theme');if(t)document.documentElement.setAttribute('data-theme',t);}catch(e){}</script>
</head>
<body>
<div class="deck-viewport">
<div class="deck-stage" id="stage">
"""
TAIL = """</div>
<div class="deck-progress"><div class="bar" id="progress"></div></div>
</div>
<aside class="deck-notes" id="notes" hidden><div class="notes-head"><b>Presenter notes</b><span>N to hide</span></div><div class="notes-body" id="notes-body"></div></aside>
<div class="deck-help" id="help" hidden><div class="help-card"><h2>Keys</h2><table>
<tr><th><kbd>→</kbd> <kbd>space</kbd></th><td>next step or slide</td></tr><tr><th><kbd>←</kbd></th><td>previous</td></tr>
<tr><th><kbd>Home</kbd> <kbd>End</kbd></th><td>first, last slide</td></tr><tr><th><kbd>N</kbd></th><td>presenter notes</td></tr>
<tr><th><kbd>S</kbd></th><td>sources of this slide</td></tr><tr><th><kbd>T</kbd></th><td>light or dark</td></tr>
<tr><th><kbd>F</kbd></th><td>full screen</td></tr><tr><th><kbd>?</kbd></th><td>this help</td></tr></table>
<p>Links: <code>#/s12/3</code> is slide 12 at step 3, <code>#/p2</code> is the divider of part 2.</p></div></div>
<script src="deck.js"></script>
</body>
</html>
"""


def main() -> None:
    files = sorted(SLIDES.glob("[0-9][0-9]-*.md"))
    slides = [parse_slide(p) for p in files]
    total = len(slides)
    out: list[str] = [HEAD]
    current_part = None
    for idx, slide in enumerate(slides):
        if slide["part"] != current_part and slide["part"] in PART_TITLES:
            part = slide["part"]
            out.append(render_divider(part, [s for s in slides if s["part"] == part], total))
        current_part = slide["part"]
        out.append(render_title(slide, total) if slide["number"] == 1 else render_slide(slide, total))
    out.append(TAIL)
    OUT.write_text("\n".join(out), encoding="utf-8")
    n_sections = sum(1 for s in out if s.startswith("<section"))
    print(f"wrote {OUT.relative_to(LECTURE.parent)}: {total} slides, {n_sections} stage sections, {sum(len(s) for s in out)//1024} KB")


if __name__ == "__main__":
    main()
