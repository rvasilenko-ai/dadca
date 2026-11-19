# Slide 12 — The model becomes an attacker, two ways

**Timing:** 30–33 minutes  
**Module:** The model becomes an attacker

## On-slide content

In both, a model takes actions that serve an attacker. They are different threats.

| | Case A — owned by the attacker | Case B — hijacked from its owner |
| --- | --- | --- |
| Whose model | The attacker's own agent | A legitimate, trusted agent |
| How it turns | Built and directed to attack | Injected context or poisoned harness |
| Enters through | Stolen or obtained access | The agent's own retrieval and tools |
| The weapon is | The model itself | The organization's own authority |

> Same outcome, opposite threat model. The rest of the lecture is these two cases.

## Speaker notes

This replaces the question "where is the malware?" Case A: the attacker runs a model as a tireless operator — the autonomous intrusion, AI-orchestrated campaigns, agent-built malware. Case B: the attacker never brings a model; they turn yours against you through injected context, the mechanism from the indirect-injection slide. The distinction decides everything downstream: where attacker input enters, what the defender can observe, and where guardrails can live. Name the two clearly now; the comparison slide later makes the defensive consequences explicit.

## Transition

“Case A first: the model as the attacker's weapon.”
