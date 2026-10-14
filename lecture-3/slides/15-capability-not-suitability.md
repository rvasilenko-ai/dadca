# Slide 15 — Capability does not imply suitability

**Timing:** 58–62 minutes  
**Module:** LLMs as analysts

## On-slide content

An LLM agent may be able to:

- Explain a suspicious function
- Invoke a decompiler or sandbox
- Form and test hypotheses
- Produce an evidence-linked report

Operational questions:

- At what cost and latency?
- With what recall and consistency?
- How is the result verified?
- Which artifacts receive this treatment?

## Speaker notes

Separate two research questions:

1. Can an LLM reverse engineer and explain a selected sample?
2. Can an operational system find the important sample among millions of objects or events?

The first does not solve acquisition, fleet-wide detection, prioritization, or response. The LLM also depends on tools that transform binary state into text, graphs, and structured evidence.

## Transition

“Before the selection policy, look at what the investigator actually does with a selected sample.”

