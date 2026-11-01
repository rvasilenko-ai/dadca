# Slide 10 — 2000–2009: the executable, from worms to botnets

**Timing:** 14–18 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | Notoriety gives way to fraud and extortion: the victim's machine, its bandwidth and what it types become the product. |
| **Attackers** | Executables by mail and worm, then botnets, hidden by packers, rootkits and server-side polymorphism. |
| **Operating system** | Windows XP runs everyone as administrator with autorun on; SP2 and Vista start closing the host. |
| **Internet** | Broadband and plaintext HTTP; email is the delivery channel and the browser is full of plug-ins. |
| **Security products** | Signature antivirus learns emulation and reputation, mail gateways block executables, IDS reads plaintext payloads. |

> The attack was an executable delivered to an administrator over plaintext. Every product that mattered inspected files or payloads.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2000–2009 |
| --- | --- |
| **Motive and money** | From notoriety to fraud and extortion: adware and pay-per-install, spam botnets, DDoS extortion and DDoS for hire, click fraud, banking trojans, fake antivirus, carding. The victim's machine, its bandwidth and credentials are the product. |
| **Attackers** | Mass-mailing worms, executable attachments, and the tail of the first macro and script wave (VBScript worms, 2000–2001). Network worms against unpatched services: Code Red and Nimda (2001), Slammer and Blaster (2003), Sasser (2004). IRC botnets (Agobot, SDBot, rxbot, 2002–2004) make the infected machine a rentable platform. Packers and commercial protectors (UPX, ASPack, Armadillo, Themida). Windows XP rootkits (Hacker Defender, Sony BMG 2005, Rustock) and MBR bootkits (2007–08). Botnets and pay-per-install (Storm, Zeus, Conficker, Koobface). Server-side polymorphism and fake antivirus from about 2007. |
| **Operating system** | Windows XP (2001): users run as administrator, autorun on, firewall present but off by default until SP2 (2004) turns it on and adds DEP. Vista (2007): UAC, mandatory 64-bit driver signing, ASLR; kernel-patch protection carried over from 64-bit XP and Server 2003 SP1 (2005). Windows 7 (2009) ships PowerShell by default. |
| **Internet** | Broadband replaces dial-up. IE6, ActiveX, Flash, Java and Acrobat plugins. HTTP in plaintext; HTTPS only for login and payment. Email is the delivery channel. |
| **Security products** | Signature antivirus, then heuristics and emulation to see through packers. Outlook and mail gateways block executable attachments; Office macro security ends the first script wave. Personal firewalls and HIPS. Anti-spam gateways. Network IDS/IPS on plaintext traffic. Cloud reputation and file prevalence arrive at the end of the decade. |

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

Read the five tracks as one system, starting with the money. The attacker's unit was the executable because the victim ran as administrator on a machine with no built-in tooling worth abusing, received email and browsed with plug-in-heavy browsers, and the network carried everything in the clear. The defenses that mattered were exactly those built on that unit: file scanners, payload signatures, spam filters.

**Motive explains the volume.** The decade opens with worm authors seeking notoriety and closes with a criminal market. Adware and pay-per-install paid per infected machine; spam botnets rented out capacity; the same botnets sold DDoS, first as extortion of online businesses and then as a service for hire (Ancheta, indicted in November 2005 for selling botnet access for DDoS and spam, was the first US prosecution of its kind); click fraud monetized browsers; banking trojans and carding monetized credentials. Once an infection was worth a few cents to a few dollars, the attacker's problem became scale, and scale is what produced botnets and server-side polymorphism. The product was the victim's machine, its bandwidth and what it typed.

