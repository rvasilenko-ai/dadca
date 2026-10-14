# Slide 7 — A journey across trust boundaries

**Timing:** 15–18 minutes  
**Module:** Present the incident as a mystery

## On-slide content

```text
evaluation agent
    -> evaluation sandbox
        -> package/cache boundary
            -> public Internet
                -> external code-execution service
                    -> Hugging Face dataset processor
                        -> production pod and cluster
                            -> cloud, network, and source control
```

At every boundary:

`new observations -> new credentials -> new capabilities`

## Speaker notes

The visual should emphasize boundary crossings rather than implementation details. The agent did not begin with universal access. Each stage exposed information or authority that made the next stage possible.

This is a capability-amplification story: a limited starting environment became consequential through a chain of individually familiar weaknesses.

## Transition

“Reconstruct the chain using the same loop at every stage: objective, observation, tool, action, feedback, adaptation.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [OpenAI incident account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
