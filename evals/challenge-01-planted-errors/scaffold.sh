#!/bin/bash
set -e
mkdir -p briefs mockup
cat > briefs/pipeline-columns.md <<'MD'
# Settings › Pipeline columns

Spec: None

## Goal
- A recruiter decides which candidate fields show at each hiring stage, for the whole agency or for one client

## Stage
- Spec, about to go to engineering

## Decided
- A switch saves at once and shows an "Undo" toast; no confirmation dialog · 2026-09-24 · designer
- Changing the scope keeps the user on the page and reloads the table in place · 2026-09-24 · designer
- Fee models open from the Fee row, in their own drawer · 2026-09-27 · designer
- Rejected: fee models as a flagged row of the fields table · they're pricing rules, not a field · 2026-09-27

## Open
- None

## Worries
- Whether recruiters understand what ↺ does

## Log
MD
cat > mockup/pipeline-columns.html <<'HTML'
<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<style>
  body { font-family: Inter, sans-serif; color: #111827; background: #ffffff; margin: 0; }
  .page { padding: 24px; }
  h1 { font-size: 18px; line-height: 28px; font-weight: 600; margin: 0; }
  .hint { font-size: 14px; line-height: 20px; color: #6b7280; margin: 4px 0 16px; }
  .scope { height: 32px; border: 1px solid #d1d5db; border-radius: 8px; padding: 0 12px; font-size: 14px; margin-bottom: 16px; }
  table { border-collapse: collapse; }
  th, td { padding: 12px 16px; border-bottom: 1px solid #e5e7eb; font-size: 14px; line-height: 20px; text-align: left; }
  th { font-size: 12px; line-height: 16px; color: #4b5563; }
  .switch { width: 36px; height: 20px; border-radius: 10px; background: #d1d5db; border: 0; vertical-align: middle; }
  .switch.on { background: #1d4ed8; }
  .switch.saving { opacity: .5; cursor: wait; }
  .reset { border: 0; background: none; font-size: 14px; color: #4b5563; cursor: pointer; }
  .drawer-link { color: #1d4ed8; font-size: 14px; }
  .toast { position: fixed; bottom: 24px; left: 24px; background: #111827; color: #fff; border-radius: 8px; padding: 12px 16px; font-size: 14px; }
  .toast button { background: none; border: 0; color: #93c5fd; font-size: 14px; margin-left: 12px; }
</style></head>
<body><div class="page">
  <h1>Pipeline columns</h1>
  <p class="hint">Choose which fields show at each stage. A client inherits the agency's choices unless you change them.</p>
  <select class="scope" aria-label="Scope">
    <option>Agency (default)</option>
    <option selected>Client: Halden Logistics</option>
  </select>
  <table>
    <tr><th>Field</th><th>Sourcing</th><th>Screening</th><th>Interview</th><th>Offer</th></tr>
    <tr><td>Notice period</td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td>
      <td><button class="switch on" role="switch" aria-checked="true"></button> <button class="reset">↺</button></td>
      <td><button class="switch on saving" role="switch" aria-checked="true" disabled></button></td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td></tr>
    <tr><td>Salary expectation</td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td>
      <td><button class="switch on" role="switch" aria-checked="true"></button></td>
      <td><button class="switch on" role="switch" aria-checked="true"></button></td>
      <td><button class="switch" role="switch" aria-checked="false"></button> <button class="reset">↺</button></td></tr>
    <tr><td>Fee <a class="drawer-link" href="#">Fee models ›</a></td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td>
      <td><button class="switch" role="switch" aria-checked="false"></button></td>
      <td><button class="switch on" role="switch" aria-checked="true"></button></td></tr>
  </table>
</div>
<div class="toast">"Notice period" shown in Interview for Halden Logistics <button>Undo</button></div>
</body></html>
HTML
