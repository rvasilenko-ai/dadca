# Slide 6 — The original mental model

**Timing:** 6–7 minutes  
**Module:** From malicious programs to adversarial capabilities

## On-slide content
![The original mental model: a malicious executable, executed by a user or the system, produces malicious behavior](../figures/original-model.svg)

Build, one step per click:

0. A malicious executable: a file, written to disk.
1. A user or the system executes it.
2. The malicious behavior occurs, on that host, from that file.

> The suspicious object is persistent, transferable, and available for analysis.

## Talking points

- A useful simplification, not a mistake: when a stable file carries the capability, defenders can intercept, retain, hash, label and share it.
- The model assumes the carrier is always a file, which was nearly true for fifteen years.

## Speaker notes

Present this as a useful simplification, not an ignorant historical mistake. When a stable file carries the capability, defenders can intercept it before execution, retain it, hash it, label it, and share it. Note that the model assumes the carrier of the capability is always a file, which was nearly true for fifteen years; the four periods show the capability outgrowing it.

## Transition

“The familiar malware taxonomy grew around this object-centric model.”