**Worms, then botnets.** The first half of the decade belongs to the worms: Code Red and Nimda in 2001, Slammer and Blaster in 2003, Sasser in 2004, each exploiting an unpatched service on a machine with no firewall and spreading with no user action. XP SP2 turning the firewall on in August 2004 is the defender's answer, and the big network worms go quiet until Conficker finds MS08-067 in 2008. The second half belongs to the botnets. The IRC bot families (Agobot, SDBot, rxbot) made the compromised machine report to a channel and take orders, which is what turned infections into inventory that could be rented for spam, DDoS and installs; Ancheta was prosecuted for exactly that trade. Storm, Zeus, Conficker and Koobface are the mature form: the machine is the product and the binary is disposable.

Within the decade the attacker moved three times inside the file:

- **Packers and protectors** made the bytes on disk stop matching the code that ran. Antivirus added emulation and generic unpacking: the scanner ran the file a little to see it.
- **Rootkits and bootkits** made the live system lie about which files and processes existed. The Sony BMG case in 2005 made the technique public. Defenders inspected raw disk and memory from outside the lying layer, and Microsoft's 64-bit kernel-patch protection (2005) and Vista's mandatory driver signing (2007) were in part a response.
- **Botnets and server-side polymorphism** turned the host into a rented commodity and gave every victim a unique binary. The asset was the command-and-control infrastructure; the binary was disposable. This broke hash and byte signatures operationally and produced reputation and prevalence systems (McAfee Artemis in 2008, Symantec Quorum and Insight in 2009–2010), cloud lookups, generic detections, and pushed machine learning on file features from research (first papers in 2001) toward products (from about 2012). Lecture 3 picks that up.

The operating-system row explains why so much was possible: administrator by default, autorun, and no exploit mitigations until SP2 and Vista. Vista's UAC and driver signing were unpopular precisely because they took privileges away from the model attackers had been enjoying.

## Transition

“The next period starts with a different kind of adversary. The file stays, but it stops being an executable.”

## Sources

### Labelled events

