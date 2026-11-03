# Slide 24 — Where each change broke the pipeline

**Timing:** 60–64 minutes
**Module:** Detection pipelines: design and evolution

## On-slide content

| What changed | Stage that broke | Evidence left the... | Defender's sensor moved to... | Product that answered |
| --- | --- | --- | --- | --- |
| Packing and server-side polymorphism | extraction, detection | signature database | emulation, then reputation and prevalence | Antivirus emulation and generic unpacking; cloud reputation and prevalence (Artemis 2008, Insight 2009) |
| File types diversify once mail blocks executables: archives, documents, scripts, exploit objects | sensor, extraction | executable attachment filter | document and script scanning, detonation | Gateways that open documents and scripts; the sandbox (WildFire 2011, FireEye) |
| Memory, staging, side-loading, living off the land | sensor, acquisition | detonatable file, then any malicious artifact | the real host: EDR, memory, baselining | EDR (named 2013), Sysmon (2014), AMSI (2015); memory scanning and baselining |
| HTTPS, TLS 1.3, DoH, ECH (not an attacker move) | extraction | network payload | endpoint, metadata, decryption proxy | TLS inspection proxies; NDR on flow and TLS metadata (JA3 2017); the endpoint for the plaintext |
| Stolen identities, tokens, cloud APIs, remote-management tools | sensor | host | identity provider and SaaS audit logs | Identity provider and SaaS audit logs; identity threat detection and response (named 2022); token revocation |
| Trusted vendor and update channels | representation, detection | provenance as a proxy for safety | build provenance, behavior of trusted software | Build provenance and software bills of materials (2021 onward); behavior monitoring of trusted software |
| Instructions in data consumed by agents | sensor | every classical sensor | the agent's context, tools, and actions | Agent harness logs, guardrails, prompt-injection defenses (2024–2026); ATT&CK's Defense Impairment tactic (2026) |

> Every row is one round of the same cat-and-mouse game: the attacker moves the evidence out of a product's field of view, and the defense has to change at whatever stage broke. There is no final round.

## Speaker notes

This is slide 14's list read from the defender's side, after the two lineages, with two rows added: packing from the executable era, the first time a product's evidence moved out of its view, and the network row, because encryption was the internet changing rather than an attacker move. Each row names the stage of the pipeline that a change broke, the evidence that left that stage's view, where the sensor went, and the product generation that answered; the first four rows are the lineages you have just seen, row by row, and the last three are the pipeline being rebuilt now, around identity and the agent. It is the bridge from the history to the menu on the next slide. The second column maps each row to the pipeline: four of the seven rows broke at the sensor, packing and encryption broke extraction, and only the trusted-vendor row broke at detection, where the feature (provenance) was wrong rather than the model. Next and Previous step through the seven changes one at a time, each lighting the stage that broke; clicking a stage on the strip jumps to the first change that broke there, and the full table button shows all seven at once (the PDF prints the table). The dominant product class changed each time the attacker moved the capability to a place the current sensor did not observe.

Make three points explicit:

1. **The failures were real, and they were all the same failure.** Antivirus missed packed and polymorphic files, the sandbox missed staged and memory-only payloads, the IDS missed everything inside TLS, and EDR misses the stolen token and the remote-management tool: in each case the product did what it was built to do and the evidence was no longer where it looked, and the repair happened at the stage in the second column: a sensor on the host or at the identity provider, emulation and decryption at extraction, provenance and behavior at representation, and a better classifier only where the classifier was the stage that broke. Nothing was retired, because each still catches what stays in its field of view, but the premium control of one decade became the commodity control of the next. Say plainly that this is the normal condition of the field, not a story with an ending: every defensive success on this table changed the attacker's behavior, and the next change will break a stage somewhere in this pipeline again. A security product that cannot be re-pointed at new evidence is a product with a shelf life.
2. **The direction is consistent.** The sensor moved closer to where the capability executes and closer to who authorized it: from the artifact, to the host, to the identity, to the agent's reasoning trajectory.
3. **The next row is already here.** When a coding agent reads a repository file and acts on an instruction in it, no classical sensor has anything to classify. The telemetry that matters is the context the agent assembled, the tools it called, and the identity it acted under. Lecture 2 is built on that row.

For the undergraduate audience, this slide is also a career map: each sensor migration created a new engineering discipline, and the migration is not finished.

## Transition

“Every row ended with a product. Here is the whole menu as it stands today, every line a product of that history.”
