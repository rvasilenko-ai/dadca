# Slide 10 — MalConv: learning from raw bytes

**Timing:** 31–36 minutes  
**Module:** Representations of executable files

## On-slide content

```text
bytes
  -> byte embeddings
  -> convolution and gating
  -> pooling
  -> malicious / benign score
```

Promises:

- Less manual feature design
- End-to-end learned byte regions

Challenges:

- Extremely long sequences
- File structure remains implicit
- Padding and truncation choices
- Irrelevant or manipulated bytes

## Speaker notes

“Raw” does not mean assumption-free. The model still receives a selected file, a bounded prefix or length, a padding scheme, and labels produced by a collection process.

Consuming every byte is also not the same as understanding executable semantics. Some bytes may never execute; small semantic changes may occur far apart in the sequence.

## Transition

“A different branch of research makes code structure more explicit before learning a representation.”

## Sources

- [MalConv: Malware Detection by Eating a Whole EXE](https://arxiv.org/abs/1710.09435)

