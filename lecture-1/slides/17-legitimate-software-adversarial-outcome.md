# Slide 17 — Capabilities delivered through benign files

**Timing:** 37–40 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content

> Same tool, different procedures; same technique, different tools. And when the artifact itself is legitimate and unchanged, where does “malicious” reside?

| Remote-management tool abused | Vulnerable signed driver (BYOVD) |
| --- | --- |
| Intended remote-access capability | Legitimate, often signed kernel driver |
| Operated by an unauthorized party | Contains an exploitable vulnerability |
| Software works as designed | Used beyond its intended design |
| Same binary and hash as the legitimate install | Same binary, hash, and valid signature |
| ATT&CK: Remote Access Tools (T1219); an ATT&CK *tool*, not malware | ATT&CK: driver load, then Exploitation for Privilege Escalation (T1068) |
| Standard affiliate access path 2017–2022; Scattered Spider's main tool by 2023 | Wave of EDR killers in 2022, after EDR became the control that mattered |

Under the table, the ATT&CK matrix in its compact form with only the two cells lit: Remote Access Tools under Command and Control, Exploitation for Privilege Escalation under Privilege Escalation.

> What differs from legitimate use? The tool: only who controls it and whose objective it serves. The driver: also what it can do. Neither differs as an artifact.

## Speaker notes

Open with the first sentence on the slide, which replaces a slide of its own: ATT&CK lists software, malware and tools alike, apart from the techniques, and connects them through documented procedures. The same tool appears in different procedures (PowerShell retrieving content, a scheduler starting a payload at logon) and the same technique is realized by different tools (an implant, an operating-system utility, a cloud API, a remote-management tool), so defenders usually detect some combination of tool identity, behavior, context and sequence. Then the two sharpest cases.

The compact matrix under the table places the two cases: Remote Access Tools sits in Command and Control, Exploitation for Privilege Escalation in Privilege Escalation. These are the two cleanest examples of what the ATT&CK vocabulary is for. The same file, with the same hash and signature, appears in a legitimate procedure and in an adversarial one. ATT&CK describes the behavior (remote access; exploitation of a loaded driver) and keeps the software entry as a tool rather than malware, which is exactly the separation the previous slide argued for.

Both examples come out of the last two periods, and both are responses to defensive success. Once EDR made a custom implant visible, attackers had two options: bring no implant at all and use a legitimate remote-management tool the EDR vendor has allow-listed, or bring a vulnerable signed driver and switch the EDR off from the kernel. Ransomware affiliates adopted remote-management tools as their standard access path in 2017–2022, and Scattered Spider in 2023 ran campaigns almost entirely on them. The BYOVD wave of 2022 is the attacker's acknowledgment of which product won the previous period.

The two cases are complementary:

```text
intended capability + unauthorized controller + adversarial objective
legitimate artifact + exploited capability + adversarial controller
```

Do not say the vulnerable driver automatically becomes malware. It is an attack-enabling component in an adversarial procedure, and a valid signature establishes provenance, not current safety or authorized use. In neither case can a file classifier see the property that matters: who controls it, whose objective it serves, what it can do. Part 2 opens by naming these questions (slide 20).

## Interaction

Ask whether a file-only classifier can determine who controls the remote-access session, or whether a driver will be exploited after loading. Then ask which question each answer depended on: what it is, what it can do, who controls it, or whose objective it serves.

## Transition

“Now apply this vocabulary to an attack that never produces a malware executable file.”

## Sources

- [MITRE ATT&CK: Remote Access Tools (T1219)](https://attack.mitre.org/techniques/T1219/)
- [CISA: Scattered Spider advisory (AA23-320A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [MITRE ATT&CK: Exploitation for Privilege Escalation (T1068)](https://attack.mitre.org/techniques/T1068/)
- [MITRE ATT&CK: Driver Load data component](https://attack.mitre.org/datacomponents/DC0079/)
- [Microsoft: vulnerable and malicious driver protections](https://www.microsoft.com/en-us/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)
