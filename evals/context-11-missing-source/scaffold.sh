#!/bin/bash
set -e
cat > PRODUCT.md <<'MD'
# Northbeam

## Sources
| Role | Path | Status | Verified |
|---|---|---|---|
| guidelines | design/DESIGN.md | primary | 2026-09-20 |

## Product and users
- Hiring tool for recruiting agencies. Recruiters use it daily on a laptop

## Roles and permissions
- Recruiter: candidates

## Vocabulary
- "candidate"

## Known issues live in
- Tracker, project NB
MD
mkdir -p old
cat > old/design-system-2024.md <<'MD'
# Design system (2024)

- Buttons and inputs are 40px tall everywhere.
MD
