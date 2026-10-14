# Slide 20 — Part 2: how detection pipelines are built, and how they had to change

**Timing:** 45–46 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

# Part 2

## How detection pipelines are built, and how they had to change

> How are detection pipelines designed, and how did they evolve?

| Minutes | Module |
| --- | --- |
| 46–76 | Detection pipelines: design and evolution |
| 76–80 | Synthesis: five conclusions |

The five questions hidden in the word malware, then the detection pipeline, the options at every stage, and the stage that each change from Part 1 broke. Then the pipeline rebuilt generation by generation around the file and the host (antivirus, sandbox, EDR) and on the network (IDS, then encrypted traffic): what changed at each stage, why, and what each generation could not see. Then six misses to diagnose.

## Speaker notes

One sentence. Part 1 described the attack; Part 2 is the design and evolution of the detection pipeline: what each stage can choose from, which stage each attacker change broke, and why each period had to add a new layer when the evidence moved out of the previous one's view. The recurring PowerShell scenario from the exercise is the test case for every slide that follows.

## Transition

“Part 1 said what the attacker did. Before asking what a sensor can see of it, be precise about what we are looking for.”
