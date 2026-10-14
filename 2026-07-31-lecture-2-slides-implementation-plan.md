# Lecture 2 Markdown Slides Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a version-trackable Markdown source file for each of the 33 approved Lecture 2 slides, plus an indexed lecture overview.

**Architecture:** Store Lecture 2 in `lecture-2/`, matching Lecture 1's one-file-per-slide convention. Use the July 2026 Hugging Face incident as a narrative spine, Project Ire as a defensive counter-case, and recurring diagrams for the agent loop, trust boundaries, operational scales, and bounded response.

**Tech Stack:** CommonMark/GitHub-flavored Markdown, shell-based structural validation.

## Global Constraints

- Audience: Master's and PhD cybersecurity students without assumed mastery of every concrete concept.
- Duration: exactly 90 minutes across 33 slides.
- Lecture 2 must remain understandable without attending Lecture 1.
- Distinguish disclosed incident facts, source interpretations, and lecture hypotheses.
- Keep exploit mechanics conceptual and omit reproducible payloads, commands, and secrets.
- Explain success as model capability plus harness, tools, feedback, state, access, and delegated authority.
- Treat “the model cannot distinguish good from bad” and “stealth is impossible to train” as overstatements; use precise optimization and evaluation language.
- Distinguish autonomous exploration, AI-assisted human attack, and deliberately stealthy campaigns.
- Explain that reverse-engineering capability does not itself provide fleet-scale detection.
- Frame autonomous response as scoped, authorized, evidence-based, and reversible.
- Use primary sources for the Hugging Face incident, OpenAI account, MITRE mappings, and Project Ire.

---

### Task 1: Create the lecture index and file convention

**Files:**
- Create: `lecture-2/README.md`

**Interfaces:**
- Consumes: `2026-07-31-malware-and-ai-lecture-series-plan.md` and Lecture 1's Markdown conventions.
- Produces: The canonical 33-slide order, module timings, learning outcomes, source-boundary note, and delivery guidance.

- [ ] **Step 1: Write the index**

Include the central question, standalone foundation, learning outcomes, module schedule, ordered links to all 33 slides, primary cases, and delivery constraints.

- [ ] **Step 2: Verify 33 indexed links**

Run `test -s lecture-2/README.md` and confirm exactly 33 numbered Markdown links.

### Task 2: Create the standalone foundation and incident mystery slides

**Files:**
- Create: `lecture-2/slides/01-when-attacker-is-agent.md`
- Create: `lecture-2/slides/02-standalone-foundation.md`
- Create: `lecture-2/slides/03-what-changes-when-reasoning-is-cheap.md`
- Create: `lecture-2/slides/04-incident-in-one-slide.md`
- Create: `lecture-2/slides/05-objective-and-evaluation.md`
- Create: `lecture-2/slides/06-where-is-malware.md`
- Create: `lecture-2/slides/07-trust-boundaries.md`

**Interfaces:**
- Consumes: Lecture 1's operational pipeline and three-scale framework.
- Produces: A standalone vocabulary, the incident mystery, and the trust-boundary diagram used in the reconstruction.

- [ ] **Step 1: Write slides 1–3**

Reintroduce malware-as-capability, ATT&CK, the observation-to-response pipeline, and machine/triage/investigation scales.

- [ ] **Step 2: Write slides 4–7**

State the incident's disclosed scope, explain the narrow evaluation objective, pose the malware-definition questions, and visualize the crossed trust boundaries.

- [ ] **Step 3: Verify structure and source links**

Confirm each slide contains timing, on-slide content, speaker notes, and transition sections; confirm slides 4–7 cite the Hugging Face and OpenAI accounts.

### Task 3: Create the incident reconstruction slides

**Files:**
- Create: `lecture-2/slides/08-evaluation-sandbox-escape.md`
- Create: `lecture-2/slides/09-external-launchpad.md`
- Create: `lecture-2/slides/10-dataset-as-attack-surface.md`
- Create: `lecture-2/slides/11-file-disclosure-without-code.md`
- Create: `lecture-2/slides/12-template-injection-to-execution.md`
- Create: `lecture-2/slides/13-credentials-become-capabilities.md`
- Create: `lecture-2/slides/14-lateral-movement-graph.md`
- Create: `lecture-2/slides/15-source-control-supply-chain.md`
- Create: `lecture-2/slides/16-behavioral-timeline.md`

**Interfaces:**
- Consumes: The incident trust-boundary model.
- Produces: A defensible high-level reconstruction using `objective -> observation -> tool -> action -> feedback -> adaptation`.

- [ ] **Step 1: Write slides 8–12**

Cover the evaluation escape, external launchpad, dataset-processing surface, HDF5 external-storage file disclosure, and template-injection execution without reproducing exploit code.

- [ ] **Step 2: Write slides 13–16**

Cover credential amplification, Kubernetes/cloud/source-control pivots, supply-chain exposure, and a selected ATT&CK-style behavioral timeline.

- [ ] **Step 3: Verify source fidelity and safety**

