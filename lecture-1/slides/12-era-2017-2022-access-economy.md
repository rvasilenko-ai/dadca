# Slide 12 — 2017–2022: the access economy, identity, and the supply chain

**Timing:** 22–26 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | The organization pays directly: big-game ransomware, affiliates, double extortion and access brokers. |
| **Attackers** | Living off the land is standard; access is bought, stolen through identities, injected via vendors. |
| **Operating system** | Windows closes the easy paths: Defender built in, internet macros blocked, TPM 2.0 required, VBS on by default. |
| **Internet** | HTTPS passes 90 percent and TLS 1.3 and DoH hide the rest; the identity provider becomes the perimeter. |
| **Security products** | EDR goes mainstream, then XDR; the network falls back to metadata; the sandbox becomes a commodity. |

> Access itself became the traded commodity. The capability moved into identities, tokens and trusted vendor channels, and attackers began attacking the EDR.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2017–2022 |
| --- | --- |
| **Motive and money** | The organization pays directly: big-game ransomware, affiliates on revenue share, double extortion, initial-access brokers, infostealer log markets, cryptojacking, business email compromise the largest reported loss category through 2021, state cryptocurrency heists. |
| **Attackers** | Shadow Brokers leak (April 2017), then WannaCry and NotPetya. Emotet, TrickBot, Ryuk: big-game ransomware. Ransomware-as-a-service, affiliates, double extortion (2019), initial-access brokers, infostealers. Fileless and living-off-the-land tradecraft becomes standard: PowerShell, WMI, LOLBins, Cobalt Strike, DLL side-loading, memory-only implants. Supply chain: CCleaner, NotPetya via M.E.Doc, SolarWinds (2020), Kaseya, Log4Shell (2021). Mass exploitation of edge services (ProxyLogon 2021). Identity: MFA fatigue, help-desk social engineering, token theft (LAPSUS$ 2022). BYOVD and EDR killers. |
| **Operating system** | Windows 10 mainstream, Windows 7 end of life (2020). Defender built in with attack surface reduction rules, Credential Guard, tamper protection. Windows 11 (2021) requires TPM 2.0 and Secure Boot; virtualization-based security is on by default for new installs. Internet macros blocked by default (2022). Vulnerable-driver blocklist (2022). |
| **Internet** | HTTPS passes 90 percent of page loads for US Firefox users (2020) and for Chrome on Windows (2021). TLS 1.3 (2018), DNS over HTTPS (2018 onward). Cloud-first; remote work (2020). The identity provider is the perimeter; OAuth tokens and SaaS everywhere. MFA mainstream but phishable. |
| **Security products** | EDR mainstream, then XDR and managed detection. NDR and TLS fingerprinting (JA3, 2017). TLS inspection, SASE and zero trust (NIST SP 800-207, 2020). Sandboxes bundled and commoditized. Cloud SIEM, CASB. Identity threat detection emerges. |

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

**Spill-over.** The period opens with the Shadow Brokers publishing exploits attributed to a United States intelligence agency, including EternalBlue. Within weeks WannaCry used it as a worm; in June NotPetya combined it with credential theft and built-in administration tools, spread through Ukrainian networks and then worldwide, and was later attributed by several governments to the Russian military. Top-tier capability reached criminals and lesser states overnight, and a state operation caused global collateral damage. Patch latency and flat networks, not a novel file, decided who was hit.

**Fileless became ordinary.** The memory-only frameworks and living-off-the-land techniques that advanced operators used at the end of the previous period became the default for criminal affiliates in this one. Commodity loaders ran PowerShell and WMI, implants lived in memory, legitimate signed executables side-loaded malicious DLLs. This is the period in which the sandbox was starved of things to detonate and EDR became the control that mattered.

**The money moved from the consumer to the enterprise.** In the previous periods the attacker monetized the victim's machine or credentials through a third party. Now the victim organization pays the attacker directly, and the sums are set by what a company will pay to recover or to keep data private. That single change explains the period. Emotet delivered TrickBot, TrickBot delivered Ryuk, and by 2019 ransomware ran as a service: developers, affiliates on revenue share, initial-access brokers selling footholds, infostealers feeding the brokers, and double extortion making backups insufficient. The traded commodity was access, not malicious files, because access is what the payout required. Business email compromise, which needs no malicious file at all, was meanwhile the largest reported loss category in FBI complaint data every year from 2017 to 2021 (investment fraud overtook it in 2022), and cryptojacking and state cryptocurrency heists added quieter revenue. This is the criminal landscape of the period the way botnets were for 2005 to 2010.

