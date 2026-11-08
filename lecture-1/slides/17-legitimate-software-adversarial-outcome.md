# Slide 17 — Capabilities delivered through benign files

**Timing:** 37–40 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content

> Same tool, different procedures; same technique, different tools. And when the artifact itself is legitimate and unchanged, where does “malicious” reside?

Two case cards, revealed one at a time with Next, built from the same four lines:

| | Remote-management tool abused (T1219 Remote Access Tools, an ATT&CK *tool*, not malware) | Vulnerable signed driver (T1068 Exploitation for Privilege Escalation) |
| --- | --- | --- |
| What it is | Legitimate remote-access software, installed as designed; the same binary and hash as every other install | A legitimate kernel driver with a valid signature and an exploitable flaw; the same binary and hash the vendor shipped |
| What differs from legitimate use | Who operates the session, and whose objective it serves | Who loads it, and that its flaw is used beyond the driver's intended design |
| Where "malicious" sits | Control and objective; the software works exactly as designed | Control and objective, and also capability: what it can be made to do |
| What a file classifier sees | A clean, signed, known program | A clean, signed, known driver |

> As files, both are identical to their legitimate copies. What makes them malicious lives outside the file: who is in control and to what end, and, for the driver, what its flaw lets them do.

## Talking points

- Same tool, different procedures; same technique, different tools.
- Card one: a remote-management tool, which differs from legitimate use only in who controls it and to what end.
- Card two: a signed vulnerable driver, which differs also in what its flaw lets the holder do.
- Neither differs as a file; a file classifier sees two clean, signed programs.

## Speaker notes

Open with the first sentence on the slide, which replaces a slide of its own: ATT&CK lists software, malware and tools alike, apart from the techniques, and connects them through documented procedures. The same tool appears in different procedures (PowerShell retrieving content, a scheduler starting a payload at logon) and the same technique is realized by different tools (an implant, an operating-system utility, a cloud API, a remote-management tool), so defenders usually detect some combination of tool identity, behavior, context and sequence. Then the two sharpest cases.

Next reveals the first card, Next the second, Next the answer. The chips carry the ATT&CK placement: Remote Access Tools sits in Command and Control, Exploitation for Privilege Escalation in Privilege Escalation. These are the two cleanest examples of what the ATT&CK vocabulary is for. The same file, with the same hash and signature, appears in a legitimate procedure and in an adversarial one. ATT&CK describes the behavior (remote access; exploitation of a loaded driver) and keeps the software entry as a tool rather than malware, which is exactly the separation the previous slide argued for.

Both examples come out of the last two periods, and both are responses to defensive success. Once EDR made a custom implant visible, attackers had two options: bring no implant at all and use a legitimate remote-management tool the EDR vendor has allow-listed, or bring a vulnerable signed driver and switch the EDR off from the kernel. Ransomware affiliates adopted remote-management tools as their standard access path in 2017–2022, and Scattered Spider in 2023 ran campaigns almost entirely on them. The BYOVD wave of 2022 is the attacker's acknowledgment of which product won the previous period.

The two cases are complementary:

```text
intended capability + unauthorized controller + adversarial objective
legitimate artifact + exploited capability + adversarial controller
```

Do not say the vulnerable driver automatically becomes malware. It is an attack-enabling component in an adversarial procedure, and a valid signature establishes provenance, not current safety or authorized use. In neither case can a file classifier see the property that matters: who controls it, whose objective it serves, what it can do. The close of Part 1 names these questions (slide 18), and Part 2 asks what a sensor can see of them.

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
