# Slide 4 — Where we are going

**Timing:** 5–6 minutes  
**Module:** Where is the malware?

## On-slide content

| Part 1 · How did malware and malicious capabilities evolve? (6–45) | Part 2 · How are detection pipelines designed, and how did they evolve? (45–80) |
| --- | --- |
| Why malware came to mean a file | One word, five questions; the detection pipeline and the options at each stage |
| What broke the file-centric model, and when | Where each change broke the pipeline; the host-and-file and network lineages, stage by stage |
| ATT&CK: behavior without a family name, capabilities delivered through benign files, an attack with no malware file | Six misses to diagnose; five conclusions |

One attack recurs throughout: a stolen administrator account, an inline PowerShell command, shellcode in memory, documents out over HTTPS. It is situation 2 from the vote. The detectors themselves, machine learning and the LLM analyst, are Lecture 3.

## Speaker notes

Now that the ambiguity has been felt, make the route explicit with the two questions, one per column. Part 1 is history: malware came to mean a file for good reasons, and over twenty-five years the attacker moved the capability out of it; ATT&CK is how we describe what remains when there is no family name. Part 2 is the defender's side of the same years, organised around the detection pipeline: what each stage can choose from, which stage each attacker change broke, and how the host and the network pipelines were rebuilt in response; then six misses to diagnose and the conclusions.

Point at the columns without reading them. Say that the detectors themselves, the machine learning and the LLM analyst, are deliberately thin here and get their own lecture, so that this one can spend its time on what the detector is allowed to see.

Name the recurring scenario once so it is recognised when it returns.

## Transition

“Why did malware become so strongly associated with files in the first place?”
