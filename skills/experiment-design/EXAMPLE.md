# Example: experiment-design

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
I want to run an A/B test and need a proper plan.
Hypothesis: "We believe that showing a preview of the finished invoice while the user fills in the form will increase the share of new users who send their first invoice, because they'll feel more confident about what the client receives."
Change being tested: live preview panel on the invoice creation page (desktop only).
Available traffic: about 1,200 new sign-ups per week, of which about 70% reach the invoice creation page on desktop.
Primary metric: % of new users who send their first invoice within 7 days of sign-up (currently 41%).
```

## Output

# Experiment plan: live invoice preview

**Short version:** You can run this test, but only if you're looking for a lift of about **4 percentage points or more** (41% → 45%). That takes about 6 weeks of enrolment plus a 1-week wait for the metric to mature. With your traffic, a lift of 2 points can't be measured in any reasonable time.

---

**Experiment name:** `invoice-live-preview-desktop`

**Hypothesis:** If we show a live preview of the finished invoice next to the creation form on desktop, the share of new users who send their first invoice within 7 days of sign-up will go up by at least 4 percentage points (41% → 45%, about 10% relative). The reason is that seeing what the client will receive reduces uncertainty just before sending.

**Control / Variant**
- **Control:** the current invoice creation page, with no preview.
- **Variant:** the same form, plus a live preview panel that updates as the user types. Everything else stays the same: fields, order, CTA copy and where the Send button sits.

**Audience**
- **Who:** new users on their first visit to the invoice creation page on desktop. They're assigned at that moment, not at sign-up. Assigning at sign-up would add the ~30% who never see the change and weaken the result.
- **Split:** 50/50, randomised per user and sticky across sessions.
- **Exclusions:** existing users, mobile and tablet visits, internal and test accounts, and users invited into an existing workspace (their "first invoice" behaviour is different).
- **Analysis:** intent-to-treat. A user assigned on desktop who later sends from mobile still counts in their assigned group.

**Duration and the maths behind it**

Eligible traffic is about 1,200 × 70% = **~840 users a week**, or ~420 per group. The table assumes a two-sided test, α = 0.05, 80% power and a 41% baseline:

| Lift you want to detect | Users per group | Total | Enrolment weeks |
|---|---|---|---|
| +2 pp (41→43%) | ~9,550 | ~19,100 | **~23 weeks** ❌ |
| +3 pp (41→44%) | ~4,250 | ~8,500 | ~10 weeks ⚠️ |
| **+4 pp (41→45%)** | **~2,400** | **~4,800** | **~6 weeks** ✅ |
| +5 pp (41→46%) | ~1,540 | ~3,080 | ~4 weeks |

- **Recommended:** 6 full weeks of enrolment, then 7 more days so the last users enrolled get their full 7-day window. That's **about 7 weeks** before the readout.
- **Why not shorter:** stopping early leaves the test underpowered for a 4 pp lift. A real effect of that size would be missed about half the time, and a "significant" early result is more likely to be noise or a novelty effect. Running whole weeks also evens out weekday patterns in invoicing.
- **Plain warning:** if the team expects the preview to add only 1–2 points, **this test isn't worth running as designed**. You'd need about 5+ months of traffic. In that case, measure the leading indicator below, bundle the preview with a bigger onboarding change, or ship it as a low-risk UX improvement without an A/B test.

**One thing to check before launch:** the 41% baseline is for *all* new users. Among users who actually reach the page on desktop, the rate is probably higher, maybe 50–58%. Pull that figure and rerun the calculation. Sample sizes stay about the same in that range, but the lift you're aiming for should be based on the right baseline.

**Success criteria**
- **Primary:** first invoice sent within 7 days of sign-up, among triggered users, goes up by ≥4 pp at 95% confidence (two-sided).
- **Leading indicator (diagnostic only):** form-start → send completion rate within the first session. It reacts faster and helps explain *why* the primary metric moved.
- **Counter-metrics (none may drop significantly):**
  - Median time from form start to send (the preview could add hesitation)
  - Invoices edited, voided or re-sent within 48 hours (a proxy for errors)
  - Invoice page load time and front-end errors (a live render is extra weight)
  - Support tickets about invoice creation
  - Downstream: 7-day retention or trial-to-paid, if you can read it in the window

**Risks and mitigations**
- **Wrong baseline or analysis population:** fix the triggered population and its baseline before launch, and write them into the pre-registration.
- **Peeking or stopping early:** fix the end date in advance and don't make ship decisions from mid-test dashboards. If you need interim looks, use a sequential method (e.g. group sequential with O'Brien–Fleming bounds).
- **Sample ratio mismatch (e.g. the variant's page crashes or loads slowly and some users drop out before assignment is logged):** run an SRM check (χ² on group counts) every week. If p < 0.001, stop and debug.
- **Novelty effect:** compare the lift in weeks 1–2 with weeks 5–6.
- **Performance regression making the variant look worse:** load-test the preview before launch and watch p75 page load time.
- **Cross-device leakage:** mobile users won't see the preview. Intent-to-treat handles this, and you can report the share of desktop-assigned users who sent from mobile.
- **Seasonality or marketing changes during the 7 weeks** (for example a campaign that brings in a different kind of sign-up): randomisation protects the comparison, but log any campaigns so you can segment afterwards.
- **Small segments:** don't draw conclusions from segment cuts like plan type or country. They're far too small at this traffic and should be treated as ideas to explore, not findings.

**Decision rule** (agreed before launch)
- **Ship if** the primary metric rises by ≥4 pp at 95% confidence (or the lower bound of the confidence interval is > 0 and the point estimate is ≥ ~3 pp), and no counter-metric drops significantly.
- **Roll back if** the primary metric is significantly lower, any guardrail drops significantly (especially errors, re-sends or load time), or SRM shows up and can't be explained.
- **Iterate if** the result is flat or inconclusive (CI includes 0) but the leading indicator improves. That suggests the preview helps within a session but something else, like client details or payment setup, is blocking the send. Look at where users drop off in the funnel and test that. If the result is flat and there are no guardrail problems, you can still ship it for UX reasons, but don't claim it moved activation.

I can turn this into a pre-registration doc or a Notion page.
