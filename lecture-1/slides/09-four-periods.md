# Slide 9 — Four periods, 2000–2026

**Timing:** 12–14 minutes
**Module:** From malicious programs to adversarial capabilities

## On-slide content

```text
2000–2009   the file era                              an executable, mass-mailed to victims over an unencrypted network connection
2010–2016   APT, exploit kits, files of every kind    still a file, no longer only an executable; the sandbox peaks
2017–2022   the access economy                        identities, tokens and trusted vendors; EDR mainstream, then attacked
2023–2026   hands-on hacking, edge devices, agents      intrusion by hand through help desks, sessions and edge devices; then agents
```

Five tracks per period: motive and money, attackers, operating system, internet, security products. A few anchor events are labelled; every dot has a date on hover.

> In each period the attacker moved the capability to where the current sensor was not looking, and the money moved with it.

## Speaker notes

Two minutes, and the purpose is the shape, not the content. Point at the five lanes and name them, starting with motive and money because it explains the other four. Then read the four period names left to right and say one sentence per period from the cards. Do not read the labelled dots; they are anchors some students will recognise (Windows XP, Storm, Stuxnet, CryptoLocker, NotPetya, SolarWinds, Volt Typhoon) and they are there so the zoomed slides that follow have a reference.

Say explicitly that the next four slides zoom into one period each: the same five lanes, the period's own key events labelled, and one claim per track. The recap after the four periods returns to this timeline and draws the breaks on it.

The periods are the periods of the attacker's dominant tradecraft, not of famous incidents, and the boundaries are soft by a year or two. 2010 opens with Aurora and Stuxnet; 2017 opens with the Shadow Brokers leak and the ransomware economy it fed; 2023 opens with the Volt Typhoon advisory and the casino intrusions, campaigns with no malware file at all. Say "no file", not "no malware": by this lecture's definition the hands-on intrusion, the built-in tools and the exploits are the malicious capability, so the malware is still there and only its carrier is gone.

## Transition

“Zoom into the first period.”

## Sources

### Anchor events on the timeline

- [Gartner, Anton Chuvakin: Named: Endpoint Threat Detection & Response (July 2013)](https://blogs.gartner.com/anton-chuvakin/2013/07/26/named-endpoint-threat-detection-response/)
- [Microsoft: PowerShell security features (AMSI and script block logging, Windows 10, 2015)](https://learn.microsoft.com/en-us/powershell/scripting/security/security-features)
- [NIST SP 800-207: Zero Trust Architecture (August 2020)](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA Emergency Directive 21-01: mitigate SolarWinds Orion code compromise (December 2020)](https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise)
- [CISA advisory AA23-144A: PRC state-sponsored cyber actor living off the land (Volt Typhoon, May 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a)
- [Microsoft Research: Project Ire (August 2025)](https://www.microsoft.com/en-us/research/project/project-ire/)

### 2000–2009

- [Mark Russinovich: Sony, rootkits and digital rights management gone too far (October 2005)](https://techcommunity.microsoft.com/t5/windows-blog-archive/sony-rootkits-and-digital-rights-management-gone-too-far/ba-p/723442)
- [Microsoft: Windows XP SP2 firewall enabled by default (2004)](https://learn.microsoft.com/en-us/previous-versions/bb877964%28v=technet.10%29)
- [Microsoft: An introduction to Kernel Patch Protection (x64, 2005)](https://learn.microsoft.com/en-us/archive/blogs/windowsvistasecurity/an-introduction-to-kernel-patch-protection)
- [Conficker Working Group: lessons learned](https://www.confickerworkinggroup.org/)

### 2010–2016

- [Mandiant: APT1, exposing one of China's cyber espionage units (February 2013)](https://www.mandiant.com/resources/reports/apt1-exposing-one-of-chinas-cyber-espionage-units)
- [Lockheed Martin: Intelligence-driven computer network defense, the kill chain paper (2011)](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)
- [Google Security Blog: HTTPS encryption on the web (October 2016)](https://security.googleblog.com/2016/10/https-encryption-on-web.html)

### 2017–2022

- [CISA alert TA17-132A: indicators associated with WannaCry ransomware (May 2017)](https://www.cisa.gov/news-events/alerts/2017/05/12/indicators-associated-wannacry-ransomware)
- [White House statement attributing NotPetya to the Russian military (February 2018)](https://trumpwhitehouse.archives.gov/briefings-statements/statement-press-secretary-25/)
- [Microsoft: macros from the internet blocked by default in Office (2022)](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked)
- [Microsoft: vulnerable and malicious driver protections (December 2021)](https://www.microsoft.com/en-us/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)
- [FBI Internet Crime Complaint Center annual reports](https://www.ic3.gov/AnnualReport/Reports)
- [RFC 8446: TLS 1.3 (August 2018)](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 8484: DNS Queries over HTTPS (October 2018)](https://www.rfc-editor.org/rfc/rfc8484)

### 2023–2026

- [CISA: identifying and mitigating living off the land techniques (February 2024)](https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-off-land-techniques)
- [RFC 9849: TLS Encrypted Client Hello (2026)](https://www.rfc-editor.org/rfc/rfc9849.html)
- [Noma Security: ForcedLeak (September 2025)](https://noma.security/noma-labs/forcedleak/)
- [Hugging Face: technical timeline of the July 2026 incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)
