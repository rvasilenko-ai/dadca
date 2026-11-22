# Slide 29 — Case A defense: the same sensors, a different arithmetic

**Timing:** 73–76 minutes  
**Module:** Defense and research

## On-slide content

![Case A defense in three rows. Same sensors: EDR and XDR, identity and cloud audit, NDR and flows — the agent cannot act without touching them. A different arithmetic: a human operator issues a few hundred actions a day, a handful clearly malicious; the attacker's agent issued 7,677 on 11 July alone and about 17,600 in all, none clearly malicious on its own — ten to a thousand times more events, each less malicious, meaningful only together. So triage changes: ranking alerts by severity for humans to read gives way to evaluating every event continuously, correlated across sources, with decisions at machine speed](../figures/case-a-defense.svg)

Build, one step per click:

0. Same sensors. The attacker's agent has no way to act except through tools, and every tool action lands on a host, an identity or a network flow — EDR and XDR, identity providers and cloud audit logs, NDR and flow metadata. Case A needs no new sensor.
1. A different arithmetic. Back to the Hugging Face numbers: about 17,600 recovered actions, 7,677 of them on 11 July — one every eleven seconds, around the clock. A human operator issues a few hundred a day. One to three orders of magnitude more events, and parallel agents multiply it again.
2. Each event is less malicious on its own: a valid token enumerating a cluster, a denied cloud call, a VPN enrollment, a clone with a leaked token, a pull request. In Hugging Face's own words, each signal was ambiguous alone; only correlated did they form a coherent attack.
3. So triage has to change. Ranking alerts by severity and having humans read the top assumes a few events carry the attack; here none does — the attack is the pattern. What replaces it is continuous evaluation of every event, correlated across sources, with decisions at machine speed: the defender's loop.

> No new sensor; a new tempo. Evaluate every event, continuously, because the attack is only visible as a pattern — and run the defender's loop at the attacker's speed: bounded, reversible, audited.

## Speaker notes

Start from what the reference incident proved. Hugging Face reports that several security layers produced initial signals, that each was ambiguous alone, that an AI-based security stack correlated them into a coherent attack signal, and that the system did not assign enough criticality to page the on-call team promptly. Detection succeeded; decision failed. That separates three problems — observe, connect, act in time — and Case A is mostly the second and third.

The sensors are the ones we already deploy. The attacker's agent has no way to act except through tools, and every tool action lands on a host, an identity or a network flow — the territory of EDR, XDR, NDR, identity providers and cloud audit logs. GTIG adds that autonomous frameworks currently trade stealth for velocity: forensic traffic, recognizable identifiers and code-level traces. And Unit 42's CAIRN campaign exploited known weaknesses — credentials, authentication bypasses, exposed APIs, old CVEs — so hygiene remains the floor.

The arithmetic is the new part, and the numbers are the incident's: about 17,600 recovered actions, 7,677 on 11 July — one every eleven seconds, around the clock. The human baseline is an estimate from hands-on-keyboard intrusions, where an operator's active session is a few hundred commands a day with long gaps; say that it is an estimate. The ratio is one to three orders of magnitude, and parallel agents — the frameworks run several — multiply it. The quality changes with the quantity: the agent's actions are individually ordinary — a valid service-account token enumerating a cluster, a denied mutating call, one of 181 VPN enrollments, a clone with a leaked token, a pull request — and most of them led nowhere. A severity-ranked queue has nothing to put at the top, which is why the classic SOC model of triaging the most malicious alerts by hand does not transfer. What is needed is continuous evaluation of the whole stream, so that the pattern becomes visible while it is forming.

What must change is tempo, and tempo means a loop on the defender's side too: observe, correlate evidence, propose an action, verify authority and scope, execute a bounded response, verify the effect, roll back or escalate. Bounded is the operative word. Autonomous response must not mean a defensive model with administrator rights; separate reasoning from authority through an enforcement boundary that checks identity, scope, policy and action risk. Response tiers run from gathering more evidence, to restricting a token or workload, to disruptive containment that needs explicit approval — and the system must verify whether the action worked and whether the campaign continued by another path.

Leave the open question for the funnel slide: which model evaluates every event, and at what cost — it serves both cases. First, the structural half of Case A: where the controls go.

## Transition

“And since we own the environment, that is where the controls go.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Palo Alto Unit 42: Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors (12 November 2026)](https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/)
