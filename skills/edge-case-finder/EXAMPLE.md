# Example: edge-case-finder

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
We're about to hand this spec to engineering and I want to know what breaks before we build it.
Feature: "Invite teammates" in a project management SaaS.
Main flow: 1) Admin opens Settings > Team. 2) Types one or more email addresses and picks a role (Admin / Member / Viewer). 3) Clicks Send invites. 4) Invitee gets an email with a link valid for 7 days. 5) Invitee clicks the link, creates a password, and lands in the workspace.
Primary user action: the admin sending invites.
```

## Output

I checked the invite flow for five kinds of failure. I found **27 edge cases**, and **12 need fixing before launch**. Two problems come up again and again: the spec doesn't say what happens after an invite is sent, and it doesn't cover invitees who already have an account.

---

## 1. Input extremes

**⚠️ Edge case:** The admin clicks Send with an empty field, only spaces, or stray commas (`bob@acme.com,,`).
📍 Input · 💥 **What breaks:** Blank invites are created, or the user sees a vague server error.
✅ **Fix:** Trim and split the input on commas, semicolons and spaces, and drop empty entries. Keep Send disabled until there is at least one valid address.

**⚠️ Edge case:** The admin pastes a mixed list, like a line from Outlook (`Bob Lee <bob@acme.com>; jane@acme`), with some valid and some invalid addresses.
📍 Input · 💥 **What breaks:** Either the whole batch is rejected, or the valid ones send and the bad ones drop silently. The admin believes everyone was invited.
✅ **Fix:** Pull addresses out of the common `Name <email>` format. Show each address as a chip and mark the invalid ones inline. Send only the valid ones, then show a clear result: "4 sent, 1 invalid."

**⚠️ Edge case:** The same address appears twice with different capitalization (`Bob@Acme.com` and `bob@acme.com`).
📍 Input · 💥 **What breaks:** Two invites and two emails go out, and possibly two accounts get created.
✅ **Fix:** Lowercase addresses before looking them up and remove duplicates within the batch. Put a unique constraint on the lowercased (workspace, email) pair.

**⚠️ Edge case:** The address belongs to someone who is already a member, or who already has a pending invite.
📍 Input · 💥 **What breaks:** A second invite link is created for the same person, or an existing member gets an invite email that makes no sense to them.
✅ **Fix:** Show "Already a member" or "Invite pending, resend?" instead of creating a new invite.

**⚠️ Edge case:** The admin pastes 500 addresses, or an address longer than 254 characters.
📍 Input · 💥 **What breaks:** The email provider rate-limits you or flags you for spam, the request times out, and the app may blow past its seat limit.
✅ **Fix:** Limit each batch to around 50 addresses and point larger teams to CSV import or SSO. Validate address length per the email standard (RFC 5321).

## 2. Permissions & access

**⚠️ Edge case:** The invitee already has an account, for example in another workspace. Step 5 assumes everyone creates a password.
📍 Permissions · 💥 **What breaks:** They can't create a password for an email that's already registered. They hit a dead end, or worse, a second account gets created.
✅ **Fix:** Add a second path: if the email is already registered, ask them to sign in and join. **This is a gap in the spec.**

**⚠️ Edge case:** A Member or Viewer calls the invite API directly, or invites someone as Admin.
📍 Permissions · 💥 **What breaks:** Anyone can give themselves Admin by inviting a second address they control.
✅ **Fix:** Check on the server that the sender is an Admin, not just by hiding the button. Decide whether any Admin can invite other Admins.

**⚠️ Edge case:** The invitee forwards the email, or it goes to a shared inbox like team@.
📍 Permissions · 💥 **What breaks:** Whoever clicks first gets access with the invited role, possibly Admin.
✅ **Fix:** Lock the account email to the invited address. Make the link single-use. For Admin invites, consider asking for a second confirmation.

**⚠️ Edge case:** The invite link is guessable, sits in the database as plain text, or leaks through referrer headers or logs.
📍 Permissions · 💥 **What breaks:** Anyone who sees the link can join the workspace.
✅ **Fix:** Use a random token of at least 128 bits. Store only a hash of it. Remove it from the URL after the page loads, and add `Referrer-Policy: no-referrer`.

**⚠️ Edge case:** The admin invited the wrong person, or the admin who sent the invite has since been removed or demoted.
📍 Permissions · 💥 **What breaks:** Without a way to revoke, a bad invite, including an Admin one, stays live for 7 days.
✅ **Fix:** Add a pending-invites list with Revoke. Revoking must invalidate the token. Decide whether invites survive when the admin who sent them is removed. **This is a gap in the spec.**

**⚠️ Edge case:** The workspace requires SSO or restricts sign-ups to certain email domains.
📍 Permissions · 💥 **What breaks:** Creating a password through the invite link gets around the company's SSO policy.
✅ **Fix:** When SSO is enforced, send the invitee through SSO instead of the password form. Check domain restrictions both when the invite is sent and when it's accepted.

**⚠️ Edge case:** The invites would take the workspace over its plan's seat limit.
📍 Permissions · 💥 **What breaks:** You give away free seats, or the invitee accepts and then hits a paywall.
✅ **Fix:** Check seat count when sending, showing "3 seats left, 5 invites," and check again when an invite is accepted. Decide whether Viewers use a paid seat.

**⚠️ Edge case:** The invitee clicks the link while signed in as a different user.
📍 Permissions · 💥 **What breaks:** The invite is accepted by the wrong account.
✅ **Fix:** Detect the mismatch and show: "This invite is for bob@…. Switch account?"

**⚠️ Edge case:** The invitee clicks the link on day 8.
📍 Permissions · 💥 **What breaks:** They see a generic error and have no way forward.
✅ **Fix:** Show a clear "expired" page with a "Request a new invite" button that notifies the admins. Show an exact expiry date in the email rather than just "7 days".

## 3. Concurrency

**⚠️ Edge case:** The admin double-clicks or rage-clicks Send.
📍 Concurrency · 💥 **What breaks:** Duplicate emails go out with several valid links for each person.
✅ **Fix:** Disable the button while the request is in flight. Use an idempotency key, backed by the unique (workspace, email) constraint.

**⚠️ Edge case:** Two admins invite the same email at the same time with different roles.
📍 Concurrency · 💥 **What breaks:** Two live links exist with different roles, and whichever is clicked decides the role.
✅ **Fix:** Allow only one pending invite per email. The second admin sees "Pending as Member. Change to Admin?"

**⚠️ Edge case:** The invitee submits the form in two tabs, or accepts twice.
📍 Concurrency · 💥 **What breaks:** Two memberships or two accounts get created.
✅ **Fix:** Use up the token and create the membership in a single database transaction.

**⚠️ Edge case:** An admin revokes the invite, or the last seat gets taken, while the invitee is filling in the password form.
📍 Concurrency · 💥 **What breaks:** A revoked invitee still gets in.
✅ **Fix:** Re-check that the invite is still valid and a seat is available when the form is submitted, not only when the page loads.

## 4. External dependencies

**⚠️ Edge case:** Corporate email security tools (for example Microsoft Defender's Safe Links, Mimecast) open every link in an email automatically to scan it.
📍 Dependencies · 💥 **What breaks:** If opening the link uses it up, the scanner "accepts" the invite, and the real person gets "link already used." **This is very common with business customers.**
✅ **Fix:** Opening the link should have no side effects. Only use up the token when the password or join form is submitted.

**⚠️ Edge case:** The email provider times out or goes down when Send is clicked.
📍 Dependencies · 💥 **What breaks:** The screen says "Invites sent" but nothing was sent.
✅ **Fix:** Queue emails and retry them. Show a delivery status for each invite (Queued, Sent, Failed) in the pending list.

**⚠️ Edge case:** The email bounces or lands in spam.
📍 Dependencies · 💥 **What breaks:** The invitee never sees it, and the admin assumes they're ignoring it.
✅ **Fix:** Use the email provider's bounce notifications to mark invites "Bounced." Offer Resend, and possibly a "Copy invite link" button for admins (a security tradeoff to decide on).

**⚠️ Edge case:** The invitee's connection drops right after they submit a password.
📍 Dependencies · 💥 **What breaks:** They retry, the token is already used, and they're stuck with an account they don't know exists.
✅ **Fix:** Make accepting safe to repeat. If the token was already used by this same email, send them to sign in instead of showing an error.

## 5. User behavior

**⚠️ Edge case:** The admin makes a typo (`bob@acme.con`, or the wrong Bob).
📍 Behavior · 💥 **What breaks:** A stranger can join, possibly as Admin.
✅ **Fix:** Suggest corrections for misspelled domains, ask for confirmation when the role is Admin, and make revoking easy.

**⚠️ Edge case:** There's one role picker for the whole batch, and it may default to Admin.
📍 Behavior · 💥 **What breaks:** Admins invite people with the wrong role, usually too much access.
✅ **Fix:** Default to Member (or Viewer). Allow a different role for each address, or at least show the role on each chip before sending.

**⚠️ Edge case:** The invitee ignores the email and signs up directly on your site.
📍 Behavior · 💥 **What breaks:** They end up alone in a new empty workspace, and the invite is never used.
✅ **Fix:** On sign-up or sign-in, check for pending invites to that email and offer: "You've been invited to Acme. Join?"

**⚠️ Edge case:** The admin can't see who has accepted.
📍 Behavior · 💥 **What breaks:** Admins resend blindly or open support tickets.
✅ **Fix:** Add a pending list in Settings > Team showing status, role, expiry date, Resend and Revoke. **This is a gap in the spec**, as noted above.

**⚠️ Edge case:** The invitee presses Back or refreshes after accepting.
📍 Behavior · 💥 **What breaks:** The password form appears again and a resubmit fails with an error.
✅ **Fix:** If the invite was already accepted, redirect to the workspace or the sign-in page.

**⚠️ Edge case:** The admin types a long list and then leaves the page by accident.
📍 Behavior · 💥 **What breaks:** The list is lost.
✅ **Fix:** Warn about unsaved changes when leaving the page.

---

## Summary: 27 edge cases found

**High priority (fix before launch), 12:**
1. Path for invitees who already have an account
2. Server-side permission check on the invite endpoint
3. Forwarded links: lock the account to the invited email, single-use link
4. Token security: random, stored hashed, stripped from the URL
5. Revoke, and the pending-invites list with Resend/Revoke
6. Following SSO and domain restrictions
7. Seat limit checks
8. Preventing double-send
9. Email scanners using up the link
10. Silent email failures
11. Mixed valid/invalid lists partly dropped
12. Admin as the default role / typos in Admin invites

**Low priority (can defer):** 15 cases. These are case-sensitivity duplicates, batch caps, expired-link messaging, account mismatch, same-email races, double acceptance, the revoke-while-accepting race, bounce tracking, network retries, direct sign-ups, back/refresh, unsaved-changes warning, very long addresses, already-member messaging, and the one-role-per-batch picker.

**Questions the spec needs to answer before engineering starts:**
- What happens when an invitee already has an account?
- Does SSO override the password step?
- Do Viewers use a paid seat?
- Can an Admin invite other Admins?
- Do invites survive when the admin who sent them is removed?
- Does Resend invalidate the old link?
