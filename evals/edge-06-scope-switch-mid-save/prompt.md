---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Feature: "Pipeline columns" settings in Northbeam, a recruiting agency's hiring tool.
Main flow: 1) A recruiter opens Settings > Pipeline columns, a table of candidate fields (rows) by hiring stage (Sourcing, Screening, Interview, Offer), with a switch in each cell. 2) A scope selector at the top picks the level: "Agency" (the default every client inherits) or one client, which can override it. 3) Flipping a switch saves at once, locks that cell while it saves, and shows an "Undo" toast. 4) In a client, an overridden cell shows ↺ to go back to the agency value. 5) Changing the scope keeps the user on the page and reloads the table in place.
Primary user action: turning a column on or off for one stage, at the agency level or for one client.
What we're looking at: spec, about to go to engineering.

What breaks?
