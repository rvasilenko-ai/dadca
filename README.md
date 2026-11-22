# Malware and AI: a lecture series

Three related 90-minute lectures on how malware and malicious capabilities evolved, how the pipelines that detect them had to evolve with them, and what changes when the attacker is an agent and the detector is a model. Students may attend any lecture independently.

Hosted at <https://rvasilenko-ai.github.io/malware-and-ai/>.

| Lecture | Title | Audience | Status |
| --- | --- | --- | --- |
| 1 | [From Malware Files to Adversarial Capabilities](lecture-1/README.md) | Undergraduate and Master's | Slides, notes and an interactive deck ([open](https://rvasilenko-ai.github.io/malware-and-ai/lecture-1/deck/)) |
| 2 | [When the Attacker Is an Agent](lecture-2/README.md) | Master's and PhD | [Deck](https://rvasilenko-ai.github.io/malware-and-ai/lecture-2/deck/) · slides and notes in markdown |
| 3 | [Machine Learning for Malware Detection](lecture-3/README.md) | Master's and PhD | Seed: fourteen slides written, six outlined |

The lectures do not assume detailed prior knowledge of PE internals, reverse engineering, MITRE ATT&CK, machine-learning approaches to malware detection, or LLM agent architecture. Lectures 2 and 3 assume general graduate-level cybersecurity knowledge.

## The series' message

> AI changes where human expertise is valuable; it does not eliminate the need for expertise.

The lectures show the gap between an academic prototype and an operational security system. Many operational problems occur before or after model inference: collection, extraction, representation, indexing, prioritization, tool integration, evidence preservation, authorization, and response. Those gaps are where the research and engineering work is.

After the series, students should be able to:

1. Explain why malware is increasingly an operational and behavioral concept, rather than only a category of files.
2. Distinguish an artifact, a software capability, an observed behavior, an operator, and an adversarial objective.
3. Trace the pipeline from real-world activity through sensing, acquisition, extraction, representation, detection, investigation, decision, and response.
4. Explain how failures of visibility or extraction differ from failures of classification.
5. Compare signatures, similarity methods, conventional machine learning, neural representations, and LLM agents by their operational suitability.
6. Explain why reverse-engineering ability does not automatically produce a scalable malware detector.
7. Describe how LLM performance depends on the surrounding harness, tools, representations, feedback, verification, and delegated authority.
8. Identify credible research problems at the boundaries between collection, detection, triage, analysis, and response.

## The recurring operational model

All three lectures use one pipeline:

```text
real-world activity
    -> sensor
    -> acquisition
    -> extraction
    -> representation
    -> detection
    -> investigation
    -> decision
    -> response
```

> A detector cannot reason about evidence that the collection and extraction system never exposes to it.

And three operational scales, as a way to discuss throughput, latency, cost, evidence requirements and expected output rather than as rigid categories:

| Scale | Typical workload | Suitable methods |
| --- | --- | --- |
| Machine | Millions of files, flows, events, or alerts | Rules, signatures, indexes, streaming systems, similarity methods, conventional ML |
| Triage | Thousands of uncertain or enriched cases | Ranking, clustering, correlation, enrichment, selective analysis |
| Investigation | A small number of consequential cases | Sandboxes, reverse engineering, human analysts, tool-using LLM agents |

## Teaching approach

- For each specialized concept: a plain-language definition, one concrete technical example, then the operational limitation or open research problem.
- Techniques are compared by recurring questions rather than catalogued: what evidence does the method require, how is it acquired, what representation does the model receive, what is lost, what are the throughput, latency and cost, how is the result verified, what action can the organization take.
- Each lecture stands alone: Lectures 2 and 3 spend their first minutes reconstructing the shared model, terminology is defined on first use, and each lecture ends with its own conclusion and research questions.
- Offensive mechanics stay conceptual. No slide contains executable payloads, reproducible exploit steps or operational secrets.
- Dates and figures are checked against primary sources, which are listed per slide.

## Repository layout

- `lecture-N/README.md`: the lecture's outline, learning outcomes, module schedule with minutes, slide index and delivery guidance.
- `lecture-N/slides/NN-slug.md`: one file per slide, with on-slide content, talking points, speaker notes, interaction, transition and sources. The markdown is the source of truth.
- `lecture-1/deck/`: the interactive HTML deck generated from the slides; see its [README](lecture-1/deck/README.md) for building, presenting, printing and the slide file format.
- `index.html`: the landing page of the hosted site.

## Reference set

- MITRE ATT&CK: <https://attack.mitre.org/>
- Google Transparency Report, HTTPS encryption on the web: <https://transparencyreport.google.com/https/overview>
- Let's Encrypt statistics (Firefox HTTPS page-load telemetry): <https://letsencrypt.org/stats/>
- CISA advisory AA23-144A (Volt Typhoon, living off the land): <https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a>
- EMBER: <https://arxiv.org/abs/1804.04637>
- SOREL-20M: <https://arxiv.org/abs/2012.07634>
- MalConv, *Malware Detection by Eating a Whole EXE*: <https://arxiv.org/abs/1710.09435>
- *Semantic-aware Binary Code Representation with BERT*: <https://arxiv.org/abs/2106.05478>
- Microsoft Project Ire: <https://www.microsoft.com/en-us/research/project/project-ire/>
- Hugging Face autonomous intrusion technical timeline: <https://huggingface.co/blog/agent-intrusion-technical-timeline>
- OpenAI account of the Hugging Face evaluation incident: <https://openai.com/index/hugging-face-model-evaluation-security-incident/>

## Attribution

The deck uses [reveal.js](https://revealjs.com/) (MIT, vendored under `lecture-1/deck/vendor/`). The schematic ATT&CK matrix uses content from MITRE ATT&CK, © The MITRE Corporation, under the [ATT&CK terms of use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/); ATT&CK is a registered trademark of The MITRE Corporation.
