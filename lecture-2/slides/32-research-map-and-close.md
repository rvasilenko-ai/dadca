# Slide 32 — A map of work still to be done

**Timing:** 87–90 minutes  
**Module:** Defense and research

## On-slide content

| Layer | Open research questions |
| --- | --- |
| Observability | Which agent, identity, tool, and kernel events must be linked? |
| Representation | How do we preserve provenance and uncertainty across tools? |
| Prioritization | Which events and artifacts deserve expensive reasoning? |
| Evaluation | How do we evaluate an agent's capability, stealth, and containment — ours and the attacker's? |
| Trust | How should instructions, identities, and delegated authority be scoped? |
| Response | How can action be timely, bounded, reversible, and auditable? |
| Monitoring | How weak can a monitor be and still catch a stronger agent — and how do we measure its evasion rate? |

> If offense can repeatedly explore until one path works, defense must do more than generate alerts: it must correlate, decide, and contain at comparable speed.

## Speaker notes

Return to the incident and ask:

- Which control could have observed the first meaningful boundary crossing?
- Which control could have prevented capability amplification?
- What evidence justified containment?
- How would defenders know that blocking one path actually stopped the campaign?

End optimistically: capable models create new systems problems and make new defensive workflows possible. They increase the need for expertise in sensors, extraction, tooling, evaluation, trust architecture, and safe response.

## Interaction

Ask each student to choose one row as a potential thesis or research direction and formulate one measurable research question.

## Transition

End of the lecture.

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [OpenAI incident account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [Noma Security: ForcedLeak](https://noma.security/noma-labs/forcedleak/)
- [Varonis Threat Labs: SearchLeak](https://www.varonis.com/blog/searchleak)
- [Greenblatt et al., AI Control: Improving Safety Despite Intentional Subversion (2023)](https://arxiv.org/abs/2312.06942)
