# Lecture 2: When the Attacker Is an Agent

**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** What changes when reasoning, tool use, and persistent trial-and-error become cheap?

**Framing beat:** offensive capability diffuses from the few to the many; the 2017 Shadow Brokers spill-over (EternalBlue, then NotPetya) is the reference case. This lecture is that pattern's current instance: frontier AI capability, released commercially and as open weights, reaching everyone and lowering the skill floor, with the caveat that the diffusion is gradual and the offensive economy is not yet settled. The lecture stands alone and no slide refers to another lecture. If the same audience attended the malware lecture, the presenter can call back to its closing pattern at slide 17; if not, the one sentence above is enough.

## The spine

The lecture is built on one idea and one distinction.

- **The idea.** Attacking a learned model is not new; it runs from adversarial examples and poisoning, through evasion of ML malware detectors, to prompt injection of LLMs. Prompt injection is the oldest bug class — confusing data for code — reappearing one layer up: classic software shares code and data as bytes, an LLM shares instructions and context as text, and neither has a trust boundary in that shared channel. And the model is not the whole target; it sits in a harness of tools, skills, memory, retrieval, and delegated authority that is attacked just as directly. The vocabulary is built in that order on purpose — model, then harness, then agent — so the word "agent" is never used before it is defined.
- **The distinction.** A model becomes an attacker in two different ways: a malicious model the attacker owns and runs (Case A, the agent as a weapon), and a trusted model hijacked from its owner through injected context or a poisoned harness (Case B). Same outcome, opposite threat model, opposite defensive opportunities.

Standalone takeaway:

> Same outcome, opposite threat model: defend against someone else's agent, or prevent your own agent from becoming the attacker's execution environment.

## Learning outcomes

Students should be able to:

1. Trace adversarial machine learning as one lineage — evasion, poisoning and backdoors, model extraction, membership inference and inversion — from spam-filter attacks in 2004 to prompt injection of LLMs, and sketch how each attack works.
2. Explain prompt injection as the code/data confusion of classic software reborn in text, and why it has no clean structural fix.
3. Distinguish attacks on the model from attacks on the harness: tools, skills, memory, retrieval, and tool servers.
4. Contrast the two ways a model becomes an attacker — a malicious model the attacker owns, and a trusted model hijacked through untrusted context — by location, authority, observability, and where guardrails can live.
5. Map the real cases (the autonomous intrusion, AI-orchestrated campaigns, agent-built malware, ForcedLeak) onto that framework.
6. Identify research problems in agent-trajectory observability, authorization, incident correlation, supply-chain security, and bounded response.

## Module schedule

| Time | Module | Slides |
| --- | --- | --- |
| 0–2 | Opening | 1 |
| 2–28 | From adversarial ML to attacks on LLMs | 2–10 |
| 28–38 | From model to agent: the harness, the loop, the attack surface | 11–13 |
| 38–41 | The model becomes an attacker: two cases | 14 |
| 41–52 | Case A: a malicious model the attacker owns | 15–17 |
| 52–61 | Case B: a compromised trusted model | 18–20 |
| 61–70 | The two cases compared | 21–23 |
| 70–90 | Defense and research | 24–27 |

## Primary cases

### Case A — a malicious model the attacker owns

The July 2026 Hugging Face technical timeline describes an autonomous agent operating during an OpenAI cyber-capability evaluation. The reconstructed campaign crossed several trust boundaries, generated roughly 17,600 recovered actions, and required AI-assisted defensive reconstruction. Supporting cases, kept short: the Anthropic AI-orchestrated espionage campaign (November 2025), agent-assisted extortion (August 2025), and the file-based implants NIK C2 and VOLTA that embed an LLM call (Talos, October 2026).

### Case B — a compromised trusted model

ForcedLeak was a disclosed and demonstrated vulnerability chain in Salesforce Agentforce. Attacker-controlled instructions persisted in a CRM lead, were later retrieved during an employee's legitimate interaction with the agent, and could cause sensitive CRM data to leave through crafted image requests. A real production vulnerability and attack demonstration, not a publicly confirmed customer breach. SearchLeak (Microsoft 365 Copilot) is cited briefly as the same pattern.

## Source boundaries

- Slides label facts attributed to the Hugging Face, OpenAI, Anthropic, Talos, and ForcedLeak reports.
- The adversarial-ML history slides (2–7) cite at least one primary paper per attack; every citation was checked against the arXiv API or Crossref on 2026-11-22, and the quoted figures (1% of SpamBayes training mail, the stop-sign sticker, the GPT-2 extraction) come from the papers' own abstracts or text.
- Interpretations about the code/data parallel, optimization, noise, stealth, and future malware definitions are presented as lecture arguments or research hypotheses.
- Incident mechanics remain conceptual; slides do not reproduce payloads or exploit code.

## Slide index

1. [When the attacker is an agent](slides/01-when-attacker-is-agent.md)
2. [Attacking the model is not new](slides/02-attacking-models-is-not-new.md)
3. [Evasion: change the input, keep the model](slides/03-evasion-adversarial-examples.md)
4. [Poisoning and backdoors: change the data, keep the input](slides/04-poisoning-and-backdoors.md)
5. [Model extraction: copy the model through its API](slides/05-model-extraction.md)
6. [Membership inference and inversion: what the model remembers](slides/06-membership-inference-and-inversion.md)
7. [...and it reached malware detection](slides/07-adversarial-ml-reaches-malware.md)
8. [Code and data, instructions and context](slides/08-code-data-instructions-context.md)
9. [The shape of LLM attacks](slides/09-shape-of-llm-attacks.md)
10. [Why there is no NX bit for text](slides/10-no-nx-bit-for-text.md)
11. [The harness: what surrounds the model](slides/11-harness-and-authority.md)
12. [From model to agent: the loop](slides/12-agent-loop.md)
13. [Attacks on the harness](slides/13-attacks-on-the-harness.md)
14. [The model becomes an attacker, two ways](slides/14-model-becomes-attacker-two-ways.md)
15. [Case A: a malicious model the attacker owns](slides/15-case-a-attacker-owned-model.md)
16. [Approximately 17,600 recovered actions](slides/16-seventeen-thousand-actions.md)
17. [Case A beyond one incident](slides/17-case-a-beyond-one-incident.md)
18. [Case B: The trusted enterprise agent](slides/18-forcedleak-enterprise-agent.md)
19. [ForcedLeak: the attack path](slides/19-forcedleak-attack-path.md)
20. [Dormant instructions, live authority](slides/20-dormant-instructions-live-authority.md)
21. [Audience question: what is different?](slides/21-compare-before-reveal.md)
22. [Defense depends on who controls the agent](slides/22-defense-depends-on-agent-location.md)
23. [Is a compromised agent malware?](slides/23-is-agent-malware.md)
24. [Success hidden inside noise](slides/24-success-hidden-in-noise.md)
25. [The agentic supply chain](slides/25-agentic-supply-chain.md)
26. [Bounded autonomous response](slides/26-bounded-autonomous-response.md)
27. [A map of work still to be done](slides/27-research-map-and-close.md)
