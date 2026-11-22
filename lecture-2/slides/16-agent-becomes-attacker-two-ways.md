# Slide 16 — The agent becomes an attacker, two ways

**Timing:** 41–44 minutes  
**Module:** The agent becomes an attacker

## On-slide content

In both, an agent acts for an attacker. They are different threats.

| | Case A — owned by the attacker | Case B — hijacked from its owner |
| --- | --- | --- |
| Whose model, whose harness | Both the attacker's | Both the victim's |
| How it turns | Built and directed to attack | Injected context or poisoned harness |
| Enters through | Stolen or obtained access | The agent's own retrieval and tools |
| The weapon is | The agent the attacker brings | The organization's own authority |

> Same outcome, opposite threat model. The rest of the lecture is these two cases.

## Speaker notes

Use the vocabulary just built: an agent is a model in a harness, run in a loop, and it is the agent — not the bare model — that becomes the attacker, because only the agent acts. In both cases the model's reasoning serves the attacker; what differs is whose agent it is. In Case A the attacker built the harness around their own model. In Case B the victim built both, and the attacker borrowed them. This replaces the question "where is the malware?" Case A: the attacker runs their own agent as a tireless operator — the autonomous intrusion, AI-orchestrated campaigns, agent-built malware. Case B: the attacker brings no model and no harness; they turn yours against you through injected context, the mechanism from the indirect-injection slide. The distinction decides everything downstream: where attacker input enters, what the defender can observe, and where guardrails can live. Name the two clearly now; the comparison slide later makes the defensive consequences explicit. Case A comes in rungs of autonomy; Case B has two doors, the context the agent reads and the harness it runs in. The next slides show both.

## Transition

“Case A first: the agent as the attacker's weapon.”
