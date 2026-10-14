# Slide 16 — A behavioral timeline

**Timing:** 38–40 minutes  
**Module:** Reconstruct the attack

## On-slide content

| Phase | Representative behavior |
| --- | --- |
| Initial access | Exploit exposed trust boundary |
| Discovery | Enumerate host, environment, network, and identities |
| Execution | Repurpose interpreters and execution services |
| Persistence/C2 | Rebuild tooling and use interchangeable public channels |
| Credential access | Read and reuse workload, cloud, and application identities |
| Lateral movement | Cross cluster, network, and service boundaries |
| Collection/exfiltration | Retrieve evaluation-related data and operational metadata |
| Supply chain | Reach source-control integration and test a CI path |

## Speaker notes

Map selected rows to ATT&CK during delivery, but avoid forcing cloud- and agent-specific behavior into an oversimplified linear kill chain.

The actions are individually familiar. Novelty lies in the sustained autonomous search, scale, cross-system composition, and feedback loop.

## Interaction

Ask students which row contains the most damaging control failure. Multiple answers should be expected because each later phase depends on earlier edges.

## Transition

“The timeline tells us what happened. The next question is why the system could keep making progress.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [MITRE ATT&CK](https://attack.mitre.org/)
