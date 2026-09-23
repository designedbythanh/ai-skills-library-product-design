# Example: prd-first-draft

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
Help me write the first draft of the PRD for a new feature.
Feature: Recurring invoices, in an invoicing app for freelancers.
Core problem: freelancers with retainer clients recreate the same invoice every month by duplicating an old one and editing dates and numbers; they sometimes forget or send it late.
Target users: freelancers with at least one monthly retainer client (about 30% of active accounts).
Business goal: increase retention of paying users, and the share of invoices paid on time.
Known constraints: must work with existing invoice numbering (sequential, legally required in France); emails go through our current email provider; 6 weeks, 1 designer, 2 engineers.
Out of scope: automatic card charging, recurring expenses.
```

## Output

## Recurring Invoices: PRD (first draft)

**TL;DR:** Freelancers with retainer clients can set an invoice to repeat on a schedule. The app then creates it and sends it (or asks them to review it first) with the next legal sequential number, so they no longer rebuild it by hand each month or send it late. We want paying users to stay longer and more invoices to be paid on time.

> ⚠️ = I guessed or recommended something you didn't give me. Please check each one before this goes to review.

---

### Problem statement
About 30% of active accounts have at least one monthly retainer client. Each month these users open last month's invoice, duplicate it, and change the dates, period and number by hand. This causes three problems:
1. **Invoices go out late or not at all.** If an invoice goes out late, the freelancer gets paid late.
2. **Manual edits cause mistakes**, such as the wrong service period, an old date or a wrong amount.
3. **We add nothing to their most regular revenue.** It's a monthly chore, and nothing about it makes our product harder to leave.

⚠️ *We have no numbers on how often invoices are late or forgotten. Before the kickoff, try to get a baseline from the data, for example the days between the start of the service month and the invoice's issue date for repeat clients.*

### Goals
- [ ] Get users in the target segment to set up recurring invoices. ⚠️ Target: 40% of them have at least one active schedule within 90 days of launch (placeholder).
- [ ] Raise the share of invoices paid on time for recurring clients above the manual baseline. ⚠️ Target: +10 pts (placeholder, we need the baseline first).
- [ ] Improve retention of paying users who have an active schedule. ⚠️ No target yet, see Success metrics about self-selection.
- [ ] Never break the legal sequence of invoice numbers (0 gaps, 0 duplicates).

### Non-goals
- Charging the client's card automatically, or collecting payment in any other way.
- Recurring expenses.
- Usage-based or metered billing, where amounts are calculated from tracked time. Users can still edit amounts by hand before sending.
- Changes to the email provider or the email templating system.
- ⚠️ *My suggestion:* only monthly schedules are a must-have. Other frequencies are listed as Should have.

### User stories
1. As a freelancer on a retainer, I want to turn an existing invoice into a monthly schedule so that I never rebuild it by hand again.
2. As a freelancer, I want to review each invoice before it goes out so that I can adjust amounts or line items in a month that differs from normal.
3. As a freelancer who trusts the setup, I want invoices sent automatically on a set day so that I get paid on time without thinking about it.
4. As a freelancer, I want dates and service periods in the invoice to update themselves (e.g. "Services, October 2026") so that each invoice is correct without edits.
5. As a freelancer, I want to pause, edit or end a schedule so that I can handle a client who stops or changes the retainer.
6. As a freelancer, I want to be told if an invoice failed to send or is waiting for my review so that nothing slips through without me knowing.
7. As a French freelancer, I want each recurring invoice to get the next number in my normal sequence so that my books stay legally compliant.

### Requirements

**Must have**
- **Create a schedule** from an existing invoice or from scratch. Settings: client, line items, start date, day of the month to issue, and an optional end (a date or a number of invoices).
- **Two send modes per schedule:**
  - *Review first:* a draft is created X days before the issue date and the user is notified. It is sent only after they approve it.
  - *Auto-send:* the invoice is issued and emailed on the scheduled day.
  - ⚠️ *Which one should be the default is an open question (see below).*
- **Numbering:**
  - The invoice number is assigned **only when the invoice is issued**, never when the draft or schedule is created. Drafts don't use up a number.
  - Numbers must be given out one at a time in a safe way, so two invoices issued at the same moment (manual and recurring) can never get the same number or leave a gap.
  - An issued recurring invoice can't be deleted. It follows the same correction flow as any other invoice (credit note / *avoir*).
- **Date placeholders** in the text and line items: issue date, due date (based on the client's payment terms), and service-period month/year.
- **Month-end handling:** if the scheduled day is the 29th–31st and the month is shorter, the invoice is issued on the last day of that month.
- **Current data used at issue time:** the client's details and the user's company details (address, VAT number, legal notices) are pulled when the invoice is issued, not copied when the schedule was created.
- **Manage schedules:** a list showing each schedule's next issue date, plus pause, resume, edit and end. Edits apply to future invoices only.
- **Send through the current email provider**, using the existing invoice email template.
- **Failure handling:**
  - If sending fails or the email bounces, the user is notified by email and in the app, and the invoice is marked "issued, not delivered".
  - A failed send never takes a second number.
- **Notifications:** "Draft ready for review" (review mode) and "Invoice sent" (auto-send mode).

**Should have**
- Quarterly and yearly schedules.
- A button to skip one occurrence (e.g. the client's holiday month) without ending the schedule.
- A "Make recurring" prompt when we notice the user has invoiced the same client with similar line items 2 months in a row. This is our main way to get users to find the feature.
- A reminder if a review-mode draft hasn't been approved by the issue date.

**Nice to have**
- A preview of the next 3 upcoming invoices.
- Recurring invoices shown in the existing revenue forecast or dashboard (⚠️ if we have one).
- Payment reminders to the client after the due date. ⚠️ *This could matter more for on-time payment than the schedule itself. Do we already have reminders? If so, recurring invoices should turn them on by default.*

### Open questions (need an answer before building)
1. **Default send mode.** Auto-send gives the biggest on-time gain but costs the most when it goes wrong (a wrong invoice is sent and needs a credit note). My suggestion is to default to *review first* and offer auto-send once the user has approved 2 invoices on that schedule. Product needs to decide.
2. **Numbering details.** Is there one sequence per account, or several (e.g. prefixes, one per year)? Does the sequence restart every year? Engineering needs to check how numbers are given out today and whether that works safely when many invoices are issued at once.
3. **Email provider limits.** Most schedules will fall on the 1st of the month, so sending will spike that day. What are our rate limits and send quota? Do we need to queue or spread out sends?
4. **Time zone and send time.** Does "the 1st" mean midnight in the user's time zone, or a fixed hour like 08:00? Is there any legal reason the issue date must match the day the client receives it?
5. **Plan gating.** Is this only for paid plans (a reason to upgrade), or free as well (helps adoption)? This decides which retention goal applies.
6. **Other legal points in France.** Do we need to handle anything specific to recurring invoices, or the upcoming e-invoicing mandate? ⚠️ *I couldn't check this. Someone from legal or compliance should confirm.*
7. **Where the 30% comes from.** How was it measured? We should reuse the same definition to track adoption.
8. **Scope for 6 weeks with 1 designer and 2 engineers.** Everything under Must have probably fits. Among the Should haves, I'd add the "Make recurring" prompt first and leave the others for later. ⚠️ *This is not an engineering estimate.*

### Success metrics
| Type | Metric | Notes |
|---|---|---|
| **Primary** | Share of recurring-schedule invoices paid by their due date, compared with the same users' manual invoices before launch | ⚠️ Baseline needed |
| Adoption | % of the target segment with ≥1 active schedule at 30/60/90 days | Uses the definition from open question 7 |
| Leading | Days late between the start of the service period and the issue date (should get close to 0) | Shows the reason payments are on time |
| Retention | Paid-user churn at 3/6 months, users with a schedule vs. users without | ⚠️ Users who adopt features are more engaged anyway, so this can't be read as cause and effect. Compare matched groups or run a staged rollout if we want a real answer |
| Counter-metric | Credit notes issued against recurring invoices, and support tickets about wrong or unwanted invoices | Should not rise above the rate for manual invoices |
| Counter-metric | Numbering gaps or duplicates | Must be 0. Monitor and alert on it |
| Counter-metric | Bounces and spam complaints on recurring sends | Protects our sender reputation with the email provider |

---

**Guessed or placeholder (please confirm):** all numeric targets, the baselines for late and on-time invoices, the default send mode, the payment reminders feature, the dashboard, whether 6 weeks is enough, and the French legal details beyond sequential numbering.

I can also turn this into a shared doc your team can comment on, or run `/edge-case-finder` or `/acceptance-criteria` on the requirements next.
