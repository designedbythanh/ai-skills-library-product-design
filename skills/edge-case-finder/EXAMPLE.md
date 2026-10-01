# Example: edge-case-finder

> Real output from Claude Code (Claude Opus 5.5), run on 2026-10-01 with v1.3.2 of this skill, in `claude plugin eval`. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

**What to notice:**
- The prompt says the spec is about to go to engineering, so it doesn't ask what stage it's looking at. It first looked for a `PRODUCT.md` or brief, found none, and went ahead.
- It separates spec gaps (product decisions engineering would otherwise guess at) from bugs.
- It ends with the "Next" line, pointing to `acceptance-criteria`.
- Its summary says 31 cases; the list has 34. Left as it came out.

The [v1.0.0 run of the same prompt](https://github.com/designedbythanh/ai-skills-library-product-design/blob/v1.0.0/skills/edge-case-finder/EXAMPLE.md) found 27.

## Prompt

```text
We're about to hand this spec to engineering and I want to know what breaks before we build it.
Feature: "Invite teammates" in a project management SaaS.
Main flow: 1) Admin opens Settings > Team. 2) Types one or more email addresses and picks a role (Admin / Member / Viewer). 3) Clicks Send invites. 4) Invitee gets an email with a link valid for 7 days. 5) Invitee clicks the link, creates a password, and lands in the workspace.
Primary user action: the admin sending invites.
```

## Output

Here's the stress test of the spec. Five steps hide a lot of unstated decisions. Three of them will block engineering, because the spec doesn't define the behaviour at all: **an invitee who already has an account**, **a forwarded link**, and **seat limits**.

---

### 1. Input extremes

⚠️ **Edge case:** Admin pastes a list in mixed formats (commas, semicolons, newlines, `Jane Doe <jane@acme.com>`), maybe with trailing spaces.
📍 Input · 💥 Valid emails get rejected, or the whole string is treated as one address.
✅ Accept any common separator, pull the address out of `Name <email>`, trim spaces, and show each email as a chip so bad ones can be fixed one at a time.

⚠️ **Edge case:** One bad email in a batch of 10.
📍 Input · 💥 Either the whole batch fails or the bad one is silently dropped.
✅ Mark the bad chip inline and turn off Send until it's fixed or removed. Never drop an address without saying so.

⚠️ **Edge case:** Duplicates in the batch, including ones that differ only by case (`Bob@acme.com` and `bob@acme.com`).
📍 Input · 💥 Two invites and two emails go out, and later two accounts could be created.
✅ Make email addresses case-insensitive and remove duplicates before sending.

⚠️ **Edge case:** The email belongs to someone who's already a member, or already has a pending invite.
📍 Input · 💥 A confusing second invite. If the role differs, which role applies?
✅ Before sending, say "Already a member" or "Invite pending (sent 3 days ago) — Resend?" Role changes for existing members belong in member management, not here.

⚠️ **Edge case:** Admin pastes 500 emails, or a bad actor uses the form to spam.
📍 Input · 💥 Email provider rate limits, damage to the sending domain's reputation, and a way to abuse the product.
✅ Cap each batch (e.g. 50), limit invites per workspace per day, and point to CSV import or SSO/SCIM for bulk onboarding.

⚠️ **Edge case:** Admin clicks Send with an empty field.
📍 Input · 💥 Minor: an empty request or a vague error.
✅ Keep Send disabled until there's at least one valid email.

⚠️ **Edge case:** Admin invites themselves.
📍 Input · 💥 A pointless invite. If they accept, a role change could follow.
✅ Block it with "You're already in this workspace."

### 2. Permission & access

⚠️ **Edge case:** **The invitee already has an account** (in another workspace, or one they left).
📍 Permission · 💥 Step 5 says "creates a password," so the flow either fails or creates a second account for the same email. **The spec doesn't cover this.**
✅ Split step 5: new users create a password, existing users sign in and accept. The link must handle both paths.

⚠️ **Edge case:** **The link gets forwarded** (to a colleague, a Slack channel, or a personal inbox), especially an Admin invite.
📍 Permission · 💥 Whoever has the link joins with that role, and an Admin invite hands over the whole workspace.
✅ Tie the invite to the invited email. New accounts get that email locked in. Existing users must be signed in with the matching email or get a clear "This invite is for j***@acme.com" message.

⚠️ **Edge case:** The invitee clicks while signed in as a different account.
📍 Permission · 💥 The invite gets accepted by the wrong account.
✅ Show "You're signed in as X; this invite is for Y" with a "Switch account" button.

⚠️ **Edge case:** **The workspace is at its seat limit, or the plan charges per seat.**
📍 Permission · 💥 Surprise charges, failed acceptance, or a free plan going over its limit. **The spec doesn't cover this.**
✅ Decide: do pending invites count against seats? Do Viewers cost money? Show "This will add N paid seats" before sending, and check the seat count again at acceptance.

⚠️ **Edge case:** The workspace requires SSO or limits sign-ups to certain email domains.
📍 Permission · 💥 Creating a password lets the invitee skip SSO, or someone outside the company joins.
✅ When SSO is enforced, send invitees to SSO instead of password creation. Warn or block invites to domains outside the allowed list.

⚠️ **Edge case:** The person who sent the invite is demoted or removed, or the workspace is deleted or suspended, before the invite is accepted.
📍 Permission · 💥 Invites from someone who no longer has authority can still be accepted.
✅ Decide whether invites belong to the workspace (common) or to the person who sent them. Always reject acceptance into a deleted or suspended workspace with a clear message.

⚠️ **Edge case:** A Member or Viewer calls the invite API directly.
📍 Permission · 💥 Someone gives themselves Admin by inviting a second account.
✅ Check permissions on the server, not just by hiding the UI. Only Admins can send Admin invites.

⚠️ **Edge case:** The link is expired, already used, or revoked.
📍 Permission · 💥 A dead end with a generic error.
✅ Give each state its own page: "This invite expired. Ask [admin name] to resend," ideally with a "Request new invite" button that notifies the admins.

⚠️ **Edge case:** The token is guessable, never expires, or leaks through the Referer header or logs.
📍 Permission · 💥 Someone takes over an account.
✅ Use a long random token stored hashed, enforce the 7 days on the server, make it single-use, and set `Referrer-Policy: no-referrer` on the accept page.

### 3. Concurrency

⚠️ **Edge case:** Two admins invite the same email at the same time with different roles.
📍 Concurrency · 💥 Two pending invites with conflicting roles, and whichever is accepted first wins.
✅ Allow one pending invite per email per workspace. Show the second admin "Already invited as Member by Sam — update role?"

⚠️ **Edge case:** Admin double-clicks or rage-clicks Send.
📍 Concurrency · 💥 Duplicate emails go out.
✅ Disable the button while the request is in flight, use an idempotency key, and remove duplicates on the server.

⚠️ **Edge case:** The invitee opens the link in two tabs, or submits the password form twice.
📍 Concurrency · 💥 Two accounts or two memberships, or an error on the second tab.
✅ Make acceptance idempotent. The second attempt should just land them in the workspace.

⚠️ **Edge case:** Admin resends an invite.
📍 Concurrency · 💥 Two valid links. Does the 7-day clock reset?
✅ Either make old links invalid on resend, or keep one token and resend it with a new expiry. Pick one and write it into the spec.

⚠️ **Edge case:** The invite is revoked or its role changed while the invitee is filling in the password form.
📍 Concurrency · 💥 They join anyway, or with the old role.
✅ Check the invite's state and role again at the final submit, not just when the link is opened.

⚠️ **Edge case:** Two invitees accept at the same moment for the last free seat.
📍 Concurrency · 💥 The workspace goes over its seat limit.
✅ Check the seat count inside a single transaction at acceptance.

### 4. External dependencies

⚠️ **Edge case:** **Corporate email scanners (Microsoft Safe Links, Mimecast) open the link before the human does.**
📍 Dependencies · 💥 If opening the link uses up the token, the invitee gets "already used" every time. This is a common real-world failure.
✅ Opening the link (GET) must never use up the token. Only submitting the password or accept form (POST) does.

⚠️ **Edge case:** The email bounces, lands in spam, or never arrives.
📍 Dependencies · 💥 The admin thinks the person was invited, and the invitee never sees it. This drives support tickets.
✅ Show a pending invites list with delivery status (sent / bounced), plus Resend and a "Copy invite link" fallback.

⚠️ **Edge case:** The email provider fails partway through a batch.
📍 Dependencies · 💥 Some invites go out and some don't, with no indication which.
✅ Queue invites and send them in the background with retries. Report results per email ("8 sent, 2 failed — retry").

⚠️ **Edge case:** The network drops after Send, or during password submission.
📍 Dependencies · 💥 The user doesn't know if it worked, and retrying creates duplicates.
✅ Idempotent endpoints (covered above) plus a clear retry state in the UI.

⚠️ **Edge case:** It's unclear which timezone the 7-day expiry uses.
📍 Dependencies · 💥 Low impact: the email says "expires in 7 days" and the link dies a few hours early or late.
✅ Store expiry in UTC on the server and show it in the user's local time ("Expires Oct 8, 3:00 PM").

### 5. User behavior

⚠️ **Edge case:** Admin makes a typo (`jane@acme.con`).
📍 Behavior · 💥 The invite sits pending forever and the real person never gets it.
✅ Pending list with Revoke. Optionally suggest fixes for common typos ("Did you mean acme.com?").

⚠️ **Edge case:** **The role picker defaults to Admin, or the admin picks Admin by accident.**
📍 Behavior · 💥 Someone gets far more access than intended without anyone noticing.
✅ Default to Member. Add a confirmation step for Admin invites ("3 people will get full admin access").

⚠️ **Edge case:** The admin needs different roles in one batch, but the spec allows one role per batch.
📍 Behavior · 💥 The admin has to send several batches, or skips that and gives everyone the same role.
✅ v1: one role per batch is acceptable, but the role must be clearly visible next to the Send button. Later: a role per chip.

⚠️ **Edge case:** Admin leaves the page with emails typed but not sent.
📍 Behavior · 💥 Low impact: the work is lost.
✅ Warn "You have unsent invites" when they navigate away.

⚠️ **Edge case:** The invitee abandons password creation halfway, or opens the link on mobile and finishes on desktop.
📍 Behavior · 💥 The link no longer works because it was already "used."
✅ The token stays valid until the account is actually created (same rule as the scanner fix above).

⚠️ **Edge case:** The invitee presses Back after landing in the workspace and sees the password form again.
📍 Behavior · 💥 Low impact: a confusing "invite already used" error.
✅ If the token is used and the user is signed in as that account, redirect them straight to the workspace.

⚠️ **Edge case:** The invitee ignores the invite for 7 days.
📍 Behavior · 💥 The invite dies quietly and the admin doesn't notice.
✅ Send the invitee a reminder at day 5 (optional), and show the admin an "Expired" badge with one-click Resend.

---

## Summary: 31 edge cases found

**High priority (fix before launch):**
1. **Invitee already has an account.** Step 5 needs a sign-in-and-accept path. *Spec gap.*
2. **Link forwarding.** Tie each invite to the invited email.
3. **Seat and billing rules for invites.** *Spec gap.*
4. **SSO / domain-restricted workspaces skip password creation.** *Spec gap, if you offer SSO.*
5. **Email scanners using up tokens.** Opening the link must not use up the token.
6. **Server-side permission checks.** Only Admins can send Admin invites.
7. **Token security.** Random, hashed, single-use, expiry enforced on the server.
8. **One pending invite per email**, plus idempotent Send and acceptance.
9. **Pending invites list** with status, Resend, and Revoke. *Spec gap. Typos, bounces, and expiry all depend on it.*
10. **Results per email** for partial failures and invalid addresses.
11. **Already-a-member / already-invited detection** before sending.
12. **Role defaults to Member**, with confirmation for Admin invites.
13. **Separate pages for expired, revoked, and used links.**
14. **Resend behaviour** (old link invalidated vs. reused) defined in the spec.

**Low priority (can defer):** typo suggestions, a role per email in one batch, the unsent-invites warning, a day-5 reminder, showing expiry in local time, a "Request new invite" button, the Back-button redirect, a CSV/bulk import path.

The biggest point for the handoff: the spec describes only the happy path for a brand-new user. Points 1, 3, 4, and 9 are product decisions, not bugs. Engineering will have to guess at them unless you decide them first.

Next: `acceptance-criteria` to turn the high-priority cases into criteria. Carry over: the high-priority cases.
