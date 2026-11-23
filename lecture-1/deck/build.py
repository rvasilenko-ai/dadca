#!/usr/bin/env python3
"""Build lecture-1/deck/index.html from lecture-1/slides/*.md with the shared deck builder.

Run:  python3 lecture-1/deck/build.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools" / "deck"))
from deckbuild import DeckConfig, build  # noqa: E402

build(DeckConfig(
    lecture_dir=HERE.parent,
    title="From Malware Files to Adversarial Capabilities",
    description="Lecture 1 of DADCA: Defense Against the Dark Cyber Arts, an advanced lecture series on malware, machine learning and AI-powered threat detection: how malware and malicious capabilities evolved, and how detection pipelines evolved with them.",
    series_line="DADCA · Defense Against the Dark Cyber Arts · Lecture 1",
    series_tagline="Understanding the Threat. Mastering the Defense.",
    byline="Roman Vasilenko · Principal Engineer, Cisco Talos",
    deck_url="rvasilenko-ai.github.io/dadca/lecture-1/deck",
    # module -> part number; slides 5 and 19 are the lecture's own part dividers
    part_of={
        "Where is the malware?": 0,
        "From malicious programs to adversarial capabilities": 1,
        "ATT&CK as a language for behavior": 1,
        "Detection pipelines: design and evolution": 2,
        "Synthesis": 2,
    },
    part_titles={
        1: ("How the malicious capability outgrew the file", "Four periods across five tracks, then ATT&CK as a vocabulary for behavior"),
        2: ("How detection pipelines are built, and how they had to change", "The pipeline, two lineages, the stage each change broke, the options, six misses"),
    },
    divider_slides={4: 1, 18: 2},
    table_rows_per_page=10,
))
