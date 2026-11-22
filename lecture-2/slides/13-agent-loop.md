# Slide 13 — From model to agent: the loop

**Timing:** 33–36 minutes  
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

![The loop: the model reads the objective and the context, acts through a tool in the environment, and the output returns to the context for the next turn.](../figures/agent-loop.svg)

*The loop: the model reads the objective and the context, acts through a tool in the environment, and the output returns to the context for the next turn.*

Build, one step per click:

0. The model reads and decides; everything else is around it.
1. It receives an objective.
2. It acts by calling a tool in the environment — shell, browser, code, an API — against the target.
3. The tool's output returns as an observation and joins the context.
4. Every turn adds to the context; the next choice depends on everything so far.
5. The loop ends when the objective is met or a budget runs out. Failure along the way is new information, not termination.

> A model answers once. A model plus a harness, run in this loop, acts in the world — that is an agent.

What the agent adds to a bare model: tools to misuse, memory to poison, documents to be fed — and a loop that keeps reading.

## Speaker notes

This is where the word "agent" earns its meaning. Contrast the loop with a one-shot model response. The consequential capability is repeated interaction with an environment whose outputs change the next action.

The loop does not require every hypothesis to be correct. It requires enough feedback, retries, and state to eventually identify a useful path.

## Transition

“Model, harness, loop: that is an agent. Every pass of the loop reads the world through the harness — and that is where the attacker reaches in.”

