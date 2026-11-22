# Slide 22 — Audience question: what is different?

**Timing:** 62–64 minutes  
**Module:** The two cases compared

## On-slide content

Both agents performed actions useful to an attacker.

> What is fundamentally different about the attacks—and about our opportunities to defend?

Prompts:

- Where does each agent run?
- Who owns its model, harness, identity, and logs?
- Where does attacker-controlled input enter?
- What can the defender observe?
- Where can the defender enforce policy?
- What must be detected only from resulting behavior?

## Speaker notes

Give students two or three minutes to discuss in pairs, then collect answers without immediately grading them.

Push beyond “one is external and one is internal.” The deeper distinction is control over the decision-and-execution system. In the Hugging Face case, the defender faces an adversary-operated agent and observes only interactions with defended systems. In ForcedLeak, the organization or its SaaS provider operates the agent and therefore has additional instrumentation and enforcement points.

Ask whether greater visibility automatically means easier defense. It does not: trusted identity, high-volume legitimate activity, vendor telemetry limitations, and ambiguous natural-language inputs complicate the problem.

## Transition

“The location and ownership of the agent determine which defensive controls are even possible.”

