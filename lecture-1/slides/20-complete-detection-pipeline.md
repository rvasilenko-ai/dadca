# Slide 20 — The complete detection pipeline

**Timing:** 46–49 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

> What can a sensor see, and what has to happen before a detector sees anything?

Next and Previous step through the eight stages; each step lights the stage on the strip, shows one panel for that stage (the question, one line, two or three examples drawn from the menu on slide 25). Clicking a stage jumps to it. The thesis callout is the last step.

| Stage | Question | One line | For example |
| --- | --- | --- | --- |
| Sensor | can the system observe the event or state? | Where the pipeline touches reality: a hook, a tap, a log. | file-system hooks, process and script telemetry, a network tap, identity and SaaS logs, the agent's harness |
| Acquisition | is the evidence collected and retained? | Seeing is not keeping: what is captured, and for how long. | capture the file on write, triggered memory capture, packets for hours, flow records for months, central forwarding |
| Extraction | can usable artifacts or fields be recovered? | Raw evidence becomes something analyzable, and this stage has failures of its own. | file parsing, unpacking and emulation, script deobfuscation, decompilation, TLS decryption, process-tree reconstruction |
| Representation | what information is supplied to analysis? | What a model is allowed to learn from, and what was discarded before it arrived. | hashes and byte patterns, engineered features, sequences, graphs, text |
| Detection | is a score, rule, or verdict produced? | The only stage most people call detection. | signatures, expert rules, classifiers, anomaly baselines, similarity, reputation |
| Investigation | can evidence be connected and explained? | Where the expensive methods live. | enrichment, timelines across sources, detonation, forensics, reverse engineering, LLM-assisted analysis |
| Decision | can an appropriate action be selected? | Where authority is designed. | automatic block above a threshold, approval playbooks, pre-authorized containment, escalation |
| Response | can the action be executed in time? | A detection is not an outcome until this works. | isolate and quarantine, revoke tokens, block destinations, restore, patch, revoke an agent's tools |

> A detector cannot reason about evidence it never receives.

## Talking points

- Open with the hinge: four questions about the thing in Part 1; the fifth, what a sensor can see, is Part 2.
- Eight stages, one step each: the question, one line, two or three examples from the menu; about twenty seconds a stage.
- A detector cannot reason about evidence it never receives.

## Speaker notes

Open with the hinge, spoken: Part 1 closed with four questions about the thing itself, what it is, what it can do, who controls it, whose objective it serves, and Part 2 asks the fifth. Part 1's four questions are about the thing; every defender is limited by a fifth, what the system can actually observe, and the history of detection products is the history of that question. Every slide from here to the exercise asks what a sensor could see, and the eight stages are the vocabulary for the answers; they are a legend for everything that follows, so keep each step to its question and one example. Next and Previous step through the stages, and clicking a stage jumps to it.

The stages:

- **Sensor:** can the system observe the event or state?
- **Acquisition:** is the evidence collected and retained?
- **Extraction:** can usable artifacts or fields be recovered?
- **Representation:** what information is supplied to analysis?
- **Detection:** is a score, rule, or verdict produced?
- **Investigation:** can evidence be connected and explained?
- **Decision:** can an appropriate action be selected?
- **Response:** can the action be executed in time?

## Transition

“Every stage of this pipeline is a choice, and the choices were made in history. The host first: three generations of the same pipeline.”

