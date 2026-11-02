# Slide 20 — One word, several questions

**Timing:** 46–48 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

| Axis | Question |
| --- | --- |
| Artifact | What is it? What representation exists? |
| Capability | What can it do? |
| Control | Who controls it, or authorizes its actions? |
| Objective | Whose objective does it serve? |
| Observability | What can the defender see of any of this? |

> One word, “malware”, collapses four properties and one operational question.

## Speaker notes

Return to the vote from the start of the lecture. The disagreement came from answering different questions with the same word. A malware analyst classifies an object: the artifact. An incident responder cares about behavior: the capability. A platform engineer cares about identity, authority and trust boundaries: control. A legal definition requires intent: objective. And every defender is limited by the fifth row, what the system can actually observe.

These five words are the working vocabulary for the rest of the lecture, and Part 1 already used four of them without naming them. The history showed which property carried the malicious meaning in each period: the artifact in the file era, objective once the adversary became a campaign, control once access, tokens and vendor channels were the target, and control and objective together once a program acts under delegated authority. The ATT&CK module showed two cases where the artifact is legitimate and unchanged and only control and objective differ. The conclusions return to the vote in one sentence.

The fifth row is the one this part is about. Every slide from here to the exercise asks what a sensor could see of the other four, and the history of detection products is the history of that row.

Do not belabor the table. It is a legend for everything that follows, not a theory.

## Transition

“Each row needs different evidence, and describing a behavior does not mean our systems can observe it. Here is what has to happen before any detector sees anything.”
