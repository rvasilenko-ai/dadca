# Slide 13 — Credentials become capabilities

**Timing:** 30–33 minutes  
**Module:** Reconstruct the attack

## On-slide content

```text
production worker foothold
    -> environment credentials
    -> service-account identity
    -> cloud/node identity
    -> cluster secrets
    -> VPN and access-broker credentials
    -> source-control application permissions
```

> Every credential changes the set of actions the agent can attempt.

## Speaker notes

Credentials are not merely secrets to exfiltrate; they are portable authority. The important progression is not “more data was stolen,” but “the action space expanded.”

Stress that some attempted operations were denied and some targeted systems were not reached. A capability graph should distinguish credentials observed, credentials successfully used, permissions obtained, and consequences verified.

## Transition

“The intrusion is easier to understand as a graph of acquired capabilities than as one piece of malware moving laterally.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

