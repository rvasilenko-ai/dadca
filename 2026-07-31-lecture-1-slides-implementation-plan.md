# Lecture 1 Markdown Slides Implementation Plan

> **Superseded on 2026-10-11.** Lecture 1 was restructured to 29 slides (an ATT&CK introduction was added at 15 on 2026-10-13; three scales moved to Lecture 3 on 2026-10-13; the network lineage was split into cause and effect on 2026-10-13; the return-to-opening-examples, seven-reasons and memory-only slides were cut on 2026-10-13; including new about-me and route slides at 2 and 4, part dividers at 5 and 19, an overview timeline at 9 added 2026-10-13, the five-questions slide moved to 20 on 2026-10-13, and an options-at-each-stage slide at 22; the detectors-are-representations preview was cut on 2026-10-11 and its table moved to Lecture 3 slide 13) for an undergraduate and Master's audience; slides 15, 18 and 21–31 of this plan moved to Lecture 3, new slides 7–10, 17, 19, 20, and 24 were added, the old slide 7 became slide 11, the old slide 8 was merged into the four-axis slide (12), and the old slides 10 and 17 were merged into their neighbours. The current structure is in `lecture-1/README.md` and the design record is `docs/superpowers/specs/2026-10-11-lecture-1-split-and-defensive-evolution.md`. The file conventions and validation checks below still apply.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a version-trackable Markdown source file for each of the 33 approved Lecture 1 slides, plus an indexed lecture overview.

**Architecture:** Store Lecture 1 in `lecture-1/`, with `README.md` defining the narrative, timing, and ordered slide index and `slides/NN-slug.md` holding one slide each. Every slide file has consistent metadata followed by visible content, speaker notes, interaction guidance when applicable, a transition, and sources when the slide makes source-dependent claims.

**Tech Stack:** CommonMark/GitHub-flavored Markdown, shell-based structural validation.

## Global Constraints

- Audience: Master's and PhD cybersecurity students without assumed mastery of every concrete concept.
- Duration: exactly 90 minutes across 33 slides.
- Lecture 1 must remain independently understandable.
- Preserve the historical-progression and operational-pipeline structure.
- Use both legitimate remote-control software and BYOVD to distinguish intended-capability abuse from vulnerability exploitation.
- State that CLR/JIT behavior makes executable memory alone a low-specificity signal.
- Use one fileless PowerShell scenario across ATT&CK mapping, visibility, encrypted traffic, and diagnostic exercises.
- Distinguish visibility, distinguishability, classification, investigation, and response.
- Do not present newer ML techniques as automatic replacements for older methods.
- Do not include executable offensive payloads or operational exploitation instructions.

---

### Task 1: Create the lecture index and file convention

**Files:**
- Create: `lecture-1/README.md`

**Interfaces:**
- Consumes: The approved 33-slide Lecture 1 outline in the conversation and `2026-07-31-malware-and-ai-lecture-series-plan.md`.
- Produces: The canonical slide order, module timings, file naming convention, learning outcomes, and recurring scenario used by all slide files.

- [ ] **Step 1: Create the directory index**

Write the lecture title, central question, intended outcomes, 90-minute module schedule, ordered links to all 33 slide files, delivery guidance, and the complete recurring PowerShell scenario.

- [ ] **Step 2: Verify index completeness**

Run:

```bash
test -s lecture-1/README.md
test "$(rg -c '^1\. \[|^[0-9]+\. \[' lecture-1/README.md)" -eq 33
```

Expected: exit code 0.

### Task 2: Create the opening and historical-definition slides

**Files:**
- Create: `lecture-1/slides/01-malware-and-ai.md`
- Create: `lecture-1/slides/02-five-suspicious-situations.md`
- Create: `lecture-1/slides/03-one-word-several-questions.md`
- Create: `lecture-1/slides/04-original-mental-model.md`
- Create: `lecture-1/slides/05-classical-taxonomy.md`
- Create: `lecture-1/slides/06-files-as-unit-of-detection.md`
- Create: `lecture-1/slides/07-file-centric-model-breaks.md`
- Create: `lecture-1/slides/08-legitimate-software-adversarial-outcome.md`
- Create: `lecture-1/slides/09-four-axis-model.md`

**Interfaces:**
- Consumes: The audience definition and recurring scenarios from `lecture-1/README.md`.
- Produces: The artifact/capability/control/objective model used by all later sections.

- [ ] **Step 1: Write slides 1–3**

