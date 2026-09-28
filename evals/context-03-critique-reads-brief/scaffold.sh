#!/bin/bash
set -e
cat > PRODUCT.md <<'EOF'
# Ledgerly

## Product and users
- Bookkeeping tool for freelancers
- Users invoice 5 to 20 clients a month, mostly on a laptop

## Roles and permissions
- Single user per account

## References
- Not provided

## Vocabulary
- "invoice", "client"

## Known issues live in
- Not provided
EOF
mkdir -p briefs
cat > briefs/invoices-list.md <<'EOF'
# Invoices list

## Goal
- See at a glance which invoices are unpaid and overdue

## Stage
- Built

## Decided
- Newest invoices first · 15 Sep 2026 · Ana (designer)

## Open
- Whether overdue invoices should be pinned to the top

## Worries
- Overdue invoices don't stand out

## Log
EOF
