# Slide 2 — Attacking the model is not new

**Timing:** 2–5 minutes  
**Module:** From adversarial ML to attacks on LLMs

## On-slide content

Adversarial machine learning predates LLMs by almost two decades. Every stage of a learned model has been attacked.

```text
 training data ───────> TRAINING ───────> MODEL ───────> predictions
       ^                                    ^                 |
       |                                    |                 v
  POISONING, BACKDOORS                  EVASION         EXTRACTION
  corrupt what it learns          perturb the input      copy the model from its answers
  2008 -> 2017                    2004 -> 2014           2005 -> 2016
                                                        INFERENCE, INVERSION
                                                         learn the training data from its answers
                                                         2014 -> 2017
```

Build, one step per click:

0. A learned model is a pipeline: data in, training, a model, predictions out.
1. Poison the data, and the model learns a blind spot or a backdoor.
2. Perturb the input, and the model answers wrong at test time.
3. Read enough predictions, and you can copy the model.
4. Read them differently, and you learn what it was trained on.

> The model was always manipulable — through its data, its inputs, and its outputs.

## Speaker notes

One point: attacks on learned models are old, and they were born in security. The first evasion attacks were against statistical spam filters: Dalvi and colleagues in 2004, Lowd and Meek in 2005, adding "good words" to spam until the filter passed it. Barreno and colleagues wrote the taxonomy in 2006 — attacks on the training data versus attacks on the inputs — and it still organizes the field. Then the dates on the diagram: a spam filter poisoned in 2008, adversarial examples for deep networks in 2013 and 2014, faces inverted from a classifier in 2015, models stolen through their APIs in 2016, membership inference and the first backdoored networks in 2017. The next four slides take the four arrows one at a time, with one schematic each; then we bring it to malware detection.

The diagram's organizing idea: where in the pipeline the attacker stands. Poisoning needs a hand in the training data. Evasion needs only the input. Extraction and inference need nothing but the model's answers.

Cut cue: if running long, the two "learn a secret" attacks (slides 5 and 6) can be covered from this map in one sentence each. Evasion and poisoning (slides 3 and 4) cannot be cut; the rest of the lecture leans on them.

## Transition

“Take them one at a time, starting where it started: the input.”

## Sources

- [Dalvi et al., Adversarial classification, KDD (2004)](https://doi.org/10.1145/1014052.1014066)
- [Lowd and Meek, Adversarial learning, KDD (2005)](https://doi.org/10.1145/1081870.1081950)
- [Barreno et al., Can machine learning be secure?, ASIACCS (2006)](https://doi.org/10.1145/1128817.1128824)
- [Huang et al., Adversarial machine learning, AISec (2011)](https://doi.org/10.1145/2046684.2046692)
