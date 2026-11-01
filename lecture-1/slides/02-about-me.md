# Slide 2 — About me

**Timing:** 1–2 minutes  
**Module:** Where is the malware?

## On-slide content

# Roman Vasilenko

Principal Engineer, Cisco Talos

| Years | Where | What |
| --- | --- | --- |
| 2007–2012 | Doctor Web, then Kaspersky Lab | Virus analyst, then detection research: unpacking, polymorphic viruses, new and reputation-based detection algorithms |
| 2012–2020 | Lastline | Built the anti-malware sandbox (full-system emulation plus hypervisor) and the machine-learning and binary-similarity detection pipeline |
| 2020–2023 | VMware, after it acquired Lastline | Detection and threat-hunting pipelines for NSX Advanced Threat Prevention and NDR |
| 2023–2025 | Google Cloud, Mandiant Security Validation | Attack simulation engine: does the control actually detect? |
| 2025– | Cisco Talos | Applying current AI to threat detection and prevention |

Publications: SCRUTINIZER (code reuse in malware via decompilation and machine learning), DEEPCAPA (malicious capabilities in Windows malware). Five patents in threat and malware detection technology.  
ITMO University, Information Security, 2005–2011. Taught "Introduction to Malware Research" at Saint Petersburg State University, 2011–2012.

## Speaker notes

One minute. The table is the lecture's own periods read as a career, and that is the only point to make. The 2007–2012 row is the executable era from inside two antivirus engines: unpacking, polymorphic viruses, and the reputation-based detection that server-side polymorphism forced on the industry (slide 10). The Lastline row is the sandbox era from inside the sandbox: the product this lecture says peaked around 2016 and was starved by 2020 (slides 11 and 24). The VMware row is the network side of the same story, NDR built for a world where payload inspection had stopped working (slide 26). The Mandiant row is assume-breach made into a product: simulate the attack and check whether the control sees it. The Talos row is Lectures 2 and 3.

Say explicitly that the claims about what worked and what stopped working are a practitioner's claims, and that students should weigh them with that in mind, in both directions.

Do not read the publications line; it is there for students who want to look them up.

## Transition

“Now classify five situations before we agree on any terminology.”
