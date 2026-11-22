# Slide 32 — Both cases: cheap models, in a funnel

**Timing:** 82–84 minutes  
**Module:** Defense and research

## On-slide content

Different telemetry, the same volume problem: far more events than people can read, none decisive alone. Match the model to the scale.

![Match the model to the scale, for both cases. Two inputs — Case A's endpoint, identity and flow events, and Case B's agent transitions — feed one funnel: encoder-only classifiers at machine scale, small task-trained language models at triage, a frontier model and a human for the few investigations](../figures/funnel.svg)

Build, one step per click:

0. Two inputs, one problem. Case A: endpoint, identity and flow events from the sensors we have. Case B: the agent's own transitions — retrievals, tool calls, arguments, destinations. Millions of events either way, meaningful only together.
1. Machine scale: encoder-only classifiers — LogBERT (2021), SecureBERT (2022), Prompt Guard 2 (86M, 2025). Cheap, fixed latency, so they run at line rate inside EDR, NDR and the harness; a label, not text, so nothing to inject through; trained on the telemetry and transitions we already label.
2. Triage scale: small language models, 1–8B, trained for the task — summarize a cluster of events, correlate across sources, propose an action with its evidence. Foundation-Sec-8B (2025) is a security-specialized base at that size.
3. Investigation scale: a frontier model and a human, for the few cases the funnel selects — who also label the data that trains the tiers below, which is how the funnel improves.

> The expensive model where the few decisions are, the cheap one where the millions of events are — in both cases.

## Speaker notes

This is the economics behind both defense slides, and it is the same for both cases even though the telemetry is not. In Case A the stream is the sensors' — endpoint, identity, flow — and slide 29 showed why it has to be evaluated continuously: the attack is a pattern across thousands of individually ordinary events. In Case B the stream is the agent's own transitions — what it retrieved, what it called, with which arguments, to which destination — and the monitor M of slide 31 has to see every one of them. Either way, the arithmetic of a frontier model per event does not close. The answer is the funnel the field has always used, with new tiers.

At machine scale, encoder-only transformers: bidirectional models that read a whole input and emit a class. They are cheap, their latency is fixed, and because they do not generate text there is no output channel to inject through. They learn from the labelled telemetry a product already produces, and they can learn the transition checks we listed on slide 31 — imperative text in a retrieval, an implausible tool call for the task, an unexpected destination. LogBERT and SecureBERT show the approach on logs and security text; Prompt Guard 2 is an 86-million-parameter classifier for injected and jailbreak text, small enough to run on every input.

At triage scale, small language models fine-tuned for detection and response tasks: summarize a cluster of events, correlate across sources, propose an action with its evidence. Foundation-Sec-8B is a security-specialized base at that size. At investigation scale, the frontier model and the human — who also label the data that trains the tiers below, which is how the funnel improves.

Say what the funnel does not do: it does not replace the structural guardrails of slide 31, which need no comprehension at all. And it introduces a risk of its own, which is the next slide.

## Transition

“The cheap model is weaker than the agent it watches. That is the problem.”

## Sources

- [Guo, Yuan and Wu, LogBERT: Log Anomaly Detection via BERT (2021)](https://arxiv.org/abs/2103.04475)
- [Aghaei et al., SecureBERT: A Domain-Specific Language Model for Cybersecurity (2022)](https://arxiv.org/abs/2204.02685)
- [Meta, Llama Prompt Guard 2 (86M) model card (2025)](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M)
- [Kassianik et al., Llama-3.1-FoundationAI-SecurityLLM-Base-8B Technical Report (2025)](https://arxiv.org/abs/2504.21039)
