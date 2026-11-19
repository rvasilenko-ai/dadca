# Lecture 2: When the Attacker Is an Agent

**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** What changes when reasoning, tool use, and persistent trial-and-error become cheap?

**Framing beat (from Lecture 1):** Lecture 1 ends on a recurring pattern, offensive capability diffusing from the few to the many, with the 2017 Shadow Brokers spill-over (EternalBlue, then NotPetya) as the reference case. This lecture is that pattern's current instance: frontier AI capability, released commercially and as open weights, reaching everyone and lowering the skill floor, with the caveat that the diffusion is gradual and the offensive economy is not yet settled.

## The spine

The lecture is built on one idea and one distinction.

- **The idea.** Attacking a learned model is not new; it runs from adversarial examples and poisoning, through evasion of ML malware detectors, to prompt injection of LLMs. Prompt injection is the oldest bug class — confusing data for code — reappearing one layer up: classic software shares code and data as bytes, an LLM shares instructions and context as text, and neither has a trust boundary in that shared channel. And the model is not the whole target; it sits in a harness of tools, skills, memory, retrieval, and delegated authority that is attacked just as directly.
- **The distinction.** A model becomes an attacker in two different ways: a malicious model the attacker owns and runs (Case A, the agent as a weapon), and a trusted model hijacked from its owner through injected context or a poisoned harness (Case B). Same outcome, opposite threat model, opposite defensive opportunities.

Standalone takeaway:

> Same outcome, opposite threat model: defend against someone else's agent, or prevent your own agent from becoming the attacker's execution environment.

## Learning outcomes

Students should be able to:

1. Trace adversarial machine learning as one lineage, from evasion and poisoning of classifiers to prompt injection of LLMs.
2. Explain prompt injection as the code/data confusion of classic software reborn in text, and why it has no clean structural fix.
3. Distinguish attacks on the model from attacks on the harness: tools, skills, memory, retrieval, and tool servers.
4. Contrast the two ways a model becomes an attacker — a malicious model the attacker owns, and a trusted model hijacked through untrusted context — by location, authority, observability, and where guardrails can live.
5. Map the real cases (the autonomous intrusion, AI-orchestrated campaigns, agent-built malware, ForcedLeak) onto that framework.
6. Identify research problems in agent-trajectory observability, authorization, incident correlation, supply-chain security, and bounded response.

## Module schedule

| Time | Module | Slides |
| --- | --- | --- |
| 0–8 | Foundation | 1–3 |
| 8–22 | From adversarial ML to attacks on LLMs | 4–8 |
| 22–30 | The agent as a system: model and harness | 9–11 |
| 30–33 | The model becomes an attacker: two cases | 12 |
| 33–46 | Case A: a malicious model the attacker owns | 13–15 |
| 46–56 | Case B: a compromised trusted model | 16–18 |
| 56–66 | The two cases compared | 19–21 |
| 66–90 | Defense and research | 22–25 |

## Primary cases

### Case A — a malicious model the attacker owns

The July 2026 Hugging Face technical timeline describes an autonomous agent operating during an OpenAI cyber-capability evaluation. The reconstructed campaign crossed several trust boundaries, generated roughly 17,600 recovered actions, and required AI-assisted defensive reconstruction. Supporting cases, kept short: the Anthropic AI-orchestrated espionage campaign (November 2025), agent-assisted extortion (August 2025), and the file-based implants NIK C2 and VOLTA that embed an LLM call (Talos, October 2026).

### Case B — a compromised trusted model

ForcedLeak was a disclosed and demonstrated vulnerability chain in Salesforce Agentforce. Attacker-controlled instructions persisted in a CRM lead, were later retrieved during an employee's legitimate interaction with the agent, and could cause sensitive CRM data to leave through crafted image requests. A real production vulnerability and attack demonstration, not a publicly confirmed customer breach. SearchLeak (Microsoft 365 Copilot) is cited briefly as the same pattern.

## Source boundaries

- Slides label facts attributed to the Hugging Face, OpenAI, Anthropic, Talos, and ForcedLeak reports.
- The adversarial-ML history slides (4–5) cite the foundational papers; these citations and dates still need a verification pass of the kind run for Lecture 1.
- Interpretations about the code/data parallel, optimization, noise, stealth, and future malware definitions are presented as lecture arguments or research hypotheses.
- Incident mechanics remain conceptual; slides do not reproduce payloads or exploit code.

## Slide index

1. [When the attacker is an agent](slides/01-when-attacker-is-agent.md)
2. [Standalone foundation](slides/02-standalone-foundation.md)
3. [What changes when reasoning is cheap?](slides/03-what-changes-when-reasoning-is-cheap.md)
4. [Attacking the model is not new](slides/04-attacking-models-is-not-new.md)
5. [...and it reached malware detection](slides/05-adversarial-ml-reaches-malware.md)
6. [Code and data, instructions and context](slides/06-code-data-instructions-context.md)
7. [The shape of LLM attacks](slides/07-shape-of-llm-attacks.md)
8. [Why there is no NX bit for text](slides/08-no-nx-bit-for-text.md)
9. [Harness and authority](slides/09-harness-and-authority.md)
10. [Attacks on the harness](slides/10-attacks-on-the-harness.md)
11. [The agent loop](slides/11-agent-loop.md)
12. [The model becomes an attacker, two ways](slides/12-model-becomes-attacker-two-ways.md)
13. [Case A: a malicious model the attacker owns](slides/13-case-a-attacker-owned-model.md)
14. [Approximately 17,600 recovered actions](slides/14-seventeen-thousand-actions.md)
15. [Case A beyond one incident](slides/15-case-a-beyond-one-incident.md)
16. [Case B: The trusted enterprise agent](slides/16-forcedleak-enterprise-agent.md)
17. [ForcedLeak: the attack path](slides/17-forcedleak-attack-path.md)
18. [Dormant instructions, live authority](slides/18-dormant-instructions-live-authority.md)
19. [Audience question: what is different?](slides/19-compare-before-reveal.md)
20. [Defense depends on who controls the agent](slides/20-defense-depends-on-agent-location.md)
21. [Is a compromised agent malware?](slides/21-is-agent-malware.md)
22. [Success hidden inside noise](slides/22-success-hidden-in-noise.md)
23. [The agentic supply chain](slides/23-agentic-supply-chain.md)
24. [Bounded autonomous response](slides/24-bounded-autonomous-response.md)
25. [A map of work still to be done](slides/25-research-map-and-close.md)
