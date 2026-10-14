# Slide 13 — 2023–2026: hands-on hacking, edge devices, and agents

**Timing:** 26–30 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content

| Track | Headline |
| --- | --- |
| **Motive and money** | Data theft without encryption; session tokens as the product; agent attacks have no business model yet. |
| **Attackers** | Hands-on hacking via help desks and stolen sessions; exploited edge devices; instructions for agents. |
| **Operating system** | The host hardens by default: driver blocklist, LSA protection, passkeys; most workloads now run on Linux. |
| **Internet** | Encrypted Client Hello hides the last plaintext field; AI assistants sit between the user and the data. |
| **Security products** | Identity threat detection, baselining for living off the land, LLM triage; agent observability begins. |

> A whole campaign can run without a malware file. The newest executable is an instruction in data, and the sensor has to follow it into identity and into the agent's context.

### Detail

Behind the details button; the speaker notes pick from it.

| Track | 2023–2026 |
| --- | --- |
| **Motive and money** | Extortion without encryption (mass data theft, Cl0p and MOVEit 2023). Help-desk social engineering against high-value targets. Session tokens and SaaS data as the product. State prepositioning for disruption. AI lowers the cost of lures. Agent attacks have no settled business model yet. |
| **Attackers** | Living off the land as the whole campaign (Volt Typhoon advisory, 2023). Help-desk social engineering, SIM swaps and MFA bypass (Scattered Spider). Session cookie and token theft via infostealers. Exploitation of edge devices (Citrix, Ivanti, Fortinet, 2023–24). ClickFix: the user pastes the command. AI-assisted lures. Instructions in data that hijack enterprise agents; autonomous agents as operators (2025–26). |
| **Operating system** | Windows 11: vulnerable-driver blocklist on by default (2022); LSA protection on by default for new enterprise-joined installs; virtualization-based security on by default; Smart App Control (2022). Passkeys (2023). Hardened mobile and macOS. Most workloads on Linux in the cloud. |
| **Internet** | Encrypted Client Hello: in browsers since 2023, standardized in 2026, server-side adoption still narrow. AI assistants in browsers, IDEs and SaaS; tool-using agents and agent protocols (2024–26). SaaS-to-SaaS integrations and OAuth sprawl. Data lives behind APIs. |
| **Security products** | Identity threat detection and response. EDR tamper protection and kernel attack-surface reduction. Baselining for living-off-the-land detection. LLM triage in the SOC; agentic malware analysis (Project Ire, 2025). Guardrails, prompt-injection defenses, agent observability. |

## Speaker notes

The timeline is zoomed to this period: the labelled dots are the key events, the small dots are the rest and show their date on hover. Say the five headlines, then tell two or three of the labelled events as one story. The detail chips are behind the details button, which swaps the timeline out for them; they are for questions, not for reading aloud.

**The product is now identity and data, not the host.** Cl0p's mass exploitation of MOVEit in 2023 skipped encryption entirely and extorted on stolen data alone. Scattered Spider chose casinos and large enterprises because the payout justified live social engineering of a help desk. Infostealer markets sell session tokens because a token opens the SaaS tenant where the data lives. Volt Typhoon is the reminder that one class of adversary is not paid at all and is prepositioning for disruption. For the agent cases the business model is not yet observed; Lecture 2 treats grab-and-go theft and campaign staging as projections, not as a reported economy.

**What is new, and what is not.** Fileless tradecraft is not new here; the previous period made it standard. The period's additions are three: hands-on intrusion through people and sessions rather than payloads, edge devices as the entry point, and agents as a new actor. Say the "no malware file" part precisely, because the lecture's own definition is at stake: the malicious capability is still there, in hands-on intrusion, built-in tools, exploits and stolen sessions; what is gone is the file that used to carry it. The 2023 Volt Typhoon advisory described a state actor persisting in critical infrastructure using only built-in tools and valid accounts, which prompted dedicated living-off-the-land guidance in 2024. Scattered Spider reached large enterprises the same year through help-desk calls and MFA resets, with SIM swapping among its wider techniques. Infostealers sold session cookies that skipped authentication altogether. Edge devices, which run no EDR, became the preferred entry. In each case the host-based sensor had little to see, because the attacker used the organization's own tools under the organization's own identities.

**The user runs the payload.** ClickFix lures ask the user to paste a command into a Run dialog or terminal, turning the person into the loader. There is no attachment to scan and the process ancestry looks like the user.

**The operating-system row has largely won the host.** Driver blocklists, LSA protection on enterprise devices, virtualization-based security and passkeys close most of the previous period's paths by default. That success is part of why the attacker moved to identity, edge devices and people.

**The new executable.** When a coding agent reads a repository file, or a CRM agent reads a lead record, and acts on an instruction embedded in it, no classical sensor has anything to classify. The telemetry that matters is the context the agent assembled, the tools it called and the identity it acted under. Autonomous agents operating as attackers add persistence and volume on the other side. Lecture 2 covers both cases in depth; here they are only the latest point on the curve.

**Security products are following again.** Identity threat detection, agent observability, guardrails and prompt-injection defenses are the sensor moving into the identity provider and the agent harness. Agentic analysis systems such as Project Ire are the same reasoning capability applied on the defensive side; Lecture 3 covers that.

## Transition

“Put the four periods back on one list: what broke the file-centric model, and when.”

## Sources

- [CISA: People's Republic of China state-sponsored cyber actor living off the land (Volt Typhoon), May 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a)
- [CISA: Identifying and mitigating living off the land techniques (February 2024)](https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-off-land-techniques)
- [IETF TLS Encrypted Client Hello draft](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/)
- [Microsoft Project Ire](https://www.microsoft.com/en-us/research/project/project-ire/)
- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
- [Hugging Face: technical timeline of the July 2026 incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)