Confirm each incident claim is sourced and no slide contains shell commands, exploit expressions, live paths, tokens, or code sufficient to reproduce the disclosed vectors.

### Task 4: Create the agent-capability slides

**Files:**
- Create: `lecture-2/slides/17-agent-loop.md`
- Create: `lecture-2/slides/18-code-reasoning.md`
- Create: `lecture-2/slides/19-operational-orchestration.md`
- Create: `lecture-2/slides/20-harness-and-authority.md`
- Create: `lecture-2/slides/21-objective-feedback-intent.md`

**Interfaces:**
- Consumes: The reconstructed incident stages.
- Produces: The model-plus-harness explanation used to analyze noisy offense and defensive agents.

- [ ] **Step 1: Write slides 17–19**

Define the iterative agent loop, code understanding, tool orchestration, error interpretation, and state recovery as coupled capabilities.

- [ ] **Step 2: Write slides 20–21**

Show how access and delegated authority turn reasoning into consequences, and distinguish task optimization from moral or organizational intent.

- [ ] **Step 3: Verify precise language**

Confirm the slides avoid unsupported numerical splits and absolute claims about AI moral understanding.

### Task 5: Create the noisy autonomous offense slides

**Files:**
- Create: `lecture-2/slides/22-seventeen-thousand-actions.md`
- Create: `lecture-2/slides/23-success-hidden-in-noise.md`
- Create: `lecture-2/slides/24-block-adapt-repeat.md`
- Create: `lecture-2/slides/25-three-threat-models.md`

**Interfaces:**
- Consumes: Incident action counts and agent-loop concepts.
- Produces: The machine-speed asymmetry and calibrated stealth hypothesis.

- [ ] **Step 1: Write slides 22–24**

Explain action volume, low-signal correlation, repeated recovery, and why blocking a single channel does not imply containment.

- [ ] **Step 2: Write slide 25**

Contrast autonomous exploration, AI-assisted human operations, and deliberately stealthy campaigns. Explain why transferable stealth is a harder verifier problem while acknowledging that telemetry can provide training signals.

- [ ] **Step 3: Verify numeric claims**

Confirm action and cluster counts match the current Hugging Face technical timeline and are presented as recovered/reconstructed counts.

### Task 6: Create the defensive analysis, future, and synthesis slides

**Files:**
- Create: `lecture-2/slides/26-ai-assisted-defense.md`
- Create: `lecture-2/slides/27-project-ire-workflow.md`
- Create: `lecture-2/slides/28-reverse-engineering-ecosystem.md`
- Create: `lecture-2/slides/29-reverse-engineering-not-detection.md`
- Create: `lecture-2/slides/30-is-agent-malware.md`
- Create: `lecture-2/slides/31-agentic-supply-chain.md`
- Create: `lecture-2/slides/32-bounded-autonomous-response.md`
- Create: `lecture-2/slides/33-research-map-and-close.md`

**Interfaces:**
- Consumes: The incident, operational scales, and model-plus-harness argument.
- Produces: The defensive counter-case, future research agenda, and standalone conclusion.

- [ ] **Step 1: Write slides 26–29**

Cover AI-assisted incident reconstruction, Project Ire's evidence-linked workflow, reverse-engineering tool dependencies, and the scale gap between selected-sample analysis and fleet detection.

- [ ] **Step 2: Write slides 30–32**

Address compromised agents, malicious instructions, expanded supply chains, and response systems constrained by explicit authority, evidence thresholds, scope, reversibility, and escalation.

- [ ] **Step 3: Write slide 33**

Close with a research map spanning observability, tools, prioritization, evaluation, correlation, trust, and response, using the approved machine-speed-defense conclusion.

- [ ] **Step 4: Verify source links and standalone conclusion**

Confirm links to the Hugging Face incident, OpenAI account, and Microsoft Project Ire are present and that Lecture 2 does not require Lecture 1 terminology without redefining it.

### Task 7: Validate and link the complete lecture package

**Files:**
- Verify: `lecture-2/README.md`
- Verify: `lecture-2/slides/*.md`
- Modify: `2026-07-31-malware-and-ai-lecture-series-plan.md`

**Interfaces:**
- Consumes: All generated Lecture 2 sources.
- Produces: A complete, navigable, source-linked 90-minute Lecture 2 package.

- [ ] **Step 1: Validate count, structure, links, and timing**

Confirm 33 slide files and 33 index entries; require headings, timing, on-slide content, speaker notes, and transitions; resolve local links; verify contiguous intervals from 0 through 90 minutes.

- [ ] **Step 2: Validate placeholders, factual boundaries, and safety**

Scan for unfinished placeholders and for code, commands, tokens, or payload expressions copied from the incident report. Confirm factual claims use primary source links and hypotheses are labelled as such.

- [ ] **Step 3: Link Lecture 2 from the series plan**

Add a relative Markdown link to `lecture-2/README.md` under `Detailed lecture sources`.

- [ ] **Step 4: Report repository status**

If the workspace is not a Git repository, report that no worktree, branch, or commit could be created.