Include the opening poll, five situations, and the five diagnostic questions without resolving the malware definition prematurely.

- [ ] **Step 2: Write slides 4–7**

Explain the original file-centric model, classical taxonomy, operational reasons files became the detection unit, and the emergence of scripts, memory execution, living-off-the-land behavior, and identity/cloud abuse.

- [ ] **Step 3: Write slide 8**

Compare legitimate remote-control software with BYOVD. Explicitly contrast intended capability under unauthorized control with a legitimate signed artifact whose vulnerability is exploited.

- [ ] **Step 4: Write slide 9**

Define artifact, capability, control, objective, and defender observability as the lecture's working analytical model.

- [ ] **Step 5: Verify slide structure**

Run:

```bash
for f in lecture-1/slides/{01..09}-*.md; do
  test -s "$f"
  rg -q '^\*\*Timing:\*\*' "$f"
  rg -q '^## Speaker notes' "$f"
  rg -q '^## Transition' "$f"
done
```

Expected: exit code 0.

### Task 3: Create the ATT&CK slides

**Files:**
- Create: `lecture-1/slides/10-from-names-to-behaviors.md`
- Create: `lecture-1/slides/11-attack-levels.md`
- Create: `lecture-1/slides/12-software-is-not-behavior.md`
- Create: `lecture-1/slides/13-map-fileless-attack.md`

**Interfaces:**
- Consumes: The four-axis model and recurring PowerShell scenario.
- Produces: The tactic/technique/sub-technique/procedure vocabulary reused in the visibility section.

- [ ] **Step 1: Write slides 10–12**

Explain why behavior is more operationally useful than family names, define ATT&CK levels, and distinguish software identity from observed procedures.

- [ ] **Step 2: Write slide 13**

Use the stolen-administrator/inline-PowerShell/position-independent-shellcode scenario. Ask students to map artifacts, tools, behaviors, procedures, objective, and relevant sensors.

- [ ] **Step 3: Verify slide structure**

Run the Task 2 structural loop for files `10` through `13` and confirm slide 13 contains `position-independent` and `no malicious executable`.

Expected: exit code 0.

### Task 4: Create the observability and extraction slides

**Files:**
- Create: `lecture-1/slides/14-complete-detection-pipeline.md`
- Create: `lecture-1/slides/15-invisible-dataset-preparation.md`
- Create: `lecture-1/slides/16-memory-only-not-invisible.md`
- Create: `lecture-1/slides/17-encrypted-network-traffic.md`
- Create: `lecture-1/slides/18-extraction-changes-evidence.md`
- Create: `lecture-1/slides/19-seven-reasons-for-a-miss.md`
- Create: `lecture-1/slides/20-diagnostic-exercise.md`

**Interfaces:**
- Consumes: The PowerShell scenario and ATT&CK vocabulary.
- Produces: The activity-to-response pipeline and failure taxonomy used to compare ML representations.

- [ ] **Step 1: Write slides 14–15**

Define every pipeline stage and contrast operational collection work with a preconstructed academic dataset.

- [ ] **Step 2: Write slide 16**

Explain that memory-only execution may be observable, but executable private memory is not inherently malicious because legitimate CLR/JIT execution also generates native code in memory. Include `visibility != distinguishability != verdict`.

- [ ] **Step 3: Write slides 17–18**

Separate what TLS hides from remaining metadata and endpoint evidence, then show how every extraction representation both exposes and discards information.

- [ ] **Step 4: Write slides 19–20**

Define seven distinct causes of a missed attack and ask students to diagnose three cases by pipeline stage rather than defaulting to classifier retraining.

- [ ] **Step 5: Verify slide structure and required concepts**

Run the structural loop for files `14` through `20`, then run:

```bash
rg -q 'visibility.*distinguishability.*verdict' lecture-1/slides/16-memory-only-not-invisible.md
rg -q 'JIT' lecture-1/slides/16-memory-only-not-invisible.md
rg -q 'TLS' lecture-1/slides/17-encrypted-network-traffic.md
```

Expected: exit code 0.

### Task 5: Create the malware-ML representation slides

**Files:**
- Create: `lecture-1/slides/21-representation-ladder.md`
- Create: `lecture-1/slides/22-signatures-are-representations.md`
- Create: `lecture-1/slides/23-engineered-pe-features.md`
- Create: `lecture-1/slides/24-ember-and-sorel.md`
- Create: `lecture-1/slides/25-similarity-not-classification.md`
- Create: `lecture-1/slides/26-malconv-raw-bytes.md`
- Create: `lecture-1/slides/27-bert-code-representations.md`
- Create: `lecture-1/slides/28-compare-systems.md`

