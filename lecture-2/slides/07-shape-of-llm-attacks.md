# Slide 7 — The shape of LLM attacks

**Timing:** 18–20 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

Two ways attacker text enters the instruction channel:

| | Direct | Indirect |
| --- | --- | --- |
| Who speaks to the model | The attacker, directly | The victim's own agent |
| Vector | Jailbreak or override in the prompt | Instructions hidden in data the agent later reads |
| Example surface | A chat the attacker controls | A document, web page, CRM record, email, tool output, skill |
| Software analogy | Local exploitation | Remote exploitation |

> Indirect injection is the agent threat: the trusted agent fetches the attacker's words and follows them.

## Speaker notes

Direct injection: the person prompting the model is the attacker — jailbreaks and overrides to make the model break its own rules. It matters, but it is the smaller case here, because the attacker only controls their own session: they gain no data or authority they did not already have. Indirect injection is the dangerous one: the attacker plants instructions in content that someone else's agent will later read, so a low-privilege attacker makes a high-privilege victim's trusted agent act with the victim's authority. Map it back to the previous slide — indirect injection is the data channel carrying code, triggered remotely. This is exactly the mechanism of the hijacked enterprise agent in Case B.

## Transition

“Software eventually built partial defenses for its code/data problem. Text has none yet.”

## Sources

- [Greshake et al., Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection (2023)](https://arxiv.org/abs/2302.12173)
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)
