# Slide 15 — From names to behaviors: ATT&CK's levels

**Timing:** 33–37 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content
Tactic: why the adversary acts. Technique: what behavior achieves it. Sub-technique: a specific form. Procedure: how a given actor or tool did it.

![The whole Enterprise ATT&CK matrix, schematic: 15 tactic columns with a few technique IDs each and the true per-tactic counts, Execution expanded to the sub-technique level; then the levels lit one at a time — a tactic column, a technique, its sub-techniques, and a note on where procedures live](../figures/attack-levels.svg)

Build, one step per click:

0. The whole Enterprise matrix, schematic: 15 tactics as columns in attack order, a few real techniques per column with the true per-tactic counts (Defense Evasion became Stealth and Defense Impairment in April 2026). Hover a cell for its name.
1. Tactic — why the adversary acts: a column. Execution is the goal of getting code to run.
2. Technique — what behavior achieves it: a cell. Command and Scripting Interpreter (T1059).
3. Sub-technique — a specific form of it: the indented cells. PowerShell, Windows Command Shell, Visual Basic, JavaScript.
4. Procedure — how a given actor or tool did it. Procedures live on the technique pages with the reports they come from, not on the matrix.

---

> ==An employee receives an invoice by email and opens the attachment. The packed executable inside runs, unpacks itself in memory and injects into a browser process, then adds a Run key so it survives a reboot.== ~~It beacons to its command server over HTTP and, on command, encrypts the documents it finds.~~

![The Enterprise ATT&CK matrix, first half, Reconnaissance to Defense Impairment, with technique names; a classic trojan of the first two periods lit as a path, steps one to five, then a zoomed view of only the lit columns and cells](../figures/attack-matrix-1.svg)

Build, one step per click:

0. A classic trojan of the first two periods, as a path across the matrix — Reconnaissance to Defense Impairment first.
1. Step 1 — Initial Access: Spearphishing Attachment (T1566.001). The invoice in the mail.
2. Step 2 — Execution: User Execution, Malicious File (T1204.002). The employee opens it.
3. Step 3 — Stealth: Software Packing (T1027.002). The executable unpacks itself in memory.
4. Step 4 — Stealth: Process Injection (T1055). Into a browser process.
5. Step 5 — Persistence: Registry Run Keys (T1547.001). It survives a reboot.
6. Zoomed in: only the columns and techniques of steps 1 to 5.

---

> ~~An employee receives an invoice by email and opens the attachment. The packed executable inside runs, unpacks itself in memory and injects into a browser process, then adds a Run key so it survives a reboot.~~ ==It beacons to its command server over HTTP and, on command, encrypts the documents it finds.==

![The Enterprise ATT&CK matrix, second half, Credential Access to Impact; the trojan path continues with steps six and seven, then a zoomed view of only the lit columns and cells](../figures/attack-matrix-2.svg)

Build, one step per click:

0. The second half: Credential Access to Impact. The trojan's path continues here.
1. Step 6 — Command and Control: Web Protocols (T1071.001). The beacon over HTTP.
2. Step 7 — Impact: Data Encrypted for Impact (T1486). The documents, encrypted.
3. Zoomed in: the columns and techniques of steps 6 and 7.

> “Trojan” says less than this path: seven techniques across seven tactics, no family name, and every lit cell is a place a sensor could look.

## Talking points

- Columns are tactics (goals), cells are techniques (behaviors); the expanded column shows sub-techniques; procedures live on the technique pages.
- The matrix moves: fifteen tactics since April 2026.
- Next, two pages: a classic trojan as a path, seven techniques across seven tactics, the scenario above the matrix with the half being mapped in weight; each half ends zoomed in on the lit cells.
- The path, not a family name, is what detections are written against; every lit cell is a sensor question for Part 2.

## Speaker notes

Start with the matrix itself, because most students have seen the word and not the thing. Columns are tactics, the adversary's goals, in the order a campaign tends to need them; cells are techniques, the behaviors that achieve a goal; the expanded Execution column shows the third level, sub-techniques, under Command and Scripting Interpreter; procedures are the documented ways a named group or tool did it and live on the technique pages, not on the matrix. The count under each header is the real number of techniques in that tactic in the version named at the bottom, v20.0, released 13 October 2026; say that the matrix moves, fifteen tactics since April 2026 when Defense Evasion split into Stealth and Defense Impairment, and that the new Defense Impairment column already has a sub-technique for impairing autonomous defenses; the slide shows a few per column and says how many more there are. Hover any cell for its ID.

Then the next page: a classic trojan of the first two periods, with its two-sentence scenario above the matrix, the sentence being mapped in weight and the rest faded. It lights up as a path, numbered in attack order, across the two halves of the matrix: a phished attachment the user opens, a packed binary that injects into another process, a Run key for persistence, then, on the second page, HTTP command and control and encryption for impact. Seven techniques across seven tactics. Each half ends with one more click that zooms in on only the lit columns and cells, for the back of the room. Say that the same behavior can serve more than one goal — injection also escalates privilege — which is the matrix's point. Say that this path, not the word trojan or a family name, is what a defender can write detections against, and that every lit cell is a sensor question for Part 2. The recurring PowerShell scenario is deliberately not shown here: it is the exercise two slides on, and students should meet the empty matrix with only this example behind them.

Then the quote. Family names and broad categories remain useful for attribution, intelligence, and communication. They do not directly identify which telemetry, detection logic, or mitigation a defender needs, and behavioral descriptions survive when attackers swap one tool for another that implements the same capability. ATT&CK gives that description a shared structure.

Keep tactics and techniques distinct from tools. The same technique may be realized through malware, an operating-system utility, or a cloud API.

## Transition

“A tool is an implementation vehicle, not the behavior. Two cases where the software is not just legitimate but byte-for-byte unchanged.”

## Sources

- [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/)
- [MITRE ATT&CK Enterprise techniques](https://attack.mitre.org/techniques/enterprise/)

