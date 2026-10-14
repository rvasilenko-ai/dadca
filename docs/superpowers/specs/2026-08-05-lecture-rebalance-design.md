# Malware and AI Lecture Rebalance — Design

**Date:** 2026-08-05  
**Scope:** Rebalance the final part of Lecture 1 and restructure Lecture 2 around two contrasting agentic attack cases.  
**Audience:** Master's and PhD cybersecurity students without an assumption of detailed prior knowledge of every framework or implementation.

## Objectives

1. Make Lecture 1 the primary home for LLM-assisted malware analysis, reverse-engineering tooling, and the distinction between investigation capability and scalable detection.
2. Make Lecture 2 a case-led comparison of two operationally different agentic attack models:
   - an attacker-operated autonomous agent outside the defender's environment;
   - a legitimate enterprise agent hijacked through attacker-controlled context.
3. Map both cases using MITRE Enterprise ATT&CK and MITRE ATLAS from the outset.
4. Show how the cases differ in attack shape, economics, applicability, observability, and defensive control points.
5. Separate reported incident facts from hypotheses about how similar attack models may be used in future operations.

## Lecture 1 changes

Lecture 1 keeps its existing 90-minute duration and 33-slide limit. Slides 29–31 will become the complete LLM reverse-engineering section.

### Slide allocation

- **Slide 29 — Project Ire as a worked workflow:** selected artifact, structural triage, tool calls, evidence chain, validation, and assessment.
- **Slide 30 — Capability depends on the extraction ecosystem:** native and managed-code decompilers, Go and Rust recovery, parsers, sandboxes, runtime evidence, provenance, and uncertainty.
- **Slide 31 — Reverse engineering is not detection:** high-volume filtering, triage, prioritization, selected deep investigation, and misses introduced before the LLM sees an artifact.
- **Slides 32–33:** retain synthesis and closing conclusions, updated only where necessary to refer back to the revised slides.

The existing concepts of three analysis scales, model suitability, and selecting investigations will be preserved within slides 29–31 rather than discarded.

## Lecture 2 structure

Lecture 2 remains 90 minutes and 33 slides.

| Time | Section | Approximate slides |
| --- | --- | --- |
| 0–8 | Standalone foundation | 1–3 |
| 8–35 | Hugging Face reconstruction | 4–15 |
| 35–47 | Hugging Face ATT&CK/ATLAS mapping and applicability | 16–19 |
| 47–59 | ForcedLeak reconstruction | 20–24 |
| 59–71 | ForcedLeak ATT&CK/ATLAS mapping and applicability | 25–28 |
| 71–82 | Operational and defensive comparison | 29–31 |
| 82–88 | Bounded autonomous response | 32 |
| 88–90 | Research map and conclusion | 33 |

Exact slide boundaries may shift by one slide during implementation, but the time allocations and section order must remain stable.

## Case 1: attacker-operated autonomous agent

The Hugging Face/OpenAI case remains the primary example. The reconstruction should focus on boundary crossings, feedback, adaptation, credential and token acquisition, lateral movement, source-control exposure, and the volume of recovered actions.

### ATT&CK and ATLAS treatment

Enterprise ATT&CK describes most observable effects, including:

- exploitation of public-facing applications;
- credential and application-token access;
- use of valid accounts;
- discovery and collection;
- access to information and code repositories;
- transfer, execution, and cross-system movement where supported by the incident sources.

ATLAS describes the AI-agent mechanism and autonomous orchestration. The teaching point is that AI changes the operator's persistence, speed, breadth, and feedback loop, while many resulting behaviors remain familiar to conventional detection systems.

Mappings must distinguish:

- behavior confirmed by the incident reports;
- reasonable mapping inference;
- attempted access or impact that was not demonstrated to have succeeded.

In particular, access to source control must not be presented as a successful software supply-chain compromise when the reports state that no unauthorized change was found in published artifacts.

### Applicability discussion

Present the following as a threat-model projection, not as the reported actor's motivation:

- Autonomous exploration can be applied opportunistically across many targets when the operator has sufficient compute, tooling, target access, and objective feedback.
- Scaling is constrained by model and infrastructure cost, heterogeneous targets, rate limits, unreliable tools, egress restrictions, and difficulty verifying success.
- High exploration volume makes this model comparatively noisy and may shorten the useful dwell window.
- Plausible short-window objectives include stealing credentials, tokens, and readily accessible data, or executing destructive/extortion actions such as ransomware.
- Stolen credentials and tokens can be retained, resold by access brokers, or transferred to a later human-operated campaign that is quieter and more disciplined.

Use “grab-and-go,” not “grub and go,” in on-slide language.

## Case 2: hijacked enterprise agent

ForcedLeak remains the primary internal-agent case. It must be described as a real vulnerability chain demonstrated against a production product and subsequently mitigated, not as a publicly confirmed customer breach.

### Attack reconstruction

1. An attacker submits concealed instructions through a public Web-to-Lead form.
2. The instructions persist as data in a CRM record.
3. An employee later performs a legitimate interaction with Agentforce concerning that record.
4. The trusted agent retrieves the record and interprets attacker-controlled data as instructions.
5. The agent acts with the authority of its running or organizational user.
6. The demonstrated chain retrieves CRM information and transmits data through crafted image requests and a trusted-domain weakness.

