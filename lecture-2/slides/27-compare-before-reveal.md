# Slide 27 — Case A versus Case B: what is different?

**Timing:** 68–70 minutes  
**Module:** The two cases compared

## On-slide content

![Two reminder cards. Case A, the attacker's own agent, runs outside the organization: AI pentesting frameworks seen in intrusions, and the Hugging Face evaluation escape. Case B, the victim's own agent hijacked inside the trusted workflow: ForcedLeak through injected context, MIDNIGHT NEPTUNE through a poisoned harness](../figures/case-reminder.svg)

In all four, an agent did work for an attacker. Answer each question once for Case A and once for Case B:

- Where does the agent run, and who owns its model, harness, identity and logs?
- Where does attacker-controlled input enter?
- What can the defender observe?
- Where can the defender enforce policy?
- What can only be detected from the resulting behaviour?

> What is fundamentally different about the attacks — and about our opportunities to defend?

## Speaker notes

Give students two or three minutes to discuss in pairs, then collect answers without immediately grading them. The cards are there so nobody has to reconstruct the cases from memory: Case A is the attacker's own agent — the frameworks seen in intrusions and the Hugging Face escape — and it runs outside the organization; Case B is the victim's own agent, hijacked through what it reads (ForcedLeak) or what it runs (MIDNIGHT NEPTUNE), and it runs inside the trusted workflow.

Push beyond "one is external and one is internal." The deeper distinction is control over the decision-and-execution system. In Case A the defender faces an adversary-operated agent and observes only its interactions with defended systems — hosts, identities, network flows. In Case B the organization or its SaaS provider operates the agent and therefore has additional instrumentation and enforcement points: the context it reads, the tools it calls, the identity it acts with, the egress it uses.

Ask whether greater visibility automatically means easier defense. It does not: trusted identity, high-volume legitimate activity, vendor telemetry limitations, and ambiguous natural-language inputs complicate the problem. The next slide gives the answer as a table.

## Transition

“The location and ownership of the agent determine which defensive controls are even possible.”

