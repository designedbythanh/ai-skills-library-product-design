#!/bin/bash
set -e
cat > DESIGN.md <<'MD'
# Northbeam design rules

## 1. Color
- Text #111827, secondary text #4b5563, borders #e5e7eb, control borders #d1d5db, primary #1d4ed8.
- Status chips: soft background with the 700 shade for text.

## 2. Layout
- Page gutter 24px on desktop, 16px below 640px.
- Tables: cells padded 12px 16px.

## 3. Type
- Only these type styles: 12/16, 14/20, 18/28 (size/line height). Page titles use 18/28 semibold.
- Never set a size or line height that isn't one of these.

## 4. Spacing
- Spacing in 4px steps (4, 8, 12, 16, 24, 32). Nothing in between.

## 5. Components
- Buttons and filter chips: 32px tall at every width. Radius 8px.
- Status badges: 24px tall (4px 8px padding, 12/16 text).
- Inputs: 32px tall, radius 8px.

## 6. Copy
- Sentence case for labels and buttons.
MD
mkdir -p mockup
cat > mockup/candidates.html <<'HTML'
<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<style>
  body { font-family: Inter, sans-serif; color: #111827; background: #ffffff; margin: 0; }
  .page { padding: 24px; }
  h1 { font-size: 18px; line-height: 28px; font-weight: 600; margin: 0 0 16px; }
  .toolbar { display: flex; gap: 8px; align-items: center; margin-bottom: 16px; }
  .search { height: 32px; border: 1px solid #e5e7eb; border-radius: 8px; padding: 0 12px; font-size: 14px; }
  .chip { height: 32px; padding: 0 12px; border: 1px solid #e5e7eb; border-radius: 8px; font-size: 14px; line-height: 20px; background: #fff; }
  .chip.on { background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe; }
  table { width: 100%; border-collapse: collapse; }
  th { font-size: 12px; line-height: 16px; color: #4b5563; text-align: left; padding: 12px 16px; border-bottom: 1px solid #e5e7eb; }
  td { padding: 12px 16px; border-bottom: 1px solid #e5e7eb; font-size: 14px; line-height: 20px; }
  td .name { font-weight: 600; }
  .stage { display: inline-block; padding: 4px 8px; border-radius: 8px; font-size: 12px; line-height: 16px; background: #fef3c7; color: #b45309; }
  .btn-secondary { height: 32px; padding: 0 12px; border: 1px solid #d1d5db; border-radius: 8px; background: #ffffff; font-size: 14px; }
  .meta { font-size: 12px; line-height: 16px; color: #4b5563; }
  .cards { display: none; }
  @media (max-width: 639px) {
    .page { padding: 16px; }
    table { display: none; }
    .cards { display: flex; flex-direction: column; gap: 10px; }
    .card { border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; }
    .card .name { font-size: 16px; line-height: 24px; font-weight: 600; }
    .card .meta { margin-top: 4px; }
    .card .btn-secondary { height: 36px; margin-top: 12px; width: 100%; }
  }
</style></head>
<body><div class="page">
  <h1>Candidates</h1>
  <div class="toolbar">
    <input class="search" placeholder="Search candidates">
    <button class="chip on">All</button><button class="chip">Sourcing</button><button class="chip">Screening</button><button class="chip">Interview</button><button class="chip">Offer</button><button class="chip">Hired</button><button class="chip">Rejected</button>
  </div>
  <table>
    <tr><th>Name</th><th>Role</th><th>Stage</th><th>In stage</th><th></th></tr>
    <tr><td><span class="name">Lena Okafor</span></td><td>Senior Data Analyst</td><td><span class="stage">Screening</span></td><td>3 days</td><td><button class="btn-secondary">Move to interview</button></td></tr>
    <tr><td><span class="name">Tomás Reyes</span></td><td>Product Designer</td><td><span class="stage">Interview</span></td><td>1 day</td><td><button class="btn-secondary">Move to offer</button></td></tr>
  </table>
  <div class="cards">
    <div class="card"><div class="name">Lena Okafor</div><div class="meta">Senior Data Analyst · Screening · 3 days</div><button class="btn-secondary">Move to interview</button></div>
    <div class="card"><div class="name">Tomás Reyes</div><div class="meta">Product Designer · Interview · 1 day</div><button class="btn-secondary">Move to offer</button></div>
  </div>
</div></body></html>
HTML
