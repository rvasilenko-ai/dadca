# Slide 10 — Why there is no NX bit for text

**Timing:** 26–28 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

| Software re-drew the boundary | The LLM equivalent |
| --- | --- |
| NX / DEP: data pages cannot execute | — |
| ASLR, stack canaries, CFI | — |
| Parameterized queries: code kept apart from data | Partial: delimiters, roles, instruction hierarchy |
| Input validation and output escaping | Partial: spotlighting, filters, dual-LLM patterns |

> There is no bit that marks text as "data, never instructions." Defense is architecture, not a flag.

## Speaker notes

The software fixes were imperfect but real; each re-established some boundary between code and data. For text there is no equivalent, because the boundary is semantic, not structural — the model reads meaning, and meaning cannot be marked non-executable. The current mitigations raise the bar: delimiters, system and role separation, instruction hierarchies, spotlighting, dual-LLM or privileged-versus-quarantined designs, output filtering. None is a reliable boundary. So the defenses in the rest of this lecture are architectural — scope the authority, control the egress, observe the trajectory — not "sanitize the prompt."

## Transition

“And the model is not even the whole attack surface. It sits inside a harness.”
