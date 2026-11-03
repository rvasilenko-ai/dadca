# Slide 20 — The complete detection pipeline

**Timing:** 46–49 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

> Part 1 closed with four questions about the thing itself: what it is, what it can do, who controls it, whose objective it serves. Part 2 asks the fifth: what can a sensor see of any of that, and what has to happen before a detector sees anything?

```text
activity
  -> sensor
  -> acquisition
  -> extraction
  -> representation
  -> detection
  -> investigation
  -> decision
  -> response
```

> A detector cannot reason about evidence it never receives.

## Speaker notes

The opening callout is the hinge between the parts. Part 1's four questions are about the thing; every defender is limited by a fifth, what the system can actually observe, and the history of detection products is the history of that question. Every slide from here to the exercise asks what a sensor could see, and the eight stages are the vocabulary for the answers; do not belabor them, they are a legend for everything that follows.

Define the stages:

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