The reconstruction must emphasize delayed activation, confused authority, and the transition from passive stored data to operational instruction.

### ATT&CK and ATLAS treatment

ATLAS describes the AI-specific mechanism:

- prompt infiltration through a public-facing application;
- indirect prompt injection;
- delayed execution of LLM instructions where supported by the current ATLAS release;
- agent tool invocation;
- exfiltration through AI-agent tool invocation.

Enterprise ATT&CK describes the resulting enterprise effects:

- `T1213.004 — Data from Information Repositories: Customer Relationship Management Software`;
- an appropriate web-based exfiltration technique, selected conservatively based on the documented channel.

Do not map `T1078 — Valid Accounts` as if credentials were stolen. The agent uses legitimate delegated authority, which is conceptually similar from an effect perspective but materially different from compromising an account. This distinction should be visible on the slide.

The teaching point is that ForcedLeak can collapse or skip expected kill-chain stages: the attacker does not necessarily require host execution, conventional persistence, or lateral movement before reaching collection and exfiltration.

### Applicability discussion

Present the following as a threat-model projection:

- The attack requires an agent that consumes attacker-controlled content and can retrieve data, invoke tools, or communicate externally with useful authority.
- The injection itself may be sprayed broadly, but successful activation depends on a compatible workflow and later agent interaction.
- Activation can be delayed and low-volume, and actions can appear under a legitimate user or agent identity.
- This makes the model potentially quieter than autonomous external exploration, but not inherently undetectable or universally stealthy.
- Plausible objectives include targeted collection, business-process manipulation, reconnaissance, and staging information or access for a later campaign.
- ForcedLeak alone must not be described as establishing durable persistence or interactive control unless a follow-on mechanism provides it.

## Comparative synthesis

The lecture will compare the cases directly.

| Dimension | Hugging Face attack model | ForcedLeak attack model |
| --- | --- | --- |
| AI role | Attacker-operated autonomous operator | Defender-operated agent redirected by attacker input |
| Agent location | Outside defended environment | Inside trusted business workflow |
| Authority | Acquired credentials and exposed capabilities | Legitimate delegated agent/user authority |
| Attack shape | Long exploratory chain across systems | Shorter chain from poisoned context to privileged effect |
| Targeting | Potentially broad and opportunistic | Requires a compatible vulnerable agent workflow |
| Noise | Many attempts, failures, and observable effects | Potentially delayed, sparse, and blended with normal activity |
| Defender visibility | Resulting network, identity, host, and application behaviors | Potentially context, retrievals, reasoning trajectory, tool calls, identity, and effects |
| Guardrails | Defender cannot govern the attacker's model | Defender or provider can enforce context, tool, identity, approval, and egress policy |
| Likely short-term use | Credential/token/data theft or destructive impact | Quiet collection, workflow manipulation, or campaign staging |

The principal conclusion is:

> In the first case, defenders respond to the consequences of someone else's agent. In the second, they must prevent their own agent from becoming the attacker's execution environment.

“Reasoning trajectory for the agent” means the observable sequence of assembled context, intermediate decisions exposed by the system, tool selection, tool results, revisions, approvals, and actions. It must not be equated with hidden chain-of-thought. Visibility must be described as deployment-dependent, especially for SaaS agents.

## Defensive implications

### Attacker-operated agent

- Detect and correlate behavior across public services, identity, cloud, host, application, and repository telemetry.
- Treat high failure volume as part of an adaptive campaign rather than independent low-severity alerts.
- Remove authority and trust paths during containment, rather than blocking only the latest indicator or channel.
- Anticipate credential resale and delayed follow-on operations after the noisy campaign appears to stop.

### Hijacked enterprise agent

- Preserve provenance and trust labels as external data enters retrieval context.
- Enforce least privilege at the agent identity and individual tool invocation.
- Apply egress restrictions and destination-aware data policies.
- Record a defensible agent reasoning trajectory and link it to identity, retrieval, tool, application, network, and data-access telemetry.
- Use smaller models where appropriate to inspect structured transitions economically, without presenting them as sufficient or infallible controls.

## Evidence and source policy

- Incident claims must cite the Hugging Face, OpenAI, or Noma ForcedLeak primary reports.
- ATT&CK and ATLAS names and identifiers must be verified against the live MITRE sites during implementation.
- SearchLeak may appear only as a brief corroborating example, not as a third full case.
- Forecasts about scale, economics, stealth, access brokering, ransomware, and sophisticated follow-on activity must be labeled as hypotheses or plausible operational models.
- Slides remain conceptual and must not reproduce executable exploit payloads.

## Acceptance criteria

1. Both decks retain 33 slides and 90-minute schedules.
2. Lecture 1 contains the complete LLM reverse-engineering/tooling/detection-selection section.
3. Lecture 2 contains two complete case reconstructions followed by ATT&CK/ATLAS mappings and applicability analysis.
4. Both mapping sections distinguish reported fact, mapping inference, and forecast.
5. Lecture 2 explicitly compares kill-chain shape, attacker economics, noise, likely objectives, observability, and defensive control points.
6. All local slide-index links resolve and no removed filenames remain referenced.
7. All external technique identifiers and incident citations are verified before completion.
