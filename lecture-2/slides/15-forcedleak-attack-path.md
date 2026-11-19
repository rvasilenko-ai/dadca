# Slide 15 — ForcedLeak: the attack path

**Timing:** 48–52 minutes  
**Module:** Case B: a compromised trusted model

## On-slide content

```text
attacker submits Web-to-Lead form
  -> concealed instructions persist in CRM record
  -> employee later asks Agentforce about the lead
  -> agent retrieves attacker-controlled record
  -> data is interpreted as instructions
  -> agent accesses additional CRM information
  -> sensitive data leaves through crafted image requests
```

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

