# Slide 24 — ForcedLeak: what it adds up to

**Timing:** 62–64 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

![ForcedLeak as a sum: attacker-controlled data, plus a trusted agent (model and harness), plus organizational identity and tools, plus a permitted outbound channel, equals attacker-desired capability. Below, three readings of the same incident: the CRM record contains the payload; the agent is a compromised deputy; the agent has operationally become part of the malware](../figures/equation.svg)

Dormant instructions, live authority: the text is inert while stored and becomes consequential only when a trusted agent retrieves it and has the authority to act. No malicious file exists at any point.

## Speaker notes

The malicious text is passive while stored. It becomes consequential only when retrieved into an agent context that confuses data with instructions and possesses enough authority to act.

This is why malware is better defined by capability than by file. There may be no malicious software artifact to classify. Instead, a legitimate execution system is temporarily redirected toward an attacker objective.

Avoid insisting on one label. Ask what each label helps defenders observe, prevent, or regulate.

Cut cue: if running slow, fold this slide into slide 23 — the equation becomes the closing line of the attack path.

## Transition

“ForcedLeak needed no file. The second way into Case B ends with a very familiar one.”

## Sources

- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)

