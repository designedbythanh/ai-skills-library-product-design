---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Pretest this design with a persona before we show it to users.

Persona: Sam, operations coordinator at a recruiting agency. Sets up a new client's account in Northbeam about once a month. Keeps the agency's dropdown lists in a "lists" tab of an Excel file. Comfortable with Excel, not with settings pages.

Design: Northbeam Settings > "Fields", one page that replaces two old ones ("Lists", where the agency kept its value lists, and "Pipeline columns").
- A table: every field of the hiring pipeline tables is a row, in one shared order: Source channel, Req ID, Skills, Seniority, Languages, Name, Applied on, Salary expectation, Fee, Margin, Status, Start date. Columns are the stages Sourcing / Screening / Interview / Offer, with a switch per cell, or a dash where the field isn't used in that stage.
- Rows that own a value list (Source channel, Skills, Seniority, Languages) have a small list icon on the left and a second gray line with their first values, e.g. "LinkedIn · Referral · Job board ›". Clicking it opens a drawer to edit the values. Other rows have no icon and no second line.
- The Fee row's second line reads "Pricing basis · Contingency % · Retained · Hourly ›". It opens a "Fee models" drawer: each fee model has a label, a unit and a "per hire" checkbox. Fee models are what the agency's invoices are calculated from.
- Toolbar: search, a "Fields with a list (4)" switch, an "Only shown fields" switch, and a "New field" button. The "New field" modal asks for: Label, Attached to (Candidate / Application), Values per line (Single / Multi).
- A scope selector at the top: Agency or one client.

Sam's tasks: 1) add "Day rate" as a new fee model; 2) fill in the Languages list; 3) create a "Notice period" field and make sure it shows in the Offer stage.

Our question: do people still find and maintain the value lists, and especially the fee models, now that they don't have their own page?
