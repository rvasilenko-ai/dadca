# Lecture 2: When the Attacker Is an Agent

**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** What changes when reasoning, tool use, and persistent trial-and-error become cheap?

**Framing beat:** offensive capability diffuses from the few to the many; the 2017 Shadow Brokers spill-over (EternalBlue, then NotPetya) is the reference case. This lecture is that pattern's current instance: frontier AI capability, released commercially and as open weights, reaching everyone and lowering the skill floor, with the caveat that the diffusion is gradual and the offensive economy is not yet settled. The lecture stands alone and no slide refers to another lecture. If the same audience attended the malware lecture, the presenter can call back to its closing pattern at slide 13; if not, the one sentence above is enough.

## The spine

The lecture is built on one idea and one distinction.

- **The idea.** Attacking a learned model is not new; it runs from adversarial examples and poisoning, through evasion of ML malware detectors, to prompt injection of LLMs. Prompt injection is the oldest bug class — confusing data for code — reappearing one layer up: classic software shares code and data as bytes, an LLM shares instructions and context as text, and neither has a trust boundary in that shared channel. And the model is not the whole target; it sits in a harness of tools, skills, memory, retrieval, and delegated authority that is attacked just as directly. The vocabulary is built in that order on purpose — model, then harness, then agent — so the word "agent" is never used before it is defined.
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
| 0–2 | Opening | 1 |
| 2–19 | From adversarial ML to attacks on LLMs | 2–6 |
| 19–29 | From model to agent: the harness, the loop, the attack surface | 7–9 |
| 29–32 | The model becomes an attacker: two cases | 10 |
| 32–45 | Case A: a malicious model the attacker owns | 11–13 |
| 45–55 | Case B: a compromised trusted model | 14–16 |
| 55–65 | The two cases compared | 17–19 |
| 65–90 | Defense and research | 20–23 |

## Primary cases

### Case A — a malicious model the attacker owns

The July 2026 Hugging Face technical timeline describes an autonomous agent operating during an OpenAI cyber-capability evaluation. The reconstructed campaign crossed several trust boundaries, generated roughly 17,600 recovered actions, and required AI-assisted defensive reconstruction. Supporting cases, kept short: the Anthropic AI-orchestrated espionage campaign (November 2025), agent-assisted extortion (August 2025), and the file-based implants NIK C2 and VOLTA that embed an LLM call (Talos, October 2026).

### Case B — a compromised trusted model

ForcedLeak was a disclosed and demonstrated vulnerability chain in Salesforce Agentforce. Attacker-controlled instructions persisted in a CRM lead, were later retrieved during an employee's legitimate interaction with the agent, and could cause sensitive CRM data to leave through crafted image requests. A real production vulnerability and attack demonstration, not a publicly confirmed customer breach. SearchLeak (Microsoft 365 Copilot) is cited briefly as the same pattern.

## Source boundaries

- Slides label facts attributed to the Hugging Face, OpenAI, Anthropic, Talos, and ForcedLeak reports.
- The adversarial-ML history slides (4–5) cite the foundational papers; these citations and dates still need a verification pass against the primary sources.
- Interpretations about the code/data parallel, optimization, noise, stealth, and future malware definitions are presented as lecture arguments or research hypotheses.
- Incident mechanics remain conceptual; slides do not reproduce payloads or exploit code.

## Slide index

1. [When the attacker is an agent](slides/01-when-attacker-is-agent.md)
2. [Attacking the model is not new](slides/02-attacking-models-is-not-new.md)
3. [...and it reached malware detection](slides/03-adversarial-ml-reaches-malware.md)
4. [Code and data, instructions and context](slides/04-code-data-instructions-context.md)
5. [The shape of LLM attacks](slides/05-shape-of-llm-attacks.md)
6. [Why there is no NX bit for text](slides/06-no-nx-bit-for-text.md)
7. [The harness: what surrounds the model](slides/07-harness-and-authority.md)
8. [From model to agent: the loop](slides/08-agent-loop.md)
9. [Attacks on the harness](slides/09-attacks-on-the-harness.md)
10. [The model becomes an attacker, two ways](slides/10-model-becomes-attacker-two-ways.md)
11. [Case A: a malicious model the attacker owns](slides/11-case-a-attacker-owned-model.md)
12. [Approximately 17,600 recovered actions](slides/12-seventeen-thousand-actions.md)
13. [Case A beyond one incident](slides/13-case-a-beyond-one-incident.md)
14. [Case B: The trusted enterprise agent](slides/14-forcedleak-enterprise-agent.md)
15. [ForcedLeak: the attack path](slides/15-forcedleak-attack-path.md)
16. [Dormant instructions, live authority](slides/16-dormant-instructions-live-authority.md)
17. [Audience question: what is different?](slides/17-compare-before-reveal.md)
18. [Defense depends on who controls the agent](slides/18-defense-depends-on-agent-location.md)
19. [Is a compromised agent malware?](slides/19-is-agent-malware.md)
20. [Success hidden inside noise](slides/20-success-hidden-in-noise.md)
21. [The agentic supply chain](slides/21-agentic-supply-chain.md)
22. [Bounded autonomous response](slides/22-bounded-autonomous-response.md)
23. [A map of work still to be done](slides/23-research-map-and-close.md)
