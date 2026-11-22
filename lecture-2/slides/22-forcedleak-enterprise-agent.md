# Slide 22 — Case B: the trusted agent, two ways in

**Timing:** 56–58 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

A legitimate agent runs inside the organization and acts with its authority. The attacker cannot invoke it directly — so they change what it reads, or what it runs.

| | Route 1 — injected context | Route 2 — poisoned harness |
| --- | --- | --- |
| The incident | ForcedLeak: Salesforce Agentforce, disclosed 2025 | MIDNIGHT NEPTUNE: a suspected DPRK cluster, GTIG, November 2026 |
| What the attacker controls | A CRM record the agent will later retrieve | A committed configuration file the agent will load |
| Who triggers it | An employee asking the agent a question | A developer starting the agent |
| What the agent does for the attacker | Leaks CRM data with its authority | Fetches and runs a backdoor with the developer's identity |
| Malicious file | None | Yes — after the agent fetched it |
| On the harness map | ② retrieval | ① tools, skills, plugins and hooks |

> Same case, two doors: the context the agent reads, and the harness it runs in. The question to hold for both: how does the attacker make a trusted agent use its authority for them?

## Speaker notes

The distinction from Case A was named on slide 16; the job here is to name the two doors before walking through either. In both, the agent is benign, organizationally deployed, and useful precisely because it can reach business data or run developer tooling on behalf of users. An external attacker cannot invoke those privileges directly, and no malicious agent has to enter the environment. What the attacker can do is change one of the two things the agent takes on trust: the context it reads, or the harness it runs in — slide 14's ② and ①.

Route 1 is ForcedLeak, a vulnerability chain demonstrated against a production enterprise-agent product and subsequently mitigated. It was not a publicly confirmed customer compromise; use "disclosed and demonstrated attack path", not "observed breach". Route 2 is MIDNIGHT NEPTUNE, a suspected DPRK cluster reported by GTIG in November 2026, which edited a coding agent's committed configuration so that starting the agent fetched a backdoor; the attribution is GTIG's and carries the word "suspected".

Read the table as the differences to watch for: what the attacker controls — data the agent reads versus configuration the agent runs; who unknowingly triggers it; what the agent ends up doing; and whether a malicious file exists at any point — none in ForcedLeak, one in MIDNIGHT NEPTUNE, and even there the agent was the loader. Keep the question on the slide open; the two attack paths answer it twice.

## Transition

“Route 1 first. The attacker begins with an ordinary public business interface — not with credentials or code execution.”

## Sources

- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
