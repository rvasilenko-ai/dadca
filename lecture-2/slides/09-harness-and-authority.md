# Slide 9 — The harness: what surrounds the model

**Timing:** 22–25 minutes  
**Module:** From model to agent

## On-slide content

```text
model capability
    + tool interfaces
    + shell/network access
    + credentials
    + persistent or recoverable state
    + environmental feedback
    + delegated authority
    = real-world consequences
```

## Speaker notes

The model is one component in a larger execution system. Ask not only “What can the model reason about?” but also:

- What actions can it request?
- Which actions execute without independent authorization?
- What identity do those actions inherit?
- What observations return to the model?
- Where is state retained?

This framing applies whether the system attacks, writes code, or responds to incidents.

## Transition

“The harness defines what the model can do in the world — which also makes it where the attacker reaches in.”

