# Slide 14 — Three scales of security analysis

**Timing:** 55–58 minutes  
**Module:** LLMs as analysts

## On-slide content

```text
10,000,000 events or files    machine-scale filtering
        10,000 cases          triage and correlation
            10 cases          investigation and reverse engineering
```

| Scale | Dominant constraints |
| --- | --- |
| Machine | Throughput, latency, false-positive rate |
| Triage | Ranking, enrichment, correlation |
| Investigation | Evidence, explanation, cost, verification |

## Speaker notes

The numbers are illustrative rather than prescriptive. The purpose is to show orders-of-magnitude reduction before expensive analysis.

LLMs can participate at more than one layer, but long agentic investigations cannot simply be multiplied across every raw event without considering cost, latency, and reliability.

## Transition

“Being capable of producing a verdict does not make a method suitable for every position in this funnel.”

