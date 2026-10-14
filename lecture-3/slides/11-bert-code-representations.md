# Slide 11 — BERT-like code representations

**Timing:** 36–41 minutes  
**Module:** Representations of executable files

## On-slide content

Possible input units:

- Opcodes and instructions
- Basic blocks
- Functions
- Decompiled pseudocode
- Control-flow or calling context

```text
binary -> disassembler/decompiler -> tokens/context -> learned representation
```

## Speaker notes

Code resembles language imperfectly. Meaning also depends on control flow, data flow, memory, calling conventions, and runtime state.

BERT-like models can learn contextual representations, but they depend on prior disassembly, function discovery, architecture knowledge, and sometimes decompilation. Extraction errors become model inputs.

Do not imply that one “BERT for code” represents a single standardized successor to MalConv; this is a broad family of representations and tasks.

## Transition

“Now compare these systems by operational role rather than benchmark novelty.”

## Sources

- [DeepSemantic: Semantic-aware Binary Code Representation with BERT](https://arxiv.org/abs/2106.05478)

