# Slide 29 — Who watches the agent: cheap models, in a funnel

**Timing:** 81–83 minutes  
**Module:** Defense and research

## On-slide content

A frontier model on every event is not affordable, and not needed. Match the model to the scale.

```text
 scale          volume per day                     the model that can afford it
 machine        millions of events, flows,         encoder-only classifiers (BERT family):
                tool calls, retrieved texts        fine-tuned on product telemetry; line rate; a label, not a sentence
 triage         thousands of candidates            small language models, 1–8B, trained for the task:
                                                   summarize, correlate, propose a bounded action
 investigation  a few consequential cases          a frontier model — and a human
```

Why encoders at the bottom:

- Cheap and fixed-latency, so they can run inside EDR, NDR and the agent harness at line rate.
- They emit a label, not text, so there is nothing to inject through their output.
- They train on labelled telemetry we already have, and on agent transitions: is this retrieved text imperative? Is this tool call plausible for this task? Is this destination appropriate?

| Tier | Published examples |
| --- | --- |
| Encoder classifiers | LogBERT (log anomaly detection, 2021); SecureBERT (security-domain encoder, 2022); Prompt Guard 2 (86M-parameter injection and jailbreak classifier, 2025) |
| Small language models | Foundation-Sec-8B (a security-specialized 8B model, 2025) as the base for triage and response tasks |
| Frontier model | Investigation of the few cases the funnel selects; labelling data for the tiers below |

> Put the expensive model where the few decisions are and the cheap one where the millions of events are. The funnel is the architecture.

## Speaker notes

This is the economics behind both defense slides. The defender's loop of slide 27 and the monitor M of slide 28 have to run on every transition, and the arithmetic of a frontier model per event does not close. The answer is the funnel the field has always used, with new tiers.

At machine scale, encoder-only transformers: bidirectional models that read a whole input and emit a class. They are cheap, their latency is fixed, and because they do not generate text there is no output channel to inject through. They learn from the labelled telemetry a product already produces, and they can learn the transition checks we listed on slide 26 — imperative text in a retrieval, an implausible tool call for the task, an unexpected destination. LogBERT and SecureBERT show the approach on logs and security text; Prompt Guard 2 is an 86-million-parameter classifier for injected and jailbreak text, small enough to run on every input.

At triage scale, small language models fine-tuned for detection and response tasks: summarize a cluster of events, correlate across sources, propose an action with its evidence. Foundation-Sec-8B is a security-specialized base at that size. At investigation scale, the frontier model and the human — who also label the data that trains the tiers below, which is how the funnel improves.

Say what the funnel does not do: it does not replace the structural guardrails of slide 28, which need no comprehension at all. And it introduces a risk of its own, which is the next slide.

## Transition

“The cheap model is weaker than the agent it watches. That is the problem.”

## Sources

- [Guo, Yuan and Wu, LogBERT: Log Anomaly Detection via BERT (2021)](https://arxiv.org/abs/2103.04475)
- [Aghaei et al., SecureBERT: A Domain-Specific Language Model for Cybersecurity (2022)](https://arxiv.org/abs/2204.02685)
- [Meta, Llama Prompt Guard 2 (86M) model card (2025)](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M)
- [Kassianik et al., Llama-3.1-FoundationAI-SecurityLLM-Base-8B Technical Report (2025)](https://arxiv.org/abs/2504.21039)
