# Slide 8 — EMBER and SOREL-20M

**Timing:** 21–26 minutes  
**Module:** Representations of executable files

## On-slide content

| Dataset | Main contribution |
| --- | --- |
| EMBER | Large public benchmark of extracted PE features |
| SOREL-20M | Much larger scale, metadata, labels, tags, and baseline models |

Operational questions:

- Where do labels come from?
- What benign software is represented?
- Does the test set occur later in time?
- What changes between collection and deployment?

## Speaker notes

EMBER made a large, reproducible static-PE benchmark available with extraction code and baselines. Its initial baseline gradient-boosted model outperformed the compared MalConv result, demonstrating that domain features and simple models can remain highly competitive.

SOREL-20M increased scale substantially and included malware-related tags and metadata. Scale does not remove label noise, temporal drift, benign-data availability problems, or mismatch between extracted files and real endpoint events.

## Transition

“A malicious-versus-benign verdict is only one useful question we can ask about a sample.”

## Sources

- [EMBER paper](https://arxiv.org/abs/1804.04637)
- [SOREL-20M paper](https://arxiv.org/abs/2012.07634)
- [EMBER repository](https://github.com/elastic/ember)
- [SOREL-20M repository](https://github.com/sophos/SOREL-20M)

