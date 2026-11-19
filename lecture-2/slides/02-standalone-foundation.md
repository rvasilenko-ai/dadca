# Slide 2 — Two definitions this lecture relies on

**Timing:** 1–5 minutes  
**Module:** Foundation

## On-slide content

### Malware is a capability, not a file

Three lenses on the same incident:

| Lens | It asks | In this lecture, usually |
| --- | --- | --- |
| Artifact | Is there a malicious file? | No |
| Control | Whose instructions is the system following? | The attacker's |
| Capability | What can the attacker now make happen? | Whatever the system is allowed to do |

> A legitimate program under unauthorized control, serving an attacker's objective, is malware by the second and third lens — even when no malicious file exists.

### Detection is a chain, and every link can fail

```text
sensing -> extraction -> representation -> detection
        -> investigation -> decision -> response
```

What is never sensed is never detected. Observability is the first link.

## Speaker notes

Define each lens in one sentence, assuming nothing from before.

- Artifact: the file scanner's question, and what most people mean by "malware." It is the lens this lecture will keep failing to satisfy.
- Control: who directs execution. A trusted program following an attacker's instructions is under attacker control, whatever its hash says.
- Capability: what the attacker can now do that they could not before. This is the question an incident responder actually needs answered.

Say plainly that most of this lecture has no malicious file to point at, so the control and capability lenses do the work; the table returns near the end, applied to a compromised agent.

The chain: name the stages once. The point for this lecture is twofold. Failures before classification — nothing sensed, or the wrong representation — are invisible to the classifier, and the research map at the close is organized by these same stages.

## Transition

“The second foundation is scale: not every security problem can afford the same kind of reasoning.”
