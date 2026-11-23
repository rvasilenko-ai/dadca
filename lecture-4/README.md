# Lecture 4: Polymorphic Engines and How to Detect Them

**Status:** planned. Outline only; no slides written yet. The anchor events and dates below are candidates and must be checked against primary sources before any slide is written.  
**Duration:** 90 minutes  
**Audience:** Master's and PhD cybersecurity students  
**Central question:** When the same malicious program never looks the same twice, what stays constant, and which detection method can see it?

## Why this lecture exists

Lecture 1 names polymorphism and server-side polymorphism as the first break in the file-centric model and moves on; Lecture 3 treats detectors as consumers of representations. This lecture takes the engines themselves. It follows how polymorphic malware evolved, in binaries and in scripts, and how detection evolved against it: from decryptor signatures and generic decryption by emulation, through normalization, unpacking and similarity, to learned representations and behavior. The point to make on every slide is the same: each generation of polymorphism attacked a specific invariant the detector relied on, and each answer found a new invariant the engine could not afford to vary.

Standalone takeaway:

> A polymorphic engine varies what is cheap to vary. Detection follows what it cannot afford to change: the decryptor's behavior, the code after unpacking, the semantics after normalization, the actions at run time, the prevalence across victims.

## Learning outcomes

Students should be able to:

1. Distinguish encrypted, oligomorphic, polymorphic and metamorphic code, and say which invariant each one preserves.
2. Trace the evolution of binary polymorphism: the mutation engines of the early 1990s, entry-point obscuring, metamorphic viruses, commercial packers and protectors, and server-side polymorphism.
3. Trace the parallel evolution in scripts: macro and script viruses, obfuscated JavaScript and VBA droppers, PowerShell obfuscation and in-memory loaders, and what the Antimalware Scan Interface changed.
4. Explain the detection lineage against each: wildcard and algorithmic signatures, generic decryption through emulation, heuristics, normalization and unpacking, similarity hashing and clustering, machine learning on static and dynamic features, and script deobfuscation.
5. Evaluate a detection method against an adversary who controls the variation: its coverage, its cost per object, and the evasion it invites.
6. Place model-assisted rewriting of malware and scripts in the same lineage, and say what it changes (cost and scale of variation) and what it does not (the invariants).

## Provisional module schedule

| Time | Module | Slides | Status |
| --- | --- | --- | --- |
| 0–8 | Opening: the same program, never the same bytes | 1–2 | to write |
| 8–30 | **Part 1.** Binary polymorphism: from mutation engines to packers and server-side polymorphism | 3–8 | to write |
| 30–45 | **Part 1.** Script polymorphism: macros, JavaScript, VBA, PowerShell | 9–12 | to write |
| 45–75 | **Part 2.** Detection: what stays constant, and the method that sees it | 13–20 | to write |
| 75–85 | The adversary with a model: rewriting as the newest polymorphic engine | 21–22 | to write |
| 85–90 | Synthesis | 23 | to write |

## Proposed slides

Candidate anchors; every date and attribution is to be verified before the slide exists.

1. Title.
2. Opening: three variants of one sample side by side, different bytes, identical behavior. The question of the lecture.
3. Vocabulary: encrypted, oligomorphic, polymorphic, metamorphic. The decryptor as the weak point of the first three.
4. 1990–1992: the first polymorphic viruses and the Mutation Engine; polymorphism becomes a product other authors can link against.
5. Entry-point obscuring and mid-file infection: the end of "scan the entry point".
6. Metamorphism: code that rewrites itself without a decryptor (the 2001–2002 generation); why it stayed rare, and what it cost the author.
7. Packers and protectors as polymorphism for hire: compression, encryption, virtualization; the unpacking arms race.
8. Server-side polymorphism: a new binary per download (the 2007 botnets); the hash becomes a one-shot signature. Hand-over to Lecture 1's cloud reputation.
9. Script polymorphism I: macro viruses and the script worms of 1995–2001, and why interpreters made variation cheap.
10. Script polymorphism II: obfuscated JavaScript and VBA droppers; exploit-kit landing pages that differ per visitor.
11. Script polymorphism III: PowerShell obfuscation and in-memory loaders; the Antimalware Scan Interface and what it sees that the file scanner cannot.
12. Recap of Part 1: for each generation, what it varied and what it could not afford to vary.
13. Detection I: signatures with wildcards; algorithmic detection of the decryptor.
14. Detection II: generic decryption by emulation inside the scanner; its limits: anti-emulation tricks and the time budget per file.
15. Detection III: normalization and unpacking: generic unpackers, memory dumps at the original entry point, instruction normalization for metamorphic code.
16. Detection IV: similarity: fuzzy hashing, locality-sensitive hashing, import hashing, function-level similarity; clustering variants into families.
17. Detection V: learned representations: engineered features, byte-level models, graphs; what polymorphism does to the training distribution, and what it does not touch.
18. Detection VI: scripts: deobfuscation, syntax-tree normalization, interface-level content, behavioral telemetry of the interpreter.
19. Detection VII: when the object cannot be read: behavior at run time and prevalence across victims.
20. Evaluating against a variation-controlling adversary: coverage against cost per object, and the evasion each method invites.
21. The newest engine: model-assisted rewriting of malware and scripts. What is new: the cost and scale of variation. What is not: the invariants.
22. Defending against model-driven variation: the same lineage, applied.
23. Synthesis: the ladder of invariants, from bytes to behavior.

## Sources to gather

- Szor, *The Art of Computer Virus Research and Defense* (2005), for the engine and scanner history of the 1990s and early 2000s.
- Ferrie and Szor, *Hunting for Metamorphic* (2001).
- The fuzzy-hashing and locality-sensitive-hashing papers (2006 and 2013) and the import-hashing write-up.
- The PowerShell obfuscation research presented at security conferences from 2016, and Microsoft's documentation of the Antimalware Scan Interface.
- Analyses of the 2007 server-side-polymorphic botnets, already cited in Lecture 1's timeline data.
- Recent, well-sourced reports on model-assisted malware rewriting, to be chosen when the slides are written.
- Lecture 1's timeline (`lecture-1/tools/data.py`) for every dated event that both lectures share.

## Related lectures

- [Lecture 1: From Malware Files to Adversarial Capabilities](../lecture-1/README.md) (undergraduate and Master's)
- [Lecture 2: When the Attacker Is an Agent](../lecture-2/README.md) (Master's and PhD)
- [Lecture 3: ML for Detection of Malicious Binary Files](../lecture-3/README.md) (Master's and PhD)
