# Slide 13 — Attacks on the harness

**Timing:** 34–38 minutes  
**Module:** From model to agent

## On-slide content

An agent is a model plus a harness. The model is one component; the harness is the rest — and the larger attack surface.

| Harness component | How it is attacked |
| --- | --- |
| Tools, skills, plugins | A poisoned or hijacked skill; a tool whose description carries injection |
| Retrieval (RAG) | Instructions planted in the documents the agent will fetch |
| Memory and context | Malicious context persisted and replayed later |
| Tool servers (MCP) | A compromised server in the agent's supply chain |
| Credentials and authority | Confused or excessive delegated permissions |

> A perfectly aligned model is still subverted through its tools, its memory, and its context.

## Speaker notes

Make "poisoned skill" concrete: a skill or plugin the agent is given — installed from a marketplace, or a tool definition it loads — that carries hidden instructions or malicious behavior, which the model then invokes in good faith. Tool poisoning: the tool's metadata or output is attacker-controlled and carries injection. Memory poisoning: injected context persists and fires on a later, unrelated request. MCP supply chain: a tool server the agent connects to is malicious or compromised. The through-line from the code/data slide is that every one of these feeds the data channel into the instruction channel. This is why "fix the model" is not enough — the harness is where most real attacks land.

## Transition

“That is the surface. Now the two ways an agent actually turns into an attacker.”
