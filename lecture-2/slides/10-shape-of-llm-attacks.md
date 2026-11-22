# Slide 10 — The shape of LLM attacks

**Timing:** 25–28 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

Two ways attacker text enters the instruction channel:

| | Direct | Indirect |
| --- | --- | --- |
| Who speaks to the model | The attacker, directly | No one directly: the surrounding system feeds the model the attacker's text |
| Vector | An override typed into the application's own input | Instructions hidden in data the model later reads |
| Example surface | A chat the attacker controls | A document, web page, CRM record, email, tool output: anything the model is wired to read |
| Software analogy | Local exploitation | Remote exploitation |

> Indirect injection is the dangerous one: the attacker never talks to the model. The system around the model feeds it their words — and that system is where we go, after one more comparison with software.

## Speaker notes

Direct injection: the person prompting the model is the attacker, typing an override into the application's own input — the 2022 translation demonstration. Keep it apart from a jailbreak: direct injection attacks the application's prompt, a jailbreak attacks the model's training, even though in both the attacker is the user, and one session may do both. Direct injection matters, but it is the smaller case here, because the attacker only controls their own session: they gain no data or authority they did not already have. Indirect injection is the dangerous one: the attacker plants instructions in content that a system will later retrieve and feed to the model on someone else's behalf, so a low-privilege attacker makes a high-privilege victim's own model-driven system act with the victim's authority. Map it back to the previous slide — indirect injection is the data channel carrying code, triggered remotely. We have not yet named that system around the model; slides 12 to 14 do, and Case B is it being hijacked.

## Transition

“Software eventually built partial defenses for its code/data problem. Text has none yet.”

## Sources

- [Greshake et al., Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection (2023)](https://arxiv.org/abs/2302.12173)
- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)
