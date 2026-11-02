# Slide 16 — From names to behaviors: ATT&CK's levels

**Timing:** 34–37 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content

Tactic: why the adversary acts. Technique: what behavior achieves it. Sub-technique: a specific form. Procedure: how a given actor or tool did it.

The Enterprise ATT&CK matrix, schematic: 15 tactics as columns in attack order (Defense Evasion became Stealth and Defense Impairment in April 2026), a few real techniques per column with the true per-tactic counts, and the Execution column expanded under Command and Scripting Interpreter to show the sub-technique level (PowerShell, Windows Command Shell, Visual Basic, JavaScript).

Then a classic trojan of the first two periods lit as a path across it: Spearphishing Attachment (T1566.001), User Execution: Malicious File (T1204.002), Registry Run Keys (T1547.001), Software Packing (T1027.002), Process Injection (T1055), Web Protocols (T1071.001), Data Encrypted for Impact (T1486).

> “Trojan” says less than this path: seven techniques across seven tactics, no family name, and every lit cell is a place a sensor could look.

## Speaker notes

Start with the matrix itself, because most students have seen the word and not the thing. Columns are tactics, the adversary's goals, in the order a campaign tends to need them; cells are techniques, the behaviors that achieve a goal; the expanded Execution column shows the third level, sub-techniques, under Command and Scripting Interpreter; procedures are the documented ways a named group or tool did it and live on the technique pages, not on the matrix. The count under each header is the real number of techniques in that tactic in the version named at the bottom, v20.0, released the day this was checked; say that the matrix moves, fifteen tactics since April 2026 when Defense Evasion split into Stealth and Defense Impairment, and that the new Defense Impairment column already has a sub-technique for impairing autonomous defenses; the slide shows a few per column and says how many more there are. Hover any cell for its ID.

Then press Next: a classic trojan of the first two periods lights up as a path, numbered in attack order: a phished attachment the user opens, a Run key for persistence, a packed binary that injects into another process, HTTP command and control, and encryption for impact. Seven techniques across seven tactics. Process Injection lights in two columns because the same behavior serves more than one goal, which is the matrix's point. Say that this path, not the word trojan or a family name, is what a defender can write detections against, and that every lit cell is a sensor question for Part 2. The recurring PowerShell scenario is deliberately not shown here: it is the exercise two slides on, and students should meet the empty matrix with only this example behind them.

Then the quote. Family names and broad categories remain useful for attribution, intelligence, and communication. They do not directly identify which telemetry, detection logic, or mitigation a defender needs, and behavioral descriptions survive when attackers swap one tool for another that implements the same capability. ATT&CK gives that description a shared structure.

Keep tactics and techniques distinct from tools. The same technique may be realized through malware, an operating-system utility, or a cloud API.

## Transition

“A tool is an implementation vehicle, not the behavior. Two cases where the software is not just legitimate but byte-for-byte unchanged.”

## Sources

- [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/)
- [MITRE ATT&CK Enterprise techniques](https://attack.mitre.org/techniques/enterprise/)

