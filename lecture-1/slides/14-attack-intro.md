# Slide 14 — MITRE ATT&CK: what it is

**Timing:** 31–33 minutes
**Module:** ATT&CK as a language for behavior

## On-slide content

> A public, curated knowledge base of adversary behavior, built from observed intrusions, maintained by MITRE since 2015 and updated every April and October.

| What is in it | What it is for | What it is not |
| --- | --- | --- |
| Three domains: Enterprise, Mobile, ICS. Enterprise v20.0 (October 2026): 15 tactics, 227 techniques, 479 sub-techniques | A shared vocabulary for behavior, independent of tool and family names | A complete list of everything an attacker can do |
| Procedure examples from documented campaigns; groups, software (malware and tools), campaigns | Mapping what a detection pipeline covers, and where the gaps are | An order of attack: tactics are goals, not steps |
| Mitigations, data sources and detections for each technique | Structuring threat intelligence, red and purple teaming, product comparison in ATT&CK Evaluations | Evidence: a technique ID names a behavior, it does not observe one |

> ATT&CK names behaviors. Observing them is the detection pipeline's job.

## Talking points

- A knowledge base of observed adversary behavior, free, versioned every April and October.
- Walk the three columns once: what is in it, what it is for, what it is not.
- A technique ID names a behavior; it is not evidence that the behavior happened.

## Speaker notes

Two minutes. ATT&CK began as an internal MITRE research effort in 2013 and was published in May 2015. It is free to use, maintained by MITRE's ATT&CK team, and versioned every April and October, which is why the matrix on the next slide names its version: the current one, v20.0, was released in October 2026.

Walk the three columns once. What is in it: three domains, Enterprise being the one this lecture uses, and for every technique the procedure examples from real campaigns, the groups and software seen using it, the mitigations, and the data sources and detections a defender would need. What it is for: a vocabulary that survives attackers swapping one tool for another that does the same thing; coverage mapping, where a team lays its detections over the matrix and sees the gaps; structuring intelligence; red and purple teaming; and the ATT&CK Evaluations, in which vendors' products are run against an emulated adversary and the results published per technique.

Then what it is not, because students over-read it. It is a knowledge base of observed adversary behavior, not a universal ontology of every capability software might possess; the tactics are goals, not a required sequence; and a sequence of ATT&CK identifiers is not automatically a complete incident narrative. Above all a technique ID names a behavior, it is not evidence that the behavior happened. That last point is the bridge to Part 2.

## Transition

“Here is what the matrix looks like, and how to read it.”

## Sources

- [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/)
- [MITRE ATT&CK: versions of ATT&CK](https://attack.mitre.org/resources/versions/)
- [Strom et al., MITRE ATT&CK: Design and Philosophy (March 2020)](https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf)
- [MITRE ATT&CK Evaluations](https://evals.mitre.org/)
