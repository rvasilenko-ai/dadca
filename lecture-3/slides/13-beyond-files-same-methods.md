# Slide 13 — Beyond files: the same methods on other evidence

**Timing:** 45–55 minutes (provisional)  
**Module:** Beyond files: behavioral and telemetry representations

## On-slide content

```text
exact bytes -> expert features -> similarity sketches -> raw-byte embeddings -> instructions and functions -> semantic summaries
```

| Approach | Benchmarked on | Also runs on, when a sensor supplies it | Common blind spot |
| --- | --- | --- | --- |
| Hash/signature | File bytes and strings | Memory regions (YARA in EDR), packets (IDS content rules), scripts (AMSI), command lines | Novel variation |
| Engineered-feature ML | Parsed PE features | Process trees and event sequences, memory-region features, flow and TLS metadata, URLs and mail | Feature and dataset shift |
| Similarity search | Sketches of file features | Function-level code reuse in dumped implants, campaign infrastructure, document templates | No verdict by itself |
| Raw-byte or sequence model | A bounded byte sequence from a file | Memory dumps, network payloads, scripts, log sequences | Structure left implicit |
| Code representation | Disassembly or decompilation of a file | Memory-resident code once dumped; scripts and bytecode | Extraction errors |
| LLM investigation | Text and tool output about a file | Anything rendered as text: memory, traffic, logs, agent trajectories | Scale and verification |

> No method family is tied to the file. Each is tied to what the sensor hands it. The benchmarks are file-centric; the methods are not.

## Speaker notes

Start with the oldest row. A signature, whether a cryptographic hash, a byte pattern with wildcards, a string and structure condition, or a behavioral rule, encodes an expert-selected invariant. It is cheap, interpretable and precise while the invariant holds, and it fails when the invariant changes, is easy to manipulate, or describes a family rather than the capability. In the product lineage the signature is the antivirus era's unit of knowledge; the sandbox and EDR added behavioral rules rather than discarding byte rules. Every later row widens the invariant into something learned.

Slides 3 to 12 covered each row on files. The purpose here is the single observation in the callout, and it has to be stated carefully. The method families are defined by the representation they consume and the cost at which they consume it, not by the kind of object. A signature engine that matches byte patterns in files is the same engine that matches YARA rules over process memory in an EDR or content rules over packets in an IDS, and AMSI exists so that the antivirus engine can see script content before an interpreter runs it. Gradient-boosted models over engineered features run just as well over process-tree and command-line features, memory-region properties, or flow and TLS metadata as over PE headers. Byte-level neural models have been applied to memory dumps and network payloads. Function similarity finds code reuse in a dumped implant as readily as in a dropped file.

What is file-centric is the public evidence base. EMBER, SOREL-20M and most of the literature use files because files are what could be collected, labeled and shared at scale. Memory images, telemetry and network captures from real intrusions are rarely public, so the methods are better documented on files than on the inputs that matter for the last two periods of Lecture 1. The public exceptions are few and small next to the file corpora, which is why this lecture spends most of its time on files and why leaderboard results do not transfer.

The consequence is Lecture 1's pipeline argument again. Whether a detector can run on memory, identity events or an agent's context is decided by whether a sensor collects that input and a representation preserves the signal, not by the detector family. When the attack moved, the method families followed wherever a sensor existed and starved wherever none did.

Do not present the ladder as a replacement sequence. Production systems combine several rows because they answer different questions under different budgets. Higher abstraction exposes semantics and hides low-level evidence; lower-level input preserves bytes and forces the model to infer structure.

## Transition

“Whatever the detector is, it cannot run the same expensive reasoning on everything. Scale decides where each method belongs.”
