# Slide 21 — Case B: The trusted enterprise agent

**Timing:** 55–58 minutes  
**Module:** Case B: a trusted agent hijacked

## On-slide content

Salesforce Agentforce — **ForcedLeak** (disclosed 2025)

- A legitimate agent operates inside the organization
- It can retrieve CRM data and act with organizational authority
- An external attacker cannot invoke those privileges directly
- No malicious agent or executable needs to enter the environment

Question to hold:

> How can an attacker make the trusted agent use its authority for them?

## Speaker notes

Introduce this as a second mystery. Do not yet reveal the conceptual distinction from the Hugging Face case.

ForcedLeak was a real vulnerability chain demonstrated against a production enterprise-agent product and subsequently mitigated. It was not a publicly confirmed customer compromise. Use “disclosed and demonstrated attack path,” not “observed breach.”

The important initial facts are that the agent is benign, organizationally deployed, and useful precisely because it can access business data on behalf of users.

## Transition

“The attacker begins with an ordinary public business interface—not with credentials or code execution.”

## Sources

- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)

