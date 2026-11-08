# Slide 27 — Five conclusions

**Timing:** 75–80 minutes  
**Module:** Synthesis

## On-slide content

1. The capability stopped depending on the file because file defenses worked and the money moved; the file stayed as one carrier among several.
2. Software identity is not the same as adversary behavior.
3. Detection begins with visibility and extraction.
4. Every product observes one unit of evidence; when the evidence moves, the product keeps catching what stayed and misses what moved, and a new layer is added.
5. A detection is not an outcome: investigation, decision and response are stages too, and half of the misses were there.

> Better reasoning cannot recover evidence that was never observed or was destroyed during representation.

## Talking points

- Recall the close of the vote in one sentence.
- Five conclusions: the capability outgrew the file and the file stayed; software identity is not behavior; detection begins with visibility; one unit of evidence per product; a detection is not an outcome.
- Better reasoning cannot recover evidence never observed; Lecture 3 opens with the prioritization that follows.
- End by asking the room what the next sensor will have to see.

## Speaker notes

Recall the close of the vote from slide 18 in one sentence before the conclusions: all five situations were malicious capability in use; they differed in the artifact, in who controlled it and whose objective it served, and in which sensor could see it, which is why the room disagreed and why the lecture spent its time on evidence rather than on a definition.

Conclusion 5 is Part 2's own: cases D to F were misses with every sensor working and every alert right. The bridge to Lecture 3 is the callout: an LLM agent that can explain one selected sample, call a decompiler or a sandbox and write an evidence-linked report answers "can it analyze this?", not "can the system find it among millions of objects?", and it repairs none of the sensing or acquisition failures of Part 2. Choosing which ten artifacts deserve thirty minutes each is a research problem in its own right, and Lecture 3 opens with it.

End optimistically. More capable AI does not erase the need for security expertise; it exposes new research work in sensing, extraction, representations, scalable filtering, prioritization, verification, and response.

One pattern worth naming on the way out, because it recurs: offensive capability keeps diffusing from the few to the many, and the defender meets the commoditized version at scale. A leaked state exploit did it in 2017; frontier AI is doing it now, more slowly and more broadly. That is where Lecture 2 begins.

Preview the other two lectures without requiring them. Lecture 3 covers the detectors themselves: signatures, engineered features, similarity, raw-byte and code models, and the LLM as analyst. Lecture 2 examines what happens when the same reasoning capability receives tools, feedback, persistence, and authority in an adversarial environment.

## Transition

End of Lecture 1. Open the discussion with the callout, not with “Any questions?”: ask the room what the next sensor will have to see.
