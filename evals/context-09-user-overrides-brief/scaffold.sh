#!/bin/bash
set -e
cat > PRODUCT.md <<'MD'
# Northbeam

## Sources
| Role | Path | Status | Verified |
|---|---|---|---|
| feature | briefs/<slug>.md | primary | 2026-10-01 |

## Product and users
- Hiring tool for recruiting agencies. Recruiters use it daily on a laptop, between calls

## Roles and permissions
- Admin: settings. Recruiter: candidates

## Vocabulary
- "candidate", "client"

## Known issues live in
- Tracker, project NB
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
- Archive happens at once, with an Undo toast · 2 Oct 2026 · Mia (designer)

## Open
- Whether archived candidates count in totals

## Worries
- Recruiters archive by mistake

## Log
MD
