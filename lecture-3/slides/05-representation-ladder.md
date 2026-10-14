# Slide 5 — A representation ladder

**Timing:** 14–17 minutes  
**Module:** Signatures and the file-centric literature

## On-slide content

```text
exact bytes
  -> expert features
  -> similarity sketches
  -> raw-byte embeddings
  -> instructions and functions
  -> semantic summaries
```

Across the ladder:

- Different extraction cost
- Different abstraction
- Different information loss
- Different operational scale

## Speaker notes

Do not present this as a clean replacement sequence. Production systems combine multiple representations because they answer different questions and operate under different budgets.

Higher abstraction can expose semantics while hiding low-level evidence. Lower-level input preserves bytes but forces the model to infer structure.

## Transition

“Every rung is an extraction, and every extraction discards something. Look at what a parser keeps and loses before trusting any rung.”

