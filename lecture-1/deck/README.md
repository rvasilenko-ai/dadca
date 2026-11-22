# Lecture 1 deck

The HTML slides generated from the markdown sources in `../slides/`. The markdown remains the source of truth; do not edit `index.html` by hand. The deck runs on the machinery shared by every lecture in `tools/deck/` (the builder, the runtime, the theme and the SVG primitives), so the lectures stay visually in sync.

## Build

```bash
python3 lecture-1/tools/gen_diagrams.py lecture-1/figures   # the SVG figures, from tools/data.py
python3 lecture-1/deck/build.py                              # the deck
```

Then open `lecture-1/deck/index.html` in a browser, or serve the `lectures/` folder (`python3 -m http.server`) and open `/lecture-1/deck/`. Everything is local: no dependencies, no web fonts, no network needed in the lecture hall. `index.html` links `../../tools/deck/deck.css` and `deck.js`, so keep the checkout together.

## Present

| Key | Action |
| --- | --- |
| → or Space | next step, then next slide |
| ← | previous |
| Home, End | first, last slide |
| N | presenter notes (planned minutes, talking points, notes, interaction, transition) |
| S | the slide's sources, in a panel |
| T | light or dark theme |
| F | full screen |
| ? | keyboard help |

Links address a slide and a step: `#/s16/4` is slide 16 at step 4, `#/s10b` the continuation page of slide 10. `?theme=light` or `?theme=dark` forces a theme; `?still` turns motion off (screenshots).

## What steps

Every figure is an SVG with `data-build` groups that the runtime reveals one click at a time, with a caption per step under it; a group with `data-build-until` hides again at that step, which is how a zoomed view can replace a figure (the print keeps the figure). Hover any dot or cell for its tooltip (the runtime shows it instantly, in the theme).

- **Slide 3:** the ladder of five situations, one rung per click.
- **Slide 9:** the 2000–2026 timeline, five lanes, every event a dot with its date and detail on hover, the anchors labelled; the four period bands light one at a time, and clicking a period name jumps to its slide.
- **Slides 10–13:** one period zoomed, key events labelled; the five tracks light in turn with their headlines; the detail table follows as a continuation page.
- **Slide 14:** the six breaks as bars on the axis, one per click, then the malware-free share inset; the table follows as a continuation page.
- **Slide 16:** three pages. The first shows the whole Enterprise ATT&CK matrix, schematic and compact (15 tactic columns, v20.0 counts, technique IDs; hover for names), and lights its levels one click at a time: a tactic column, a technique, its sub-techniques, a note on procedures. The second and third map a classic trojan the same way as slide 18: the matrix in two halves with technique names, the scenario above both with the half being mapped in weight, steps 1–5 then 6–7, each half ending zoomed in on the lit cells.
- **Slide 18:** the recurring scenario mapped on the two halves of the matrix (Reconnaissance to Defense Impairment, then Stealth to Impact), steps 1–4 on the first page and 5–8 on the second, the full scenario above both pages with the half being mapped in weight and the rest faded; each page ends with one more click that replaces the matrix by a zoomed view of only the lit columns and cells (`#/s18/5`, `#/s18b/5`), for the back of the room.
- **Slide 17:** the two benign-file cards, then the verdict.
- **Slides 20, 21, 23, 24:** the eight-stage pipeline strip; each click lights a stage (or, on 24, the stage a change broke) with its caption; the full tables follow as continuation pages.
- **Slide 25:** the strip again; each click lights a stage and lists its options, one per line with what each captures; the full menu with what each misses is in the presenter notes.
- **Slide 22:** the HTTPS adoption chart, four series with hover values, then the four protocol steps as markers.
- **Slide 26:** six case cards above the strip; each answer lights the card and the stage that failed.

## Print

Open `index.html` in Chrome and print to PDF (landscape, no margins). Every build and every caption is shown on the printed page.

## Layout

- `build.py` — the lecture's configuration (title, parts, the two divider slides) over `tools/deck/deckbuild.py`.
- `../tools/gen_diagrams.py` — the figure generator; `../tools/data.py` — timeline events (`k` marks the key events labelled on the period slides, `h` the anchors labelled on the overview), breaks, pipeline stages, HTTPS series and the ATT&CK subset. Dates fact-checked 2026-10-11; ATT&CK checked against v20.0 on 2026-10-13.
- `../figures/*.svg` — the generated figures; they theme themselves when viewed alone and take the deck's tokens when inlined.

## Slide file format

Each slide is one markdown file, `slides/NN-slug.md`, numbered in presentation order:

- `# Slide N — Title` as its first line, then `**Timing:** a–b minutes` and `**Module:** …`;
- `## On-slide content`: a markdown subset (paragraphs, lists, tables, `>` callouts; `==text==` sets the part to read now in weight and `~~text~~` fades the rest, for a scenario shown twice), a figure as `![alt](../figures/name.svg)`, and a `Build, one step per click:` numbered list whose items are the captions, one per build step (item 0 shows before the first click; an indented `- ` line under an item is a sub-item on its own line, an indented `+ ` line a card: cards sit side by side, each in a fixed colour by position, and a `**Label** — text` card takes the label as its heading, which is how the lineage slides keep antivirus, sandbox and EDR in the same colours step after step). A callout written before a table stays on the slide; the table and anything after it move to continuation pages. A line with only `---` is a page break: what follows renders as a second page of the same slide (`#/s18b`), with its own figure and captions;
- `## Talking points`, `## Speaker notes`, optionally `## Interaction`, then `## Transition` and `## Sources`.

Slides 5 and 19 are the part dividers: their `##` heading is the title, the first `>` line the lead, the Minutes | Module table the chips.

## Checks before a commit

```bash
python3 lecture-1/tools/gen_diagrams.py lecture-1/figures && python3 lecture-1/deck/build.py   # numbering must be contiguous
grep -c '^[0-9]*\. \[' lecture-1/README.md                        # index entries = slide files
! grep -rn 'TBD\|TODO\|FIXME\|PLACEHOLDER' lecture-1/slides       # no placeholders
! grep -rn 'Invoke-Shellcode\|VirtualAlloc(\|CreateThread(\|FromBase64String(' lecture-1   # no payloads
```

Timings must be contiguous from minute 0 and end where the README's schedule says. Render a changed slide in both themes before committing (headless Chrome with `?still&theme=dark#/s9/4` works).
