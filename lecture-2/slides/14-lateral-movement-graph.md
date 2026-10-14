# Slide 14 — Lateral movement as a capability graph

**Timing:** 33–36 minutes  
**Module:** Reconstruct the attack

## On-slide content

```text
worker code execution
   ├─> service-account API access
   ├─> cloud metadata and node identity
   ├─> privileged workload creation
   ├─> cluster secrets
   ├─> corporate mesh enrollment
   └─> internal access broker
           └─> additional clusters and services
```

For every edge, ask:

- What authority enabled it?
- What control should have denied it?
- What telemetry could correlate it?

## Speaker notes

Avoid teaching Kubernetes mechanics in depth. The structural lesson is that workload identity, cloud identity, cluster permissions, network identity, and application credentials formed a connected graph.

Least privilege, short-lived credentials, workload isolation, metadata restrictions, admission controls, and origin-aware authentication each remove or weaken graph edges.

## Transition

“One of the most consequential graph edges reached the software-development supply chain.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

