# Slide 8 — Why files became the unit of detection

**Timing:** 9–11 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Because attackers used them (2000 onward; the only way until the mid-2010s) | Because defenders could use them |
| --- | --- |
| Executable attachments, then macro documents | Files cross trust boundaries |
| Drive-by downloads dropping an EXE | Files persist |
| Worms and autorun media carrying their own binary | Files can be hashed and compared |
| Banking trojans and bots installed as programs | Files can be scanned before execution |
| Victim hosts had little built-in tooling to abuse | Samples can be retained, shared, and labeled |

> The file was the attack. The defense followed it.

## Talking points

- Left column: attackers used files because the victim's machine offered little else to abuse.
- Right column: files cross boundaries, persist, hash identically, can be scanned before they run and shared between vendors.
- Ask what a 2005 attacker had to put on the machine to steal documents, and a 2025 attacker; the gap is the lecture.
- Do not preview how the model breaks; the four periods do that.

## Speaker notes

Start with the left column. It is the first two periods on slides 10 and 11: the executable era proper, and then the period in which the file diversified into documents, scripts and exploit objects but remained the deliverable. For roughly fifteen years the attacker's problem was to get their own code onto the victim's machine and run it, because the victim's machine offered little else to work with. PowerShell did not ship by default until Windows 7 in 2009, remote-management tooling was not ubiquitous, and business data lived on the host rather than behind cloud APIs. Email attachments, drive-by downloads, removable media, worms, and bundled installers all delivered a program. The program was the capability, so the program was the right thing to catch.

The right column is why the industry could build on that. Files cross the boundary the defender controls, persist long enough to inspect, hash identically everywhere, and can be scanned before they run. Samples flow between vendors, signature databases grow, sandboxes detonate them, and supervised datasets are built from them. Connect this to antivirus hooks, sample exchanges, and later the public PE datasets covered in Lecture 3.

Stop here. Do not preview how the model breaks; the next four slides show it period by period, and slide 14 draws the list. The only forward-looking sentence this slide needs is that the model held for about fifteen years.

## Interaction

Ask the class what a 2005 attacker had to put on the victim's machine to steal documents, and what a 2025 attacker has to put there. The two answers are slide 10 and slide 13; the gap between them is the rest of the lecture.

## Transition

“That model held for about fifteen years and then broke in stages. First the whole span: four periods across five tracks, motive and money, attackers, the operating system, the internet, and security products.”
