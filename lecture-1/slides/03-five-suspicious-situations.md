# Slide 3 — Five suspicious situations

**Timing:** 2–4 minutes
**Module:** Where is the malware?

## On-slide content
> Where does malware stop?

Five situations, ordered by distance from the file. Which of them is malware?

![A ladder of five situations, from the file at the top to no file at the bottom: a trojan executable written to disk; PowerShell downloading and running code; a Portable Executable image that exists only in process memory; an attacker controlling a legitimate remote-management tool; repository instructions that make a coding agent exfiltrate secrets](../figures/ladder.svg)

Build, one step per click:

0. A trojan executable is written to disk — the file.
1. PowerShell downloads and runs code — a command, and whatever it fetches.
2. A Portable Executable image exists only in process memory — bytes that were never a file on disk.
3. An attacker controls a legitimate remote-management tool — a session under the wrong control.
4. Repository instructions cause a coding agent to exfiltrate secrets — an instruction in data; no file at all.

## Talking points

- Read the five rungs aloud, then one show of hands: the last rung you would still call malware.
- Expect clusters at the top and the bottom and hesitation at rung 3; do not resolve it.
- One student from each end: what decided it? Usually "there is a file" against "someone is doing harm".
- Hold the disagreement; Part 1 ends by naming what it was about.

## Speaker notes

One show of hands, not five. Read the five rungs aloud, then ask the room to raise a hand at the last rung they would still call malware, and count down from five. Expect a spread: a cluster at 1 or 2, a cluster at 4 or 5, hesitation at 3. Do not resolve it. The purpose is to make visible that students are classifying different things, an artifact, a behavior, who is in control, or an outcome, and Part 1 spends its time earning the vocabulary for that.

Pick one student from the top of the ladder and one from the bottom and ask what decided it, two sentences each. The answers are usually "there is a file" and "someone is doing harm", which are two of the four questions slide 18 names when it closes the vote.

## Interaction

The show of hands and the two students. In a large room, ask for hands at rung 2 and at rung 4 only; the gap between them is the lecture.

## Transition

“Hold on to that disagreement; it comes back at the end of Part 1. First, the route.”
