# Slide 19 — Operational orchestration

**Timing:** 46–49 minutes  
**Module:** Why the agent succeeded

## On-slide content

- Invoke tools through shells and APIs
- Parse outputs and errors
- Install or rebuild a toolchain
- Transfer state through external channels
- Retry with altered parameters
- Switch channels after failure
- Return to earlier leads

## Speaker notes

Do not assign a literal “50/50” split between code reasoning and orchestration. They are interdependent. Better code insight selects better actions; better orchestration supplies the observations needed for code reasoning.

The Hugging Face report describes repeated rebuilding across short-lived environments and fallback to multiple channels. That persistence is a systems capability, not merely a language-model benchmark score.

## Transition

“Neither ability matters operationally until the harness gives it a consequential action surface.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

