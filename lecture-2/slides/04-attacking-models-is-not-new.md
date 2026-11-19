# Slide 4 — Attacking the model is not new

**Timing:** 8–11 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

Adversarial machine learning predates LLMs by a decade.

| Attack | What it does | First shown |
| --- | --- | --- |
| Adversarial examples | A tiny input perturbation flips the prediction | 2013–2014 |
| Evasion | Craft a sample that is misclassified at test time | 2013 onward |
| Data poisoning | Corrupt training data to plant a blind spot or backdoor | long-standing |
| Model extraction | Query a model enough to clone it | ~2016 |
| Membership inference / inversion | Recover whether, or what, data was used in training | 2015–2017 |

> The model was always manipulable — through its inputs and through its training data.

## Speaker notes

One point: attacks on learned models are old. Szegedy and colleagues showed adversarial examples for neural networks in 2013; Goodfellow and colleagues explained and weaponized them in 2014, the panda-to-gibbon image. These are attacks on the model's statistics, not on the software around it. The pattern to hold: a model learns a function from data, and both the function's inputs and its training data can be adversarially shaped. Keep this brief; it establishes that LLMs inherit a long problem rather than inventing one.

## Transition

“These attacks hit image and malware classifiers first — including the machine-learning malware detectors we turn to next.”

## Sources

- [Szegedy et al., Intriguing properties of neural networks (2013)](https://arxiv.org/abs/1312.6199)
- [Goodfellow et al., Explaining and Harnessing Adversarial Examples (2014)](https://arxiv.org/abs/1412.6572)
