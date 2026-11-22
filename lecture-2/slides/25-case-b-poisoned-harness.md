# Slide 25 — MIDNIGHT NEPTUNE: the attack path

**Timing:** 64–67 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

Case B, second route — the poisoned harness. A suspected DPRK cluster, reported by GTIG, November 2026

![MIDNIGHT NEPTUNE path across three zones. On the Internet: a fake recruiter with a model-generated photo, then a fake meeting page with a ClickFix lure. Inside the organization: a foothold and a pivot into the internal code repositories, where the committed agent settings gain a startup hook. For every developer: starting the coding agent on an ordinary morning runs the hook, which downloads the SOMBERMEME backdoor, and GitHub tokens named after Copilot disguise the lateral movement. Red arrows mark the trust boundaries crossed](../figures/poisoned-harness.svg)

Nothing was injected into the agent's context. Its harness was edited — and the settings file is meant to be committed, so one commit reached every developer who opened those repositories.

| | ForcedLeak | MIDNIGHT NEPTUNE |
| --- | --- | --- |
| Route in | Injected context: a CRM record | Poisoned harness: a configuration hook |
| Who triggers it | An employee asking the agent a question | A developer starting the agent |
| What the agent does for the attacker | Leaks CRM data with its authority | Fetches and runs a backdoor with the developer's identity |
| Malicious file | None | Yes — after the agent fetched it |

> Same case, two doors: the context the agent reads, and the harness it runs in. Slide 14's ① and ②, each now with a real incident.

## Speaker notes

Walk the chain. The social engineering is classic — fake recruiters, a fake meeting platform, a "run this fix" lure — and GTIG notes the recruiter photos carried SynthID watermarks, so the personas were model-generated. What is new is the persistence step: after the foothold, the actor "pivoted into internal code repositories" and modified `.claude/settings.json` "so that when users started up Claude Code, it would automatically trigger the download of the SOMBERMEME backdoor." The project settings file is designed to be committed and shared, so the hook travelled with the code to every developer who opened those repositories — in GTIG's words, "a supply chain vector internal to the organization," "exploiting native AI agent execution hooks as enterprise access vectors." GTIG did not publish the modified file; a hook that runs on start is the mechanism its description implies. The targets were cryptocurrency organizations in North America and Europe; the attribution is "suspected."

Put it beside ForcedLeak. Both are the victim's own agent, run by the victim, serving the attacker. ForcedLeak enters through what the agent reads and ends with no file at all; MIDNIGHT NEPTUNE enters through what the agent runs and ends with a very ordinary backdoor — the agent was the loader. On the harness diagram that is ① tools, skills, plugins and hooks, with ④ the supply chain, since the poisoned configuration arrived through the repository.

Two more GTIG observations belong here as footnotes, not slides: PRC-linked actors staging lures and exfiltrating data through a frontier model's file-hosting infrastructure and backend API — the AI vendor as a trusted channel, the trusted-vendor pattern from the malware world — and tokens named after an AI assistant so that lateral movement looks like tooling. Defensive takeaway for the close: agent configuration is code, so review it like code; and the agent's own identity and network are what to watch.

## Transition

“Two cases, three incidents. Before naming the difference, compare them as defenders.”

## Sources

- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Claude Code documentation: settings files and their scope](https://docs.claude.com/en/docs/claude-code/settings)
- [Claude Code documentation: hooks](https://docs.claude.com/en/docs/claude-code/hooks)
