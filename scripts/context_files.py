#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Thanh Nguyen
"""Writes the shared "Context files:" paragraph into every skill, from scripts/context-files.txt.

Edit the paragraph there, then run from the repo root:
  python3 scripts/context_files.py           write it into every skill
  python3 scripts/context_files.py --check   list the skills that differ, change nothing (check_repo.py runs this)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts/context-files.txt"

# The guidelines.md sections each skill reads. A new skill needs a line here ("" for none).
SECTIONS = {
    "acceptance-criteria": "Patterns, States and Microcopy",
    "assumption-reversal": "",
    "cross-industry-steal": "",
    "data-interpretation": "",
    "decision-rationale": "Values",
    "design-critique-facilitator": "Patterns, States, AI features, Microcopy, Examples and Review checklist",
    "design-scope-negotiator": "Values",
    "edge-case-finder": "Patterns, States and AI features",
    "experiment-design": "",
    "explain-to-4-audiences": "",
    "five-whys-root-cause": "",
    "persona-pretest": "Microcopy",
    "prd-first-draft": "AI features",
    "success-metrics-definition": "",
    "user-interview-synthesis": "",
}

# Deliberate wording differences: skill -> (shared text, what this skill says instead).
VARIANTS = {
    # It asks for intent first, so it says when a brief already gives it.
    "design-critique-facilitator": (
        "Use what the files say instead of asking again; ask only",
        "A brief the designer wrote counts as their intent, unlike a spec: if its Worries, Decided and Open sections"
        " are filled in, don't ask for them again. Ask only",
    ),
}

# product-context writes these files instead of reading them, so it has its own wording.
SKIP = {"product-context"}
LINE = re.compile(r"^Context files: .*$", re.M)


def expected(name):
    sections = SECTIONS[name]
    clause = ""
    if sections:
        noun = "section" if re.search(r", | and ", sections) is None else "sections"
        clause = f", and the `guidelines.md` {noun} {sections}"
    text = TEMPLATE.read_text().strip().replace("{guidelines}", clause)
    if name in VARIANTS:
        shared, variant = VARIANTS[name]
        if shared not in text:
            raise SystemExit(f"context-files.txt no longer contains the text {name} replaces: update VARIANTS")
        text = text.replace(shared, variant)
    return text


def skill_names():
    return sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir() and p.name not in SKIP)


def problems():
    """One message per skill whose paragraph isn't what the template gives."""
    out = []
    for name in skill_names():
        if name not in SECTIONS:
            out.append(f"skills/{name}: not in SECTIONS in scripts/context_files.py")
            continue
        m = LINE.search((ROOT / "skills" / name / "SKILL.md").read_text())
        if not m:
            out.append(f"skills/{name}/SKILL.md: no 'Context files:' paragraph")
        elif m.group(0) != expected(name):
            want, got = expected(name), m.group(0)
            i = next((i for i, (a, b) in enumerate(zip(got, want)) if a != b), min(len(got), len(want)))
            out.append(f"skills/{name}/SKILL.md: 'Context files:' differs from scripts/context-files.txt at "
                       f"'…{got[max(0, i - 30):i + 30]}…'; run python3 scripts/context_files.py")
    return out


def write():
    changed = []
    for name in skill_names():
        if name not in SECTIONS:
            raise SystemExit(f"skills/{name}: not in SECTIONS in scripts/context_files.py")
        path = ROOT / "skills" / name / "SKILL.md"
        text = path.read_text()
        if not LINE.search(text):
            raise SystemExit(f"skills/{name}/SKILL.md: no 'Context files:' paragraph to replace")
        new = LINE.sub(lambda _: expected(name), text, count=1)
        if new != text:
            path.write_text(new)
            changed.append(name)
    print(f"Updated {len(changed)} skills: {', '.join(changed)}" if changed else "Every skill already matches")


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        found = problems()
        print("\n".join(f"✗ {p}" for p in found) or "✓ every 'Context files:' paragraph matches")
        sys.exit(1 if found else 0)
    write()
