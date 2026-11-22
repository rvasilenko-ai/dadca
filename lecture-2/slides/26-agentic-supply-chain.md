# Slide 26 — The agentic supply chain

**Timing:** 74–78 minutes  
**Module:** Defense and research

## On-slide content

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

## Interaction

Ask students which inputs in their current development workflow are treated as data but could be interpreted as instructions by an agent.

## Transition

“If attacks adapt at machine speed, detection alone is insufficient—but unconstrained automated response is also dangerous.”

