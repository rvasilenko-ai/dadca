# Slide 25 — Host and file lineage: antivirus, sandbox, EDR

**Timing:** 58–64 minutes
**Module:** Detection pipelines: design and evolution

## On-slide content

| Stage | Antivirus (since the late 1980s) | Sandbox (since the late 2000s) | EDR (since c. 2011) |
| --- | --- | --- | --- |
| built for | Prevention on the endpoint: block malware before it runs, known families and, through heuristics and emulation, unknown ones | Detection by execution: run the object in an instrumented virtual machine and judge it by what it does, catching exploit documents, zero-days and novel implants that static analysis misses | Assume breach: detect and investigate what prevention missed |
| sensor | On-access hooks on the host: files at rest, on write and on execute; later process behavior and memory | None of its own: it receives objects from other products' sensors, the mail and web gateways, the endpoint agent, an analyst's submission | The same on-host hooks as antivirus (files, processes, registry, network, memory; ETW and AMSI on Windows), often in the same agent |
| acquisition | The file at scan time, and the events the hooks see, taken as they happen on the host | The submitted file and a recording of its run | The same as antivirus: the same agent collects the same files and events |
| extraction | Parsing, unpacking, emulation | Runtime behavior: API calls, dropped files, connections | Process-tree and session reconstruction; script content through AMSI |
| representation | Bytes, hashes, strings, file features | A behavior report | Event sequences and graphs across hosts |
| detection | Signatures and generic family detections, heuristics and emulation; then reputation and ML | Behavioral rules and ML over the report | Analytics over the forwarded stream across hosts: baselining, prevalence, indicators |
| investigation | A family name | The report, read by an analyst | Timeline, hunting, remote forensics over a central, retained record of the stream |
| decision | Verdict on the object before it runs, automatic | Inline: verdict before delivery, automatic; out of band (TAP mode): an alert after delivery | Alert for triage; automatic only when confident |
| response | Quarantine or delete the file | Block the file and its hash | Isolate the host, kill the process, collect, roll back |
| starved by | Packing, polymorphism, scripts, memory | Inline commands, staged payloads, side-loaded DLLs, memory-only implants, evasion | Legitimate tools, identity abuse, off-host activity, tampering from the kernel (BYOVD) |

> EDR is not a next-gen antivirus. It is a different control, built on the assumption that prevention will fail.
> Each generation judges one unit of evidence: an object before it runs, an object in detonation, activity on the host. When the capability leaves that unit, the product keeps catching what stays inside it and misses what left, so a new layer is added on top.

## Speaker notes

The slide is called host and file, not endpoint, because the sandbox was a network and mail product that sat at the gateway; what the three share is the file-centric evidence they were built around, until EDR moved the unit of evidence to activity on the host. The years in the column headers are when each generation was added to the stack, and nothing was removed: today's endpoint agent is an EDR with the antivirus engine inside it, sold as one product, and the sandbox is a commodity component that both call. Antivirus dates from the late 1980s; the sandbox as a product from CWSandbox and the first FireEye appliances in the late 2000s, and it became the premium purchase around 2011 to 2013 with WildFire, Lastline and FireEye's IPO; EDR's first products, Carbon Black's sensor and Mandiant's MIR before it, date from around 2011 and earlier; the name came in 2013. Antivirus still matters: it is the prevention layer of that agent, and it still stops most commodity malware before anything else sees it. Each later generation was added because a kind of evidence had left the previous one's view, not because the previous one stopped working.

The slide steps through the pipeline from slide 22 one stage at a time, with the three generations side by side for that stage. Next and Previous move between stages, clicking a stage on the strip jumps to it, and the table button shows the whole matrix if a question needs it; the PDF prints the table.

Use two stages to explain why each next generation exists. Antivirus to sandbox: antivirus already reached for unknown files and unknown families with heuristics, generic detections and emulation, but as a preventive control it had to do so at a false-positive rate a blocking product can afford, and the extraction and detection rows still failed on packed, polymorphic and novel files, so the industry added a generation that runs the file instead of parsing it. The sandbox added no sensor of its own; it borrowed the gateway's and the endpoint's and asked them for the file. Sandbox to EDR: because the sandbox depends on another product handing it a self-contained object, once the capability was an inline command, a staged payload or a memory-only implant nothing arrived to detonate, and nothing further down a pipeline can repair an empty first row. The answer was the host, where antivirus's hooks already were: EDR took the same sensor and the same collection and changed what happens to the data. Instead of being judged on the host and discarded, it is forwarded, retained and correlated centrally, so detection, investigation, decision and response were rebuilt around a record of activity rather than a verdict on an object. The difference between the two columns starts below the acquisition row, and the decision row carries the preventive-versus-detective difference: antivirus and the sandbox render a verdict on an object before it runs, EDR records activity and alerts after the fact.

