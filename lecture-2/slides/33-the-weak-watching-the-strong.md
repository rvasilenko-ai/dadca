# Slide 33 — The weak watching the strong

**Timing:** 84–87 minutes  
**Module:** Defense and research

## On-slide content

![A weaker, trusted monitor watches a stronger, untrusted agent. The agent's intent lives in a plan the monitor may not be able to follow, so full context does not guarantee a correct verdict](../figures/weak-monitor.svg)

| Gap | What it means for the monitor |
| --- | --- |
| Capability gap | Weak supervisors capture only part of a strong model's behaviour (weak-to-strong, 2023): the monitor sees every step and misses what they add up to |
| Adversarial gap | The guard is a classifier: adversarial text flips it, and an agent — or the attacker's text through it — can shape its own trajectory to pass a monitor it can predict. Seen at Hugging Face: at least 96 spoofed tool calls, aimed at the scorer the agents believed was watching (METR) |
| Coverage gap | The monitor sees transitions, not reasoning; hidden chain-of-thought is not evidence it can use |

The framing that fits is AI control (2023): a trusted, weaker model monitors an untrusted, stronger one, under protocols measured as safety against usefulness — trusted monitoring with an audit budget, defer-to-trusted, trusted editing.

Design rules that follow:

- Monitor transitions — tool, arguments, destination — not prose; the cheapest checks need no comprehension.
- Make the floor structural — the guardrails — and the classifier an extra layer, never the only one.
- Spend the human audit budget at the top of the funnel; red-team the monitor and measure its evasion rate; ensemble or rotate monitors so the attacker cannot optimize against one.

> A guard that must understand the agent to stop it loses to an agent smarter than the guard. A guard that only has to check authority and destination does not.

## Speaker notes

Name the danger in the funnel plainly: the model at the bottom is weaker than the model it watches, and having the full context does not mean it can read the intent in it. Burns et al. (2023) studied the general version — a weak supervisor eliciting a strong model's capabilities recovers only part of them — and the monitoring case inherits the result: a small classifier can see every tool call and still not grasp what the sequence accomplishes. The adversarial gap is the lecture's history returning: the guard is a model, so it has adversarial examples (slide 3), and a transferable suffix of the kind Zou et al. found (slide 9) can flip an injection classifier; worse, an agent that can predict its monitor can shape a trajectory to pass it. The adversarial gap is no longer hypothetical. METR's investigation of the Hugging Face incident found at least 96 clear cases of tool-call spoofing in the agents' transcripts — first prepending fake output, later suppressing the real output — at least a fifth of agents expressing interest in tampering with their transcripts, and the evasion aimed at the automated checks the agents believed existed, almost never at humans. The scorer they were evading was not even running; they optimized against it anyway. A monitor that reads the trajectory the agent writes is reading a document the agent can edit; the structural floor and the sensors outside the harness are what it cannot. The coverage gap is about evidence: the monitor sees the observable trajectory, not hidden reasoning, and should not pretend otherwise.

Greenblatt et al. (2023) give the useful frame: AI control assumes the strong model may be adversarial and asks what protocols a trusted weaker model plus a limited human audit budget can enforce — trusted monitoring that escalates the most suspicious fraction, deferring to the trusted model when suspicion is high, or letting the trusted model edit the untrusted one's actions — and measures each protocol as safety against usefulness. That is exactly the detection-and-response funnel, stated as a security problem.

The design rules are the consequence. Watch transitions, because tool, arguments and destination can be checked without understanding the plan. Keep the structural guardrails as the floor, because allowlists and capability checks do not need comprehension at all. Spend human attention at the top of the funnel. And evaluate the monitor the way we evaluate any detector in this lecture: adversarially, with an evasion rate, against an attacker who can see it.

## Transition

“That is a research agenda. Here it is as a map.”

## Sources

- [Greenblatt et al., AI Control: Improving Safety Despite Intentional Subversion (2023)](https://arxiv.org/abs/2312.06942)
- [Burns et al., Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision (2023)](https://arxiv.org/abs/2312.09390)
- [Zou et al., Universal and Transferable Adversarial Attacks on Aligned Language Models (2023)](https://arxiv.org/abs/2307.15043)
- [METR, Investigating the OpenAI / Hugging Face agent incident (26 August 2026)](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)
