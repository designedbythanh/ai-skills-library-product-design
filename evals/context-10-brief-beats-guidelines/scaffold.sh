#!/bin/bash
set -e
cat > PRODUCT.md <<'MD'
# Northbeam

## Sources
| Role | Path | Status | Verified |
|---|---|---|---|
| guidelines | guidelines.md | primary | 2026-10-01 |
| feature | briefs/<slug>.md | primary | 2026-10-01 |

## Product and users
- Hiring tool for recruiting agencies. Recruiters use it daily on a laptop, between calls

## Roles and permissions
- Recruiter: candidates

## Vocabulary
- "candidate", "archive" (not "delete")

## Known issues live in
- Tracker, project NB
MD
cat > guidelines.md <<'MD'
# Northbeam — Design Guidelines

## Patterns

### Destructive actions
1. Every action that removes something from a list asks for confirmation in a dialog first.

## Review checklist
- [ ] Removing something from a list asks for confirmation
MD
mkdir -p briefs
cat > briefs/candidate-archive.md <<'MD'
# Candidate archive

Spec: None

## Goal
- Let a recruiter clear candidates they're no longer working with, without losing them

## Stage
- Prototype

## Decided
- Archive happens at once, with an Undo toast, no confirmation dialog: it's reversible and recruiters archive many in a row · 2 Oct 2026 · Mia (designer)

## Open
- Whether archived candidates count in totals

## Worries
- Recruiters miss the Undo toast

## Log
MD
