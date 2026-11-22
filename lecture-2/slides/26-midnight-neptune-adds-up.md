# Slide 26 — MIDNIGHT NEPTUNE: what it adds up to

**Timing:** 66–68 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

![MIDNIGHT NEPTUNE as a sum: attacker-controlled configuration, plus a trusted agent (model and harness), plus a developer's identity and machine, plus a permitted outbound channel, equals attacker-desired capability. Below, three readings of the same incident: the repository contains the payload; the agent is the loader; the settings file is the supply chain](../figures/equation-neptune.svg)

Dormant configuration, live authority: the hook is inert in the repository and runs when any developer starts the agent. This time a file does arrive — a very ordinary backdoor — and the agent fetched it.

## Speaker notes

Same four ingredients as ForcedLeak, different instances. Attacker-controlled data has become attacker-controlled configuration: a hook in the project's committed settings, which the agent treats as its own instructions rather than as content. The trusted agent is the same kind of thing — a model in a harness — and here the harness itself was the door. The identity is a developer's, on a developer's machine, with whatever the developer can reach. The outbound channel is an ordinary download that nothing blocked. The sum is the same: capability the attacker wanted, obtained through authority the attacker never had.

The three readings deserve the same treatment as before. The repository contains the payload: configuration is code, and a configuration hook is executable intent, so review it like code — the defensive takeaway for the close. The agent is the loader: the first malicious file appears only after the agent fetched it, so a file-centric detector sees the backdoor and not the mechanism, and the mechanism is what repeats. The settings file is the supply chain: GTIG's phrase is "a supply chain vector internal to the organization," because the file is designed to be shared, and one commit reached every developer who opened those repositories.

Contrast with ForcedLeak in one sentence: there, nothing was a file and the agent leaked data; here, a file arrived and the agent ran it. Both are the victim's own agent, run by the victim, serving the attacker. That is the pair to carry into the comparison.

## Transition

“Two cases, three incidents. Before naming the difference, compare them as defenders.”

## Sources

- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Claude Code documentation: settings files and their scope](https://docs.claude.com/en/docs/claude-code/settings)
- [Claude Code documentation: hooks](https://docs.claude.com/en/docs/claude-code/hooks)
