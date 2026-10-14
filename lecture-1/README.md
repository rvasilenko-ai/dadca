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
| 0–6 | Where is the malware? (title, about me, vote, route) | 1–4 |
| 6–32 | **Part 1.** From malicious programs to adversarial capabilities (divider, three framing slides, the overview timeline, four zoomed periods, the recap) | 5–14 |
| 32–45 | **Part 1.** ATT&CK as a language for behavior (an introduction, then a schematic ATT&CK matrix on 16, 18 and 19) | 15–19 |
| 45–76 | **Part 2.** Detection pipelines: design and evolution (divider, the five questions in one word, pipeline, options at each stage, the stage each change broke, the host-and-file lineage, the network change and the network lineage, exercise) | 20–28 |
| 76–80 | **Part 2.** Synthesis (conclusions) | 29 |
| 80–90 | Questions and discussion | |

Per-slide timings sum to 80 minutes and already include the three exercises and the two one-minute part dividers. The last ten minutes are a deliberate buffer, ten to fifteen minutes for questions plus room to run over, and the only slack; if a module runs long, the period slides (10–13) are the first place to compress: say the five headlines and tell one labelled event instead of three, and the short prompts listed under delivery guidance can be dropped one at a time.

## Recurring scenario

Using a stolen administrator account, an attacker remotely launches PowerShell with an inline command. The command retrieves encoded, position-independent shellcode, decodes it in memory, and transfers control to it. The payload enumerates documents, compresses selected content in memory, and uploads it over HTTPS.

No malicious executable is written to disk, and the in-memory payload is not organized as a PE or ELF file. Other evidence still exists: authentication records, command-line and PowerShell telemetry, network activity, memory state, file access, and follow-on behavior.

The scenario is situation 2 of the opening vote written out in full, and it is the standard tradecraft of the 2017–2022 period. The same scenario is used for ATT&CK mapping, the sandbox and EDR comparison, memory visibility, encrypted-traffic analysis, and pipeline diagnosis.

## Two parts, two threads

Part 1 (slides 5–19) traces the evolution of malware and malicious capabilities; Part 2 (slides 20–29) the design and evolution of the detection pipelines built against them. Each part opens with a divider slide. The lecture runs two parallel histories and joins them at slide 24:

- **Offensive thread, Part 1 (slides 6–14):** the capability leaves the executable file. An overview timeline (slide 9) shows the whole span first: five lanes, four period bands, a few anchor events. Four zoomed period slides (10–13) then align motive and money, attacker tradecraft, the operating system, the internet, and the security products of the same years: the file era (2000–2009); APT, exploit kits and files of every kind (2010–2016); the access economy, identity and the supply chain (2017–2022); and hands-on hacking, edge devices and agents (2023–2026). Slide 14 recaps the periods as the list of breaks in the file-centric model, each partly a consequence of defensive success against the previous one, with its notes naming which property (artifact, objective, control) carried the malicious meaning in each period, in the vocabulary that Part 2 opens by naming (slide 21). Slide 18, inside the ATT&CK module, asks where "malicious" resides for the two hardest cases (a remote-management tool and a vulnerable signed driver, both legitimate and unchanged).
- **Defensive thread, Part 2 (slides 21–27):** opens with the five questions hidden in the word malware (slide 21, moved here from the opening so that the vocabulary arrives where detection is discussed) and is then organised around the detection pipeline. Slide 22 defines the stages, slide 23 lists the options at each stage, slide 24 maps the seven changes from Part 1's recap onto the stage each one broke and where the sensor went, and slides 25 and 27 show the pipeline rebuilt generation by generation around the file and the host (antivirus, sandbox, EDR) and on the network (IDS, then encrypted traffic), stage by stage, with what starved each generation; slide 26, between them, is the HTTPS curve and the four protocol steps that caused the network change. Each product class is built around one unit of evidence; when the capability leaves that unit, the product keeps catching what stays inside it and misses what left, so a new layer is added and the sensor moves: to the host, to the identity provider, and now into the agent's context and tool calls. Slide 24 is slide 14's list read from the defender's side, with the stage that broke in each row.

## Slide index