Around 2016, the network and mail sandbox was the premium control. It solved the real problem of its time: judging an object by what it does rather than by what it looks like, so that exploit documents, zero-days and novel implants arriving by mail and web were caught regardless of packing, polymorphism or signature coverage. Detonate it, record the behavior, and decide.

The sandbox needs a self-contained, detonatable artifact. Walk through what starves it, using the recurring scenario where possible:

- **Inline commands.** The PowerShell one-liner is text in a process command line. There is no file to submit.
- **Staged payloads.** A stager fetches its second stage only from the real victim. The command-and-control server is geo-fenced, rate-limited, or offline when the sandbox asks. The sandbox records a harmless download attempt.
- **DLL side-loading.** The malicious DLL only runs when the legitimate signed host executable loads it from a specific directory layout, sometimes with a specific argument or environment. Submit the DLL alone and nothing happens.
- **Memory-only implants.** The implant never exists as a file on any system. The only artifact the sandbox could receive is the loader, and the loader is often legitimate.
- **Evasion.** Sleeps, environment checks, user-interaction gating, and hardware fingerprinting detect the analysis VM itself. The VM was a generic image, rarely anything like the victim's machine, which is also why environment-keyed payloads did nothing in it.

**EDR came from a different premise.** By the early 2010s, after Aurora, years of antivirus misses and breach reports measuring dwell time in months (Mandiant's median was 416 days for 2011 and 243 for 2012), defenders accepted that a determined adversary would get past prevention. The response was "assume breach": if prevention will fail, the control that matters is the one that lets you detect and investigate the compromise afterward. The term endpoint detection and response was coined in 2013 for tools built on that premise. Antivirus and the sandbox are preventive controls that render a verdict on an object before it runs. EDR is a detective and investigative control over activity: it records process ancestry, command lines, script content, memory regions, module loads, network connections and the identity behind them, whether or not anything was blocked, so that an analyst can reconstruct what happened, hunt for what was missed, and contain it remotely. Dwell time, which antivirus never measured, is the metric EDR was built against.

This is also why EDR survived the attacker's departure from files: it never depended on a file. The production host became the place where real execution is observed, and containment and rollback were added behind pre-execution judgment. Students who think of EDR as "next-generation antivirus" miss that the two answer different questions: "should this object run?" versus "what has already happened on this host?"

Be precise on the slide. The sandbox did not become useless. It became a commodity capability with a narrower role: commodity droppers and malicious documents at machine scale, and detonation as one tool among several at investigation scale. Lecture 3 returns to it as a tool an analyst agent calls.

EDR has its own starvation column. It sees the host. It does not see the attacker's session in a SaaS console, a cloud API call made with a stolen token, or a legitimate remote-management tool doing exactly what it was designed to do. That is where identity telemetry, and the control and objective questions from slide 21, take over.

On the detection stage, say what the EDR's memory telemetry actually gives, using the recurring scenario. PowerShell runs on .NET, and the CLR legitimately JIT-compiles intermediate language into native code in process memory; browsers, JVMs, emulators and instrumentation do the same. So executable private memory, or a protection change, is observable and is not a verdict: visibility is not distinguishability, and distinguishability is not a verdict. The defender needs context the representation has to keep, identity and process ancestry, command and script content, network provenance, the memory region's provenance and backing, control transfers and thread context, follow-on behavior. Once the sensor sat on the host, the problem did not disappear; it moved from sensor and acquisition to representation and detection, which is why Case A in the exercise is a sensor failure and Case C a classifier one.

As a rhetorical question, not an exercise: which column of the recurring scenario would each product have captured, the command line, the shellcode, the document access, or the upload? The EDR captures the most and still cannot say "malicious" from any single event.

## Transition

“The network sensor went through the same decade. There the evidence was taken away not by the attacker but by encryption.”

## Sources

- [MITRE ATT&CK: Virtualization/Sandbox Evasion (T1497)](https://attack.mitre.org/techniques/T1497/)
- [MITRE ATT&CK: Hijack Execution Flow: DLL (T1574.001; side-loading was merged into it in April 2025)](https://attack.mitre.org/techniques/T1574/001/)
- [MITRE ATT&CK: Reflective Code Loading (T1620)](https://attack.mitre.org/techniques/T1620/)
- [Microsoft: PowerShell security features](https://learn.microsoft.com/en-us/powershell/scripting/security/security-features)
- [Microsoft: .NET managed execution process](https://learn.microsoft.com/en-us/dotnet/standard/managed-execution-process)
- [Mandiant M-Trends 2021, global median dwell time 2011–2020](https://services.google.com/fh/files/misc/rpt-mtrends-2021-en.pdf)
- [Gartner, Anton Chuvakin: Named: Endpoint Threat Detection & Response (July 2013)](https://blogs.gartner.com/anton-chuvakin/2013/07/26/named-endpoint-threat-detection-response/)
