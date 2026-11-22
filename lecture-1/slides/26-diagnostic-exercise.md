# Slide 26 — Diagnostic exercise

**Timing:** 68–75 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content
![Diagnostic exercise: six misses as cards above the pipeline strip — a memory-resident payload missed by an on-write scanner; an HTTPS transfer missed by a plaintext signature; a parsed PE file scored benign; three low-severity alerts closed as noise; a correct alert whose isolation needed an unreachable approval; an isolation order the EDR could not deliver — each answer lighting the stage that failed](../figures/exercise.svg)

Build, one step per click:

0. Six misses. For each: which pipeline stage failed, what additional evidence is needed, and would retraining help? Hands per case, in the pipeline's words.
1. Case A — sensor and acquisition mismatch: memory or behavioral evidence is needed; the antivirus and sandbox column of the host lineage. Retraining does not help.
2. Case B — payload visibility mismatch at the sensor: metadata or endpoint evidence may help; the network lineage. Retraining does not help.
3. Case C — representation or classifier failure: retraining may be relevant, after checking labels and distribution shift.
4. Case D — investigation failure: every alert was right; the evidence was never connected. Correlation, not a better classifier.
5. Case E — decision failure: an appropriate action existed and was not authorized in time. Fix the authorization design, not the evidence.
6. Case F — response failure: the decision was correct and could not be executed. Containment has to work where the host actually is.

## Talking points

- Hands per case in the pipeline's words, then reveal with Next.
- A and B are sensor failures, C representation or classifier, D investigation, E decision, F response.
- Only some misses are repaired by retraining; name the failed stage before proposing a bigger model.
- A detection is not an outcome: half of the misses happened after a correct detection.

## Speaker notes

Expected emphasis:

- **A:** sensor/acquisition mismatch; memory or behavioral evidence is needed. This is the sandbox and antivirus column of slide 21.
- **B:** payload visibility mismatch; metadata or endpoint evidence may help. This is the network lineage of slide 23.
- **C:** representation or classifier failure; retraining may be relevant after checking labels and distribution shift.
- **D:** investigation failure. Every sensor worked and every alert was right; the evidence was never connected across sources. Correlation and timeline reconstruction are needed, not a better classifier. This is the pattern Lecture 2 shows at scale.
- **E:** decision failure. An appropriate action existed and was not authorized in time. The fix is authorization design, such as pre-approved containment above a confidence threshold, not more evidence.
- **F:** response failure. The decision was correct and could not be executed. Containment paths have to work where the host actually is.

Two points to state while the cases are discussed. First, only some misses can be repaired by retraining the classifier; make students name the failed stage before they propose a larger model, and remember the miss that is not a miss at all, when no malicious activity occurred. Second, a detection is not an outcome: a correct alert that arrives too late, lacks recoverable evidence, or cannot trigger containment is not equivalent to stopping the attack. Cases D to F make that second point concrete.

**A and C together carry the memory nuance.** Once an EDR sees executable private memory or a protection change, that is observable and is not a verdict: PowerShell runs on .NET and the CLR legitimately compiles code into process memory at run time, as do browsers, JVMs and instrumentation. Visibility is not distinguishability, and distinguishability is not a verdict. The defender needs the context the representation has to keep: identity and process ancestry, command and script content, network provenance, the memory region's provenance and backing, control transfers and follow-on behavior. That is why A is a sensor failure and C a representation or classifier one: once the sensor sat on the host the problem moved down the pipeline, it did not disappear.

Several answers may be defensible if students state their assumptions.

## Interaction

Use a rapid show of hands per case, in the pipeline's words: sensor, acquisition, extraction, representation, detection, investigation, decision, or response. Then reveal the answer with Next (or the case's Reveal button).

## Transition

“Every answer was a row on the options slide. Five conclusions.”
