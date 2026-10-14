# Slide 7 — Engineered PE features

**Timing:** 17–21 minutes  
**Module:** Representations of executable files

## On-slide content

```text
PE file
  -> headers
  -> sections
  -> imports and exports
  -> strings
  -> byte histograms and entropy
  -> fixed feature vector
```

Question:

> Which features express program semantics, and which are correlations?

## Speaker notes

Define PE briefly as the executable and library container used by Windows. Show only a simplified structure: headers describe loading, sections contain code/data/resources, and import tables describe external dependencies.

Engineered features incorporate domain knowledge and can be computed efficiently. They can also encode accidental correlations involving compiler, packaging, signing, or data-collection practices.

## Transition

“Public datasets made this representation reproducible at research scale.”

