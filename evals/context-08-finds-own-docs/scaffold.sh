#!/bin/bash
set -e
cat > README.md <<'MD'
# Northbeam web app

Design decisions are recorded as ADRs in `docs/adr/`. Design tokens live in `tokens.json`.
MD
mkdir -p docs/adr
cat > docs/adr/0003-undo-instead-of-confirm.md <<'MD'
# 3. Undo instead of confirmation dialogs

Date: 2026-08-14
Status: Accepted

Reversible actions happen at once and show an Undo toast. Confirmation dialogs are kept for actions that can't be undone.
MD
cat > tokens.json <<'MD'
{ "color": { "text": "#111827", "muted": "#4b5563" }, "space": [4, 8, 12, 16, 24, 32] }
MD
