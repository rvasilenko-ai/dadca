# Slide 25 — Options at each stage

**Timing:** 64–68 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content
![Options at each stage: the pipeline strip with each stage lit in turn and its menu of options; the full menu, with what each option captures and misses, follows as a table](../figures/pipeline-options.svg)

Build, one step per click:

0. Sensor — File system and on-write hooks · Process and script telemetry · Memory scanning · Network tap, proxy, NDR · Identity and SaaS audit logs · Cloud control-plane logs · Mail and web gateways · Agent harness logs.
1. Acquisition — Capture the artifact on write or on execute · Triggered memory capture · Full packet capture · Metadata-only flow records · Log retention windows and sampling · Central forwarding.
2. Extraction — File parsing (PE, Office, PDF, archives) · Unpacking and emulation · Script and macro deobfuscation · Disassembly and decompilation · TLS decryption at a proxy · Process-tree and session reconstruction.
3. Representation — Hashes and byte patterns · Engineered features · Sequences (API calls, events, bytes) · Graphs · Similarity sketches · Text (decompiled code, logs, reports).
4. Detection — Signatures and indicators · Expert rules (YARA, Sigma, Snort) · Supervised classifiers · Anomaly detection and baselining · Similarity and clustering · Reputation and prevalence.
5. Investigation — Triage and enrichment · Timeline reconstruction across sources · Sandbox detonation · Memory and disk forensics · Reverse engineering · LLM-assisted analysis.
6. Decision — Automatic block above a threshold · Human approval playbooks · Risk-based policy by asset criticality · Pre-authorized containment · Escalation and deferral.
7. Response — Isolate, kill, quarantine · Revoke tokens, reset credentials · Block destinations and domains · Restore from backup, roll back changes · Patch and reconfigure · Revoke an agent's tools or authority.

> Every stage has options, and every line here came from that history; the sensor and extraction rows changed most.

| Stage | Option | What it captures | What it misses |
| --- | --- | --- | --- |
| sensor | File system and on-write hooks | Files written, opened, executed | Inline commands, memory-only code, identity actions |
| sensor | Process and script telemetry | Process trees, command lines, script content (ETW, Sysmon, AMSI, script block logging) | Activity inside legitimate signed tools; anything off the host |
| sensor | Memory scanning | Injected or reflectively loaded code, hooks | Short-lived regions; legitimate JIT noise |
| sensor | Network tap, proxy, NDR | Flows, DNS, TLS metadata; payload only with decryption | Encrypted content; east-west blind spots |
| sensor | Identity and SaaS audit logs | Sign-ins, tokens, consent, data access | The host and the payload |
| sensor | Cloud control-plane logs | API calls, role assumptions, configuration changes | Data-plane content |
| sensor | Mail and web gateways | Attachments, URLs, downloads at delivery | Anything after delivery |
| sensor | Agent harness logs | Context assembled, tool calls, actions, identity used | Deployment-dependent; often hidden in SaaS agents |
| acquisition | Capture the artifact on write or on execute | The file as delivered | Memory-only payloads |
| acquisition | Triggered memory capture | The process or region at alert time | Anything before the trigger |
| acquisition | Full packet capture | Everything on the wire | Cost limits retention to hours or days |
| acquisition | Metadata-only flow records | Long, cheap retention | Content |
| acquisition | Log retention windows and sampling | What is kept, for how long | The slow campaign that outlives the window |
| acquisition | Central forwarding | Correlation across hosts | Hosts offline or outside the network |
| extraction | File parsing (PE, Office, PDF, archives) | Structure, imports, embedded objects | Malformed or novel formats |
| extraction | Unpacking and emulation | Code hidden behind packers | Custom protectors; environment-keyed code |
| extraction | Script and macro deobfuscation | The command that actually runs | Payloads built only at runtime |
| extraction | Disassembly and decompilation | Functions, control flow; .NET, Go and Rust each need their own tooling | Errors that become model input; stripped, statically linked binaries |
| extraction | TLS decryption at a proxy | Payload content | Pinned and east-west traffic; legal and performance cost |
| extraction | Process-tree and session reconstruction | Who started what, under which identity | Gaps where telemetry was missing |
| representation | Hashes and byte patterns | Exact identity | Any variation |
| representation | Engineered features | Headers, imports, strings, entropy: fast, interpretable | Order, arguments, causality |
| representation | Sequences (API calls, events, bytes) | Order | Long-range context; cost |
| representation | Graphs | Process trees, call graphs, identity graphs: relationships | Cost of inference at scale |
| representation | Similarity sketches | Neighbors and families | No verdict |
| representation | Text (decompiled code, logs, reports) | Semantics an LLM can read | Fidelity to machine semantics |
| detection | Signatures and indicators | Known threats, cheaply | Novel variation |
| detection | Expert rules (YARA, Sigma, Snort) | Capability patterns across hosts and traffic | Maintenance; evasion by rewording |
| detection | Supervised classifiers | Generalization inside the training distribution | Shift, label noise |
| detection | Anomaly detection and baselining | Deviations without a label | False positives; slow drift |
| detection | Similarity and clustering | Campaign grouping, novelty | No verdict by itself |
| detection | Reputation and prevalence | Rare or new objects | First victims; legitimate rarities |
| investigation | Triage and enrichment | Context from intelligence, asset and identity data | Throughput |
| investigation | Timeline reconstruction across sources | The sequence of events | Retention and correlation keys |
| investigation | Sandbox detonation | A captured artifact's behavior | Staged and environment-aware payloads |
| investigation | Memory and disk forensics | What actually ran | Time and skill |
| investigation | Reverse engineering | The capability in full | Cost; only for selected samples |
| investigation | LLM-assisted analysis | Summaries, hypotheses, tool orchestration | Verification; scale |
| decision | Automatic block above a threshold | Speed | False positives on production systems |
| decision | Human approval playbooks | Accountability | Delay; availability of approvers |
| decision | Risk-based policy by asset criticality | Proportional response | Policy maintenance |
| decision | Pre-authorized containment | Speed with accountability, for defined scenarios | Scenario coverage |
| decision | Escalation and deferral | Expert judgment | Time |
| response | Isolate, kill, quarantine | Stops host activity: isolate the host, kill the process, quarantine the file | Hosts offline or unreachable |
| response | Revoke tokens, reset credentials | Stops identity-led activity: revoke sessions, reset credentials, disable accounts | Re-issued tokens; service accounts |
| response | Block destinations and domains | Cuts the channel | Infrastructure rotation |
| response | Restore from backup, roll back changes | Recovery | Time; data since the last backup |
| response | Patch and reconfigure | Closes the entry | Change windows |
| response | Revoke an agent's tools or authority | Stops a hijacked agent | Depends on harness support |