1. [Title](slides/01-title.md)
2. [About me](slides/02-about-me.md)
3. [Five suspicious situations](slides/03-five-suspicious-situations.md)
4. [Where we are going](slides/04-where-we-are-going.md)
5. [Part 1: how the malicious capability left the file](slides/05-part-1.md)
6. [The original mental model](slides/06-original-mental-model.md)
7. [The classical taxonomy](slides/07-classical-taxonomy.md)
8. [Why files became the unit of detection](slides/08-files-as-unit-of-detection.md)
9. [Four periods, 2000–2026](slides/09-four-periods.md)
10. [2000–2009: the file era](slides/10-era-2000-2009-file-era.md)
11. [2010–2016: APT, exploit kits, and files of every kind](slides/11-era-2010-2016-apt-and-exploit-kits.md)
12. [2017–2022: the access economy, identity, and the supply chain](slides/12-era-2017-2022-access-economy.md)
13. [2023–2026: hands-on hacking, edge devices, and agents](slides/13-era-2023-2026-hands-on-edge-devices-agents.md)
14. [What broke the file-centric model, and when](slides/14-what-broke-and-when.md)
15. [MITRE ATT&CK: what it is](slides/15-attack-intro.md)
16. [From names to behaviors: ATT&CK's levels](slides/16-attack-levels.md)
17. [Software is not behavior](slides/17-software-is-not-behavior.md)
18. [Capabilities delivered through benign files](slides/18-legitimate-software-adversarial-outcome.md)
19. [Map an attack with no malware file](slides/19-map-fileless-attack.md)
20. [Part 2: how detection pipelines are built, and how they had to change](slides/20-part-2.md)
21. [One word, several questions](slides/21-one-word-several-questions.md)
22. [The complete detection pipeline](slides/22-complete-detection-pipeline.md)
23. [Options at each stage](slides/23-options-at-each-stage.md)
24. [Where each change broke the pipeline](slides/24-where-each-change-broke-the-pipeline.md)
25. [Host and file lineage: antivirus, sandbox, EDR](slides/25-host-and-file-lineage.md)
26. [The network changed under the sensor: HTTPS, TLS 1.3, DoH, ECH](slides/26-network-change-encryption.md)
27. [Network lineage: what each stage lost](slides/27-network-lineage.md)
28. [Diagnostic exercise](slides/28-diagnostic-exercise.md)
29. [Five conclusions](slides/29-five-conclusions.md)

## Delivery guidance

- Reuse the operational pipeline and recurring scenario instead of introducing disconnected examples.
- Slide 9 is the overview: name the lanes and the four periods, two minutes. On the zoomed period slides (10–13), say the five headlines, then tell two or three of the labelled events as one story and name what the period removed from the previous defense's view. The detail chips are behind the details button, which swaps the timeline out for them; use them for questions, not for reading. The PDF prints the headline view and the markdown keeps the full table.
- The scope is deliberately Windows-centric and enterprise-centric. Mobile, macOS, Linux and cloud-native attacks appear only in passing; say so once on slide 10 if the audience asks.
- Keep product claims qualified on the slide. Say "commodity and narrow" for sandboxes and "payload inspection without decryption" for IDS; use the stronger spoken form only in the room.
- Use "remote-management tool" consistently for the abused legitimate remote-access software (slides 3, 18, 24).
- The HTTPS figures on slide 26 were verified in October 2026 against Mozilla's ssl_ratios dataset and the Google Transparency Report data. Re-check only if the deck is reused after 2027.
- Treat qualitative throughput and cost comparisons as workload-dependent, not universal rankings.
- Define PE, JIT, EDR, NDR, TLS, and ATT&CK terminology just in time.
- The three exercises are slides 3, 19 and 28; the shorter prompts on slides 7, 8, 14 and 18 can be dropped individually to recover a minute each. The part dividers (5 and 20) are one minute each; do not skip them, they are the only on-screen statement of the structure.
- Slide 2 is one minute. Name the one career line that bears on the lecture (the sandbox years) and move on.
- Keep offensive mechanics conceptual; the teaching objective is observability and system design.
- Defer detector internals to Lecture 3 when a question goes deep. The detection panel on slide 23 names the families, and its notes answer whether they are file-only methods (they are not; the benchmarks are).

## Slide deck

The presentable deck is an offline HTML build in [deck/](deck/): open `deck/index.html` in a browser, press S for speaker notes with the planned minutes and a timer, T for the dark theme, and `?print-pdf` for a PDF. It is generated from the markdown slides by `deck/build.py`; edit the markdown, then rebuild. Interactive parts: the overview timeline on slide 9, the zoomed period timelines on slides 10–13 with a details toggle, the breaks timeline on 14, the live vote tally on slide 3, the clickable pipeline on slides 22 to 28 (Next and Previous step through the panels on slides 23, 24, 25 and 27; clicking jumps), the HTTPS adoption chart on slide 26, and a schematic ATT&CK matrix on slides 16, 18 and 19 (hover a cell for its ID; Next lights the recurring scenario as a path). See [deck/README.md](deck/README.md).

## Related lectures

- [Lecture 2: When the Attacker Is an Agent](../lecture-2/README.md) (Master's and PhD)
- [Lecture 3: Machine Learning for Malware Detection](../lecture-3/README.md) (Master's and PhD)
