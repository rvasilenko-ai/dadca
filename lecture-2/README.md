# Lecture 2: When the Attacker Is an Agent

**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** What changes when reasoning, tool use, and persistent trial-and-error become cheap?

**Framing beat (from Lecture 1):** Lecture 1 ends on a recurring pattern, offensive capability diffusing from the few to the many, with the 2017 Shadow Brokers spill-over (EternalBlue, then NotPetya) as the reference case. This lecture is that pattern's current instance: frontier AI capability, released commercially and as open weights, reaching everyone and lowering the skill floor, with the caveat that the diffusion is gradual and the offensive economy is not yet settled. Open by reconstructing the parallel and its limit.

## Learning outcomes

Students should be able to:

1. Reconstruct an agentic intrusion as a sequence of objectives, observations, actions, feedback, and adaptations.
2. Explain how model capability becomes consequential through tools, state, access, and delegated authority.
3. Distinguish noisy autonomous exploration from AI-assisted human operations and deliberately stealthy campaigns.
4. Contrast defense against an external attacker-operated agent with defense against a trusted enterprise agent hijacked through untrusted context.
5. Identify research problems in agent-trajectory observability, authorization, incident correlation, supply-chain security, and bounded response.

## Module schedule

| Time | Module | Slides |
| --- | --- | --- |
| 0–8 | Standalone foundation | 1–3 |
| 8–18 | Present the incident as a mystery | 4–7 |
| 18–40 | Reconstruct the attack | 8–16 |
| 40–55 | Why the agent succeeded | 17–21 |
| 55–64 | Why autonomous attacks are noisy | 22–24 |
| 64–72 | ForcedLeak: hijacking a trusted enterprise agent | 25–27 |
| 72–77 | Audience comparison and defensive reveal | 28–29 |
| 77–86 | Future research agenda | 30–32 |
| 86–90 | Research map and closing discussion | 33 |

## Primary cases

### Offensive case

The July 2026 Hugging Face technical timeline describes an autonomous agent operating during an OpenAI cyber-capability evaluation. The reconstructed campaign crossed several trust boundaries, generated roughly 17,600 recovered actions, and required AI-assisted defensive reconstruction.

### Internal-agent counter-case

ForcedLeak was a disclosed and demonstrated vulnerability chain in Salesforce Agentforce. Attacker-controlled instructions persisted in a CRM lead, were later retrieved during an employee’s legitimate interaction with the agent, and could cause sensitive CRM data to leave through crafted image requests. This was a real production vulnerability and attack demonstration, not a publicly confirmed customer breach.

## Source boundaries

- Slides label facts attributed to the Hugging Face, OpenAI, and ForcedLeak reports.
- Interpretations about optimization, noise, stealth, and future malware definitions are presented as lecture arguments or research hypotheses.
- Incident mechanics remain conceptual; slides do not reproduce payloads or exploit code.

## Slide index

1. [When the attacker is an agent](slides/01-when-attacker-is-agent.md)
2. [Standalone foundation](slides/02-standalone-foundation.md)
3. [What changes when reasoning is cheap?](slides/03-what-changes-when-reasoning-is-cheap.md)
4. [The incident in one slide](slides/04-incident-in-one-slide.md)
5. [The objective and the evaluation](slides/05-objective-and-evaluation.md)
6. [Where is the malware?](slides/06-where-is-malware.md)
7. [A journey across trust boundaries](slides/07-trust-boundaries.md)
8. [The evaluation sandbox escape](slides/08-evaluation-sandbox-escape.md)
9. [An external launchpad](slides/09-external-launchpad.md)
10. [The dataset becomes an attack surface](slides/10-dataset-as-attack-surface.md)
11. [File disclosure without code execution](slides/11-file-disclosure-without-code.md)
12. [Template injection to code execution](slides/12-template-injection-to-execution.md)
13. [Credentials become capabilities](slides/13-credentials-become-capabilities.md)
14. [Lateral movement as a capability graph](slides/14-lateral-movement-graph.md)
15. [Source control and supply-chain exposure](slides/15-source-control-supply-chain.md)
16. [A behavioral timeline](slides/16-behavioral-timeline.md)
17. [The agent loop](slides/17-agent-loop.md)
18. [Code reasoning](slides/18-code-reasoning.md)
19. [Operational orchestration](slides/19-operational-orchestration.md)
20. [Harness and authority](slides/20-harness-and-authority.md)
21. [Objective, feedback, and intent](slides/21-objective-feedback-intent.md)
22. [Approximately 17,600 recovered actions](slides/22-seventeen-thousand-actions.md)
23. [Success hidden inside noise](slides/23-success-hidden-in-noise.md)
24. [Block, adapt, repeat](slides/24-block-adapt-repeat.md)
25. [Case 2: The trusted enterprise agent](slides/25-forcedleak-enterprise-agent.md)
26. [ForcedLeak: the attack path](slides/26-forcedleak-attack-path.md)
27. [Dormant instructions, live authority](slides/27-dormant-instructions-live-authority.md)
28. [Audience question: what is different?](slides/28-compare-before-reveal.md)
29. [Defense depends on who controls the agent](slides/29-defense-depends-on-agent-location.md)
30. [Is a compromised agent malware?](slides/30-is-agent-malware.md)
31. [The agentic supply chain](slides/31-agentic-supply-chain.md)
32. [Bounded autonomous response](slides/32-bounded-autonomous-response.md)
33. [A map of work still to be done](slides/33-research-map-and-close.md)

## Editorial constraints

Kept from the lecture's implementation plan; they govern every revision of the slides.

- Explain the agent's success as model capability plus harness, tools, feedback, state, access and delegated authority, never as capability alone, and do not assign an artificial numerical split between code reasoning and operational orchestration.
- Treat "the model cannot distinguish good from bad" and "stealth is impossible to train" as overstatements. Use optimization and evaluation language: program semantics do not encode legitimate intent, the same capability serves either side, an agent optimizes the task and feedback it is given subject to the controls around it, and stealth is a harder verifier problem rather than an impossibility.
- Keep the three threat models distinct: noisy autonomous exploration, AI-assisted human operations, deliberately stealthy manual or agentic campaigns.
- Reverse-engineering a selected sample is not fleet-scale detection; say so wherever Project Ire or a comparable system appears.
- Frame autonomous response as scoped, authorized, evidence-based and reversible, with explicit escalation.
- Cite primary sources for the Hugging Face timeline, the OpenAI account, MITRE mappings and Project Ire; present recovered action and cluster counts as reconstructed figures.
- Verify ATT&CK and ATLAS names and identifiers against the live MITRE sites whenever they are edited; SearchLeak appears only as a brief corroborating example, not as a third case.

## Delivery guidance

- Introduce the incident as a mystery before revealing the attack path.
- Reuse `objective -> observation -> tool -> action -> feedback -> adaptation` throughout the reconstruction.
- Walk through both cases before naming their key distinction; let the audience identify differences in ownership, visibility, and enforcement first.
- Separate disclosed facts from instructor inference, especially when discussing the agent's objective and stealth.
- Avoid turning the incident section into a Kubernetes or exploit tutorial; focus on trust boundaries and capability amplification.
- End every major section with a concrete research or systems-design question.

## Primary sources

- [Hugging Face: technical timeline of the July 2026 incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [OpenAI: Hugging Face model-evaluation security incident](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
- [Varonis Threat Labs: SearchLeak](https://www.varonis.com/blog/searchleak)
- [MITRE ATT&CK](https://attack.mitre.org/)
