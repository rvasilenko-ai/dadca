# Slide 8 — From model to agent: the loop

**Timing:** 22–25 minutes  
**Module:** From model to agent

## On-slide content

```text
objective
   -> observe environment
   -> form a hypothesis
   -> select a tool or action
   -> execute
   -> interpret result
   -> update state
   -> repeat
```

Failure is often new information, not termination.

> A model answers once. A model plus a harness, run in this loop, acts in the world — that is an agent.

What the agent adds to a bare model: tools to misuse, memory to poison, documents to be fed — and a loop that keeps reading.

## Speaker notes

This is where the word "agent" earns its meaning. Contrast the loop with a one-shot model response. The consequential capability is repeated interaction with an environment whose outputs change the next action.

The loop does not require every hypothesis to be correct. It requires enough feedback, retries, and state to eventually identify a useful path.

## Transition

“Model, harness, loop: that is an agent. Every pass of the loop reads the world through the harness — and that is where the attacker reaches in.”