- [Microsoft: Outlook 2002 developer security overview, Level 1 attachments blocked by default (2002)](https://learn.microsoft.com/en-us/previous-versions/office/developer/office-xp/aa140151%28v=office.10%29)
- [Microsoft KB 262631: the Outlook 2000 SR-1 e-mail security update (archived copy)](https://web.archive.org/web/20130109224234/http://support.microsoft.com/kb/262631)
- [Microsoft: Windows XP is here (press release, 25 October 2001)](https://news.microsoft.com/2001/10/25/windows-xp-is-here/)
- [Mark Russinovich: Sony, rootkits and digital rights management gone too far (31 October 2005)](https://techcommunity.microsoft.com/t5/windows-blog-archive/sony-rootkits-and-digital-rights-management-gone-too-far/ba-p/723442)
- [F-Secure Labs: Small.DAM spammed around, the Storm Worm's first big run (19 January 2007; archived copy)](http://web.archive.org/web/20130308064153/http://www.f-secure.com/weblog/archives/00001086.html)
- [Microsoft: Windows Vista and Office 2007 launch to consumers worldwide (29 January 2007)](https://news.microsoft.com/source/2007/01/29/microsoft-launches-windows-vista-and-microsoft-office-2007-to-consumers-worldwide/)
- [Michael Howard: address space layout randomization in Windows Vista (2006)](https://learn.microsoft.com/en-us/archive/blogs/michael_howard/address-space-layout-randomization-in-windows-vista)
- [McAfee: Artemis Technology announced (press release, 8 September 2008; archived copy)](http://web.archive.org/web/20080914114358/http://www.mcafee.com/us/about/press/corporate/2008/20080908_180000_q.html)
- [Microsoft security bulletin MS08-067, the vulnerability Conficker exploited (23 October 2008)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067)
- [Microsoft: Worm:Win32/Conficker.A, published 23 November 2008](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Worm:Win32/Conficker.A)
- [Microsoft: Win32/Gaobot threat description (Agobot: IRC-controlled worm family, 2002–2004)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Gaobot)
- [Microsoft: Win32/Rbot threat description (SDBot and rxbot derivatives)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Rbot)
- [US-CERT alert TA09-088A: Conficker worm targets Microsoft Windows systems (March 2009)](https://www.cisa.gov/news-events/alerts/2009/03/29/conficker-worm-targets-microsoft-windows-systems)
- [Conficker Working Group: lessons learned (archived copy)](https://web.archive.org/web/20151218171845/http://www.confickerworkinggroup.org/wiki/)
- [Microsoft: PowerShell v2 is already part of Windows 7 (November 2009)](https://learn.microsoft.com/en-us/archive/blogs/josebda/download-for-powershell-v2-for-windows-7-no-need-its-already-there)

### Detail

- [CERT/CC: the 2001 CERT advisories, including CA-2001-19 Code Red (19 July 2001) and CA-2001-26 Nimda (18 September 2001)](https://www.sei.cmu.edu/library/2001-cert-advisories/)
- [CERT/CC: the 2003 CERT advisories, including CA-2003-04 MS-SQL Server worm, Slammer (25 January 2003) and CA-2003-20 W32/Blaster (11 August 2003)](https://www.sei.cmu.edu/library/2003-cert-advisories/)
- [Microsoft security bulletin MS01-033, the IIS vulnerability Code Red exploited (18 June 2001)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2001/ms01-033)
- [Microsoft security bulletin MS02-039, the SQL Server vulnerability Slammer exploited (24 July 2002)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2002/ms02-039)
- [Microsoft security bulletin MS03-026, the RPC DCOM vulnerability Blaster exploited (16 July 2003)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2003/ms03-026)
- [Microsoft security bulletin MS04-011, the LSASS vulnerability Sasser exploited (13 April 2004)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2004/ms04-011)
- [Microsoft: Win32/Msblast threat description (Blaster)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Msblast)
- [Microsoft: Worm:Win32/Sasser threat description](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Worm:Win32/Sasser)
- [Microsoft: Microsoft joins law enforcement to track perpetrators of emerging worm attacks (Sasser and Agobot, 2 May 2004)](https://news.microsoft.com/source/2004/05/02/microsoft-joins-law-enforcement-to-track-perpetrators-of-emerging-worm-attacks-against-computer-users/)
- [Microsoft: reward program helps lead to arrest related to the Sasser worm, within seven days of its launch (8 May 2004)](https://news.microsoft.com/source/2004/05/08/microsoft-reward-program-helps-lead-to-information-resulting-in-arrest-related-to-sasser-internet-worm/)
- [Kaspersky: Kaspersky Lab detects new worms attacking MySpace and Facebook (Koobface, 1 August 2008)](https://www.kaspersky.com/about/press-releases/kaspersky-lab-detects-new-worms-attacking-myspace-and-facebook)
- [Information Warfare Monitor, Nart Villeneuve: Koobface, inside a crimeware network (12 November 2010)](https://citizenlab.ca/2010/11/koobface-inside-a-crimeware-network/)

### Headlines

- [US Department of Justice: computer virus broker arrested for selling armies of infected computers to hackers and spammers (Ancheta indictment, 3 November 2005)](https://www.justice.gov/archive/criminal/cybercrime/press-releases/2005/anchetaArrest.htm)
- [US Department of Justice: “botherder” dealt record prison sentence for selling and spreading malicious computer code (Ancheta sentenced, 8 May 2006)](https://www.justice.gov/archive/criminal/cybercrime/press-releases/2006/anchetaSent.htm)
- [Microsoft: Windows XP SP2 firewall enabled by default (2004)](https://learn.microsoft.com/en-us/previous-versions/bb877964%28v=technet.10%29)
- [Microsoft: An introduction to Kernel Patch Protection (x64, 2005)](https://learn.microsoft.com/en-us/archive/blogs/windowsvistasecurity/an-introduction-to-kernel-patch-protection)
- [MITRE ATT&CK: Obfuscated Files or Information: Software Packing (T1027.002)](https://attack.mitre.org/techniques/T1027/002/)
- [MITRE ATT&CK: Bootkit (T1542.003)](https://attack.mitre.org/techniques/T1542/003/)
