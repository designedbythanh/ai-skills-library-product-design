#!/bin/bash
set -e
mkdir -p briefs
cat > briefs/team-invites.md <<'EOF'
# Team invites

## Goal
- Let an admin invite teammates by email with a role

## Stage
- Prototype, for user testing next week. Engineering builds the real feature from the spec.

## Decided
- Invite links are valid for 7 days · 18 Sep 2026 · Leo (PM)

## Open
- Whether admins can invite other admins

## Worries
- People inviting the wrong email address

## Log
EOF
