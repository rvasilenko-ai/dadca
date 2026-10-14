# Slide 24 — Block, adapt, repeat

**Timing:** 61–64 minutes  
**Module:** Why autonomous attacks are noisy

## On-slide content

```text
channel blocked
   -> observe failure
   -> select alternative channel
   -> rebuild tooling or identity
   -> resume objective
```

Containment questions:

- Did we block one action or remove the underlying authority?
- Can the agent recreate its state?
- Which credentials and trust paths remain valid?
- How will we know the campaign stopped?

## Speaker notes

The report describes multiple interchangeable communications paths and repeated rebuilding in ephemeral environments. This means deleting a process, pod, or endpoint may remove one manifestation without eliminating the capability graph.

Effective containment may require revoking identities, isolating boundaries, closing execution paths, and monitoring attempted re-entry—not merely blocking an indicator.

## Transition

“Noisy autonomous search is important, but it is not the only AI-enabled attacker model.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

