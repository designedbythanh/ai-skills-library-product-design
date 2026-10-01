#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Thanh Nguyen
"""Repo checks run in CI: manifests, skill files, internal links, lists that must name every skill.

Run from the repo root: python3 scripts/check_repo.py
"""
import json
import os
import re
import sys
import urllib.request
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

# The checks below each come from a mistake that reached the public repo once.

# Skill counts written in prose match the number of skill folders.
count_re = r"\b(\d+) (?:structured )?(?:AI )?skills\b"
for path in ["README.md", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
    for n in re.findall(count_re, (ROOT / path).read_text()):
        if int(n) != len(skills):
            err(f"{path}: says {n} skills, there are {len(skills)}")

# Every example says which version it ran on, in its header.
for name in skills:
    example = ROOT / "skills" / name / "EXAMPLE.md"
    header = "\n".join(example.read_text().splitlines()[:8]) if example.exists() else ""
    if example.exists() and not re.search(r"run on \d{4}-\d{2}-\d{2} [^.\n]*?v\d+\.\d+\.\d+", header):
        err(f"skills/{name}/EXAMPLE.md: header doesn't say which version it ran on")

# Every eval page starts with its at-a-glance table.
for page in sorted((ROOT / "skills").glob("*/EVAL.md")):
    if "## At a glance" not in page.read_text():
        err(f"{page.relative_to(ROOT)}: no '## At a glance' section")

# The changelog has an entry for the current version.
changelog = (ROOT / "CHANGELOG.md").read_text()
if not re.search(rf"^## {re.escape(str(plugin.get('version')))} ", changelog, re.M):
    err(f"CHANGELOG.md: no entry for {plugin.get('version')}")

# Every "N of M" result in the README appears in an eval page.
eval_text = "\n".join(p.read_text() for p in (ROOT / "skills").glob("*/EVAL.md"))
for claim in sorted(set(re.findall(r"\b\d+ of \d+\b", readme))):
    if claim not in eval_text:
        err(f"README.md: '{claim}' isn't in any EVAL.md")
# A "with, against without" pair must sit on one line of an eval table, in that order.
for with_, without in re.findall(r"\b(\d+ of \d+)(?: runs)?, against (\d+ of \d+)", readme):
    if not re.search(rf"{with_}[^\n]*\|[^\n]*{without}", eval_text):
        err(f"README.md: '{with_}, against {without}' isn't a row in any EVAL.md")

# Every eval case is listed in evals/README.md, by name or inside a "`a-01` to `a-05`" range.
evals_readme = (ROOT / "evals/README.md").read_text()
ranges = re.findall(r"`([a-z]+)-(\d+)` to `\1-(\d+)`", evals_readme)
for case in sorted(p.name for p in (ROOT / "evals").iterdir() if p.is_dir() and p.name != "results"):
    m = re.match(r"([a-z]+)-(\d+)", case)
    named = f"`{m.group(0)}`" in evals_readme if m else case in evals_readme
    in_range = bool(m) and any(m.group(1) == p and int(a) <= int(m.group(2)) <= int(b) for p, a, b in ranges)
    if not (named or in_range):
        err(f"evals/README.md doesn't list {case}")

# On GitHub (CI only, needs the network): the repo description and the profile README give the same count.
if os.environ.get("GITHUB_ACTIONS") or os.environ.get("CHECK_GITHUB"):
    for label, url, key in [
        ("repo description", "https://api.github.com/repos/designedbythanh/ai-skills-library-product-design", "description"),
        ("profile README", "https://raw.githubusercontent.com/designedbythanh/designedbythanh/main/README.md", None),
    ]:
        try:
            body = urllib.request.urlopen(url, timeout=15).read().decode()
            text = json.loads(body).get(key) or "" if key else body
            for n in re.findall(count_re, text):
                if int(n) != len(skills):
                    err(f"GitHub {label}: says {n} skills, there are {len(skills)}")
        except OSError as e:
            err(f"GitHub {label}: couldn't fetch ({e})")

if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(skills)} skills, manifests and links OK")
