# Slide 14 — What broke the file-centric model, and when

**Timing:** 30–32 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| What broke the model | Became dominant | What the defender lost |
| --- | --- | --- |
| Diversification of file types: archives, documents, scripts, exploit objects | 2010–2016, once mail blocked executable attachments; first wave 1995–2001 | The executable as the main thing to scan |
| Process injection, reflective loading, memory-resident execution | End of 2010–2016; standard 2017–2022 | A file to detonate |
| Living-off-the-land tools | 2017–2022; the whole campaign by 2023 | A malicious artifact at all |
| Stolen identities, tokens and cloud APIs | 2017–2022 onward | The host as the place where the attack happens |
| Trusted vendor and update channels | 2017–2022 | Provenance as a proxy for safety |
| Tool-using agents and external instructions | 2025–2026 | A program as the thing that executes intent |

> Each break was partly a consequence of defensive success against the previous one.
> The money and motivation moved too: from the victim's machine, to the victim's credentials, to the victim's organization, to the victim's identity and data.

## Speaker notes

This slide is the recap of the four periods. Each row is something students have just seen, now stated as a break in the model from slide 6, ordered by when it became dominant rather than when it was first seen. Every row has a precedent, and the first row is the clearest case of defense causing the next move. Macro viruses from 1995 and the VBScript worms of 2000–2001 were the first wave of non-executable files; Office macro security levels and Outlook attachment blocking absorbed them. Then Outlook and the mail gateways blocked executable attachments outright, so by the late 2000s an .exe rarely arrived by mail at all. Attackers answered by diversifying the file type: archives wrapping executables, PDF and Office exploit documents, macro documents again from 2014, JavaScript, VBScript and HTA downloaders, shortcut files, and the browser itself through exploit kits. That diversification is what changed what the sandbox had to detonate. Memory-resident code and living off the land likewise have earlier precedents; what matters for the defender is the moment a technique stops being an exception and becomes the default.

Make the causal point explicit now that the evidence is on the table. File-centric defense worked: signatures, reputation, cloud lookups, download warnings and code-signing enforcement made delivering an unknown executable expensive, so attackers diversified the file. Sandboxes made the unknown document and dropped executable expensive, so attackers went to memory and built-in tools. EDR made implants visible, so attackers went to identities, vendors and remote-management tools. Operating-system hardening closed the host, so attackers went to people, edge devices and agents. Each row is partly a consequence of winning the previous row.

The second callout is the motive track read across the four periods. Defensive success explains why the attacker had to move; the payout explains where they moved to. When the product was the machine, the attack was a file on the machine. When the product became the organization's willingness to pay, the attack became access to the organization. When the product became identity and data in SaaS, the attack became a token or an instruction. Students who remember only this sentence can reconstruct most of the table.

In words that Part 2 names formally (slide 21): the artifact carried the malicious meaning in the file era; the APT era added objective, because the same file meant something different inside a campaign; the access economy moved the meaning to control, since a legitimate tool, a valid token or a real vendor update was malicious only because of who held it; and the agent period adds a controller that is itself a program acting under delegated authority, so control and objective have to be read from the agent's context and actions. Each move is also a move in what evidence the defender needs, which is the second half of the lecture.

Avoid claiming that “fileless” always means literally no disk artifacts. The important distinction is that the primary malicious capability may never appear as a conventional executable file supplied to a scanner. The first row is the mildest break: still a file, no longer an executable, which is why file-based defenses extended rather than collapsed in that period.

Cloud and identity abuse go further: the attacker may realize an objective through legitimate APIs without delivering executable code to the victim host. The last row goes further still: the thing that executes is an instruction consumed by a program that was supposed to be on the defender's side.

## Interaction

Ask which row is the first where a perfect file classifier with a perfect signature database would have had nothing useful to classify. Expect answers spread across the first row (it had a file, just not an executable), the second and third (no file to detonate, no artifact at all), and the fourth (nothing on the host). Each answer locates "nothing to classify" at a different pipeline stage, which is the point of the next module but one.

## Transition

“When the file is no longer the unit, we need a vocabulary for the behavior instead.”

