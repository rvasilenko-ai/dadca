# Slide 11 — File disclosure without code execution

**Timing:** 26–28 minutes  
**Module:** Reconstruct the attack

## On-slide content

### Vector 1: format-driven local file disclosure

```text
maliciously crafted data container
  -> external-storage feature references a worker-local file
  -> production worker reads the file
  -> file content appears in processed dataset output
  -> attacker retrieves output through the normal API
```

What was exposed:

- Environment data and credentials
- Worker implementation details

## Speaker notes

Hugging Face reports that an HDF5 external-storage feature was abused so the worker read local content as dataset data. No attacker-supplied code needed to execute for this first vector.

This matters pedagogically: focusing exclusively on code execution can miss powerful capability. A file read can reveal credentials and implementation details that enable the next stage.

## Transition

“The leaked source then helped reveal how the pipeline could be made to execute code.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

