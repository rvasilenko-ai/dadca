# Slide 18 — Case A beyond one incident

**Timing:** 50–53 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

The weaponized model is reported in the wild, not only in a lab.

| Case | What it shows |
| --- | --- |
| AI-orchestrated espionage (Nov 2025) | An agent ran most of a multi-target intrusion campaign |
| Agent-assisted extortion, "vibe hacking" (Aug 2025) | Reasoning used to scale a data-extortion operation |
| NIK C2 (Oct 2026) | A Go remote-access tool that calls an LLM from the victim's host |
| VOLTA (Oct 2026) | An infostealer that asks a model to rank the victim's assets |

> It lowers the skill floor: offensive capability that was concentrated in a few hands now reaches many, with the attacker's own model doing the work.

## Speaker notes

Keep each short; they are illustrations, not deep dives. Anthropic reported, on 13 November 2025, a state-linked operator whose agent performed an estimated eighty to ninety percent of an intrusion campaign across roughly thirty targets; the August 2025 report described agent-assisted data extortion at scale. NIK C2 and VOLTA, reported by Talos in late October 2026, are ordinary file-based implants that embed an LLM call — a Go remote-access tool with an OpenAI client, and an infostealer that sends the stolen bundle to a model to prioritize what to take. The through-line: offensive capability diffusing from the few to the many, here with the attacker's model doing operator-grade work.

## Transition

“Case B brings no model at all. The attacker uses yours.”

## Sources

- [Anthropic: disrupting the first reported AI-orchestrated cyber espionage campaign (13 November 2025)](https://www.anthropic.com/news/disrupting-AI-espionage)
- [Anthropic: detecting and countering misuse of AI, agent-assisted extortion (27 August 2025)](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)
- [Cisco Talos: NIK C2, an AI-enabled framework (29 October 2026)](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)
- [Cisco Talos: model-driven victim prioritization in the VOLTA infostealer (31 October 2026)](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
