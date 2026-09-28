---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Feature: "Invite teammates" in Stackroom, a project management tool.
Main flow: 1) An admin opens Settings > Team. 2) Types one or more email addresses and picks a role. 3) Clicks Send invites. 4) The invitee gets an email link valid for 7 days. 5) The invitee sets a password and lands in the workspace.
Primary user action: the admin sending invites.

What breaks?
