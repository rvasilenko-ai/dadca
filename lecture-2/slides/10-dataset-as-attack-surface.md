# Slide 10 — The dataset becomes an attack surface

**Timing:** 23–26 minutes  
**Module:** Reconstruct the attack

## On-slide content

```text
uploaded dataset configuration
       -> production data loader
           -> file and format processing
               -> results returned through the platform API
```

> Data becomes active when a privileged system interprets it.

## Speaker notes

The dataset processor accepted user-controlled formats and configuration, interpreted them in production workers, and returned processed output. The attacker did not initially need a direct route to the production network; the platform performed actions on its behalf.

Connect this to agent security: repository content, configuration, documents, and tool output may appear passive but become consequential when an automated system interprets them as instructions or parameters.

## Interaction

Ask which trust boundary is crossed when untrusted configuration selects privileged parser behavior.

## Transition

“The first successful vector extracted information without executing attacker code.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

