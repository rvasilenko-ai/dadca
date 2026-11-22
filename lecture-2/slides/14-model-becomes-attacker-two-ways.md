# Slide 14 — The model becomes an attacker, two ways

**Timing:** 38–41 minutes  
**Module:** The model becomes an attacker

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

Use the vocabulary just built. In both cases the model's reasoning serves the attacker — that is why the slide says "the model becomes an attacker" — but what differs is the harness: in Case A the attacker built it, in Case B they borrowed it. This replaces the question "where is the malware?" Case A: the attacker runs their own agent as a tireless operator — the autonomous intrusion, AI-orchestrated campaigns, agent-built malware. Case B: the attacker brings no model and no harness; they turn yours against you through injected context, the mechanism from the indirect-injection slide. The distinction decides everything downstream: where attacker input enters, what the defender can observe, and where guardrails can live. Name the two clearly now; the comparison slide later makes the defensive consequences explicit.

## Transition

“Case A first: the model as the attacker's weapon.”
