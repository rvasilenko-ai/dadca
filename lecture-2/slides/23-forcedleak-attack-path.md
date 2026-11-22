# Slide 23 — ForcedLeak: the attack path

**Timing:** 59–62 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

![ForcedLeak attack path across three zones. On the Internet, the attacker submits a public Web-to-Lead form; the concealed instructions persist in the Salesforce CRM record; inside the organization an employee later asks Agentforce about the lead, the agent retrieves the attacker-controlled record, the data is interpreted as instructions, the agent reaches more CRM data with its own authority, and sensitive data leaves through crafted image requests back to the attacker. Red arrows mark the trust boundaries crossed](../figures/forcedleak-path.svg)

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

