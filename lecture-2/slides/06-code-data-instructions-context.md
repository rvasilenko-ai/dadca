# Slide 6 — Code and data, instructions and context

**Timing:** 14–18 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

| Classic software | Large language model |
| --- | --- |
| Code and data share one memory; both are bytes | Instructions and context share one window; both are text |
| Exploit: attacker **data** is executed as **code** | Exploit: attacker **text** is obeyed as **instruction** |
| Buffer overflow, SQL / command injection, XSS | Prompt injection, jailbreak, tool and skill poisoning |
| Root cause: no trust boundary in a shared channel | Root cause: no trust boundary in a shared channel |

> The oldest bug class — confusing data for code — reappears one layer up, in text.

## Speaker notes

This is the organizing idea of the lecture. In a von Neumann machine, code and data are both bytes in the same memory, and every classic exploit works by getting attacker-supplied data interpreted as instructions. A language model has no architectural separation between the developer's instructions and the untrusted context it reads — user input, a retrieved document, a tool result — all of it is one text stream that it interprets by meaning. So prompt injection is code/data confusion, reborn.

Be precise, because students will push on it: this is an analogy, not an identity. There is no instruction pointer; the "execution" is statistical interpretation, not a jump to an address. But the shape is the same, and so is the difficulty of fixing it. Keep this parallel visible; it reappears at the harness and at Case B.

## Transition

“If the channel is ambiguous, the attack arrives in two forms.”
