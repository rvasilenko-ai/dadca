# Slide 25 — Defense depends on who controls the agent

**Timing:** 67–70 minutes  
**Module:** The two cases compared

## On-slide content

| | Attacker-operated agent | Hijacked enterprise agent |
| --- | --- | --- |
| Location | Outside the organization | Inside the trusted workflow |
| Authority | Obtained or stolen credentials | Legitimate delegated identity |
| Defender sees | Network, identity, host, and application effects | Potentially context, retrievals, tool calls, results, and effects |
| Guardrails | Not available to defender | Available at context, tool, identity, and egress boundaries |
| Core problem | Detect and contain adaptive behavior | Prevent trusted authority from following untrusted intent |

> Case A: defend against the consequences of someone else’s agent.  
> Case B: prevent our agent from becoming the attacker’s execution environment.

## Speaker notes

Use “reasoning trajectory for the agent” for the observable sequence of context, intermediate decisions, tool selection, tool results, revisions, and actions. Do not equate this with access to hidden chain-of-thought.

Visibility is deployment-dependent. A SaaS customer may not see every internal step, but the system owner can potentially capture much more than a defender observing an external attacker’s model.

Small models can economically inspect structured transitions: whether retrieved data contains imperative instructions, whether selected data and tools are necessary for the user’s request, and whether an outbound destination is appropriate. They are one control in a defense-in-depth system, not a guarantee.

Mention SearchLeak briefly as corroborating evidence: Microsoft 365 Copilot Enterprise could be induced through a crafted link to search data available to the victim and exfiltrate results. The specific mechanics differed, but the repeated pattern was attacker input plus trusted agent authority plus an egress path.

## Transition

“This comparison changes how we answer the apparently simple question: is a compromised agent malware?”

## Sources

- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
- [Varonis Threat Labs: SearchLeak](https://www.varonis.com/blog/searchleak)