## Talking points

- Do not read every card; step to two stages, sensor and response, and name one trade-off for each of the others.
- Each product class in the lineages is one or two lines here; the history is the industry adding lines.
- Signatures and machine learning are not file-only methods; the public evidence base is.
- Use the panel to answer "why not just do X": X is a row, with its blind spot in the last column.

## Speaker notes

Next and Previous step through the eight stages (clicking a stage works too); do not read every card. Spend the time on two of them. The sensor row is the one the lineages were about: each product class in the host-and-file and network lineages is one or two lines here, and the history you have just seen is the industry adding lines as the capability moved. The response row is the one students rarely think about: isolating a host does nothing against a stolen token, and revoking a token does nothing against a hijacked agent unless the harness lets you take its tools away.

For the other stages, name the trade-off in one sentence each. Acquisition trades cost against retention; extraction turns raw evidence into something analyzable and introduces its own failures; representation decides what a model can learn; detection is the only place this lecture names the detector families, each with its blind spot, and Lecture 3 covers them in depth; investigation is where expensive methods live; decision is where authority is designed.

If someone asks whether signatures or machine learning are file-only methods, the answer is no, and the detection panel is where to say it. The signature engine that matches byte patterns in files is the same engine that matches YARA rules over process memory in an EDR and content rules over packets in an IDS, and AMSI exists so that it can see script content before the interpreter runs it. Boosted trees over engineered features run over process trees, command lines, memory-region properties and flow and TLS metadata as readily as over PE headers; byte and sequence models have been applied to memory dumps and network payloads; function similarity finds code reuse in a dumped implant as readily as in a dropped file. Each family is tied to what the sensor hands it, not to the file. What is file-centric is the public evidence base: EMBER, SOREL-20M and most of the literature use files because files are what could be collected, labeled and shared at scale. Lecture 3 makes that gap explicit.

This slide sits after the history on purpose: slide 20 gave the questions, the lineages showed the menu being built twice, once on the endpoint and once on the network, and this is the menu as it stands today. The exercise comes next, and every answer is a row here: a miss is a stage whose chosen option could not see the evidence. Use the panel to answer "why not just do X" questions: almost every X is a row here, with its blind spot in the last column.

## Transition

“Six misses to diagnose. Every answer is a row on this slide, and ‘we need better AI’ is not one of them.”
