# Slide 14 — What broke the file-centric model, and when

**Timing:** 30–32 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| What broke the model | Became dominant | What the defender lost |
| --- | --- | --- |
| Diversification of file types (archives, documents, scripts, exploit objects) and of runtimes inside the executable (.NET, Go, Rust) | From about 2010. Each channel blocked executables (mail 2000 and 2004, messengers 2005, social networks 2010) and was answered within months: archives, exploit documents, exploit kits, links. Go and Rust from 2020 | The executable as the one thing to scan, and one toolchain to analyse it |
| Process injection, reflective loading, memory-resident execution | End of 2010–2016; standard from 2017 | A file to detonate |
| Living-off-the-land tools | 2017–2022; the whole campaign by 2023 | A malicious artifact at all |
| Stolen identities, tokens and cloud APIs | 2017–2022 onward | The host as the place where the attack happens |
| Trusted vendor and update channels | 2017 onward: CCleaner, SolarWinds, then XZ Utils and XCPE | Provenance as a proxy for safety |
| Tool-using agents and external instructions | 2025–2026 | A program as the thing that executes intent |

> In each period the attacker moved the capability to where the sensor was not looking; each break was partly a consequence of defensive success against the one before.
> The money and motivation moved too: from the victim's machine, to the victim's credentials, to the victim's organization, to the victim's identity and data.

Beside the callout, a small figure: the malware-free share of CrowdStrike detections, 40 percent in 2018, 51 in 2019, 62 at the end of 2021, 79 in 2024.

## Speaker notes

This slide is the recap of the four periods. Each row is something students have just seen, now stated as a break in the model from slide 6, ordered by when it became dominant rather than when it was first seen. Every row has a precedent, and the first row is the clearest case of defense causing the next move. Macro viruses from 1995 and the VBScript worms of 2000–2001 were the first wave of non-executable files; Office macro security levels and Outlook attachment blocking absorbed them. Then the channels blocked the executable itself, and the dates matter because they are earlier than students expect: Outlook in June 2000 and by default from Outlook 2002, Gmail from its first months in 2004 with zip archives included, the mail gateways in between, MSN Messenger in April 2005 after the Bropia and Kelvir worms, Facebook Messages from their launch in November 2010. Each block was answered within months, and the answer was always a container the block did not cover. MyDoom mailed itself in zip archives in January 2004 and Bagle in password-protected zips a month later, with the password shown as an image by March. Kelvir sent a link to its .pif rather than the file, which the messenger filter did not catch, and Koobface spread through social networks by link from 2008. A Word zero-day carried targeted attacks in May 2006, a PDF exploit with zero antivirus detections circulated in November 2008, and MPack, the first exploit kit sold commercially, was documented in 2007; from then on the browser, not the attachment, delivered the executable. Macro documents returned in 2014, and JavaScript, VBScript and HTA downloaders, shortcut files and ISO images followed each later block. The collaboration tools of the 2020s repeat the cycle: Teams carried Storm-0324's phishing in 2023 and Black Basta's fake help-desk calls in 2024, and Discord's content network hosted payloads until it switched to expiring links in November 2023. That diversification is what changed what the sandbox had to detonate, and it is why the first bar on the timeline starts in 2004 rather than 2010: dominance came later, the diversification began the moment the executable was blocked. The row now also carries the diversification inside the executable: from about 2020 implants, loaders and ransomware moved to Go, Rust and .NET (BlackCat in Rust in November 2021 is the marker), all still PE files, but each runtime needs its own unpacking, symbol recovery and decompilation, so this break is at extraction as much as at the sensor; Part 2's options slide has the row for it. Memory-resident code and living off the land likewise have earlier precedents; what matters for the defender is the moment a technique stops being an exception and becomes the default.

Make the causal point explicit now that the evidence is on the table. File-centric defense worked: signatures, reputation, cloud lookups, download warnings and code-signing enforcement made delivering an unknown executable expensive, so attackers diversified the file. Sandboxes made the unknown document and dropped executable expensive, so attackers went to memory and built-in tools. EDR made implants visible, so attackers went to identities, vendors and remote-management tools. Operating-system hardening closed the host, so attackers went to people, edge devices and agents. Each row is partly a consequence of winning the previous row.

The second callout is the motive track read across the four periods. Defensive success explains why the attacker had to move; the payout explains where they moved to. When the product was the machine, the attack was a file on the machine. When the product became the organization's willingness to pay, the attack became access to the organization. When the product became identity and data in SaaS, the attack became a token or an instruction. Students who remember only this sentence can reconstruct most of the table.

The figure is the one measurement in Part 1 that states the thesis as a number: the share of CrowdStrike's detections that involved no malware file went from 40 percent in 2018 to 79 percent in 2024 (the 2021 point is the fourth quarter of that year). Say that the metric is one vendor's telemetry and that the direction, not the decimal, is the point.

**What did not change.** The person as the way in, and the file as a carrier. Phishing is the one initial-access capability that runs unchanged from the executable attachments of 2000 to the help-desk calls and ClickFix lures of 2024; the tracks do not show it because it never moved, and that is why it survives every row of this table. And the file never left: most campaigns still begin with an executable or a document, and the implants, loaders and infostealers sold on criminal markets in 2026 are files, now in Go, Rust and .NET, some with an LLM call inside (slide 13). This table records that the file stopped being required, not that it became rare; a lecture that says "malware is no longer a file" has overstated its own evidence.

