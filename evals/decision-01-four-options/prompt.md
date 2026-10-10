---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

I have to pick a direction this week and write down why, so the team doesn't reopen it in a month.

Context: Northbeam is a recruiting tool for agencies. Each agency sets pipeline fields once (which candidate fields show at each hiring stage), and can change that for a single client. Today, the client's own settings and the agency's defaults look the same in the table, so account managers can't tell what they changed for a client. About 30 support tickets a month come from this.

The options on the table:
- Option 0: keep the page as it is and add a help article.
- Option A: mark each client setting that differs from the agency default with a dot and a "Reset to agency" link on hover.
- Option B: add a "Changed for this client" filter above the table, so account managers see only what they changed.
- Option C: a side-by-side view, agency default on the left and the client on the right, with differences highlighted.

Constraints: two developers for one sprint (two weeks). Account managers set up a new client about once a month and mostly work on a laptop screen.
