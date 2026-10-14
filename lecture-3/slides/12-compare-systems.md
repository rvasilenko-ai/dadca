# Slide 12 — Compare systems, not leaderboards

**Timing:** 41–45 minutes  
**Module:** Representations of executable files

## On-slide content

| Approach | Typical scale | Extraction cost | Primary role | Common blind spot |
| --- | --- | --- | --- | --- |
| Hash/signature | Very high | Low | Known-threat matching | Novel variation |
| Engineered ML | High | Low–medium | Classification/ranking | Feature and dataset shift |
| Similarity search | High | Low–medium | Retrieval/clustering | No inherent verdict |
| Raw-byte model | Medium | Low parser dependence | File classification | Weak explicit structure |
| Code representation | Lower | High | Semantic comparison/analysis | Extraction errors |
| LLM investigation | Low | Very high | Explanation and evidence gathering | Scale and verification |

## Speaker notes

The table is deliberately qualitative and workload-dependent. Production systems combine methods in a cascade. The appropriate question is “What role does this method play under our evidence and resource constraints?”

## Transition

“Every row of this table receives a file. What happens when the attack never delivers one?”