In the words of the four questions that close Part 1 (slide 18): the artifact carried the malicious meaning in the file era; the APT era added objective, because the same file meant something different inside a campaign; the access economy moved the meaning to control, since a legitimate tool, a valid token or a real vendor update was malicious only because of who held it; and the agent period adds a controller that is itself a program acting under delegated authority, so control and objective have to be read from the agent's context and actions. Each move is also a move in what evidence the defender needs, which is the second half of the lecture.

Avoid claiming that “fileless” always means literally no disk artifacts. The important distinction is that the primary malicious capability may never appear as a conventional executable file supplied to a scanner. The first row is the mildest break: still a file, no longer an executable, which is why file-based defenses extended rather than collapsed in that period.

Cloud and identity abuse go further: the attacker may realize an objective through legitimate APIs without delivering executable code to the victim host. The last row goes further still: the thing that executes is an instruction consumed by a program that was supposed to be on the defender's side.

## Interaction

Ask which row is the first where a perfect file classifier with a perfect signature database would have had nothing useful to classify. Expect answers spread across the first row (it had a file, just not an executable), the second and third (no file to detonate, no artifact at all), and the fourth (nothing on the host). Each answer locates "nothing to classify" at a different pipeline stage, which is the point of the next module but one. Then close the loop with the vote in one breath, stated rather than asked: situation 1 is the model itself and has no row; 3 is the second row; 2 the second and third; 4 the third and fourth; 5 the last.

## Transition

“When the file is no longer the unit, we need a vocabulary for the behavior instead.”

## Sources

### Blocking and the answer

- [Google: file types blocked in Gmail (executables, also inside archives)](https://support.google.com/mail/answer/6590?hl=en)
- [Gmail Help, 2005 archived copy: Gmail does not accept executable files, even zipped (text updated October 2005; the article existed by June 2004)](https://web.archive.org/web/20051130002942/http://gmail.google.com/support/bin/answer.py?answer=6590)
- [Google Workspace Updates: Gmail will restrict .js file attachments from 13 February 2017 (25 January 2017)](https://workspaceupdates.googleblog.com/2017/01/gmail-will-restrict-js-file-attachments.html)
- [Microsoft Exchange Team: changes to file types blocked in Outlook on the web (25 September 2019)](https://techcommunity.microsoft.com/blog/exchange/changes-to-file-types-blocked-in-outlook-on-the-web/874451)
- [F-Secure: Novarg (MyDoom), attachments with zip, bat, cmd, exe, pif or scr extensions (January 2004)](https://www.f-secure.com/v-descs/novarg)
- [F-Secure: Bagle.F, password-protected zip attachments, found 29 February 2004 (archived copy)](https://web.archive.org/web/20050207084930/http://www.f-secure.com/v-descs/bagle_f.shtml)
- [Kaspersky Securelist: MSN makes an attempt to stop IM-worms, Messenger 7 blocks .pif and filters executable transfers (8 April 2005)](https://securelist.com/msn-makes-an-attempt-to-stop-im-worms/29993/)
- [Microsoft: Win32/Kelvir, activated when a user clicks a link in a Messenger message (2005)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Kelvir)
- [Nathan Power, Full Disclosure: Facebook Messages will not allow an executable attachment, and a bypass (27 October 2011)](https://seclists.org/fulldisclosure/2011/Oct/899)
- [SANS Internet Storm Center: targeted attack with a Word zero-day (May 2006)](https://isc.sans.edu/diary/1345)
- [SANS Internet Storm Center: Adobe Reader vulnerability exploited in the wild, zero antivirus detections (7 November 2008)](https://isc.sans.edu/diary/5312)
- [SANS Internet Storm Center: MPack analysis, a kit sold for $500 to $1,000 (20 June 2007)](https://isc.sans.edu/diary/3015)
- [Microsoft: Storm-0324 phishing through Teams, and the Teams restrictions that followed (12 September 2023)](https://www.microsoft.com/en-us/security/blog/2023/09/12/malware-distributor-storm-0324-facilitates-ransomware-access/)
- [BleepingComputer: Discord will switch to temporary file links to block malware delivery, with Discord's statement (4 November 2023)](https://www.bleepingcomputer.com/news/security/discord-will-switch-to-temporary-file-links-to-block-malware-delivery/)

### Executables diversify

- [Palo Alto Networks Unit 42: BlackCat ransomware, written in Rust, first observed mid-November 2021 (27 January 2022)](https://unit42.paloaltonetworks.com/blackcat-ransomware/)
- [Mandiant: GoReSym, Go symbol recovery, on why stripped and statically linked Go binaries are hard to analyse (28 February 2022)](https://cloud.google.com/blog/topics/threat-intelligence/golang-internals-symbol-recovery)

### Figure

- [CrowdStrike: 2020 Global Threat Report press release, malware-free 40 percent of attacks in 2018 and 51 percent in 2019 (3 March 2020)](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-global-threat-report-reveals-big-game-hunting-telecommunication-targeting-top-adversary-trends/)
- [CrowdStrike: 2022 Global Threat Report press release, 62 percent of detections malware-free in the fourth quarter of 2021 (15 February 2022)](https://www.crowdstrike.com/en-us/press-releases/crowdstrikes-annual-threat-report-exposes-evolution-of-ecrime-ecosystem/)
- [CrowdStrike: 2025 Global Threat Report, malware-free activity 79 percent of detections in 2024 (27 February 2025)](https://go.crowdstrike.com/rs/281-OBQ-266/images/CrowdStrikeGlobalThreatReport2025.pdf)

