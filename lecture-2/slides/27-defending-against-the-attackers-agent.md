# Slide 27 — Case A defense: the sensors we have, decisions at machine speed

**Timing:** 73–77 minutes  
**Module:** Defense and research

## On-slide content

![The attacker's agent acts only through tools, so every action lands on an endpoint, identity or network flow that EDR, XDR, NDR and identity and flow logs already record; what must change is not the sensor but the tempo — a correlation problem at machine speed](../figures/case-a-defense.svg)

| What we have | What must change |
| --- | --- |
| EDR, XDR, NDR, identity and cloud audit logs: the agent cannot act without touching them | Correlate across them continuously, not alert by alert |
| The harness leaves traces: forensic traffic, recognizable identifiers, code-level artifacts (GTIG) | Detect the harness and the tempo, not the model |
| Human-paced triage and response | A defender's loop: observe → correlate → propose → verify authority and scope → act, bounded and reversible → verify effect → escalate |

> Case A needs no new sensor. It needs the defender's loop to run as fast as the attacker's — with explicit authorization, evidence thresholds, limited blast radius, reversibility and an audit trail.

## Speaker notes

Start from what the reference incident proved. Hugging Face reports that several security layers produced initial signals and that an AI-based security stack correlated them, but the system did not assign enough criticality to page the on-call team promptly. Detection succeeded; decision failed. That separates three problems — observe, connect, act in time — and Case A is mostly the second and third.

The sensors are the ones we already deploy. The attacker's agent has no way to act except through tools, and every tool action lands on a host, an identity or a network flow — the territory of EDR, XDR, NDR, identity providers and cloud audit logs. GTIG adds that autonomous frameworks currently trade stealth for velocity: forensic traffic, recognizable identifiers and code-level traces. And Unit 42's CAIRN campaign exploited known weaknesses — credentials, authentication bypasses, exposed APIs, old CVEs — so hygiene remains the floor.

What must change is tempo, and tempo means a loop on the defender's side too: observe, correlate evidence, propose an action, verify authority and scope, execute a bounded response, verify the effect, roll back or escalate. Bounded is the operative word. Autonomous response must not mean a defensive model with administrator rights; separate reasoning from authority through an enforcement boundary that checks identity, scope, policy and action risk. Response tiers run from gathering more evidence, to restricting a token or workload, to disruptive containment that needs explicit approval — and the system must verify whether the action worked and whether the campaign continued by another path.

Leave the open question for two slides on: which model runs that loop, and at what cost per event.

## Transition

“Case B is the opposite situation: we own the agent, so we can build the controls in.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Palo Alto Unit 42: Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors (12 November 2026)](https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/)
