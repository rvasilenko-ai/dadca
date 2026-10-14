# Lecture 1 deck

Interactive HTML slides generated from the markdown sources in `../slides/`. The markdown remains the source of truth; do not edit `index.html` by hand.

## Build

```bash
python3 lecture-1/deck/build.py
```

Then open `lecture-1/deck/index.html` in a browser. Everything is local: reveal.js 5.1.0 is vendored under `vendor/reveal/`, there are no web fonts, and no network is needed in the lecture hall.

## Present

| Key | Action |
| --- | --- |
| → or Space | next step (fragments, then next slide) |
| ← | previous step |
| S | speaker view: notes, elapsed timer, next slide preview |
| F | fullscreen |
| Esc or O | overview of all slides |
| T | toggle light and dark theme (light is the default for lit rooms) |
| B | blank the screen |
| ? | keyboard help |

Speaker notes carry the planned minutes for each slide at the top, then the speaker notes, interaction, transition and sources from the markdown.

## Interactive parts

- **Slide 9 (overview):** the whole 2000–2026 timeline, five lanes, four period bands, anchor events labelled; hover any dot for its date; click a period name to jump to its slide.
- **Slides 10–13 (periods):** the timeline zoomed to one period, key events labelled, the rest on hover. One headline per track; the details button swaps the timeline and headlines for the full detail chips, and back (the PDF prints the headline view; the detail stays in the markdown and the notes).
- **Slide 14 (recap):** the same timeline reduced to the six breaks as bars; the table shows at once and the callout reveals on Next.
- **Slide 3 (vote):** a live tally; click + and − per cell, Reset to clear.
- **Slides 22–25, 27 and 28 (pipeline):** click a stage for its question; on 23 Next and Previous step through the eight stages, each listing its options with what each captures and misses (clicking a stage jumps to it; all eight panels print in the PDF); on 24 Next and Previous step through the seven changes one panel at a time, lighting the stage that broke; on 25 and 27 they step through the stages one panel at a time, the generations side by side, with a table button for the full matrix (clicking a stage jumps to it); on 28 Next reveals the six answers in turn, one per failing stage (the Reveal buttons jump to a case).
- **Slides 16, 18 and 19 (ATT&CK matrix):** a schematic Enterprise matrix built offline from `attack.js`: 15 tactic columns (v20.0) with the real per-tactic counts, a few real techniques each; hover a cell for its ID. On 16 Next lights the recurring scenario as a numbered path; on 18 the compact form shows only the two cells that matter; on 19 Next lights the mapping one step at a time.
- **Slide 26 (HTTPS chart):** hover for a crosshair with all series; Table switches to the data table.

## PDF

Open `index.html?print-pdf` in Chrome and print to PDF (landscape, no margins). Fragments are flattened and the expanded chips are shown.

## Layout

- `build.py` — generator (markdown subset converter, period layout, notes).
- `page.html` — page shell and reveal.js configuration.
- `theme.css` — tokens (light and dark), slide chrome, component styles.
- `attack.js` — the schematic ATT&CK matrix: tactics, curated techniques, per-tactic counts and the version they were checked against.
- `data.js` — timeline events (k marks the key events labelled on the zoomed period slides, h the anchors labelled on the overview), breaks, pipeline stages, HTTPS series. Dates fact-checked 2026-10-11.
- `components.js` — timeline, chips, pipeline, vote, chart, theme toggle.
- `templates/<slug>.html` — hand-designed bodies for slides that need more than the auto conversion, named after the slide file without its number so renumbering never touches them; `{{auto}}` injects the converted markdown.
- `vendor/reveal/` — reveal.js 5.1.0 (MIT), reset and base CSS, notes plugin.