**Interfaces:**
- Consumes: The extraction/representation pipeline and failure taxonomy.
- Produces: A common operational comparison across signatures, conventional ML, similarity methods, raw-byte models, code models, and LLM investigation.

- [ ] **Step 1: Write slides 21–23**

Introduce the representation ladder, explain signatures as expert-selected invariants, and give a minimal PE explanation with representative engineered features.

- [ ] **Step 2: Write slides 24–25**

Explain the contributions and limitations of EMBER and SOREL-20M, then distinguish maliciousness classification from similarity retrieval and clustering with a conceptual MinHash/LSH explanation.

- [ ] **Step 3: Write slides 26–27**

Explain MalConv's raw-byte representation and BERT-like representations over instructions/functions/decompiler output, including the assumptions and extraction dependencies of each.

- [ ] **Step 4: Write slide 28**

Compare approaches qualitatively by throughput, extraction cost, interpretability, purpose, and primary blind spot. State that workload determines the appropriate combination.

- [ ] **Step 5: Verify slide structure and source links**

Run the structural loop for files `21` through `28`, then confirm links to the EMBER, SOREL-20M, MalConv, and DeepSemantic primary papers are present.

Expected: exit code 0.

### Task 6: Create the LLM placement and synthesis slides

**Files:**
- Create: `lecture-1/slides/29-three-scales.md`
- Create: `lecture-1/slides/30-capability-not-suitability.md`
- Create: `lecture-1/slides/31-selecting-investigations.md`
- Create: `lecture-1/slides/32-return-to-opening-examples.md`
- Create: `lecture-1/slides/33-five-conclusions.md`

**Interfaces:**
- Consumes: All earlier concepts.
- Produces: The standalone Lecture 1 conclusion and explicit bridge to Lecture 2.

- [ ] **Step 1: Write slides 29–31**

Define machine, triage, and investigation scales; distinguish LLM capability from operational suitability; and frame selective reverse engineering as a ranking and expected-information problem.

- [ ] **Step 2: Write slides 32–33**

Return to all five opening situations, resolve them using the four-axis and pipeline models, summarize five conclusions, and close with three research prompts.

- [ ] **Step 3: Verify slide structure**

Run the structural loop for files `29` through `33` and confirm slide 33 contains the approved closing statement about evidence never observed or destroyed during representation.

Expected: exit code 0.

### Task 7: Validate the complete lecture package

**Files:**
- Verify: `lecture-1/README.md`
- Verify: `lecture-1/slides/*.md`
- Modify: `2026-07-31-malware-and-ai-lecture-series-plan.md`

**Interfaces:**
- Consumes: All generated Markdown sources.
- Produces: A structurally complete, navigable, 90-minute Lecture 1 source package linked from the series plan.

- [ ] **Step 1: Check file count and required sections**

Run:

```bash
test "$(find lecture-1/slides -maxdepth 1 -type f -name '*.md' | wc -l)" -eq 33
for f in lecture-1/slides/*.md; do
  rg -q '^# Slide [0-9]+ — ' "$f"
  rg -q '^\*\*Timing:\*\*' "$f"
  rg -q '^## On-slide content' "$f"
  rg -q '^## Speaker notes' "$f"
  rg -q '^## Transition' "$f"
done
```

Expected: exit code 0.

- [ ] **Step 2: Check total timing and index links**

Manually confirm that slide intervals are contiguous from minute 0 through minute 90. Resolve every Markdown link in `lecture-1/README.md` to an existing slide file.

- [ ] **Step 3: Check for placeholders and unsafe content**

Run:

```bash
! rg -n 'TBD|TODO|FIXME|PLACEHOLDER' lecture-1
! rg -n 'Invoke-Shellcode|VirtualAlloc\(|CreateThread\(|FromBase64String\(' lecture-1
```

Expected: exit code 0.

- [ ] **Step 4: Link the generated lecture from the series plan**

Add a `Detailed lecture sources` section to `2026-07-31-malware-and-ai-lecture-series-plan.md` linking to `lecture-1/README.md`.

- [ ] **Step 5: Report repository status**

Run `git status --short` only if the workspace has become a Git repository. Otherwise report that the Markdown files were created without a commit.
