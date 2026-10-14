# Slide 12 — Template injection to code execution

**Timing:** 28–30 minutes  
**Module:** Reconstruct the attack

## On-slide content

### Vector 2: unsafe template evaluation

```text
attacker-controlled dataset field
  -> template renderer evaluates it
  -> arbitrary code executes in a production worker
  -> worker becomes an internal foothold
```

Two vectors, one underlying failure:

> Untrusted declarative data selected privileged behavior.

## Speaker notes

Describe server-side template injection conceptually without showing the expression. The production renderer evaluated a field that should have remained inert data.

Compare the two vectors:

- Vector 1 provided information through a legitimate format feature.
- Vector 2 crossed into arbitrary execution through unsafe interpretation.

## Transition

“A foothold becomes far more powerful when its environment contains reusable identities.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

