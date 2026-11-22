# Slide 28 — Case B defense: guardrails, the boundary text does not have

**Timing:** 77–81 minutes  
**Module:** Defense and research

## On-slide content

Same harness, third time. Every red point of the attack view gets a control.

![Guardrails: a control at every point the attacker can write to — tools, retrieval, memory, tool servers, credentials — plus egress control and a monitor on every transition](../figures/harness-guardrails.svg)

*Guardrails: a control at every point the attacker can write to — tools, retrieval, memory, tool servers, credentials — plus egress control and a monitor on every transition*

Build, one step per click:

0. The harness of slide 12 with the attack points of slide 14. The model stays untrusted by design.
1. ① Tools, skills, plugins, hooks: allowlists, least privilege, human approval for consequential actions; skills and hooks signed and reviewed like code.
2. ② Retrieval: untrusted text is labelled and spotlighted, and in the strongest designs never reaches the model that holds authority.
3. ③ Memory: provenance travels with what is stored; nothing imperative persists without review.
4. ④ Tool servers: pinned, signed, allowlisted — the supply chain of slide 15.
5. ⑤ Credentials: a per-agent identity with short-lived, scoped tokens, never more than the user has.
6. E — Egress: trusted destinations only and output filtering; Salesforce's own ForcedLeak fix was a trusted-URL allowlist.
7. M — Monitor: the trajectory is logged and every transition classified. That is the next slide.

| Pattern | What it does | Strength |
| --- | --- | --- |
| Instruction hierarchy (training) | The model learns to rank system over user over tool text | Raises the bar; still probabilistic |
| Spotlighting (marking) | Untrusted text is delimited or transformed so the model can tell it apart | Raises the bar |
| Dual LLM / quarantined model | The model that reads untrusted text has no tools; the privileged one never reads it | Structural |
| CaMeL: capabilities and control flow | A trusted model writes the plan; untrusted data carries capabilities that policy checks at every tool call | Structural, with guarantees for a class of attacks |
| Six design patterns (2025) | Action-selector, plan-then-execute, map-reduce, dual LLM, code-then-execute, context minimization | Structural; each trades some utility |
| Injection classifiers | A small model flags imperative or jailbreak text in inputs | Probabilistic; evadable |

> There is no NX bit for text, so the guardrail is architecture: restrict what untrusted text can reach, what the agent can do, and where its output can go. Training raises the bar; structure holds it. Break the lethal trifecta — private data, untrusted content, an exfiltration channel — and most of Case B cannot happen.

## Speaker notes

Walk the diagram against slide 14: every control sits exactly where an attack arrow ended. Then give the architecture view, because this is where the research is. Willison's dual-LLM pattern (2023) and lethal-trifecta rule (2025) are the simplest statements: a model that reads untrusted content must not also hold tools and an exfiltration channel. CaMeL (Debenedetti et al., 2025) makes it systematic — a privileged model produces a program from the user's request, a quarantined model parses untrusted data, and capabilities attached to data are checked by policy before any tool call, which gives provable protection for a class of injections at a utility cost — measured on AgentDojo, the benchmark of injection attacks and defenses for agents, which is the measurable artifact to point students at. Beurer-Kellner et al. (2025) catalogue six design patterns that make the same trade in different places. The instruction hierarchy (Wallace et al., 2024) and spotlighting (Hines et al., 2024) are training- and marking-based: they raise the bar but remain probabilistic, which is why they sit above the structural rows, not instead of them. Detection classifiers for injected text are the cheap outer layer — and models, so attackable; hold that for slide 30.

Map ForcedLeak onto the diagram: the record entered at ②, became instruction in context, inherited ⑤, and left through the actions arrow — the fix at E closed the last step, and a control at ② or ⑤ would have closed it earlier. Map MIDNIGHT NEPTUNE: ① and ④, and the fix is review of agent configuration as code. The OWASP agentic threats-and-mitigations guide is the practitioner's checklist for the same points.

## Transition

“Both cases end at the same question: something has to watch every transition — and a frontier model on every event is not affordable.”

## Sources

- [Willison, The Dual LLM pattern for building AI assistants that can resist prompt injection (2023)](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/)
- [Willison, The lethal trifecta for AI agents (2025)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [Debenedetti et al., Defeating Prompt Injections by Design — CaMeL (2025)](https://arxiv.org/abs/2503.18813)
- [Beurer-Kellner et al., Design Patterns for Securing LLM Agents against Prompt Injections (2025)](https://arxiv.org/abs/2506.08837)
- [Debenedetti et al., AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents (2024)](https://arxiv.org/abs/2406.13352)
- [Wallace et al., The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions (2024)](https://arxiv.org/abs/2404.13208)
- [Hines et al., Defending Against Indirect Prompt Injection Attacks With Spotlighting (2024)](https://arxiv.org/abs/2403.14720)
- [OWASP, Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
