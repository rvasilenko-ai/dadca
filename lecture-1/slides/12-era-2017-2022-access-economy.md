# Slide 12 — 2017–2022: the access economy, identity, and the supply chain

**Timing:** 21–25 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | The organization pays directly: big-game ransomware, affiliates, double extortion and access brokers. |
| **Attackers** | Living off the land is standard; access is bought, stolen through identities, injected via vendors. |
| **Operating system** | Windows closes the easy paths: Defender as default antivirus and EDR, internet macros blocked, credentials isolated. |
| **Internet** | HTTPS passes 90 percent; TLS 1.3 hides the certificate and encrypted DNS the lookup; identity is the perimeter. |
| **Security products** | EDR goes mainstream, then XDR; the network falls back to metadata; the sandbox becomes a commodity. |

> Access itself became the traded commodity. The capability moved into identities, tokens and trusted vendor channels, and attackers began attacking the EDR.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2017–2022 |
| --- | --- |
| **Motive and money** | The organization pays directly: big-game ransomware, affiliates on revenue share, double extortion, Colonial Pipeline (2021), initial-access brokers, infostealer log markets, cryptojacking, business email compromise the largest reported loss category through 2021, state cryptocurrency heists. |
| **Attackers** | Shadow Brokers leak (April 2017), then WannaCry and NotPetya. Emotet, TrickBot, Ryuk: big-game ransomware. Ransomware-as-a-service, affiliates, double extortion (2019), initial-access brokers, infostealers. Fileless and living-off-the-land tradecraft becomes standard: PowerShell, WMI, living-off-the-land binaries (LOLBins), Cobalt Strike, DLL side-loading, memory-only implants. Implants, loaders and ransomware move to Go and Rust (BlackCat in Rust, November 2021): still PE files, each runtime with its own analysis tooling. Supply chain: CCleaner, NotPetya via M.E.Doc, SolarWinds (2020), Kaseya, Log4Shell (2021). Edge appliances exploited from 2019 (Citrix ADC, Pulse Secure), then mass exploitation (ProxyLogon 2021). Identity: multi-factor authentication (MFA) fatigue, help-desk social engineering, token theft (LAPSUS$ 2022). Bring-your-own-vulnerable-driver (BYOVD) EDR killers. Wipers in Ukraine and the Viasat attack (February 2022). |
| **Operating system** | Windows 10 mainstream, Windows 7 end of life (2020). Defender, antivirus and EDR, becomes the default on the enterprise endpoint, with attack surface reduction rules, Credential Guard, tamper protection. Windows 11 (2021) requires TPM 2.0 and Secure Boot; virtualization-based security is on by default for new installs. Internet macros blocked by default (2022). Vulnerable-driver blocklist (2022). |
| **Internet** | HTTPS passes 90 percent of page loads for US Firefox users (2020) and for Chrome on Windows (2021). TLS 1.3 (2018), DNS over HTTPS (2018 onward). Flash end of life (2020). Cloud-first; remote work (2020). The identity provider is the perimeter; OAuth tokens and SaaS everywhere. MFA mainstream but phishable. |
| **Security products** | EDR mainstream, measured technique by technique in the ATT&CK Evaluations (2018), then XDR (detection across host, network and identity) and managed detection. NDR (network detection and response) and TLS fingerprinting (JA3, 2017). TLS inspection, SASE and zero trust (NIST SP 800-207, 2020). Sandboxes bundled and commoditized; FireEye sells its products business (2021). Cloud SIEM, CASB. Identity threat detection emerges. |

## Talking points

- Default story: NotPetya (state capability spills over); Ryuk, Maze and Colonial Pipeline (the organization pays, then pays not to be published); SolarWinds and the BYOVD wave (trusted channels, the winning control attacked).
- Fileless became ordinary: malware-free detections from 40 percent in 2018 to 79 percent in 2024.
- The commodity was access, because access is what the payout required.
- Edge appliances were already an entry point from 2019; implants move to Go and Rust.

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

