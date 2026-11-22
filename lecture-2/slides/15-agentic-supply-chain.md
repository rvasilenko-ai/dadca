# Slide 15 — The agentic supply chain

**Timing:** 39–41 minutes  
**Module:** From model to agent

## On-slide content

Arrow ④ on the previous slide, as a supply chain. The software one is familiar; the agent adds every input it will later read as instructions.

Traditional focus:

`source -> dependencies -> build -> artifact -> deployment`

Agentic additions:

- Repository instructions and Markdown
- Issues, comments, and retrieved documents
- Agent skills, plugins, and tool descriptions
- Model and policy configuration
- Memory and retrieved context
- Credentials and delegated permissions
- Approval interfaces and generated diffs

## Speaker notes

Prompt injection becomes a supply-chain concern when untrusted content can influence an agent that possesses trusted authority. The risk is not only malicious generated code; it includes tool calls, configuration changes, disclosure, and misleading summaries presented for approval.

Open research problems include instruction provenance, typed trust boundaries, context isolation, least-authority tools, human-review usability, and end-to-end auditability.

## Interaction (optional, only if the room is ahead of time)

Ask students which inputs in their current development workflow are treated as data but could be interpreted as instructions by an agent.

## Transition

“That is the surface. Now the two ways an agent actually turns into an attacker.”

## Sources

- [OWASP, Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [Beurer-Kellner et al., Design Patterns for Securing LLM Agents against Prompt Injections (2025)](https://arxiv.org/abs/2506.08837)
