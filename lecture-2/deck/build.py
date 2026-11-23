#!/usr/bin/env python3
"""Build lecture-2/deck/index.html from lecture-2/slides/*.md with the shared deck builder.

Run:  python3 lecture-2/deck/build.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools" / "deck"))
from deckbuild import DeckConfig, build  # noqa: E402

build(DeckConfig(
    lecture_dir=HERE.parent,
    title="When the Attacker Is an Agent",
    description="Lecture 2 of DADCA: Defense Against the Dark Cyber Arts, an advanced lecture series on malware, machine learning and AI-powered threat detection: adversarial ML, attacks on LLMs, the agent as a system, and what happens when the agent is the attacker.",
    series_line="DADCA · Defense Against the Dark Cyber Arts · Lecture 2",
    series_tagline="Understanding the Threat. Mastering the Defense.",
    byline="Roman Vasilenko · Principal Engineer, Cisco Talos",
    deck_url="rvasilenko-ai.github.io/malware-and-ai/lecture-2/deck",
    # module -> part number; the first module of a part names its divider
    part_of={
        "Opening": 0,
        "From adversarial ML to attacks on LLMs": 1,
        "From model to agent": 2,
        "The agent becomes an attacker": 3,
        "Case A: an agent the attacker owns": 3,
        "Case B: a trusted agent hijacked": 3,
        "The two cases compared": 3,
        "Defense and research": 4,
    },
    part_titles={
        1: ("Attacking the model", "Adversarial machine learning, then the failure that LLMs add"),
        2: ("From model to agent", "The harness, the loop, the attack surface, the supply chain"),
        3: ("The agent becomes an attacker", "Two cases: an agent the attacker owns, and a trusted agent hijacked"),
        4: ("Defense and research", "Case A and Case B defenses, the cheap-model funnel, the weak watching the strong"),
    },
))