**Default story, three events and one image.** NotPetya (2017): state capability spills into the world through a vendor's update. Ryuk, Maze and Colonial Pipeline (2018–2021): the organization pays, then pays not to be published. SolarWinds (2020) and the BYOVD wave (2022): trusted channels as delivery, and the winning control attacked. The image: the ransom note arrives after weeks in which the only malware on most hosts was PowerShell and a legitimate remote-management tool.

**Spill-over.** The period opens with the Shadow Brokers publishing exploits attributed to a United States intelligence agency, including EternalBlue. Within weeks WannaCry used it as a worm; in June NotPetya combined it with credential theft and built-in administration tools, spread through Ukrainian networks and then worldwide, and was later attributed by several governments to the Russian military. Top-tier capability reached criminals and lesser states overnight, and a state operation caused global collateral damage. Patch latency and flat networks, not a novel file, decided who was hit.

**Fileless became ordinary.** The memory-only frameworks and living-off-the-land techniques that advanced operators used at the end of the previous period became the default for criminal affiliates in this one. Commodity loaders ran PowerShell and WMI, implants lived in memory, legitimate signed executables side-loaded malicious DLLs. CrowdStrike's yearly counts make the curve visible: malware-free detections were 40 percent in 2018, 51 percent in 2019, 62 percent at the end of 2021 and 79 percent in 2024. This is the period in which the sandbox was starved of things to detonate and EDR became the control that mattered; FireEye selling its products business in 2021, a year after VMware bought Lastline, is the bookend to the 2013 IPO.

**The money moved from the consumer to the enterprise.** In the previous periods the attacker monetized the victim's machine or credentials through a third party. Now the victim organization pays the attacker directly, and the sums are set by what a company will pay to recover or to keep data private. That single change explains the period. Emotet delivered TrickBot, TrickBot delivered Ryuk, and by 2019 ransomware ran as a service: developers, affiliates on revenue share, initial-access brokers selling footholds, infostealers feeding the brokers, and double extortion, encrypting and also threatening to publish the stolen data, making backups insufficient. Colonial Pipeline in May 2021, fuel lines shut for days, a ransom paid and most of it seized a month later, is the incident that made ransomware a national-security matter. The traded commodity was access, not malicious files, because access is what the payout required. Business email compromise, which needs no malicious file at all, was meanwhile the largest reported loss category in FBI complaint data every year from 2017 to 2021 (investment fraud overtook it in 2022), and cryptojacking and state cryptocurrency heists added quieter revenue. This is the criminal landscape of the period the way botnets were for 2005 to 2010.

**Trust channels became delivery channels.** CCleaner, M.E.Doc, SolarWinds and Kaseya delivered through the vendor relationship. Edge appliances were already an entry point from 2019, Citrix ADC and Pulse Secure VPNs first, and Log4Shell and ProxyLogon showed mass exploitation of exposed services with no attachment at all; the next period makes the appliance the main way in. The period ends as it began, with a state operation: the wipers and the Viasat attack of February 2022.

**Identity became the target.** With the identity provider as the perimeter and tokens everywhere, LAPSUS$ in 2022 reached large companies through MFA fatigue and help-desk calls. No implant was required where a stolen session would do.

**The defense that mattered was attacked.** EDR became the dominant control, so attackers brought vulnerable signed drivers to kill it: bring your own vulnerable driver, BYOVD. It is the attacker's acknowledgment of which product won the period, and the ATT&CK Evaluations from 2018 are the market's: EDR products measured technique by technique, the vocabulary of the previous module turned into a benchmark. Slide 17 returns to BYOVD with remote-management tools as the other response.

The operating-system row is Microsoft closing the paths of the previous period: macros from the internet blocked, a driver blocklist, credential isolation, tamper protection. Each closure moved attackers one step further from the host.

## Transition

