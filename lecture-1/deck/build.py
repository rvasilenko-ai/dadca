#!/usr/bin/env python3
"""Build lecture-1/deck/index.html from lecture-1/slides/*.md.

The markdown slide files remain the source of truth. This script:
  * parses each slide's metadata, on-slide content, speaker notes, interaction,
    transition and sources;
  * converts the on-slide markdown subset to HTML;
  * renders the four period slides as a zoomed timeline with one headline per track;
  * substitutes a hand-written template from deck/templates/<slug>.html (or NN.html) when one
    exists ({{auto}} inside a template injects the converted markdown body);
  * emits speaker notes for the reveal.js notes plugin (press S while presenting).

Run:  python3 lecture-1/deck/build.py
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE.parent / "slides"
TEMPLATES = HERE / "templates"
OUT = HERE / "index.html"

def period_slides() -> dict[int, str]:
    """Period slides are the files named NN-era-*.md, in order; numbering may shift."""
    files = sorted(SLIDES.glob("[0-9][0-9]-era-*.md"))
    return {int(p.name[:2]): f"p{i + 1}" for i, p in enumerate(files)}


PERIOD_SLIDES = period_slides()
TRACK_KEYS = {
    "Motive and money": "money",
    "Attackers": "attackers",
    "Operating system": "os",
    "Internet": "internet",
    "Security products": "products",
}
SECTION_NAMES = ["On-slide content", "Speaker notes", "Interaction", "Transition", "Sources"]
MODULE_SLUGS = {
    "Where is the malware?": "m1",
    "From malicious programs to adversarial capabilities": "m2",
    "ATT&CK as a language for behavior": "m3",
    "Detection pipelines: design and evolution": "m4",
    "Synthesis": "m5",
}


# --------------------------------------------------------------------------- inline
def inline(text: str) -> str:
    """Escape HTML, then apply the inline markdown subset used in the slides."""
    s = html.escape(text, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        s,
    )
    return s


# --------------------------------------------------------------------------- blocks
def md_to_html(md: str) -> str:
    """Convert the markdown subset used in slide files to HTML."""
    out: list[str] = []
    lines = md.strip("\n").split("\n")
    i = 0
    para: list[str] = []

    def flush_para() -> None:
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_para()
            i += 1
            buf: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            out.append('<pre class="ascii"><code>' + html.escape("\n".join(buf), quote=False) + "</code></pre>")
            continue

        if stripped.startswith("|"):
            flush_para()
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", c) for c in rows[1]):
                head, body = rows[0], rows[2:]
            else:
                head, body = [], rows
            t = ["<table>"]
            if head:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        if stripped.startswith("- "):
            flush_para()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue

        if re.match(r"^\d+\. ", stripped):
            flush_para()
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue

        if stripped.startswith(">"):
            flush_para()
            qs = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                qs.append(lines[i].strip()[1:].strip())
                i += 1
            out.append('<blockquote class="callout">' + "".join(f"<p>{inline(q)}</p>" for q in qs if q) + "</blockquote>")
            continue

        m = re.match(r"^(#{1,3}) (.+)$", stripped)
        if m:
            flush_para()
            level = len(m.group(1))
            cls = ' class="display"' if level == 1 else ""
            out.append(f"<h{level}{cls}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if not stripped:
            flush_para()
            i += 1
            continue

        para.append(line)
        i += 1

    flush_para()
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

    sections: dict[str, str] = {}
    pattern = re.compile(r"^## (" + "|".join(map(re.escape, SECTION_NAMES)) + r")\s*$", flags=re.M)
    marks = list(pattern.finditer(text))
    for idx, mk in enumerate(marks):
        end = marks[idx + 1].start() if idx + 1 < len(marks) else len(text)
        sections[mk.group(1)] = text[mk.end():end].strip("\n")
    return {
        "number": number,
        "title": title,
        "timing": timing,
        "module": module,
        "slug": MODULE_SLUGS.get(module, "m0"),
        "file_slug": path.stem[3:],
        "file": path.name,
        **{k.lower().replace(" ", "_"): v for k, v in sections.items()},
    }


# --------------------------------------------------------------------------- period slides
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(])")


def render_period(slide: dict, period: str) -> str:
    """Zoomed period layout: context strip and period timeline, one headline per track,
    the detail chips behind a toggle (and in print), callout."""
    content = slide["on-slide_content"]
    headlines: list[tuple[str, str]] = []
    detail: list[tuple[str, str]] = []
    callout = ""
    current = "detail"
    for line in content.split("\n"):
        s = line.strip()
        if s.startswith("| Track"):
            current = "head" if "Headline" in s else "detail"
            continue
        m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|$", s)
        if m:
            (headlines if current == "head" else detail).append((m.group(1), m.group(2)))
        elif s.startswith(">"):
            callout += f"<p>{inline(s[1:].strip())}</p>"
    years = slide["title"].split(":")[0]
    parts = [
        f'<div class="period zoomed" data-period="{period}">',
        f'<div class="tl" data-component="timeline" data-mode="zoom" data-focus="{period}" aria-label="Timeline of {years} across five tracks; key events labelled"></div>',
        '<div class="headlines">',
    ]
    for name, text in headlines:
        key = TRACK_KEYS.get(name, "other")
        parts.append(f'<div class="hl" data-track="{key}"><span class="track-name">{inline(name)}</span><span class="hl-text">{inline(text)}</span></div>')
    parts.append('<button type="button" class="details-toggle" aria-pressed="false">details</button>')
    parts.append("</div>")
    parts.append('<div class="tracks detail">')
    for name, cell in detail:
        key = TRACK_KEYS.get(name, "other")
        items = [x.strip() for x in SENTENCE_SPLIT.split(cell) if x.strip()]
        chips = "".join(f'<li class="chip">{inline(it.rstrip("."))}</li>' for it in items)
        parts.append(f'<div class="track" data-track="{key}"><div class="track-name">{inline(name)}</div><ul class="chips">{chips}</ul></div>')
    parts.append("</div>")
    if callout:
        parts.append(f'<blockquote class="callout period-callout">{callout}</blockquote>')
    parts.append("</div>")
    parts.append(render_sources(slide))
    return "\n".join(parts)


# --------------------------------------------------------------------------- stage options
STAGE_QUESTIONS = {
    "sensor": "can the system observe the event or state?",
    "acquisition": "is the evidence collected and retained?",
    "extraction": "can usable artifacts or fields be recovered?",
    "representation": "what information is supplied to analysis?",
    "detection": "is a score, rule, or verdict produced?",
    "investigation": "can evidence be connected and explained?",
    "decision": "can an appropriate action be selected?",
    "response": "can the action be executed in time?",
}


def render_stage_options(slide: dict) -> str:
    """Group the Stage | Option | Captures | Misses table into one panel per stage, each option a card."""
    groups: dict[str, list[list[str]]] = {}
    for line in slide["on-slide_content"].split("\n"):
        st = line.strip()
        if not st.startswith("|") or st.startswith("| Stage") or re.match(r"^\|\s*-", st):
            continue
        cells = [c.strip() for c in st.strip("|").split("|")]
        if len(cells) != 4:
            continue
        groups.setdefault(cells[0], []).append(cells[1:])
    out = ['<div class="stage-panels">']
    for i, stage in enumerate(STAGE_QUESTIONS):
        rows = groups.get(stage, [])
        cards = "".join(
            f'<div class="opt"><b>{inline(o)}</b><p><span class="lab">sees</span>{inline(c)}</p><p><span class="lab">misses</span>{inline(m)}</p></div>'
            for o, c, m in rows)
        cols = 4 if len(rows) > 6 else 3
        out.append(
            f'<div class="stage-panel{" active" if i == 0 else ""}" data-stage="{stage}">'
            f'<h3><span class="k">{stage}</span> <span class="q">{STAGE_QUESTIONS[stage]}</span></h3>'
            f'<div class="opt-cards cols-{cols}">{cards}</div></div>'
        )
    out.append("</div>")
    # empty fragment markers: reveal.js steps them with Next/Previous and the deck script shows the matching panel
    for i, stage in enumerate(STAGE_QUESTIONS):
        if i:
            out.append(f'<span class="fragment stage-step" data-stage="{stage}" data-fragment-index="{i - 1}" aria-hidden="true"></span>')
    return "\n".join(out)


ROW_QUESTIONS = dict(STAGE_QUESTIONS)
ROW_QUESTIONS.update({
    "built for": "what problem it was bought to solve",
    "starved by": "what moved out of its field of view",
    "decision and response": "can an action be selected and executed in time?",
    "challenge": "what changed, and what remains observable",
})
ROW_IDS = {"built for": "built", "starved by": "starved", "challenge": "challenge", "decision and response": "decision,response"}


def render_stage_matrix(slide: dict) -> str:
    """A Stage | generation | generation ... table becomes one panel per stage (the generations side by side),
    stepped with Next and Previous; the full table is kept for print and behind a toggle."""
    header: list[str] = []
    rows: list[list[str]] = []
    for line in slide["on-slide_content"].split("\n"):
        st = line.strip()
        if not st.startswith("|") or re.match(r"^\|\s*-", st):
            continue
        cells = [c.strip() for c in st.strip("|").split("|")]
        if st.startswith("| Stage"):
            header = cells
        elif header and len(cells) == len(header):
            rows.append(cells)
    if not header or not rows:
        sys.exit(f"slide {slide['number']}: no Stage table for the matrix")
    cols = header[1:]
    out = ['<div class="panel-area">', '<div class="row-panels">']
    for k, cells in enumerate(rows):
        stage, values = cells[0], cells[1:]
        sid = ROW_IDS.get(stage, stage)
        cards = "".join(f'<div class="gen"><b>{inline(c)}</b><p>{inline(v)}</p></div>' for c, v in zip(cols, values))
        out.append(
            f'<div class="row-panel{" active" if k == 0 else ""}" data-row="{k}" data-stage="{sid}">'
            f'<h3><span class="k">{inline(stage)}</span> <span class="q">{html.escape(ROW_QUESTIONS.get(stage, ""))}</span></h3>'
            f'<div class="gen-cards">{cards}</div></div>'
        )
    out.append("</div>")
    out.append('<button type="button" class="table-toggle" aria-pressed="false">full table</button>')
    out.append("</div>")
    thead = "".join(f"<th>{inline(h)}</th>" for h in header)
    tbody = "".join(
        f'<tr data-stage="{ROW_IDS.get(c[0], c[0])}">' + "".join(f"<td>{inline(v)}</td>" for v in c) + "</tr>" for c in rows)
    out.append(f'<table class="matrix full"><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>')
    for k, cells in enumerate(rows):
        if k:
            out.append(f'<span class="fragment stage-step" data-row="{k}" data-stage="{ROW_IDS.get(cells[0], cells[0])}" data-fragment-index="{k - 1}" aria-hidden="true"></span>')
    return "\n".join(out)


def render_change_panels(slide: dict) -> str:
    """A What changed | Stage that broke | ... table becomes one panel per change: the change as the headline,
    the other columns as cards, the stage column lighting the strip; the full table is kept for print and a toggle."""
    header: list[str] = []
    rows: list[list[str]] = []
    for line in slide["on-slide_content"].split("\n"):
        st = line.strip()
        if not st.startswith("|") or re.match(r"^\|\s*-", st):
            continue
        cells = [c.strip() for c in st.strip("|").split("|")]
        if not header:
            header = cells
        elif len(cells) == len(header):
            rows.append(cells)
    if not header or not rows:
        sys.exit(f"slide {slide['number']}: no table for the change panels")
    try:
        si = next(i for i, h in enumerate(header) if h.lower().startswith("stage"))
    except StopIteration:
        sys.exit(f"slide {slide['number']}: no stage column")
    def sid(cells: list[str]) -> str:
        return ",".join(s.strip() for s in cells[si].split(","))
    out = ['<div class="panel-area">', '<div class="row-panels">']
    for k, cells in enumerate(rows):
        cards = "".join(f'<div class="gen"><b>{inline(h)}</b><p>{inline(v)}</p></div>' for h, v in zip(header[1:], cells[1:]))
        out.append(
            f'<div class="row-panel{" active" if k == 0 else ""}" data-row="{k}" data-stage="{sid(cells)}">'
            f'<h3><span class="q">{inline(header[0])}:</span> <span class="k">{inline(cells[0])}</span></h3>'
            f'<div class="gen-cards">{cards}</div></div>'
        )
    out.append("</div>")
    out.append('<button type="button" class="table-toggle" aria-pressed="false">full table</button>')
    out.append("</div>")
    thead = "".join(f"<th>{inline(h)}</th>" for h in header)
    tbody = "".join(f'<tr data-stage="{sid(c)}">' + "".join(f"<td>{inline(v)}</td>" for v in c) + "</tr>" for c in rows)
    out.append(f'<table class="matrix full"><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>')
    for k, cells in enumerate(rows):
        if k:
            out.append(f'<span class="fragment stage-step" data-row="{k}" data-stage="{sid(cells)}" data-fragment-index="{k - 1}" aria-hidden="true"></span>')
    return "\n".join(out)


def render_sources(slide: dict) -> str:
    """An expandable on-slide list of the slide's sources (the same list the notes carry), opening over the slide."""
    src = slide.get("sources") or ""
    links = re.findall(r"\[[^\]]+\]\(https?://[^)]+\)", src)
    if not links:
        return ""
    return (f'<details class="srcs"><summary>Sources ({len(links)})</summary>'
            f'<div class="panel">{md_to_html(src)}</div></details>')


