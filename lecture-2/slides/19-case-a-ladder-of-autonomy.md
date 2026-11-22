# Slide 19 — Case A is a ladder of autonomy

**Timing:** 49–52 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

The weaponized agent is reported in the wild, at every level of autonomy.

```text
 5  the agent on your bill        LLMjacking: stolen cloud LLM credentials run the attacker's agent
 4  the agent runs alone          exploit_agent: diff the patch, write the exploit, fire it — no human
 3  the agent runs the campaign   ~80–90% of a thirty-target intrusion; the human sets objectives
 2  the model inside an implant   NIK C2 asks a model for commands; VOLTA asks it to rank the loot
 1  the model as assistant        a commercial model for reconnaissance, lures, translating loot
```

Build, one step per click:

0. Rungs, bottom up. Each rung hands the model more of the loop from slide 13.
1. The model answers questions; a human does everything else. State actors use commercial models for reconnaissance, lures and translating exfiltrated data.
2. Ordinary file-based implants embed one LLM call: NIK C2 to choose commands, VOLTA to rank a victim's assets.
3. The agent chooses and executes most steps; the human sets objectives and unblocks. In November 2025 an agent did an estimated 80–90% of a campaign across about thirty targets.
4. No human in the loop. exploit_agent compares code before and after a patch, drafts an exploit and runs it. Open-source multi-agent pentesting frameworks are picked up as attack platforms — the next slide looks at where they came from.
5. The attacker's agent, the victim's model. Stolen cloud LLM credentials: single-day bills above $100,000, $1 million cumulative; a key-escalation bug in LiteLLM; "LLM Mixers" resell the stolen access.

> November 2026, Google's threat-intelligence group: actors "fully automate vulnerability discovery and exploitation without a human in the loop for the first time." It lowers the skill floor — and, for now, trades stealth for velocity.

## Speaker notes

Keep each rung short; they are illustrations, not deep dives, and the ladder — not any one case — is the point: the loop from slide 13 with the human removed one step at a time.

Rung 1: GTIG reports Iranian and PRC-linked actors using Gemini for reconnaissance, social engineering and analysing stolen data; the model is a research assistant. Rung 2: NIK C2 and VOLTA, reported by Talos in late October 2026, are ordinary file-based implants that embed an LLM call — a Go remote-access tool with an OpenAI client, and an infostealer that sends the stolen bundle to a model to prioritize what to take. Rung 3: Anthropic reported, on 13 November 2025, a state-linked operator whose agent performed an estimated eighty to ninety percent of an intrusion campaign across roughly thirty targets; the August 2025 report described agent-assisted data extortion at scale. Rung 4, from GTIG's tracker of 16 November 2026: exploit_agent, found on an exposed staging server, runs continuous differential analysis of popular web applications, "drafts exploits, and automatically executes them without human intervention," with post-compromise scripts for reconnaissance, brute-forcing and webshells; CAIRN, an open-source multi-agent pentesting framework running an OODA loop over a shared blackboard, was seen in intrusions including US aerospace; a customized PentAGI platform scanned organizations across Asia between late August and early October 2026; HexStrike AI, an MCP harness over 150 offensive tools and 12 sub-agents, has been seen only in experimentation. Rung 5 is not an intrusion technique but an economy: LLMjacking steals cloud LLM credentials and resells the capacity. GTIG reports single-day fraudulent charges above $100,000 and $1 million cumulative, exploitation of CVE-2026-40217 in LiteLLM to turn limited virtual keys into administrator credentials, and "LLM Mixer" storefronts reselling access at $0.10 to $25 per million tokens. In the vocabulary of slide 16 that is Case A with a stolen model: the attacker's harness and objective, the victim's model capacity.

Where the reference incident sits: rung 4 under evaluation conditions; exploit_agent is rung 4 in the wild. Two cautions. The "first time" claim is a vendor's own observation. And the same report says autonomous frameworks currently trade stealth for velocity — forensic traffic, recognizable identifiers, code-level traces — which returns on the noise slide. The through-line: offensive capability that was concentrated in a few hands now reaches many, and the attacker's own agent does the work.

## Transition

“Rung four is worth its own slide: those agents are published research, released as open source.”

## Sources

- [Anthropic: disrupting the first reported AI-orchestrated cyber espionage campaign (13 November 2025)](https://www.anthropic.com/news/disrupting-AI-espionage)
- [Anthropic: detecting and countering misuse of AI, agent-assisted extortion (27 August 2025)](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)
- [Cisco Talos: NIK C2, an AI-enabled framework (29 October 2026)](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)
- [Cisco Talos: model-driven victim prioritization in the VOLTA infostealer (31 October 2026)](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Google Threat Intelligence Group, LLMjacking: Monetizing Compromised Cloud Models (2026)](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)
