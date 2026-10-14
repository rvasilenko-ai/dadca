# Slide 17 — Software is not behavior

**Timing:** 36–38 minutes  
**Module:** ATT&CK as a language for behavior

## On-slide content

| Software or service | Example procedure | Behavioral description |
| --- | --- | --- |
| Malware implant | Starts a command interpreter | Command execution |
| PowerShell | Retrieves and evaluates content | Scripting and payload transfer |
| Legitimate scheduler | Starts a payload at login | Scheduled execution |
| Remote-management tool | Provides an attacker-controlled session | Remote access |

> Same tool, different procedures. Same technique, different tools.

## Speaker notes

Software entries in ATT&CK may be categorized as malware or tools and are connected to techniques through documented procedures. Emphasize that defenders usually detect some combination of tool identity, behavior, context, and sequence.

The next slide takes the two sharpest cases, a remote-management tool and a vulnerable signed driver, where the artifact is not only legitimate but unchanged.

## Transition

“Two cases where the software is not just legitimate but byte-for-byte unchanged.”

