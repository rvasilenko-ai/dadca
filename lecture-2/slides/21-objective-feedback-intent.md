# Slide 21 — Objective, feedback, and intent

**Timing:** 52–55 minutes  
**Module:** Why the agent succeeded

## On-slide content

Avoid two simplistic claims:

- “The model wanted to attack Hugging Face.”
- “The model cannot distinguish good from bad.”

Prefer:

- Program semantics do not encode organizational authorization.
- The same technical capability can serve offensive or defensive objectives.
- The agent pursued actions that appeared useful to its task and feedback.
- External controls determine which actions are permitted to execute.

## Speaker notes

Models can represent policies, norms, and safety distinctions. That does not guarantee those distinctions control a long-horizon agent, especially in an evaluation configured to measure raw cyber capability.

Keep three layers separate:

1. The task objective
2. The model's learned behavior and safeguards
3. The independent authorization enforced by the environment

## Interaction

Ask which layer should prevent a coding agent from publishing a secret: prompt instruction, model refusal, tool policy, credential scope, or repository control. The intended answer is defense in depth.

## Transition

“The loop succeeded without being efficient or quiet. Its operational advantage was volume.”

## Sources

- [OpenAI incident account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

