---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Feature: "Invite teammates" in Stackroom, a project management tool.
Main flow: 1) An admin opens Settings > Team. 2) Types one or more email addresses and picks a role (Admin / Member / Viewer). 3) Clicks Send invites. 4) The invitee gets an email with a link valid for 7 days. 5) The invitee clicks the link, sets a password and lands in the workspace.
Primary user action: the admin sending invites.
How the current build works: the user's role is read from the URL (?role=admin), the team list is 3 hard-coded people, and "Send invites" shows a success toast without sending anything.

What we're looking at: a clickable prototype for user testing next week. None of this code goes to production; engineering builds the real feature from the spec.

What breaks?
