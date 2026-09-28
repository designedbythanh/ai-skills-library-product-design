---
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Bash, Read]
---

Can you critique the Invoices list in Ledgerly, a bookkeeping tool for freelancers? It's built. CSS:

```css
body { background: #ffffff; }
.invoice-title  { color: #111827; font-size: 15px; }
.invoice-meta   { color: #4b5563; font-size: 13px; }
.row            { border-bottom: 1px solid #6b7280; }
.status-paid    { color: #0f766e; font-size: 13px; }
```

Layout: a table of invoices (client, amount, due date, status), newest first, with a "New invoice" button top right. Each row opens the invoice.
Goal: see at a glance which invoices are unpaid and overdue. Users: freelancers who invoice 5 to 20 clients a month. Stage: built.
Decided: newest first.
Open: whether overdue invoices should be pinned to the top.
My concern: overdue invoices don't stand out.
Compare with: nothing specific yet.
