# Slide 19 — Part 2: how detection pipelines are built, and how they had to change

**Timing:** 45–46 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

# Part 2

## How detection pipelines are built, and how they had to change

> How are detection pipelines designed, and how did they evolve?

| Minutes | Module |
| --- | --- |
| 46–75 | Detection pipelines: design and evolution |
| 75–80 | Synthesis: five conclusions |

The detection pipeline and the question each stage answers. Then the pipeline as it was actually built, generation by generation, around the file and the host (antivirus, sandbox, EDR) and on the network (IDS, then encrypted traffic): what changed at each stage, why, and what each generation could not see. Then every change from Part 1 on one list, with the stage it broke and the product that answered; the menu of options at every stage as it stands today; and six misses to diagnose.

## Speaker notes

One sentence. Part 1 described the attack; Part 2 is the design and evolution of the detection pipeline, history first: the stages, the two pipelines rebuilt generation by generation, the stage each change broke, the menu as it stands today, and six misses. The recurring PowerShell scenario from the exercise is the test case: each lineage ends with what its generations would have captured of it.

## Transition

“Part 1 said what the attacker did and closed with four questions about it. Part 2 asks the fifth: what can a sensor see of any of it, and what has to happen first.”
