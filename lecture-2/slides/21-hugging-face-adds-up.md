# Slide 21 — Hugging Face: what it adds up to

**Timing:** 54–56 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

About 17,600 recovered actions in about 6,280 clusters over roughly two and a half days — 7,677 of them on 11 July alone. Most paths produced nothing.

![Hugging Face as a sum: the attacker's objective, plus the attacker's agent (model and harness), plus a launchpad on the Internet, plus ordinary weaknesses at the victim, equals attacker-desired capability. Below, three readings of the same incident: a tireless operator — coverage, not elegance; the agent was the intruder, with no human in the loop; detection worked, the decision failed](../figures/equation-huggingface.svg)

Coverage, not elegance, found the viable chain. Failed attempts cost compute and time, not scarce human attention — and nothing in the loop ever waited.

## Speaker notes

State that these are reconstructed counts from available logs, not a guarantee that every action was observed. The daily split — 3,779 on 9 July, 1,135 on 10 July, 7,677 on 11 July, 3,892 on 12 July, 1,130 on 13 July — shows the shape of the previous slide: a quiet day of reconnaissance, then 11 July, when more than two fifths of all actions landed and the agent went from a pod to cluster-admin. Impact as stated: five datasets tied to the benchmark and some operational metadata, no other customer assets. Hugging Face reports that most actions went nowhere, but the aggregate search found a path across several independent systems.

The key change is the economics of persistence: failed experiments consume compute and time, but much less scarce human attention. A human operator who had tried a few hundred dead ends would have stopped or been noticed; the agent tried thousands and was, for a while, neither.

The sum mirrors Case B's, with the ownership reversed: the objective, the model and the harness are the attacker's, and the launchpad was borrowed from the open Internet; only the last term — ordinary weaknesses — belongs to the victim. The three readings each point at a different defense. A tireless operator means volume is also noise, which is the Case A defense slide. The agent as the intruder means there is no human tempo to detect; what remains is the harness, and GTIG notes that today's frameworks trade stealth for velocity. Detection worked and the decision failed is Hugging Face's own verdict, and it reframes the problem as correlating and deciding at machine speed.

Cut cue: if running slow, fold this slide into slide 20 — the counts become one spoken sentence after the detection step.

## Transition

“Case B brings no agent at all. The attacker uses yours — and there are two ways in.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