# --------------------------------------------------------------------------- notes
def render_notes(slide: dict) -> str:
    bits = [f'<p class="plan"><strong>Planned {slide["timing"]}</strong> · {html.escape(slide["module"])}</p>']
    if slide.get("speaker_notes"):
        bits.append(md_to_html(slide["speaker_notes"]))
    if slide.get("interaction"):
        bits.append("<h4>Interaction</h4>" + md_to_html(slide["interaction"]))
    if slide.get("transition"):
        bits.append("<h4>Transition</h4>" + md_to_html(slide["transition"]))
    if slide.get("sources"):
        bits.append("<h4>Sources</h4>" + md_to_html(slide["sources"]))
    return '<aside class="notes">' + "\n".join(bits) + "</aside>"


# --------------------------------------------------------------------------- assembly
def render_slide(slide: dict) -> str:
    n = slide["number"]
    auto = md_to_html(slide["on-slide_content"])
    tpl = TEMPLATES / f"{slide['file_slug']}.html"
    if not tpl.exists():
        tpl = TEMPLATES / f"{n:02d}.html"
    if n in PERIOD_SLIDES:
        body = render_period(slide, PERIOD_SLIDES[n])
        heading = f'<h2 class="title">{inline(slide["title"])}</h2>'
    elif tpl.exists():
        body = tpl.read_text(encoding="utf-8").replace("{{auto}}", auto).replace("{{title}}", inline(slide["title"]))
        if "{{stage_options}}" in body:
            body = body.replace("{{stage_options}}", render_stage_options(slide))
        if "{{stage_matrix}}" in body:
            body = body.replace("{{stage_matrix}}", render_stage_matrix(slide))
        if "{{change_panels}}" in body:
            body = body.replace("{{change_panels}}", render_change_panels(slide))
        if "{{sources}}" in body:
            body = body.replace("{{sources}}", render_sources(slide))
        heading = ""  # templates own their heading
    else:
        body = auto
        heading = f'<h2 class="title">{inline(slide["title"])}</h2>'
    return (
        f'<section class="slide s{n} k-{slide["file_slug"]} {slide["slug"]}" data-slide="{n}" data-module="{html.escape(slide["module"])}" '
        f'data-timing="{html.escape(slide["timing"])}">\n{heading}\n<div class="body">\n{body}\n</div>\n'
        f'<footer class="chrome"><span class="module">{html.escape(slide["module"])}</span>'
        f'<span class="timing">min {html.escape(slide["timing"].replace(" minutes", ""))}</span></footer>\n{render_notes(slide)}\n</section>'
    )


def main() -> None:
    files = sorted(SLIDES.glob("[0-9][0-9]-*.md"))
    slides = [parse_slide(p) for p in files]
    expected = list(range(1, len(slides) + 1))
    if [s["number"] for s in slides] != expected:
        sys.exit("slide numbering is not contiguous")
    sections = "\n\n".join(render_slide(s) for s in slides)
    page = (HERE / "page.html").read_text(encoding="utf-8")
    page = page.replace("{{SECTIONS}}", sections).replace("{{COUNT}}", str(len(slides)))
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parent.parent)} with {len(slides)} slides")


if __name__ == "__main__":
    main()
