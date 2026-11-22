# Slide 30 — Case A defense: guardrails in the environment

**Timing:** 76–79 minutes  
**Module:** Defense and research

## On-slide content

We do not own the attacker's agent; we own everything it has to act in. So the controls go on the environment: one at every point its actions can land.

![Case A guardrails, the environment view. Outside, dashed and not ours to control: the attacker's objective, model and harness. Inside the environment we own, a numbered control and sensor on each component the agent's actions land on: endpoints and edge devices, identity and credentials, workloads and clusters, cloud resources, source control and CI, network and egress; and a monitor M that evaluates every event continuously and correlates across sources](../figures/environment-guardrails.svg)

Build, one step per click:

0. The attacker's agent — objective, model, harness — sits outside, and nothing we do reaches it. Its actions reach us: every one lands on a component of the environment we own, instrument and constrain.
1. ① Endpoints and edge devices: EDR and XDR as the sensor; least privilege and patched software as the control. The CAIRN intrusions ran on dated CVEs and default credentials.
2. ② Identity and credentials: short-lived, scoped tokens tied to their origin; no shared administrator credential. One connector credential bound to the cluster superuser group was a Hugging Face root cause.
3. ③ Workloads and clusters: admission policies that forbid privileged pods; the metadata service blocked from pods; secrets out of environment variables — three more of the incident's root causes.
4. ④ Cloud resources: every API call audited, deny by default, private links. The denied mutating calls and the timed-out database connection were the controls that held.
5. ⑤ Source control and CI: protected branches; scoped, short-lived app tokens; configuration reviewed as code. The pull request that did not ship.
6. ⑥ Network and egress: NDR and flow logs as the sensor; egress allowlists; device identity before the mesh admits a node — 181 enrollments from one sandbox should not have been possible.
7. M — the monitor over everything: every event evaluated continuously and correlated across sources, with critical-severity alerting for the behaviours above. That is the defender's loop from the previous slide; which model runs it is the funnel, two slides on.

> Case A's guardrails are the environment's: the agent can still act, but every action lands on a control and a sensor. Structure first, correlation second — Hugging Face's own fix list is this slide.

## Speaker notes

Say the symmetry out loud, because it is the organizing idea of the defense module. On the next slide, for Case B, the big block is the harness, because we own it, and the environment is a small dashed box. Here the big block is the environment, because that is what we own, and the agent is the small dashed box. In both, the method is the same: find every point the attacker's agent can reach and put a structural control there first, a sensor second, and a monitor over all of it.

Walk the six against the incident, since every one of them maps to a root cause or a control that held. Endpoints and edge devices: the frameworks in the wild — CAIRN, PentAGI — exploited dated CVEs, default credentials and exposed services, so patching and least privilege remain the floor, and EDR and XDR are the sensors that see the agent's tool actions. Identity: Hugging Face's root causes include a shared connector credential bound to the superuser group and long-lived credentials in environment variables; the fix list is short-lived, scoped credentials, workload identity, and tokens flagged when used from an unexpected origin. Workloads: no admission policy blocked privileged pods, and pods could reach the instance metadata service; both are now closed. Cloud: the mutating calls were denied and the production database sat behind an allow-listed private link — the controls that held, and the audit trail is where the 17,600 actions came from. Source control: the GitHub App installation token and the pull request aimed at CI are the reason configuration and CI changes need review as code, protected branches and short-lived app tokens. Network: 181 mesh enrollments from a single sandbox is what device identity and egress allowlists are for, and flow logs are the sensor.

M is slide 29 restated as a control: evaluate every event continuously, correlate across sources, alert on the pattern — Hugging Face added critical-severity alerting for exactly the observed behaviours. Structure first, because allowlists, admission policies and short-lived credentials need no comprehension; correlation second, because the pattern is what the agent cannot hide. Which model does the correlating, and at what cost, is the funnel slide.

## Transition

“Case B is the opposite situation: we own the agent, so we can build the controls in.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Palo Alto Unit 42: Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors (12 November 2026)](https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/)
