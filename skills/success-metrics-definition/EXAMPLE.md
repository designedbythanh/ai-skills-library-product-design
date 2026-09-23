# Example: success-metrics-definition

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
Before we build it, I want to define what success looks like for this feature.
Feature: Recurring invoices in an invoicing app for freelancers (set an invoice to repeat monthly, sent automatically).
Problem it solves: freelancers with retainer clients recreate the same invoice every month and sometimes forget or send it late.
Target user: freelancers with at least one monthly retainer client.
Business objective: retention of paying users.
```

## Output

# Success metrics: Recurring invoices

**Two constraints shape everything below:**
1. **The cycle is monthly.** At day 30 a schedule has fired once at most, so early targets have to be about setup and the first send. The feature can't show it has stopped a missed month until at least cycle 2.
2. **Users choose whether to adopt it.** Freelancers who bother to set up automation are probably more engaged already, so they'll retain better regardless. If you only compare adopters with non-adopters, you'll overstate the feature's impact. You need a holdout (see "How to instrument").

**Eligible user:** a paying user with at least one detected retainer client. A retainer client is one invoiced at least 3 times in the last 4 months, 25–35 days apart, with amounts within ±15% of each other. This can be calculated from existing invoice history, and every rate below uses it as the denominator.

**Targets are placeholders.** I don't have your baselines. Pull the pre-launch numbers first (most of them can be backfilled from invoice history), then set targets relative to them.

---

## Primary metric (north star)

**Metric:** On-time automated retainer billing rate

**Definition:** % of eligible users who have at least one retainer client invoiced by an active recurring schedule, auto-sent within ±1 day of the scheduled date, for 2 or more consecutive cycles with no manual send or recreation in between.

**Why this one:** It measures the problem directly: the invoice goes out, on time, without the user rebuilding it, and it keeps happening. A schedule that someone creates and then abandons doesn't count.

| Horizon | Target | Note |
|---|---|---|
| 30 days | ≥25% of eligible users have an active schedule and ≥90% of first auto-sends succeed | Only setup and the first send are measurable this early |
| 60 days | ≥15% of eligible users meet the full definition | First point where 2 consecutive cycles are possible |
| 90 days | ≥25% of eligible users meet it | Retention effect starts to become measurable (see below) |

## Supporting metrics

| Metric | Type | Definition | Target |
|---|---|---|---|
| Schedule setup rate | Leading | % of eligible users who create a recurring schedule for a detected retainer client | 30% by day 30 |
| Suggestion conversion | Leading | % of in-app prompts on detected retainer clients that lead to a schedule | ≥20% |
| Auto-send success rate | Leading | Auto-sends delivered ÷ auto-sends attempted. Failures include bounces, missing client email and validation errors | ≥98% |
| Schedule survival | Leading | % of schedules still active after the 2nd cycle, not paused or cancelled | ≥80% |
| Late/missed retainer invoices | Lagging | Per retainer client-month: sent more than 3 days after that client's historical median send day, or not sent at all. Compare adopters' pre- and post-adoption rates, and treatment vs holdout | ≥50% reduction vs baseline |
| Days-to-paid on retainer invoices | Lagging | paid_at minus sent_at, median, for retainer invoices | No worse than baseline; better is a bonus because earlier sending means earlier payment |
| **Paid-user retention (business proof)** | Lagging | 90-day subscription retention of eligible users, **treatment vs holdout** | +X pp over holdout. Set X after a power calculation (see note) |

## Counter-metrics

- **Invoice correction rate after auto-send:** % of auto-sent invoices later voided, credited or edited-and-resent. Catches wrong amounts, stale line items, and invoices sent to clients who have ended the retainer. Must stay ≤ the manual-invoice baseline.
- **Pause or cancel right after the first send:** a high rate here means users were surprised by what went out. Add a `reason` field so it can be diagnosed.
- **Support tickets tagged recurring/auto-send**, per 100 schedules.
- **Days-to-paid** (also in the table above): if clients ignore automated invoices, this rises.
- **Invoices sent to churned clients:** voided auto-invoices where the client had no payment in the prior 60 days.
- **Retention of eligible users who don't adopt**, in treatment vs holdout: checks that the rollout, such as aggressive prompts, isn't annoying anyone.

## How to instrument

| Event | Key properties | Feeds |
|---|---|---|
| `invoice_created` | source (manual / duplicate / recurring), client_id, amount | Retainer detection, recreation baseline |
| `invoice_sent` | trigger (manual / auto), scheduled_for, sent_at, schedule_id | North star, lateness, success rate |
| `recurring_schedule_created` | client_id, interval, entry_point (suggestion / manual) | Setup rate, suggestion conversion |
| `recurring_schedule_paused` / `_cancelled` / `_edited` | reason, cycles_completed | Survival, surprise counter-metric |
| `recurring_run_failed` | failure_reason | Auto-send success rate |
| `retainer_suggestion_shown` / `_dismissed` | client_id | Suggestion conversion |
| `invoice_voided` / `credit_note_issued` / `invoice_resent_after_edit` | original trigger | Correction rate |
| `invoice_paid` | paid_at | Days-to-paid |
| Subscription events: renewed, cancelled, downgraded | plan, cancellation reason | Retention |
| Support ticket tag `recurring` | — | Support load |
| Experiment assignment | treatment / holdout, assigned_at | Every causal comparison |

**Holdout:** keep about 10% of eligible users without the feature for 90 days. This is the only clean way to attribute retention to the feature. Check sample size first. If monthly churn among eligible users is around 3% and the eligible population is small, a 90-day holdout may not detect a 1-point lift. If it can't, say so up front and rely on the problem metrics (lateness, missed months) as the main evidence, with retention as directional only.

## What can't be measured reliably

- **"Forgetting" as such.** You only see its effects: a missed month or a late send compared with the client's normal send day. That's why the metrics use those proxies.
- **Time saved.** Time spent in the invoice editor is noisy: people leave tabs open or edit other invoices. Don't report it as a headline number. If you need it, ask in a one-question survey after the 2nd cycle.
- **Retainers the app can't see**, e.g. a client billed irregularly or from a different template. The detection rule will undercount eligible users, so all rates are lower bounds.

## Vanity metrics to avoid

- **Schedules created:** creating a schedule proves nothing, and one abandoned before its first send looks the same as a working one. Use schedule survival and the north star instead.
- **Total auto-invoices sent:** it grows on its own every month and counts invoices to churned clients as wins.
- **Feature adoption as % of all users:** the wrong denominator. Most users have no retainer, so the number looks low and says nothing. Always divide by eligible users.
- **Adopters' retention vs non-adopters'** without a holdout: self-selection all but guarantees a flattering gap. It will look like strong evidence, but it isn't.
- **Total invoice volume or revenue processed:** mostly driven by seasonality and user growth. The feature moves when invoices go out, not how many there are.

Next step: backfill the lateness, missed-month and days-to-paid baselines from existing invoice history before launch, so the targets start from real numbers.
