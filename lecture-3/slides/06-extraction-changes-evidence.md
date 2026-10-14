# Slide 6 — Extraction changes the evidence

**Timing:** 17–19 minutes (provisional)  
**Module:** Representations of executable files

## On-slide content

```text
binary
  -> parser
  -> sections, imports, strings, histograms
  -> fixed feature vector
```

> Extraction makes learning practical by selecting—and discarding—information.

Examples:

- String sets lose order and control flow.
- API counts lose arguments and causality.
- Decompiled text approximates machine semantics.
- Fixed-length inputs may truncate relevant content.

## Speaker notes

Representations are necessary; no model consumes “reality.” The engineering question is whether the discarded information matters for the intended task and adversary.

Extraction itself can fail on malformed or unfamiliar artifacts. The downstream model cannot distinguish “feature absent” from “parser failed” unless the interface preserves that information.

## Transition

“Start one rung above the signature: features an expert selects from the parsed file.”

