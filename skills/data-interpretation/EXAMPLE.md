# Example: data-interpretation

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
I'm looking at our numbers and need to draw a real conclusion before Monday's meeting.
Data: trial-to-paid conversion was 18% in June, 17% in July, and 12% in August. Sign-ups in August were up 40% compared to July. In August, we launched a partnership with a freelancer community that sent a lot of new sign-ups. Also in August we moved the pricing page link from the top navigation into the account menu. Average time-to-first-invoice for new users stayed flat (about 2 days).
Goal: trial-to-paid conversion above 15%.
Time period: June to August.
Known external factors: August is holiday season in France, where most of our users are.
```

## Output

Everything the analysis needs is in your message. Here's the read.

---

## What the data shows (facts only)

- Trial-to-paid conversion went from 18% in June to 17% in July to 12% in August. August is 3 points below the 15% goal. June and July were above it.
- August sign-ups were 40% higher than July's.
- Three things changed in August at the same time:
  1. The freelancer partnership started sending sign-ups.
  2. The pricing link moved from the top nav into the account menu.
  3. French holiday season began.
- Time-to-first-invoice stayed flat at about 2 days.
- **Arithmetic from your numbers:** if July had N sign-ups, it produced about 0.17N paid customers. August had 1.4N sign-ups at 12%, which is about 0.168N paid customers. **The number of new paying customers was almost the same in July and August. Only the rate fell.**

## Most likely explanation (interpretation)

*This is a hypothesis, not a finding:* the drop is mainly a **mix shift**. A large new group of partner sign-ups converts at a much lower rate than your usual users. It pulled the blended rate down while the number of paying customers stayed flat. The flat time-to-first-invoice points the same way: the product experience for new users doesn't look broken.

## Alternative explanations to rule out

| Factor | How to verify or dismiss |
|---|---|
| **Partner cohort mix** (the main hypothesis) | Split August conversion by acquisition source. If non-partner users converted at about 17%, this explains most of the drop. |
| **Pricing link moved to the account menu** | Compare pricing-page views and upgrade clicks per trial user before and after the change date. Check whether non-partner conversion also fell. Note that flat time-to-first-invoice rules out an activation problem, but not a problem at the purchase step. |
| **French holidays** | Look up August conversion from last year. Split August by country: did French users drop while other countries held? Also check whether trials were extended or left to lapse because people were away. |
| **Immature August cohort** (measurement lag) | If trials last 14–30 days, many late-August trials hadn't ended when the month's number was calculated. A spike of partner sign-ups late in the month would make this worse. Recompute August after all its trials have ended and compare cohorts on the same basis: trial start date, same number of days. |

## Confidence level: **Low to medium**

The mix-shift story fits the arithmetic well. But all three changes landed in the same month, and there's no segmented data yet. Right now the four explanations can't be told apart. Several of them may each explain part of the drop.

## Recommended action

**Before Monday (a few queries):**
1. Split August conversion by source: partner vs. everyone else. This one number decides most of the story.
2. Recompute conversion by trial-start cohort, counting only trials that have ended.
3. Pull pricing-page visits and upgrade clicks per trial for the weeks before and after the link moved.
4. Pull last August's conversion rate as a seasonal baseline.

**How to frame it in the meeting:** "The blended conversion rate fell to 12%, but new paying customers were flat while sign-ups grew 40%. We're checking whether this is lower-intent partner traffic, rather than our core funnel getting worse." Don't present any single cause as established until step 1 is done.

**Decisions depending on the result:**
- **Non-partner conversion held at ~17%:** your core funnel is fine. Treat the partnership as a separate channel with its own conversion target and judge it on paid customers and cost, not on the blended rate. Consider tracking the 15% goal on non-partner traffic, or per channel.
- **Non-partner conversion also fell:** look at the pricing link first. It's the only cause you control, and it's cheap to reverse. Put it back in the top nav, ideally as an A/B test, so you know what the move cost.
- **French users and last August both dropped:** it's mostly seasonal. Watch September to see whether conversion recovers.

**What to monitor next:** September conversion by source and by country, and pricing-page views per trial.
