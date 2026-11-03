# Slide 4 — Where we are going

**Timing:** 5–6 minutes  
**Module:** Where is the malware?

## On-slide content

| Part 1 · How did malware and malicious capabilities evolve? (6–45) | Part 2 · How are detection pipelines designed, and how did they evolve? (45–80) |
| --- | --- |
| Why malware came to mean a file | The detection pipeline, and what each stage can see |
| What broke the file-centric model, and when | How the host and network pipelines were rebuilt, and where each change broke them |
| ATT&CK: describing behavior without a family name | The options at each stage today; six misses to diagnose |

## Speaker notes

Now that the ambiguity has been felt, make the route explicit with the two questions, one per column. Part 1 is history: malware came to mean a file for good reasons, and over twenty-five years the attacker moved the capability beyond it, without giving the file up; ATT&CK is how we describe what remains when there is no family name. Part 2 is the defender's side of the same years, organised around the detection pipeline: the pipeline and its stages, the host and the network pipelines rebuilt generation by generation, the stage each attacker change broke and the product that answered, the options at each stage as they stand today; then six misses to diagnose and the conclusions.

Point at the columns without reading them. Say that the detectors themselves, the machine learning and the LLM analyst, are deliberately thin here and get their own lecture, so that this one can spend its time on what the detector is allowed to see.

The recurring scenario is not on the slide; it is situation 2 from the vote and introduces itself when it returns on the mapping exercise.

## Transition

“Why did malware become so strongly associated with files in the first place?”
