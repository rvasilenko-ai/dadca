# Slide 18 — Map an attack with no malware file

**Timing:** 40–45 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content

> Using a stolen administrator account, an attacker remotely launches PowerShell with an inline command. The command retrieves encoded, position-independent shellcode, decodes it in memory, and transfers control to it. The payload enumerates documents, compresses selected content in memory, and uploads it over HTTPS.

Below the scenario, the ATT&CK matrix, empty. Map in pairs: artifacts, tools, techniques and procedures, objective, relevant sensors. Then the mapping lights up one step at a time:

1. Valid Accounts (T1078)
2. Remote Services (T1021); the sub-technique depends on the remote mechanism
3. PowerShell (T1059.001) with Command Obfuscation (T1027.010)
4. Reflective Code Loading (T1620)
5. File and Directory Discovery (T1083), Data from Local System (T1005), Archive Collected Data (T1560)
6. Web Protocols (T1071.001), Exfiltration Over C2 Channel (T1041)

## Speaker notes

This is situation 2 from the opening vote written out in full, and it is the standard tradecraft of the 2017–2022 period on slide 12. No malicious executable is written to disk, and the in-memory payload is not organized as a PE or ELF file. Do not say that no evidence or representation exists: the command is text, the payload is encoded bytes, HTTPS and compression have formats, and multiple system events may be produced.

The six steps on the slide are one defensible mapping, not the only one: the remote launch is Remote Services with a sub-technique that depends on the mechanism (WinRM, SMB, RDP), the retrieval of the shellcode could also be tagged Ingress Tool Transfer, and an upload to a cloud service rather than to the C2 server would be Exfiltration to Cloud Storage instead of Exfiltration Over C2 Channel. Reward pairs who argue about the mechanism; that is the exercise working.

**Close the vote, spoken, nothing on the slide.** After the sixth step, name the five situations from slide 3 from memory. By the working definition from slide 5 all five are malware, because each is a malicious capability in use. What the room disagreed about were four different questions asked with one word: a malware analyst classifies an object, the artifact, what it is; an incident responder cares about the capability, what it can do; a platform engineer cares about control, who holds it and who authorized it; a legal definition needs the objective, whose purpose it serves. The five situations differ in the carrier and the evidence, a file on disk, a command line, bytes in memory, a session under the wrong control, an instruction in data, and the four questions are the vocabulary Part 1 has been using without naming it: the artifact carried the malicious meaning in the executable era, objective was added when the adversary became a campaign, control when access, tokens and vendor channels became the target, and control and objective together once a program acts under delegated authority. Part 2 asks the fifth question, what a sensor can see of any of this, which is the question the vote was really about.

## Interaction

Give pairs two minutes with the empty matrix, then reveal the six steps with Next and let the room compare. During the debrief, separate “PowerShell” as software from “an inline command retrieved and executed content” as a procedure.

## Transition

“That is Part 1: how malware and malicious capabilities evolved. Part 2 asks how the pipelines that detect them were built, and how they had to change.”

