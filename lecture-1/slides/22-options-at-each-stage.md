# Slide 22 — Options at each stage

**Timing:** 50–54 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

| Stage | Option | What it captures | What it misses |
| --- | --- | --- | --- |
| sensor | File system and on-write hooks | Files written, opened, executed | Inline commands, memory-only code, identity actions |
| sensor | Process and script telemetry (ETW, Sysmon, AMSI, script block logging) | Process trees, command lines, script content | Activity inside legitimate signed tools; anything off the host |
| sensor | Memory scanning | Injected or reflectively loaded code, hooks | Short-lived regions; legitimate JIT noise |
| sensor | Network tap, proxy, NDR | Flows, DNS, TLS metadata; payload only with decryption | Encrypted content; east-west blind spots |
| sensor | Identity provider and SaaS audit logs | Sign-ins, tokens, consent, data access | The host and the payload |
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
| extraction | Disassembly and decompilation | Functions, control flow | Errors that become model input |
| extraction | TLS decryption at a proxy | Payload content | Pinned and east-west traffic; legal and performance cost |
| extraction | Process-tree and session reconstruction | Who started what, under which identity | Gaps where telemetry was missing |
| representation | Hashes and byte patterns | Exact identity | Any variation |
| representation | Engineered features (headers, imports, strings, entropy) | Fast, interpretable | Order, arguments, causality |
| representation | Sequences (API calls, events, bytes) | Order | Long-range context; cost |
| representation | Graphs (process trees, call graphs, identity graphs) | Relationships | Cost of inference at scale |
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
| investigation | Sandbox detonation of a captured artifact | The artifact's behavior | Staged and environment-aware payloads |
| investigation | Memory and disk forensics | What actually ran | Time and skill |
| investigation | Reverse engineering | The capability in full | Cost; only for selected samples |
| investigation | LLM-assisted analysis | Summaries, hypotheses, tool orchestration | Verification; scale |
| decision | Automatic block above a confidence threshold | Speed | False positives on production systems |
| decision | Human approval playbooks | Accountability | Delay; availability of approvers |
| decision | Risk-based policy by asset criticality | Proportional response | Policy maintenance |
| decision | Pre-authorized containment for defined scenarios | Speed with accountability | Scenario coverage |
| decision | Escalation and deferral | Expert judgment | Time |
| response | Isolate the host, kill the process, quarantine the file | Stops host activity | Hosts offline or unreachable |
| response | Revoke tokens and sessions, reset credentials, disable accounts | Stops identity-led activity | Re-issued tokens; service accounts |
| response | Block destinations and domains | Cuts the channel | Infrastructure rotation |
| response | Restore from backup, roll back changes | Recovery | Time; data since the last backup |
| response | Patch and reconfigure | Closes the entry | Change windows |
| response | Revoke an agent's tools or authority | Stops a hijacked agent | Depends on harness support |

> Every stage has options. The history that follows is mostly the sensor and extraction rows changing.

## Speaker notes

Next and Previous step through the eight stages (clicking a stage works too); do not read every card. Spend the time on two of them. The sensor row is the one the next four slides are about: the next slide maps every change from Part 1 onto the stage it broke, and each product class in the host-and-file and network lineages is one or two lines here, and the history is the industry adding lines as the capability moved. The response row is the one students rarely think about: isolating a host does nothing against a stolen token, and revoking a token does nothing against a hijacked agent unless the harness lets you take its tools away.

For the other stages, name the trade-off in one sentence each. Acquisition trades cost against retention; extraction turns raw evidence into something analyzable and introduces its own failures; representation decides what a model can learn; detection is the only place this lecture names the detector families, each with its blind spot, and Lecture 3 covers them in depth; investigation is where expensive methods live; decision is where authority is designed.

If someone asks whether signatures or machine learning are file-only methods, the answer is no, and the detection panel is where to say it. The signature engine that matches byte patterns in files is the same engine that matches YARA rules over process memory in an EDR and content rules over packets in an IDS, and AMSI exists so that it can see script content before the interpreter runs it. Boosted trees over engineered features run over process trees, command lines, memory-region properties and flow and TLS metadata as readily as over PE headers; byte and sequence models have been applied to memory dumps and network payloads; function similarity finds code reuse in a dumped implant as readily as in a dropped file. Each family is tied to what the sensor hands it, not to the file. What is file-centric is the public evidence base: EMBER, SOREL-20M and most of the literature use files because files are what could be collected, labeled and shared at scale. Lecture 3 makes that gap explicit.

This slide sits directly after the pipeline definition on purpose: slide 21 gives the questions, this one gives the menu of answers at each stage, and the lineage slides that follow show the menu being rebuilt twice, once on the endpoint and once on the network, as the capability moved. The exercise comes back to it: a miss is a stage whose chosen option could not see the evidence. Use the panel to answer "why not just do X" questions: almost every X is a row here, with its blind spot in the last column.

## Transition

“Part 1 listed what changed. Here is the stage of this pipeline that each change broke.”
