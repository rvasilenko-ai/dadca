# Slide 13 — 2023–2026: hands-on hacking, edge devices, and agents

**Timing:** 25–29 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | Data theft without encryption; session tokens as the product; agent attacks have no business model yet. |
| **Attackers** | Hands-on hacking via help desks and stolen sessions; edge devices as the main entry; instructions for agents. |
| **Operating system** | The host hardens by default: driver blocklist, protected credentials, passkeys; the cloud host is Linux. |
| **Internet** | Encrypted Client Hello hides the last plaintext field; AI assistants sit between the user and the data. |
| **Security products** | Identity threat detection, baselining for living off the land, LLM triage; agent observability begins. |

> A whole campaign can now run without a malware file, while most still start with one. The newest executable is an instruction in data, and the sensor has to follow it into identity and into the agent's context.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2023–2026 |
| --- | --- |
| **Motive and money** | Extortion without encryption (mass data theft, Cl0p and MOVEit 2023). Help-desk social engineering against high-value targets. Session tokens and SaaS data as the product (Snowflake 2024). State prepositioning for disruption, and state theft at record scale (Bybit 2025). AI lowers the cost of lures. Bandwidth as the product again: residential proxies and ad fraud sold from device firmware (XCPE 2026). Agent attacks have no settled business model yet. |
| **Attackers** | Living off the land as the whole campaign (Volt Typhoon advisory, 2023). Help-desk social engineering, SIM swaps and MFA bypass (Scattered Spider). Session cookie and token theft via infostealers. Edge devices become the main entry (Citrix, Ivanti, Fortinet, 2023–24; Salt Typhoon in the telecoms, 2024). Supply chain into open source (XZ Utils 2024) and into consumer devices: firmware botnets in set-top boxes (BADBOX 2.0 2025, XCPE 2026). Infostealer credentials against SaaS (Snowflake 2024). ClickFix: the user pastes the command. AI-assisted lures. Instructions in data that hijack enterprise agents; AI-orchestrated campaigns reported (2025); autonomous agents as operators (2026). Files still arrive: implants, loaders and infostealers for sale, now in Go, Rust and .NET, some calling an LLM (NIK C2 in Go; VOLTA's model-ranked victims; October 2026). |
| **Operating system** | Windows 11: vulnerable-driver blocklist on by default (2022); LSA protection on by default for new enterprise-joined installs; virtualization-based security on by default; Smart App Control (2022). Passkeys (2023). Windows 10 end of support (2025). Hardened mobile and macOS. The cloud host is Linux, where XZ Utils showed the supply chain. |
| **Internet** | Encrypted Client Hello: in browsers since 2023, standardized in 2026, server-side adoption still narrow. AI assistants in browsers, IDEs and SaaS; tool-using agents and agent protocols (2024–26). SaaS-to-SaaS integrations and OAuth sprawl. Data lives behind APIs. Collaboration tools are the new mail: phishing and fake help-desk calls through Teams (2023–24), payloads on Discord's network until its links expired (2023). |
| **Security products** | Identity threat detection and response. EDR tamper protection and, after the CrowdStrike outage (2024), endpoint security moving out of the kernel. Baselining for living-off-the-land detection. LLM triage in the SOC; agentic malware analysis (Project Ire, 2025). ATT&CK adds Defense Impairment (April 2026) and Impair Autonomous Defenses (October 2026). Guardrails, prompt-injection defenses, agent observability. |

## Talking points

- Default story: Volt Typhoon (a whole campaign on built-in tools); Scattered Spider (a phone call, not an exploit); the agent incidents (an instruction in data as the executable).
- Say "no malware file", never "no malware".
- What did not leave: most campaigns still start with a file; implants in Go, Rust and .NET, some with an LLM call inside.
- XCPE: the botnet-for-hire model of 2005 on devices no one patches; found from the network, answered by the platform owner.

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

**Default story, three events and one image.** Volt Typhoon (2023): a whole campaign on built-in tools and valid accounts. Scattered Spider (2023): a phone call to the help desk instead of an exploit. The agent incidents (2025–2026): an instruction in data as the executable. The image: the attacker phones the help desk, gets the MFA reset, logs in as the employee, and never runs a file on the laptop.

**The product is now identity and data, not the host.** Cl0p's mass exploitation of MOVEit in 2023 skipped encryption entirely and extorted on stolen data alone. Scattered Spider chose casinos and large enterprises because the payout justified live social engineering of a help desk. Infostealer markets sell session tokens because a token opens the SaaS tenant where the data lives; the Snowflake customer breaches of 2024 are the cleanest case, infostealer credentials, no MFA, about 165 tenants, no host touched. Volt Typhoon is the reminder that one class of adversary is not paid at all and is prepositioning for disruption, and North Korea's Bybit heist of February 2025, about $1.5 billion, is the state revenue line at record scale. For the agent cases the business model is not yet observed; Lecture 2 treats grab-and-go theft and campaign staging as projections, not as a reported economy.

**What is new, and what is not.** Fileless tradecraft is not new here; the previous period made it standard. The period's additions are three: hands-on intrusion through people and sessions rather than payloads, edge devices as the entry point, and agents as a new actor. Say the "no malware file" part precisely, because the lecture's own definition is at stake: the malicious capability is still there, in hands-on intrusion, built-in tools, exploits and stolen sessions; what is gone is the file that used to carry it. The 2023 Volt Typhoon advisory described a state actor persisting in critical infrastructure using only built-in tools and valid accounts, which prompted dedicated living-off-the-land guidance in 2024. Scattered Spider reached large enterprises the same year through help-desk calls and MFA resets, with SIM swapping among its wider techniques. Infostealers sold session cookies that skipped authentication altogether. Edge devices, which run no EDR, had been an entry point since 2019; in this period they became the main one, and Salt Typhoon showed the same path into the telecoms. In each case the host-based sensor had little to see, because the attacker used the organization's own tools under the organization's own identities.

**What did not leave.** Say this plainly, because the period's name invites overstatement: most campaigns still start with a file, and the implants, loaders and infostealers sold on criminal markets are files. What changed inside them is the runtime, Go, Rust and .NET rather than C, which keeps the PE format and defeats the analysis toolchain built for C, and, in the newest ones, an LLM call: Talos described NIK C2 in October 2026, a Go remote-access tool with an OpenAI client that bills the victim's own key, and VOLTA, a built-to-order infostealer that sends the stolen bundle to a model to rank the victim's assets. The file stopped being required; it did not become rare.

**The user runs the payload.** ClickFix lures ask the user to paste a command into a Run dialog or terminal, turning the person into the loader. There is no attachment to scan and the process ancestry looks like the user.

**The operating-system row has largely won the host.** Driver blocklists, LSA protection on enterprise devices, virtualization-based security and passkeys close most of the previous period's paths by default. That success is part of why the attacker moved to identity, edge devices and people. XZ Utils in March 2024 is the reminder that the host is now also Linux, and that its supply chain can be the way in.

**The device supply chain.** XCPE, disclosed by Google on 2 November 2026, is the Mirai line arriving at the consumer and the supply-chain row of slide 14 at the device level: a manufacturer built a backdoor into the firmware partition of more than 1.3 million Android TV boxes, designed to pass certification checks, and sold access to affiliates for residential proxies and ad fraud; Google assessed that the affiliates' control domains reached at least 10 million more devices. That is the botnet-for-hire model of 2005, bandwidth as the product, on hardware that can never run an agent. BADBOX (2023) and BADBOX 2.0 (FBI warning, June 2025) were the precedents. No endpoint product answered: the traffic was seen from the network by a home-WiFi vendor and a carrier's research team, and the response was legal action against the control domains and the platform owner banning the manufacturer from certified devices, which is Part 2's point that the fix lands at whatever stage can see the evidence.

**The new executable.** When a coding agent reads a repository file, or a CRM agent reads a lead record, and acts on an instruction embedded in it (prompt injection: data the agent reads, written to be obeyed as instructions), no classical sensor has anything to classify. The telemetry that matters is the context the agent assembled, the tools it called and the identity it acted under. Autonomous agents operating as attackers add persistence and volume on the other side; reports of agent-orchestrated campaigns began in 2025, before the July 2026 incident. Lecture 2 covers both cases in depth; here they are only the latest point on the curve.

**Security products are following again.** The CrowdStrike outage of July 2024 showed the cost of the kernel sensor that won the previous period, and Microsoft's resiliency initiative moves endpoint security out of the kernel: a change in where the sensor sits, not in what it sees. ATT&CK's April 2026 release (v19) split off Defense Impairment as a tactic, and the October 2026 release (v20) added Impair Autonomous Defenses, prompt injection against LLM-assisted analysis among its methods: the first time the framework named attacks on the defender's own agents. Identity threat detection, agent observability, guardrails and prompt-injection defenses are the sensor moving into the identity provider and the agent harness. Agentic analysis systems such as Project Ire are the same reasoning capability applied on the defensive side; Lecture 3 covers that.

## Transition

“Put the four periods back on one list: what broke the file-centric model, and when.”

## Sources

### Labelled events

- [Microsoft: Introducing Microsoft 365 Copilot (16 March 2023)](https://www.microsoft.com/en-us/copilot/blog/2023/03/16/introducing-microsoft-365-copilot-a-whole-new-way-to-work/)
- [CISA advisory AA23-144A: PRC state-sponsored cyber actor living off the land, Volt Typhoon (May 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a)
- [CISA advisory AA23-158A: CL0P ransomware gang exploits MOVEit Transfer, extortion without encryption (June 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a)
- [MGM Resorts: Form 8-K on the September 2023 cybersecurity issue (filed 13 September 2023)](https://www.sec.gov/Archives/edgar/data/789570/000119312523233855/d502352d8k.htm)
- [Caesars Entertainment: Form 8-K, social engineering attack on an outsourced IT vendor (filed 14 September 2023)](https://www.sec.gov/Archives/edgar/data/1590895/000119312523235015/d537840d8k.htm)
- [CISA advisory AA23-320A: Scattered Spider (November 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Microsoft: passkeys arrive in Windows 11 (26 September 2023)](https://blogs.windows.com/windowsexperience/2023/09/26/the-most-personal-windows-11-experience-begins-rolling-out-today/)
- [Proofpoint: ClickFix social engineering technique floods the threat landscape (November 2024)](https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape)
- [Microsoft: Think before you ClickFix, first observed March to June 2024 (August 2025)](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/)
- [Microsoft Research: Project Ire (August 2025)](https://www.microsoft.com/en-us/research/project/project-ire/)
- [Noma Security: ForcedLeak (September 2025)](https://noma.security/noma-labs/forcedleak/)
- [Hugging Face: technical timeline of the July 2026 incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [Microsoft: helping our customers through the CrowdStrike outage, 8.5 million Windows devices (20 July 2024)](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)
- [Microsoft: Windows security and resiliency, the Windows Resiliency Initiative moves security products out of kernel mode (19 November 2024)](https://blogs.windows.com/windowsexperience/2024/11/19/windows-security-and-resiliency-protecting-your-business/)

### Detail

- [Mandiant: UNC5537 targets Snowflake customer instances for data theft and extortion, about 165 organizations (10 June 2024)](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)
- [FBI and CISA: joint statement on PRC targeting of commercial telecommunications infrastructure (13 November 2024)](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-peoples-republic-china-prc-targeting-commercial-telecommunications)
- [CISA: reported supply chain compromise affecting XZ Utils, CVE-2024-3094 (29 March 2024)](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094)
- [Andres Freund, oss-security: backdoor in upstream xz/liblzma leading to ssh server compromise (29 March 2024)](https://www.openwall.com/lists/oss-security/2024/03/29/4)
- [FBI PSA I-022625: North Korea responsible for the $1.5 billion Bybit hack (26 February 2025)](https://www.ic3.gov/PSA/2025/PSA250226)
- [Anthropic: detecting and countering misuse of AI, agent-assisted data extortion (27 August 2025)](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)
- [Anthropic: disrupting the first reported AI-orchestrated cyber espionage campaign (13 November 2025)](https://www.anthropic.com/news/disrupting-AI-espionage)
- [Microsoft: Windows 10 Home and Pro lifecycle, end of support 14 October 2025](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)
- [MITRE ATT&CK: April 2026 updates, v19 splits Defense Evasion into Stealth and Defense Impairment (28 April 2026)](https://attack.mitre.org/resources/updates/updates-april-2026/)
- [MITRE ATT&CK: Impair Autonomous Defenses (T1685.007), added in v20 (13 October 2026)](https://attack.mitre.org/techniques/T1685/007/)
- [Google Threat Intelligence Group: shutting the door on the XCPE botnet, 1.3 million set-top boxes backdoored in firmware by the manufacturer (2 November 2026)](https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet)
- [Plume: Google leads industry takedown of a botnet hidden in more than 1.3 million set-top boxes (2 November 2026)](https://www.plume.com/newsroom/google-leads-industry-takedown-of-botnet-hidden-in-more-than-1-3-million-set-top-boxes-across-200-countries)
- [FBI PSA: home internet-connected devices facilitate criminal activity, the BADBOX 2.0 botnet (5 June 2025)](https://www.ic3.gov/PSA/2025/PSA250605)
- [Microsoft: Storm-0324 phishing through Teams, and the Teams restrictions that followed (12 September 2023)](https://www.microsoft.com/en-us/security/blog/2023/09/12/malware-distributor-storm-0324-facilitates-ransomware-access/)
- [Microsoft: Storm-1811 (Black Basta) uses Teams calls to impersonate help desks, June 2024 update (15 May 2024)](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
- [BleepingComputer: Discord will switch to temporary file links to block malware delivery, with Discord's statement (4 November 2023)](https://www.bleepingcomputer.com/news/security/discord-will-switch-to-temporary-file-links-to-block-malware-delivery/)
- [Cisco Talos: NIK C2, a new AI-enabled framework, a Go implant with an OpenAI client (29 October 2026)](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)
- [Cisco Talos: appraisal by AI, model-driven victim prioritization in the VOLTA infostealer (31 October 2026)](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)

### Headlines

- [CISA advisory AA23-325A: LockBit affiliates exploit Citrix Bleed, CVE-2023-4966 (November 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-325a)
- [CISA advisory AA24-060B: exploitation of Ivanti Connect Secure gateways (February 2024)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060b)
- [CISA: identifying and mitigating living off the land techniques (February 2024)](https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-off-land-techniques)
- [Microsoft: added LSA protection enabled by default on new enterprise-joined Windows 11 22H2 installs](https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection)
- [RFC 9849: TLS Encrypted Client Hello (2026)](https://www.rfc-editor.org/rfc/rfc9849.html)
- [IETF TLS Encrypted Client Hello draft](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/)
- [Anthropic: introducing the Model Context Protocol (25 November 2024)](https://www.anthropic.com/news/model-context-protocol)