“The current period keeps the same capabilities and can run without a file at all: intrusion by hand, through edge devices, and then by agents acting on instructions. The file does not disappear; it stops being required.”

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
- [CISA advisory AA21-131A: DarkSide ransomware against a US pipeline company (11 May 2021)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)
- [US Department of Justice: $2.3 million in cryptocurrency paid to DarkSide seized, 63.7 of about 75 bitcoin (7 June 2021)](https://www.justice.gov/archives/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside)
- [CrowdStrike: 2020 Global Threat Report press release, malware-free 40 percent of attacks in 2018 and 51 percent in 2019 (3 March 2020)](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-global-threat-report-reveals-big-game-hunting-telecommunication-targeting-top-adversary-trends/)
- [CrowdStrike: 2022 Global Threat Report press release, 62 percent of detections malware-free in the fourth quarter of 2021 (15 February 2022)](https://www.crowdstrike.com/en-us/press-releases/crowdstrikes-annual-threat-report-exposes-evolution-of-ecrime-ecosystem/)
- [CrowdStrike: 2025 Global Threat Report, malware-free activity 79 percent of detections in 2024 (27 February 2025)](https://go.crowdstrike.com/rs/281-OBQ-266/images/CrowdStrikeGlobalThreatReport2025.pdf)
- [Symantec ISTR: living off the land and fileless attack techniques (July 2017)](https://docs.broadcom.com/doc/istr-living-off-the-land-and-fileless-attack-techniques-en)

### Detail

- [Palo Alto Networks Unit 42: BlackCat ransomware, written in Rust, first observed mid-November 2021 (27 January 2022)](https://unit42.paloaltonetworks.com/blackcat-ransomware/)
- [CISA advisory AA23-353A: #StopRansomware, ALPHV Blackcat (December 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a)
- [Mandiant: GoReSym, Go symbol recovery, on why stripped and statically linked Go binaries are hard to analyse (28 February 2022)](https://cloud.google.com/blog/topics/threat-intelligence/golang-internals-symbol-recovery)
- [Intezer: year of the Gopher, the 2020 Go malware round-up (2021)](https://www.intezer.com/blog/malware-analysis/year-of-the-gopher-2020-go-malware-round-up/)
- [CISA advisory AA20-020A: Citrix ADC vulnerability CVE-2019-19781, reported 17 December 2019 (20 January 2020)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-020a)
- [CISA advisory AA20-010A: continued exploitation of Pulse Secure VPN vulnerability CVE-2019-11510 (10 January 2020)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-010a)
- [CISA advisory AA22-057A: destructive malware targeting organizations in Ukraine, HermeticWiper (26 February 2022)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-057a)
- [Viasat: KA-SAT network cyber-attack overview, 24 February 2022 (30 March 2022)](https://www.viasat.com/perspectives/corporate/2022/ka-sat-network-cyber-attack-overview/)
- [Adobe: Flash Player end of life, 31 December 2020](https://www.adobe.com/products/flashplayer/end-of-life.html)
- [Microsoft: MITRE evaluation of EDR capabilities, results published 29 November 2018 (15 March 2019)](https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/mitre-evaluation-highlights-industry-leading-edr-capabilities-in-windows-defende/369831)
- [FireEye: sale of the FireEye products business to Symphony Technology Group for $1.2 billion (SEC Form 8-K exhibit, 2 June 2021)](https://www.sec.gov/Archives/edgar/data/1370880/000110465921075725/tm2118082d1_ex99-1.htm)
- [VMware: intent to acquire Lastline, announced June 2020 and closed 18 June 2020](https://blogs.vmware.com/security/2020/06/lastline.html)

### Headlines

- [CISA Emergency Directive 21-01: mitigate SolarWinds Orion code compromise (December 2020)](https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise-closed)
- [Sophos: Maze ransomware, one year and counting](https://www.sophos.com/en-us/blog/maze-ransomware-1-year-counting)
- [FBI Internet Crime Complaint Center annual reports (business email compromise losses)](https://www.ic3.gov/AnnualReport/Reports)
- [RFC 8484: DNS Queries over HTTPS (October 2018)](https://www.rfc-editor.org/rfc/rfc8484)
