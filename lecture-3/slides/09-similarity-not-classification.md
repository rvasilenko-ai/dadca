# Slide 9 — Similarity is not classification

**Timing:** 26–31 minutes  
**Module:** Representations of executable files

## On-slide content

Three different questions:

1. Is this object malicious?
2. Have we seen something similar?
3. Which objects belong together?

```text
features or shingles
  -> MinHash / LSH-style sketch
  -> approximate neighbor candidates
  -> clustering or retrieval
```

## Speaker notes

Explain the intuition without deriving the full mathematics: similar sets are likely to share sketch values, and locality-sensitive hashing lets systems retrieve candidates without comparing every object with every other object.

Uses include deduplication, family discovery, campaign grouping, novelty estimation, and analyst navigation. Similarity does not itself establish maliciousness, and malware within one campaign may be deliberately diverse.

## Transition

“What if we avoid a PE parser and ask a neural model to consume the byte sequence directly?”

