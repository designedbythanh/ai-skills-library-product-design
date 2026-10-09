#!/bin/bash
set -e
mkdir -p briefs
cat > briefs/candidates-list.md <<'MD'
# Candidates list

## Goal
- A recruiter sees at a glance which candidates need them this week

## Stage
- Prototype, before handoff to engineering

## Decided
- One Stage filter value at a time for v1 · 2 Oct 2026 · Mia (designer)
- Rejected: write the next step into the Progress column ("to call", "to send offer") · Progress stays a status, the next step lives in the candidate page · 4 Oct 2026 · Mia (designer)

## Open
- Whether archived candidates count in the list's total

## Worries
- Recruiters miss candidates who are waiting on them

## Log
- 4 Oct 2026 · design-critique-facilitator
  - The yellow Screening pill text is 1.8:1 on its background; use the 700 shade (4.6:1).
  - Archive has no confirmation and no undo; add an "Undo" toast.
  - "In progress" appears in both the pill and the Progress column.
MD
