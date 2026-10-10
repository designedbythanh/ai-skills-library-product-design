---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Help me choose between two directions and write down a rationale my team can stand behind.

Context: Northbeam is a recruiting tool for agencies. Agencies set fee models (how invoices are calculated: contingency %, retained, hourly) once for the agency, and can change them for a single client. Today these live on two pages: "Agency fees" and "Client fees".

Last spring, an account manager changed the agency-wide contingency rate while she thought she was editing one client. 40 clients were invoiced at the wrong rate before anyone noticed. Since then, the team's rule is: agency-wide and client-level fee settings are never editable on the same screen.

- Option A: merge both pages into one "Fees" page, one table, with an Agency / Client selector at the top that switches what the table edits. Account managers asked for it in interviews (fewer clicks), it removes a page from the navigation, and it's the cheaper option to build: about 4 days.
- Option B: keep two pages, and add a banner on "Client fees" showing which agency defaults the client inherits, with a link to "Agency fees". About 6 days.

Constraint: this has to ship by the end of the month.
