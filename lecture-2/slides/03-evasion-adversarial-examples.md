# Slide 3 — Evasion: change the input, keep the model

**Timing:** 5–8 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

```text
 input x ──────────────────────────> MODEL ──> "panda"   58%
    |
    + δ      a perturbation too small to see, chosen from the model's gradient
    v
 x' = x + δ ───────────────────────> MODEL ──> "gibbon"  99%

 the attacker never touches the model; it stays correct on everything else
```

Build, one step per click:

0. A trained model, correct on an ordinary input.
1. The attacker asks the model's gradient which pixels push the decision over the line, and moves each one a little.
2. To a human the image is unchanged. The model is confidently wrong.
3. Without the gradient: train a substitute on the model's answers; the perturbation transfers.
4. In security, "small" means something else: the sample must still work — the spam must still sell, the PDF must still exploit.

| Attacker knows | How the attack is built |
| --- | --- |
| The model (white box) | Follow the gradient, one step or many |
| Only its answers (black box) | Build a substitute model; adversarial examples transfer |

> The decision boundary is not where the designer thinks it is. Every common model class has such inputs.

## Speaker notes

Szegedy and colleagues found adversarial examples in 2013: imperceptible perturbations that flip a deep network's prediction, and that transfer between models trained on different data. Goodfellow, Shlens and Szegedy explained them in 2014 — the network behaves too linearly in high dimensions — and gave the one-step fast gradient sign method; their figure is the panda read as a gibbon with 99% confidence. Papernot and colleagues showed in 2016 that a black-box attacker can train a substitute from the model's labels and transfer the attack. Biggio and colleagues had already run the security version in 2013: gradient-descent evasion of a PDF malware detector.

Two ideas to hold. First, the attacker exploits a gap between the function the model learned and the function the designer believes it learned. Second, in security the constraint is not imperceptibility but functionality: the evading sample has to remain a working attack. That constraint is what makes malware evasion harder than image evasion, and it returns on slide 7.

## Transition

“That was the attacker touching the input. The other way in is the training data.”

## Sources

- [Szegedy et al., Intriguing properties of neural networks (2013)](https://arxiv.org/abs/1312.6199)
- [Goodfellow et al., Explaining and Harnessing Adversarial Examples (2014)](https://arxiv.org/abs/1412.6572)
- [Biggio et al., Evasion Attacks against Machine Learning at Test Time, ECML PKDD (2013)](https://arxiv.org/abs/1708.06131)
- [Papernot et al., Practical Black-Box Attacks against Machine Learning (2016)](https://arxiv.org/abs/1602.02697)
