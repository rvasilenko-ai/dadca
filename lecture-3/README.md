# Lecture 3: Machine Learning for Malware Detection

**Status:** seed. Fourteen slides were moved or copied from Lecture 1 on 2026-10-11; the remaining slides are outlined below and not yet written.  
**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** What does each detector actually receive, and what did the extraction discard before it arrived?

## Why this lecture exists

Lecture 1 argues that malware left the executable file and that the sensor had to follow it. This lecture examines the detectors themselves and makes one tension explicit: most of the academic literature on machine learning for malware, and all of the major public benchmarks, still operate on files. That is a legitimate and productive research area for the artifact-centric fraction of the problem, and it is also why a strong leaderboard result does not translate directly into an operational detection system.

Standalone takeaway:

> A model learns from a representation, not from reality. Compare detectors by what they receive, what the extraction lost, and where in the funnel they can afford to run.

## Learning outcomes

Students should be able to:

1. Explain signatures, engineered features, similarity sketches, raw-byte models, and learned code representations by input, extraction cost, and information loss.
2. Describe how EMBER and SOREL-20M are constructed and what operational facts a prepared dataset hides.
3. Distinguish classification, similarity retrieval, and clustering as different operational questions.
4. Explain why most file-centric detectors receive nothing from fileless, identity-led, or agent-mediated attacks, and what behavioral and telemetry representations exist instead.
5. Describe an LLM reverse-engineering workflow such as Project Ire and its dependence on the extraction ecosystem.
6. Explain why reverse-engineering a selected sample is a different problem from detecting it among millions of objects, and frame selection as a research problem.

## Provisional module schedule

| Time | Module | Slides | Status |
| --- | --- | --- | --- |
| 0–8 | Standalone foundation | 1–2 | to write |
| 8–17 | Signatures and the file-centric literature | 3–5 | moved from Lecture 1 |
| 17–45 | Representations of executable files | 6–12 | moved from Lecture 1 (timings provisional; rebalance when slide 13 is written) |
| 45–55 | Beyond files: behavioral and telemetry representations | 13 | table moved from Lecture 1; notes to extend |
| 55–75 | LLMs as analysts | 14–18 | 14, 15, 18 moved; 16, 17 to write |
| 75–90 | Synthesis | 19–20 | to write |

## Slide index

Slides without a link do not exist yet.

1. Title and central question
2. Standalone foundation: malware is more than a file, the detection pipeline, three scales (reuse the pattern of Lecture 2 slide 2)
3. [Signatures are representations too](slides/03-signatures-are-representations.md)
4. [The invisible dataset preparation](slides/04-invisible-dataset-preparation.md)
5. [A representation ladder](slides/05-representation-ladder.md)
6. [Extraction changes the evidence](slides/06-extraction-changes-evidence.md)
7. [Engineered PE features](slides/07-engineered-pe-features.md)
8. [EMBER and SOREL-20M](slides/08-ember-and-sorel.md)
9. [Similarity is not classification](slides/09-similarity-not-classification.md)
10. [MalConv: learning from raw bytes](slides/10-malconv-raw-bytes.md)
11. [BERT-like code representations](slides/11-bert-code-representations.md)
12. [Compare systems, not leaderboards](slides/12-compare-systems.md)
13. [Beyond files: the same methods on other evidence](slides/13-beyond-files-same-methods.md) (the comparison table cut from Lecture 1 on 2026-10-11; extend with process trees, command lines, scripts, memory regions, flows, authentication and cloud audit events, and why these datasets are rarely public)
14. [Three scales of security analysis](slides/14-three-scales.md)
15. [Capability does not imply suitability](slides/15-capability-not-suitability.md)
16. Project Ire as a worked workflow: selected artifact, structural triage, tool calls, evidence chain, validation, assessment
17. Capability depends on the extraction ecosystem: native and managed-code decompilers, Go and Rust recovery, parsers, sandboxes as analyst tools, provenance, uncertainty
18. [Selecting what deserves investigation](slides/18-selecting-investigations.md)
19. Synthesis: one table comparing every method by input, extraction loss, scale, verification, and the attacks from Lecture 1 it would never receive
20. Conclusions and research prompts

## Notes for implementation

- Slide 3 (signatures) was removed from Lecture 1 on 2026-10-11 and now lives only here; slide 14 (three scales) was Lecture 1's until 2026-10-13 and now lives only here. Slide 6 was moved out of Lecture 1 on 2026-10-11 in the timing pass.
- The timings on the moved slides are provisional and widen the per-slide time compared with Lecture 1, where the same material was too dense for the time available.
- Slide 12's transition points at slide 13; slide 15's points at the unwritten slide 16.
- Primary sources carried over: EMBER, SOREL-20M, MalConv, DeepSemantic. Add Project Ire when slide 16 is written, and at least one behavioral-telemetry dataset or paper to slide 13's notes.

## Related lectures

- [Lecture 1: From Malware Files to Adversarial Capabilities](../lecture-1/README.md) (undergraduate and Master's)
- [Lecture 2: When the Attacker Is an Agent](../lecture-2/README.md) (Master's and PhD)
