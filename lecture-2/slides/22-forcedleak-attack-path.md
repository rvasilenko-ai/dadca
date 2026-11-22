# Slide 22 — ForcedLeak: the attack path

**Timing:** 58–61 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

![ForcedLeak attack path, step by step: an attacker submits a public Web-to-Lead form; concealed instructions persist in the CRM record; an employee later asks Agentforce about the lead; the agent retrieves the attacker-controlled record; the data is interpreted as instructions; the agent reaches more CRM data with its authority; sensitive data leaves through crafted image requests](../figures/forcedleak-path.svg)

The employee’s request is legitimate.  
The agent’s identity is legitimate.  
The resulting behavior serves the attacker.

## Speaker notes

Walk through the sequence slowly. The prompt injection is indirect and time-delayed: the person who activates it may be performing an ordinary business task long after the attacker submitted the record.

According to the disclosure, execution occurred in the context of the agent’s running user or the organizational user interacting with it. The demonstrated exfiltration path used image requests and a trusted-domain weakness. Salesforce later enforced Trusted URL allowlists as a defense-in-depth control.

Keep the technical focus on trust boundaries: external data crossed into model context, became operational instruction, inherited legitimate authority, and reached an egress channel.

## Transition

“Nothing here was malicious when considered only as a binary. Where, then, did the payload live?”

## Sources

- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)

