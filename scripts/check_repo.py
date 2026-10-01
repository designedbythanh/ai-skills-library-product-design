#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Thanh Nguyen
"""Repo checks run in CI: manifests, skill files, internal links, lists that must name every skill.

Run from the repo root: python3 scripts/check_repo.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


# Plugin manifests: valid JSON, same version in both.
plugin = {}
try:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    listed = [p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
    if not listed:
        err(f"marketplace.json doesn't list plugin '{plugin.get('name')}'")
    elif listed[0].get("version") != plugin.get("version"):
        err(f"version mismatch: plugin.json {plugin.get('version')}, marketplace.json {listed[0].get('version')}")
except (OSError, json.JSONDecodeError) as e:
    err(f"plugin manifest: {e}")

# Each skill: SKILL.md with frontmatter name = folder name and a description; EXAMPLE.md next to it.
skills = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
for name in skills:
    skill_md = ROOT / "skills" / name / "SKILL.md"
    if not skill_md.exists():
        err(f"skills/{name}: missing SKILL.md")
        continue
    m = re.match(r"^---\n(.*?)\n---\n", skill_md.read_text(), re.S)
    if not m:
        err(f"skills/{name}/SKILL.md: missing frontmatter")
        continue
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M))
    if fm.get("name") != name:
        err(f"skills/{name}/SKILL.md: name is '{fm.get('name')}', expected '{name}'")
    if not fm.get("description", "").strip('" '):
        err(f"skills/{name}/SKILL.md: empty description")
    # Version twice: metadata.version for tools, and a comment as the body's first line,
    # since frontmatter is dropped when a skill loads and only the body reaches the transcript.
    version = plugin.get("version")
    if f'metadata:\n  version: "{version}"' not in m.group(1):
        err(f"skills/{name}/SKILL.md: metadata.version isn't \"{version}\"")
    if not skill_md.read_text()[m.end():].lstrip("\n").startswith(f"<!-- product-design-skills {version} -->"):
        err(f"skills/{name}/SKILL.md: body doesn't start with <!-- product-design-skills {version} -->")
    if not (ROOT / "skills" / name / "EXAMPLE.md").exists():
        err(f"skills/{name}: missing EXAMPLE.md")

# README and the feedback form must name every skill.
readme = (ROOT / "README.md").read_text()
form = (ROOT / ".github/ISSUE_TEMPLATE/skill-feedback.yml").read_text()
for name in skills:
    if f"skills/{name}/SKILL.md" not in readme:
        err(f"README.md doesn't link skills/{name}/SKILL.md")
    if not re.search(rf"^\s+- {re.escape(name)}\s*$", form, re.M):
        err(f"skill-feedback.yml doesn't list {name}")

# Relative links in Markdown files point to files that exist.
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = re.sub(r"```.*?```", "", md.read_text(), flags=re.S)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        path = (md.parent / target.split("#")[0]).resolve()
        if not path.exists():
            err(f"{md.relative_to(ROOT)}: broken link '{target}'")

if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(skills)} skills, manifests and links OK")
