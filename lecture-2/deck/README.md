# Lecture 2 deck

The HTML deck for *When the Attacker Is an Agent*, built from the markdown slides in `../slides/`.
The markdown stays the source of truth; `index.html` is generated.

Live: https://rvasilenko-ai.github.io/malware-and-ai/lecture-2/deck/

## Build

```sh
python3 lecture-2/deck/build.py
```

No dependencies. The script parses each slide file, converts the on-slide markdown, inlines the
SVG diagrams from `../figures/` (so their `data-build` groups can be stepped), links the paper
figures, and emits one `<section>` per slide plus a divider per part.

## Run locally

Open `index.html` directly, or serve the `lectures/` folder (the figures are referenced as `../figures/`):

```sh
cd lectures && python3 -m http.server 8765
# then http://localhost:8765/lecture-2/deck/
```

## Presenting

| Key | Does |
| --- | --- |
| `→` `space` `PageDown` | next step, then next slide |
| `←` `PageUp` | previous |
| `Home` `End` | first, last slide |
| `N` | presenter notes panel (speaker notes, interaction, transition) |
| `S` | open this slide's sources |
| `T` | light or dark |
| `F` | full screen |
| `?` | help |

Links address a slide and a step: `#/s12/3` is slide 12 at step 3, `#/s28b` the continuation of
slide 28, `#/p2` the divider of part 2. Query switches: `?theme=light` or `?theme=dark` forces a
theme without storing it; `?still` turns motion off (used for screenshots).

## How the markdown maps to the stage

- `# Slide N — Title`, `**Timing:**`, `**Module:**` give the title, the footer and the part.
- The on-slide content renders as markdown: fenced blocks become text schematics, tables, callouts
  (`>`), lists, `###` headings.
- A list under `Build, one step per click:` becomes stepped captions, one visible at a time; on a
  slide with an SVG diagram the caption index drives the diagram's `data-build` groups.
- `![alt](../figures/x.svg)` inlines a diagram; `![alt](../figures/x.png)` places a figure in the
  right column with the following `*italic*` line as its caption.
- A diagram slide that also has a table gets a continuation slide (`s14b`, `s28b`) for the table.
- `## Sources` becomes the Sources button at the bottom right; `## Speaker notes`, `## Interaction`
  and `## Transition` go to the presenter notes panel.
- The build estimates each slide's height and applies `slide--dense` or `slide--denser` type scales
  when the content would not fit the 1920 x 1080 stage.

## Screenshots for review

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --screenshot=out.png --window-size=1920,1080 "file://$PWD/lecture-2/deck/index.html?still&theme=light#/s12/3"
```
