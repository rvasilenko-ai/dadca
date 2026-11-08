# Slide 10 — 2000–2009: the executable, from worms to botnets

**Timing:** 13–17 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | Notoriety gives way to fraud and extortion: the victim's machine, its bandwidth and what it types become the product. |
| **Attackers** | Executables arrive by mail and by worm, then botnets; packers, rootkits and server-side polymorphism hide them. |
| **Operating system** | Windows XP runs everyone as administrator with autorun on; SP2 and Vista start closing the host. |
| **Internet** | Broadband and plaintext HTTP; email is the delivery channel and the browser is full of plug-ins. |
| **Security products** | Signature antivirus learns emulation and reputation, mail gateways block executables, IDS reads plaintext payloads. |

> The attack was an executable, mailed to a user running as administrator or spreading by worm over an unencrypted network. The products of the decade inspected files and payloads.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2000–2009 |
| --- | --- |
| **Motive and money** | From notoriety to fraud and extortion: adware and pay-per-install, spam botnets, DDoS extortion and DDoS for hire, click fraud, banking trojans, fake antivirus, carding. The victim's machine, its bandwidth and credentials are the product. |
| **Attackers** | Mass-mailing worms, executable attachments, and the tail of the first macro and script wave (VBScript worms, 2000–2001). Network worms against unpatched services: Code Red and Nimda (2001), Slammer and Blaster (2003), Sasser (2004). Mass-mailers answer attachment blocking within weeks with zip and password-protected archives (MyDoom, Bagle, 2004); IM worms spread over MSN Messenger by file and by link (Bropia, Kelvir, 2005); exploit documents (Word 2006, PDF 2008) and the first commercial exploit kit (MPack, 2007) follow. IRC botnets (Agobot, SDBot, rxbot, 2002–2004) make the infected machine a rentable platform. Packers and commercial protectors (UPX, ASPack, Armadillo, Themida). Windows XP rootkits (Hacker Defender, Sony BMG 2005, Rustock) and MBR bootkits (2007–08). Botnets and pay-per-install (Storm, Zeus, Conficker, Koobface). Server-side polymorphism and fake antivirus from about 2007. |
| **Operating system** | Windows XP (2001): users run as administrator, autorun on, firewall present but off by default until SP2 (2004) turns it on and adds DEP (no-execute memory). Vista (2007): UAC (consent prompts for administrative actions), mandatory 64-bit driver signing, ASLR (randomized memory layout); kernel-patch protection carried over from 64-bit XP and Server 2003 SP1 (2005). Windows 7 (2009) ships PowerShell by default. |
| **Internet** | Broadband replaces dial-up. IE6, ActiveX, Flash, Java and Acrobat plugins. HTTP in plaintext; HTTPS only for login and payment. Email is the delivery channel. |
| **Security products** | Signature antivirus, then heuristics and emulation to see through packers. Outlook (2000) and mail gateways, then Gmail (2004, zips included), block executable attachments; messengers filter unsafe transfers after the 2005 IM worms; Office macro security ends the first script wave. Personal firewalls and HIPS. Anti-spam gateways. Network intrusion detection and prevention (IDS/IPS) on plaintext traffic. Cloud reputation and file prevalence arrive at the end of the decade. |

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

**Default story, three events and one image.** Windows XP (2001): everyone an administrator, autorun on, firewall off. The IRC botnets of 2003–2004 and the Ancheta case: the infected machine becomes inventory, sold for spam, DDoS and installs. Storm (2007) and McAfee Artemis (2008): a unique binary per victim, answered by reputation in the cloud. The image for students who were not there: in August 2003 an unpatched XP laptop plugged into a university network was infected by Blaster within minutes, with nothing opened and nothing clicked.

Read the five tracks as one system, starting with the money. The attacker's unit was the executable because the victim ran as administrator on a machine with no built-in tooling worth abusing, received email and browsed with plug-in-heavy browsers, and the network carried everything in the clear. The defenses that mattered were exactly those built on that unit: file scanners, payload signatures, spam filters.

**Motive explains the volume.** The decade opens with worm authors seeking notoriety and closes with a criminal market. Adware and pay-per-install paid per infected machine; spam botnets rented out capacity; the same botnets sold DDoS, first as extortion of online businesses and then as a service for hire (Ancheta, indicted in November 2005 for selling botnet access for DDoS and spam, was the first US prosecution of its kind); click fraud monetized browsers; banking trojans and carding monetized credentials. Once an infection was worth a few cents to a few dollars, the attacker's problem became scale, and scale is what produced botnets and server-side polymorphism. The product was the victim's machine, its bandwidth and what it typed.

