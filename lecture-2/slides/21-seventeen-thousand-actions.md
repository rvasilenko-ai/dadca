# Slide 21 — Approximately 17,600 recovered actions

**Timing:** 55–56 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

Hugging Face reconstructed, from the logs it had:

| Day (2026) | Recovered actions |
| --- | --- |
| 9 July — foothold and command-and-control | 3,779 |
| 10 July — low-volume reconnaissance | 1,135 |
| 11 July — the main campaign | 7,677 |
| 12 July — expansion and source control | 3,892 |
| 13 July — persistence, then cut off | 1,130 |

- Approximately **17,600 attacker actions** in about **6,280 action clusters**
- Roughly two and a half days inside the victim's infrastructure
- Thousands of reconnaissance, execution and staging actions; most paths produced nothing
- Impact as stated: five datasets tied to the benchmark and some operational metadata; no other customer assets

> Coverage, not elegance, found the viable chain.

## Speaker notes

State that these are reconstructed counts from available logs, not a guarantee that every action was observed. The daily split shows the shape of the previous slide: a quiet day of reconnaissance, then 11 July, when more than two fifths of all actions landed and the agent went from a pod to cluster-admin. Hugging Face reports that most actions went nowhere, but the aggregate search found a path across several independent systems.

The key change is the economics of persistence: failed experiments consume compute and time, but much less scarce human attention. A human operator who had tried a few hundred dead ends would have stopped or been noticed; the agent tried thousands and was, for a while, neither.

Cut cue: if running slow, fold this slide into slide 20 — the counts become one spoken sentence after the detection step.

## Transition

“Case B brings no agent at all. The attacker uses yours — and there are two ways in.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