**Trust channels became delivery channels.** CCleaner, M.E.Doc, SolarWinds and Kaseya delivered through the vendor relationship. Log4Shell and ProxyLogon showed mass exploitation of exposed services with no attachment at all.

**Identity became the target.** With the identity provider as the perimeter and tokens everywhere, LAPSUS$ in 2022 reached large companies through MFA fatigue and help-desk calls. No implant was required where a stolen session would do.

**The defense that mattered was attacked.** EDR became the dominant control, so attackers brought vulnerable signed drivers to kill it. BYOVD is the attacker's acknowledgment of which product won the period. Slide 18 returns to it with remote-management tools as the other response.

The operating-system row is Microsoft closing the paths of the previous period: macros from the internet blocked, a driver blocklist, credential isolation, tamper protection. Each closure moved attackers one step further from the host.

## Transition

“The current period keeps the same capabilities and loses the file altogether: intrusion by hand, through edge devices, and then by agents acting on instructions.”

## Sources

### Labelled events

- [Microsoft Security Response Center: protecting customers and evaluating risk, the Shadow Brokers release (April 2017)](https://www.microsoft.com/en-us/msrc/blog/2017/04/protecting-customers-and-evaluating-risk/)
- [US-CERT alert TA17-132A: indicators associated with WannaCry ransomware (May 2017)](https://www.cisa.gov/news-events/alerts/2017/05/12/indicators-associated-wannacry-ransomware)
- [US-CERT alert TA17-181A: Petya ransomware (27 June 2017)](https://www.cisa.gov/news-events/alerts/2017/07/01/petya-ransomware)
- [White House statement attributing NotPetya to the Russian military (February 2018)](https://trumpwhitehouse.archives.gov/briefings-statements/statement-press-secretary-25/)
- [RFC 8446: TLS 1.3 (August 2018)](https://www.rfc-editor.org/rfc/rfc8446)
- [Microsoft: defeating fileless malware with behavior monitoring, AMSI and next-gen antivirus (September 2018)](https://www.microsoft.com/en-us/security/blog/2018/09/27/out-of-sight-but-not-invisible-defeating-fileless-malware-with-behavior-monitoring-amsi-and-next-gen-av/)
- [Palo Alto Networks: Cortex XDR introduced (26 February 2019)](https://www.paloaltonetworks.com/company/press/2019/palo-alto-networks-introduces-cortex-the-industrys-only-open-and-integrated-ai-based-continuous-security-platform)
- [FBI PSA I-100219: high-impact ransomware attacks threaten US businesses (October 2019)](https://www.ic3.gov/PSA/2019/PSA191002)
- [BleepingComputer: Allied Universal breached by Maze ransomware, stolen data leaked (first report of double extortion, 21 November 2019)](https://www.bleepingcomputer.com/news/security/allied-universal-breached-by-maze-ransomware-stolen-data-leaked/)
- [NIST SP 800-207: Zero Trust Architecture (August 2020)](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA advisory AA20-352A: SolarWinds Orion supply chain compromise (13 December 2020)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)
- [Microsoft: Windows 11 enables security by design, VBS and Secure Boot on by default (June 2021)](https://www.microsoft.com/en-us/security/blog/2021/06/25/windows-11-enables-security-by-design-from-the-chip-to-the-cloud/)
- [Microsoft: Windows 11 requirements, TPM 2.0 and UEFI Secure Boot](https://learn.microsoft.com/en-us/windows/whats-new/windows-11-requirements)
- [Microsoft: DEV-0537, LAPSUS$ (22 March 2022)](https://www.microsoft.com/en-us/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Microsoft: macros from the internet blocked by default in Office (2022)](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked)
- [Microsoft: vulnerable and malicious driver protections, BYOVD (December 2021)](https://www.microsoft.com/en-us/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)

### Headlines

- [CISA Emergency Directive 21-01: mitigate SolarWinds Orion code compromise (December 2020)](https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise-closed)
- [Sophos: Maze ransomware, one year and counting](https://www.sophos.com/en-us/blog/maze-ransomware-1-year-counting)
- [FBI Internet Crime Complaint Center annual reports (business email compromise losses)](https://www.ic3.gov/AnnualReport/Reports)
- [RFC 8484: DNS Queries over HTTPS (October 2018)](https://www.rfc-editor.org/rfc/rfc8484)
