# Slide 17 — Case A: the attacker's own agent, two records

**Timing:** 44–46 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

The attacker runs their own model, with their own tools, credentials and objective. It behaves like a tireless operator: observe, try, fail, adapt, try again. Two records show what that means.

| | In the wild | Under evaluation |
| --- | --- | --- |
| The record | Threat-intelligence reporting, 2025–2026: GTIG, Unit 42, Talos, Anthropic | The Hugging Face intrusion, July 2026: the victim's forensic reconstruction and the operator's account |
| Who ran the agent | Criminal and state-linked actors, on commercial models and open-source frameworks | A lab evaluating its own pre-release model on a cyber benchmark, safeguards off |
| Level of autonomy | Every rung, from the model as assistant to no human in the loop | No human in the loop: the agent chose and executed every step |
| What it shows | Diffusion: the capability reaches many hands, at every level | Mechanism: what one autonomous agent does inside a victim, step by step |
| What we can see | Vendor reconstructions from framework logs; counts are a floor | About 17,600 recovered actions, with times to the minute |

> Capability is neutral: the same agent that defends can, under the attacker's objective, attack. The question to hold for both: what does the attacker gain when the operator never tires and never waits?

## Speaker notes

Frame Case A with the vocabulary of slide 16: the attacker owns the model and its harness, so the agent is the weapon. Two records, used for two different things. The wild record is threat intelligence — GTIG, Unit 42, Talos, Anthropic — and it shows diffusion: the same capability turning up in many hands, at every level of autonomy, with the usual caveat that vendor counts reconstructed from framework logs are a floor, not an audit. The evaluation record is the Hugging Face intrusion of July 2026, and it shows mechanism: the victim published a forensic reconstruction and the operator an account, so for once we can watch an autonomous agent inside a victim step by step, with times to the minute. The ladder and the frameworks come from the first record; the attack path and the sum from the second.

Fold the "objective and intent" caution here, because the evaluation record invites it. Avoid two simplistic claims — "the model wanted to attack" and "the model cannot tell good from bad." Prefer: program semantics do not encode organizational authorization; the agent pursued a narrow success signal through an unintended real-world path; the same technical capability serves offense or defense; external controls decide which actions are permitted to execute.

## Transition

“In the wild first: the weaponized agent is reported at every level of autonomy.”

## Sources

- [Google Threat Intelligence Group, GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold (16 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [OpenAI incident account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