**Worms, then botnets.** The first half of the decade belongs to the worms: Code Red and Nimda in 2001, Slammer and Blaster in 2003, Sasser in 2004, each exploiting an unpatched service on a machine with no firewall and spreading with no user action. XP SP2 turning the firewall on in August 2004 is the defender's answer, and the big network worms go quiet until Conficker finds MS08-067 in 2008. The second half belongs to the botnets. The IRC bot families (Agobot, SDBot, rxbot) made the compromised machine report to a channel and take orders, which is what turned infections into inventory that could be rented for spam, DDoS and installs; Ancheta was prosecuted for exactly that trade. Storm, Zeus, Conficker and Koobface are the mature form: the machine is the product and the binary is disposable.

**Each block got an answer.** Outlook blocked executable attachments in 2000 and Gmail from 2004, zips included; the mass-mailers switched to zip within weeks (MyDoom, January 2004) and to password-protected zips with the password shown as an image (Bagle, February to March 2004). When the IM worms of 2005 made MSN Messenger filter .pif and executable transfers, Kelvir was already sending a link instead. Exploit documents (a Word zero-day in May 2006, PDF in November 2008) and MPack, the first exploit kit sold commercially (2007), are the same answer with a different container: the file diversified as soon as the executable was blocked, which is why slide 14's first bar starts in this period and not in 2010.

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

### Blocking and the answer

- [Gmail Help, 2005 archived copy: Gmail does not accept executable files, even zipped (the article existed by June 2004)](https://web.archive.org/web/20051130002942/http://gmail.google.com/support/bin/answer.py?answer=6590)
- [F-Secure: Novarg (MyDoom), attachments with zip, bat, cmd, exe, pif or scr extensions (January 2004)](https://www.f-secure.com/v-descs/novarg)
- [F-Secure: Bagle.F, password-protected zip attachments, found 29 February 2004 (archived copy)](https://web.archive.org/web/20050207084930/http://www.f-secure.com/v-descs/bagle_f.shtml)
- [F-Secure weblog: Bagle.N, the archive password shown as an image (13 March 2004; archived copy)](https://web.archive.org/web/20080127190533/http://www.f-secure.com/weblog/archives/00000092.html)
- [Microsoft: Win32/Bropia, a worm that spreads using MSN Messenger (February 2005)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Bropia)
- [Microsoft: Win32/Kelvir, activated when a user clicks a link in a Messenger message (2005)](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Win32/Kelvir)
- [Microsoft: global availability of MSN Messenger 7 (7 April 2005)](https://news.microsoft.com/source/2005/04/07/global-availability-of-msn-messenger-and-msn-spaces-connects-people-around-the-world/)
- [Kaspersky Securelist: MSN makes an attempt to stop IM-worms, Messenger 7 blocks .pif and filters executable transfers (8 April 2005)](https://securelist.com/msn-makes-an-attempt-to-stop-im-worms/29993/)
- [Microsoft security bulletin MS06-027: the Word vulnerability exploited in targeted attacks (13 June 2006)](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2006/ms06-027)
- [SANS Internet Storm Center: targeted attack with a Word zero-day (May 2006)](https://isc.sans.edu/diary/1345)
- [SANS Internet Storm Center: MPack analysis, a kit sold for $500 to $1,000 (20 June 2007)](https://isc.sans.edu/diary/3015)
- [Symantec: MPack, packed full of badness (27 May 2007; archived copy)](https://web.archive.org/web/20071225144348/http://www.symantec.com/enterprise/security_response/weblog/2007/05/mpack_packed_full_of_badness.html)
- [SANS Internet Storm Center: Adobe Reader vulnerability exploited in the wild, zero antivirus detections (7 November 2008)](https://isc.sans.edu/diary/5312)
- [CERT/CC vulnerability note VU#593409: Adobe Reader util.printf, CVE-2008-2992 (4 November 2008)](https://kb.cert.org/vuls/id/593409)

### Headlines

- [US Department of Justice: computer virus broker arrested for selling armies of infected computers to hackers and spammers (Ancheta indictment, 3 November 2005)](https://www.justice.gov/archive/criminal/cybercrime/press-releases/2005/anchetaArrest.htm)
- [US Department of Justice: “botherder” dealt record prison sentence for selling and spreading malicious computer code (Ancheta sentenced, 8 May 2006)](https://www.justice.gov/archive/criminal/cybercrime/press-releases/2006/anchetaSent.htm)
- [Microsoft: Windows XP SP2 firewall enabled by default (2004)](https://learn.microsoft.com/en-us/previous-versions/bb877964%28v=technet.10%29)
- [Microsoft: An introduction to Kernel Patch Protection (x64, 2005)](https://learn.microsoft.com/en-us/archive/blogs/windowsvistasecurity/an-introduction-to-kernel-patch-protection)
- [MITRE ATT&CK: Obfuscated Files or Information: Software Packing (T1027.002)](https://attack.mitre.org/techniques/T1027/002/)
- [MITRE ATT&CK: Bootkit (T1542.003)](https://attack.mitre.org/techniques/T1542/003/)
