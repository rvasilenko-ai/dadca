# Slide 5 — Model extraction: copy the model through its API

**Timing:** 11–13 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

```text
 attacker ──── x1, x2, ... xn  (chosen inputs) ────────> prediction API ──> victim MODEL f
 attacker <─── f(x1) ... f(xn), with confidence scores ──┘
     |
     v   train on the (x, f(x)) pairs
 substitute f' ≈ f    -> evade it offline, probe it for private data, resell it
```

Build, one step per click:

0. A model behind a pay-per-query API. Its parameters are the secret.
1. The attacker sends chosen inputs and keeps every answer.
2. Confidence scores leak far more than labels: hundreds to a few thousand queries recovered logistic regressions, decision trees and small networks with near-perfect fidelity.
3. With a copy in hand, every white-box attack can be prepared offline, where the defender sees nothing.

> Everything the model says out loud is a channel. The API is the trust boundary, and it was never designed as one.

## Speaker notes

Tramèr and colleagues in 2016 extracted models from commercial machine-learning-as-a-service APIs — BigML and Amazon — using the fact that those APIs return confidence values and accept partial inputs. For simple model classes the attack is equation solving; for others it is retraining on the victim's labels. The precursor is Lowd and Meek in 2005, who reverse-engineered linear spam classifiers with membership queries.

Why it matters for detection: a stolen copy of a detector lets the attacker test evasions offline, without the query volume that might alert the defender. The malware evasion on slide 7 assumed black-box access to the detector; extraction removes even that constraint. There is also the plain commercial loss: a model is expensive to train and free to copy once it answers questions.

## Transition

“The model's parameters are one secret. Its training data is another.”

## Sources

- [Tramèr et al., Stealing Machine Learning Models via Prediction APIs, USENIX Security (2016)](https://arxiv.org/abs/1609.02943)
- [Lowd and Meek, Adversarial learning, KDD (2005)](https://doi.org/10.1145/1081870.1081950)
