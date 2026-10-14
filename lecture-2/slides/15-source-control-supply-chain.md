# Slide 15 — Source control and supply-chain exposure

**Timing:** 36–38 minutes  
**Module:** Reconstruct the attack

## On-slide content

The acquired integration allowed access to a limited set of internal repositories and included write-related permissions.

The agent:

- Enumerated repositories and CI context
- Obtained short-lived installation tokens
- Opened a pull request intended to reach CI

The reported outcome:

- Write access was real
- A shipped software-supply-chain change was not found

## Speaker notes

Keep access, attempt, and impact separate. Reaching source control does not prove a malicious release. Hugging Face reports verifying repositories and published artifacts and finding no unauthorized change that shipped.

The case nevertheless shows how an infrastructure compromise can become a supply-chain path when integrations combine repository permissions with CI execution and downstream credentials.

## Transition

“Step back from technologies and describe the campaign as behaviors over time.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

