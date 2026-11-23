# Lecture 1: From Malware Files to Adversarial Capabilities

**Duration:** 90 minutes (80 minutes of slides, 10 minutes for questions and discussion)  
**Audience:** Undergraduate and Master's cybersecurity students  
**Central question:** How did malware and malicious capabilities evolve, and how did detection pipelines have to evolve with them?

## Learning outcomes

Students should be able to:

1. Separate artifact, capability, control, objective, and observability, and say which one a given control can observe.
2. Describe four periods of the threat landscape since 2000 and, for each, how motive, attacker tradecraft, the operating system, the internet, and security products changed together.
3. Use ATT&CK to describe behavior without relying on a malware-family label.
4. Explain what evidence left the view of antivirus, sandboxes, and network intrusion detection, what sensor was added after each one (nothing was retired; today's endpoint agent contains all of them), and why EDR is a different control rather than a next-gen antivirus.
5. Diagnose failures across sensing, extraction, representation, detection, investigation, and response.
6. State why the detector's intelligence is bounded by the evidence that reaches it, and where the detectors themselves are covered (Lecture 3).

## Module schedule

| Time | Module | Slides |
| --- | --- | --- |
| 0–5 | Where is the malware? (title, the ladder of five situations, route) | 1–3 |
| 5–31 | **Part 1.** From malicious programs to adversarial capabilities (divider, three framing slides, the overview timeline, four zoomed periods, the recap) | 4–13 |
| 31–45 | **Part 1.** ATT&CK as a language for behavior (an introduction, the matrix with a trojan lit as a path, the two benign-file cases, the mapping exercise that closes the vote) | 14–17 |
| 45–75 | **Part 2.** Detection pipelines: design and evolution (divider, pipeline, the host-and-file lineage, the network change and the network lineage, the stage each change broke, options at each stage, exercise) | 18–25 |
| 75–80 | **Part 2.** Synthesis (conclusions) | 26 |
| 80–90 | Questions and discussion | |

Per-slide timings sum to 80 minutes and already include the three exercises and the two one-minute part dividers. The last ten minutes are a deliberate buffer, ten to fifteen minutes for questions plus room to run over, and the only slack; if a module runs long, the period slides (9–12) are the first place to compress: say the five headlines and tell one labelled event instead of three, and the short prompts listed under delivery guidance can be dropped one at a time.

## Recurring scenario

Using a stolen administrator account, an attacker runs PowerShell. A script downloads a legitimate, signed but vulnerable kernel driver, loads it, and uses it to disable the endpoint protection and antivirus from the kernel. It then downloads a memory-only implant and injects it into explorer.exe. The implant enumerates documents, compresses selected content, and uploads it over HTTPS.

The only file written to disk is a legitimate, signed driver; the malicious capability, disabling the defenses and the in-memory implant, never appears as a malware file. Other evidence still exists: authentication records, PowerShell and command-line telemetry, the driver load and the kernel tampering, the implant and exfiltration network flows, memory state, injection, and file access.

The scenario is situation 2 of the opening ladder taken further, standard tradecraft from 2017 with BYOVD (2022) and defense impairment (2026) folded in. The same scenario runs through ATT&CK mapping, the sandbox and EDR comparison, memory visibility, encrypted-traffic analysis, and pipeline diagnosis.

## Two parts, two threads

Part 1 (slides 4–17) traces the evolution of malware and malicious capabilities; Part 2 (slides 18–26) the design and evolution of the detection pipelines built against them. Each part opens with a divider slide. The lecture runs two parallel histories and joins them at slide 23:

- **Offensive thread, Part 1 (slides 5–13):** the capability stops depending on the executable file, without giving it up. An overview timeline (slide 8) shows the whole span first: five lanes, four period bands, a few anchor events. Four zoomed period slides (9–12) then align motive and money, attacker tradecraft, the operating system, the internet, and the security products of the same years: the executable, from worms to botnets (2000–2009); APT, exploit kits and files of every kind (2010–2016); the access economy, identity and the supply chain (2017–2022); and hands-on hacking, edge devices and agents (2023–2026). Slide 13 recaps the periods as the list of breaks in the file-centric model, each partly a consequence of defensive success against the previous one, with its notes naming which property (artifact, objective, control) carried the malicious meaning in each period, in the vocabulary that the close of Part 1 names (slide 17). Slide 16, inside the ATT&CK module, asks where "malicious" resides for the two hardest cases (a remote-management tool and a vulnerable signed driver, both legitimate and unchanged).
- **Defensive thread, Part 2 (slides 19–25):** organised around the detection pipeline, history first. Slide 19 defines the stages and asks the fifth question, what a sensor can see of the thing Part 1's four questions describe; slides 20 and 22 show the pipeline rebuilt generation by generation around the file and the host (antivirus, sandbox, EDR) and on the network (IDS, then encrypted traffic), stage by stage, with what starved each generation and a scenario check at the end of each, and slide 21, between them, is the HTTPS curve and the four protocol steps that caused the network change; slide 23 is slide 13's list read from the defender's side, with the stage each change broke and the product that answered; slide 24 is the menu of options at every stage as it stands today; slide 25 the six misses. Each product class is built around one unit of evidence; when the capability leaves that unit, the product keeps catching what stays inside it and misses what left, so a new layer is added and the sensor moves: to the host, to the identity provider, and now into the agent's context and tool calls.

## Slide index

1. [Title](slides/01-title.md)
2. [Five suspicious situations](slides/02-five-suspicious-situations.md)
3. [Where we are going](slides/03-where-we-are-going.md)
4. [Part 1: how the malicious capability outgrew the file](slides/04-part-1.md)
5. [The original mental model](slides/05-original-mental-model.md)
6. [The classical taxonomy](slides/06-classical-taxonomy.md)
7. [Why files became the unit of detection](slides/07-files-as-unit-of-detection.md)
8. [Four periods, 2000–2026](slides/08-four-periods.md)
9. [2000–2009: the executable, from worms to botnets](slides/09-era-2000-2009-executable-worms-to-botnets.md)
10. [2010–2016: APT, exploit kits, and files of every kind](slides/10-era-2010-2016-apt-and-exploit-kits.md)
11. [2017–2022: the access economy, identity, and the supply chain](slides/11-era-2017-2022-access-economy.md)
12. [2023–2026: hands-on hacking, edge devices, and agents](slides/12-era-2023-2026-hands-on-edge-devices-agents.md)
13. [What broke the file-centric model, and when](slides/13-what-broke-and-when.md)
14. [MITRE ATT&CK: what it is](slides/14-attack-intro.md)
15. [From names to behaviors: ATT&CK's levels](slides/15-attack-levels.md)
16. [Capabilities delivered through benign files](slides/16-legitimate-software-adversarial-outcome.md)
17. [Map an attack with no malware file](slides/17-map-fileless-attack.md)
18. [Part 2: how detection pipelines are built, and how they had to change](slides/18-part-2.md)
19. [The complete detection pipeline](slides/19-complete-detection-pipeline.md)
20. [Host and file lineage: antivirus, sandbox, EDR](slides/20-host-and-file-lineage.md)
21. [The network changed under the sensor: HTTPS, TLS 1.3, DoH, ECH](slides/21-network-change-encryption.md)
22. [Network lineage: what each stage lost](slides/22-network-lineage.md)
23. [Where each change broke the pipeline](slides/23-where-each-change-broke-the-pipeline.md)
24. [Options at each stage](slides/24-options-at-each-stage.md)
25. [Diagnostic exercise](slides/25-diagnostic-exercise.md)
26. [Five conclusions](slides/26-five-conclusions.md)

## Delivery guidance

- Reuse the operational pipeline and recurring scenario instead of introducing disconnected examples.
- Slide 8 is the overview: name the lanes and the four periods, two minutes. On the zoomed period slides (9–12), step through the five tracks, say each headline, then tell two or three of the labelled events as one story and name what the period removed from the previous defense's view. The detail table is the continuation page after each period slide; use it for questions, not for reading.
- The scope is deliberately Windows-centric and enterprise-centric. Mobile, macOS, Linux and cloud-native attacks appear only in passing; it is said once in the slide 8 notes.
- Keep product claims qualified on the slide. Say "commodity and narrow" for sandboxes and "payload inspection without decryption" for IDS; use the stronger spoken form only in the room.
- Use "remote-management tool" consistently for the abused legitimate remote-access software (slides 2, 16, 23).
- The HTTPS figures on slide 21 were verified in October 2026 against Mozilla's ssl_ratios dataset and the Google Transparency Report data. Re-check only if the deck is reused after 2027.
- Treat qualitative throughput and cost comparisons as workload-dependent, not universal rankings.
- Define PE, JIT, EDR, NDR, TLS, and ATT&CK terminology just in time.
- The three exercises are slides 2, 17 and 25; the shorter prompts on slides 6, 7, 13 and 16 can be dropped individually to recover a minute each. The part dividers (5 and 19) are one minute each; do not skip them, they are the only on-screen statement of the structure.
- The title slide is two minutes and carries the one sentence about who is talking; the site's About page has the rest, so there is no about-me slide.
- Keep offensive mechanics conceptual; the teaching objective is observability and system design.
- Defer detector internals to Lecture 3 when a question goes deep. The detection panel on slide 24 names the families, and its notes answer whether they are file-only methods (they are not; the benchmarks are).

## Talk track

[talk-track.md](talk-track.md) is a spoken script for delivering the lecture: one passage per slide with the handovers woven in, matched to the deck's minute ranges. It is a rehearsal and delivery aid, distilled from the per-slide speaker notes; the markdown slides remain the source of truth.

## Slide deck

The presentable deck is an offline HTML build in [deck/](deck/), on the machinery shared with the other lectures (`tools/deck/`): open `deck/index.html` in a browser, press N for the presenter notes with the planned minutes and talking points, S for the slide's sources, T for the dark theme, and print to PDF from the browser. It is generated from the markdown slides by `deck/build.py`, and its figures by `tools/gen_diagrams.py`; edit the markdown, then rebuild. Every figure steps one click at a time with a caption per step: the ladder on slide 2, the overview timeline on slide 8 and the zoomed period timelines on 10–13 (hover any dot for its date), the breaks on 14, the schematic ATT&CK matrix on 16 and 18 (hover a cell for its name; a classic trojan, then the recurring scenario, light as numbered paths), the benign-file cards on 17, the pipeline strip on 20 to 25, the HTTPS chart on 22 and the exercise on 26. See [deck/README.md](deck/README.md).

## Related lectures

- [Lecture 2: When the Attacker Is an Agent](../lecture-2/README.md) (Master's and PhD)
- [Lecture 3: ML for Detection of Malicious Binary Files](../lecture-3/README.md) (Master's and PhD)
- [Lecture 4: Polymorphic Engines and How to Detect Them](../lecture-4/README.md) (Master's and PhD)
