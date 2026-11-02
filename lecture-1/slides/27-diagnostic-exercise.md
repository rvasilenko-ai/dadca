# Slide 27 — Diagnostic exercise

**Timing:** 70–76 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

### Case A

A memory-resident payload is missed by an on-write file scanner.

### Case B

An HTTPS transfer is missed by a plaintext content signature.

### Case C

A retained PE file is parsed successfully but receives a benign score.

### Case D

Three low-severity alerts fire on three systems over two days: an unusual sign-in, a PowerShell process, a proxy connection. Each is closed as noise.

### Case E

The alert is correct and investigated, but isolating the server requires an approval that is unreachable overnight. The upload completes.

### Case F

Isolation is ordered, but the laptop is off the VPN and the EDR cannot reach it for six hours.

For each:

- Which pipeline stage failed?
- What additional evidence is needed?
- Would retraining help?

## Speaker notes

Expected emphasis:

- **A:** sensor/acquisition mismatch; memory or behavioral evidence is needed. This is the sandbox and antivirus column of slide 24.
- **B:** payload visibility mismatch; metadata or endpoint evidence may help. This is the network lineage of slide 26.
- **C:** representation or classifier failure; retraining may be relevant after checking labels and distribution shift.
- **D:** investigation failure. Every sensor worked and every alert was right; the evidence was never connected across sources. Correlation and timeline reconstruction are needed, not a better classifier. This is the pattern Lecture 2 shows at scale.
- **E:** decision failure. An appropriate action existed and was not authorized in time. The fix is authorization design, such as pre-approved containment above a confidence threshold, not more evidence.
- **F:** response failure. The decision was correct and could not be executed. Containment paths have to work where the host actually is.

Two points to state while the cases are discussed. First, only some misses can be repaired by retraining the classifier; make students name the failed stage before they propose a larger model, and remember the miss that is not a miss at all, when no malicious activity occurred. Second, a detection is not an outcome: a correct alert that arrives too late, lacks recoverable evidence, or cannot trigger containment is not equivalent to stopping the attack. Cases D to F make that second point concrete.

Several answers may be defensible if students state their assumptions.

## Interaction

Use a rapid show of hands per case, in the pipeline's words: sensor, acquisition, extraction, representation, detection, investigation, decision, or response. Then reveal the answer with Next (or the case's Reveal button).

## Transition

“Every answer was a row on the options slide. Five conclusions, and the vote we never resolved.”
