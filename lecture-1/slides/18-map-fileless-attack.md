# Slide 18 — Map an attack with no malware file

**Timing:** 40–45 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content
> ==Using a stolen administrator account, an attacker runs PowerShell. A script downloads a legitimate, signed but vulnerable kernel driver, loads it, and uses it to disable the endpoint protection and antivirus from the kernel.== ~~It then downloads a memory-only implant and injects it into explorer.exe. The implant enumerates documents, compresses selected content, and uploads it over HTTPS.~~

![The Enterprise ATT&CK matrix, first half, Reconnaissance to Defense Impairment, with technique names in the cells; the recurring scenario lit step by step: valid accounts, PowerShell with command obfuscation, exploitation for privilege escalation, disable or modify tools; then a zoomed view of only the lit columns and cells](../figures/attack-fileless-1.svg)

Build, one step per click:

0. The matrix, empty — Reconnaissance to Defense Impairment first. Map in pairs: artifacts, tools, techniques and procedures, objective, relevant sensors. Then the mapping lights up one step at a time.
1. Step 1 — Valid Accounts (T1078): the stolen administrator account.
2. Step 2 — PowerShell (T1059.001) with Command Obfuscation (T1027.010).
3. Step 3 — Exploitation for Privilege Escalation (T1068): a legitimate, signed but vulnerable driver loaded, then exploited (BYOVD).
4. Step 4 — Disable or Modify Tools (T1685): endpoint protection and antivirus disabled from the kernel.
5. Zoomed in: only the columns and techniques the attack touched, steps 1 to 4, large enough to read from anywhere in the room.

---

> ~~Using a stolen administrator account, an attacker runs PowerShell. A script downloads a legitimate, signed but vulnerable kernel driver, loads it, and uses it to disable the endpoint protection and antivirus from the kernel.~~ ==It then downloads a memory-only implant and injects it into explorer.exe. The implant enumerates documents, compresses selected content, and uploads it over HTTPS.==

![The Enterprise ATT&CK matrix, second half, Stealth to Impact, with the scenario continuing: ingress tool transfer, process injection and reflective code loading, discovery and collection, web protocols and exfiltration over the C2 channel; then a zoomed view of only the lit columns and cells](../figures/attack-fileless-2.svg)

Build, one step per click:

0. The second half, Stealth to Impact. The chain continues from the kernel.
1. Step 5 — Ingress Tool Transfer (T1105): the memory-only implant downloaded, visible to a network sensor.
2. Step 6 — Process Injection (T1055) and Reflective Code Loading (T1620): into explorer.exe, in memory. ATT&CK lists injection under Privilege Escalation too; the same behavior serves two goals.
3. Step 7 — File and Directory Discovery (T1083), Data from Local System (T1005), Archive Collected Data (T1560).
4. Step 8 — Web Protocols (T1071.001), Exfiltration Over C2 Channel (T1041): the upload, visible to a network sensor.
5. Zoomed in: the columns and techniques of steps 5 to 8.

## Talking points

- Situation 2 from the ladder, written out and taken further: a PowerShell script, a vulnerable driver, defenses off, a memory-only implant, documents out.
- The only file on disk is a legitimate signed driver; the malicious capability never appears as a malware file (slide 17's BYOVD case inside a full chain).
- Two minutes in pairs with the empty matrix, then reveal the eight steps; reward arguments about the mechanism.
- Three network crossings (driver, implant, upload) and many host events; "no malware file" does not mean no evidence.
- Close the vote in speech: all five are malware; the room answered four different questions; Part 2 asks the fifth.

## Speaker notes

This is situation 2 from the opening ladder written out and taken further: the standard tradecraft of 2017–2022 on slide 12 with the BYOVD and defense-impairment moves of 2022–2026 folded in. The only file written to disk is a legitimate, signed driver; the malicious capability, disabling the defenses and the memory-only implant, never appears as a malware file, which is slide 17's benign-driver case inside a full chain. Do not say that no evidence or representation exists: the command is text, the driver load and the kernel tampering raise system events, two downloads and the upload cross the network, and the in-memory implant leaves memory and injection evidence.

The eight steps on the slide are one defensible mapping, not the only one: the driver abuse could also be tagged under Hijack Execution Flow or a service technique, both downloads are Ingress Tool Transfer (the slide lights it once, at the implant), Process Injection lights in two columns because the same behavior serves two goals, and an upload to a cloud service rather than to the C2 server would be Exfiltration to Cloud Storage instead of Exfiltration Over C2 Channel. Reward pairs who argue about the mechanism; that is the exercise working.

**Close the vote, spoken, nothing on the slide.** After the sixth step, name the five situations from slide 3 from memory. By the working definition from slide 5 all five are malware, because each is a malicious capability in use. What the room disagreed about were four different questions asked with one word: a malware analyst classifies an object, the artifact, what it is; an incident responder cares about the capability, what it can do; a platform engineer cares about control, who holds it and who authorized it; a legal definition needs the objective, whose purpose it serves. The five situations differ in the carrier and the evidence, a file on disk, a command line, bytes in memory, a session under the wrong control, an instruction in data, and the four questions are the vocabulary Part 1 has been using without naming it: the artifact carried the malicious meaning in the executable era, objective was added when the adversary became a campaign, control when access, tokens and vendor channels became the target, and control and objective together once a program acts under delegated authority. Part 2 asks the fifth question, what a sensor can see of any of this, which is the question the vote was really about.

## Interaction

Give pairs two minutes with the empty matrix, then reveal the eight steps with Next and let the room compare. During the debrief, separate “PowerShell” as software from “an inline command retrieved and executed content” as a procedure.

## Transition

“That is Part 1: how malware and malicious capabilities evolved. Part 2 asks how the pipelines that detect them were built, and how they had to change.”

