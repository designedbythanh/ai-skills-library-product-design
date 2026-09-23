# Example: user-interview-synthesis

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
I just finished 5 user interviews for our expense-reporting app (used by small companies, 10–50 employees). Product area: submitting expense reports. Here are my raw notes, can you turn them into something the team can act on?

User 1 (sales rep): "I keep receipts in my wallet and do it all at the end of the month. Takes me a whole evening." Lost 2 receipts last quarter, didn't claim them. Uses phone camera but the photo is often blurry, has to retake.
User 2 (office manager, also approves reports): Approves ~40 reports/month. "Half of them come back to me with the wrong category." Spends Monday mornings chasing people on Slack. Would like people to submit weekly.
User 3 (consultant, travels a lot): Submits from hotel at night. "The app logs me out every time, I need to find my password." Foreign currency: types the converted amount herself using Google.
User 4 (engineer, rarely expenses): Only 3–4 expenses a year. "Every time I forget how it works." Didn't know mileage could be claimed.
User 5 (sales rep): Same as user 1, end of month. Says "honestly it's fine, it's just boring." Later mentioned he once paid a €300 client dinner and was reimbursed 7 weeks later, "that hurt."
```

## Output

# Expense submission: synthesis of 5 interviews

**Scope:** 5 interviews: 2 sales reps, 1 office manager who also approves, 1 travelling consultant, 1 engineer who rarely files expenses. Only one person spoke from the approver side, and this is a small sample. Treat these as strong leads, not proven conclusions.

## Top insights (ranked by frequency and impact)

1. **People save all their expenses for month-end, and that one habit causes most of the other problems.**
   - Evidence: U1 and U5 both do everything at the end of the month. For U1 that "takes me a whole evening" and led to 2 lost receipts. U2 gets a surge of reports and "spends Monday mornings chasing people on Slack."

2. **Submitters don't know the rules, and the approver pays for it.**
   - Evidence: U2 says "half of them come back to me with the wrong category." U4 says "every time I forget how it works" and didn't know mileage could be claimed.

3. **Employees are losing money or waiting too long for it.**
   - Evidence: U1 lost 2 receipts and never claimed them. U4 never claimed mileage. U5 waited 7 weeks for a €300 reimbursement ("that hurt").

4. **The mobile app is hardest to use at exactly the moment we want people to use it.**
   - Evidence: U1's receipt photos are often blurry and need retaking. U3 is logged out every time and has to find the password. U3 also converts foreign currency by hand using Google.

5. **Occasional users start from zero every time.**
   - Evidence: U4 files 3–4 expenses a year and relearns the process each time. Nothing in the app reminds them how it works or what they can claim.

## Key frustrations

| Frustration | Evidence |
|---|---|
| Month-end submission takes a whole evening | U1: "Takes me a whole evening"; U5: "it's just boring" |
| Paper receipts get lost before they're logged | U1: lost 2 receipts last quarter |
| Chasing and fixing reports takes up the approver's time | U2: fixes miscategorised reports, spends Monday mornings on Slack |
| Being logged out on every visit | U3: "The app logs me out every time" |
| Converting currency by hand | U3 looks up the converted amount on Google and types it in |
| Photos have to be retaken | U1: blurry photos |
| Slow reimbursement | U5: 7 weeks for €300 |

## Unspoken needs

- **Logging an expense in under 30 seconds, right when it happens.** Batching isn't a preference. U1 and U5 wait for month-end because logging each expense is a chore (blurry photos, logins). If capture were quick, the lost receipts and the long evening would mostly go away.
- **The app should get the category right so people don't have to.** Nobody asked for help choosing categories. But U2's 50% error rate and U4 forgetting the process show people are guessing.
- **Getting their money back quickly.** U5 called the process "fine" but brought up the 7-week wait unprompted. For people who pay out of their own pocket, the wait matters more than how easy the form is.
- **Being told what they're allowed to claim.** U4 missed mileage because nothing mentioned it. Occasional users need the app to point it out.
- **The approver wants a steady flow, not reminders for their own sake.** U2 asked for weekly submission. The real goal is to stop chasing people and fixing errors. A weekly nudge without faster capture would just add more reminders.

## Surprising findings

- **"It's fine" hid a real problem.** U5 rated the process as fine, then described a painful 7-week wait. Satisfaction scores will probably understate the pain, so we should ask about specific incidents, not general satisfaction.
- **The biggest pain may sit outside "submission".** A 7-week delay likely builds up across late submission, then returns and chasing, then approval and payment. That last part is my guess, not something the notes show. Improving the submission screens alone may not move the outcome users care about most.
- **What the approver asked for and what submitters do are in conflict.** U2 wants weekly submissions. Submitters batch because each submission costs effort. Reminders alone probably won't change that.

## Recommended next steps

**Quick wins to check with engineering this sprint:**
- **Session length on mobile.** Find out why U3 is logged out every time. It could be a bug or a security setting. Consider longer sessions or biometric login.
- **Automatic currency conversion** using the rate on the expense date.
- **Warning on blurry photos** at the moment of capture, before the user leaves the screen.

**Validate with data we already have:**
- Median time from expense date to submission. Does month-end batching show up across all users?
- Share of reports sent back, and which categories get mixed up most.
- Time from expense to reimbursement, split into stages (submit → approve → paid) to see where the 7 weeks goes.
- How many eligible users have never filed a mileage claim.

**Further research:**
- Interview 3–4 more approvers. We have only one, and their pain drives several of these insights.
- Test a "log it now, submit later" prototype (photo → automatic category → saved as draft) with the two sales reps. Does it change when they log expenses?
- Talk to finance/payroll to learn how reimbursements get paid out (payroll cycle vs. on demand). This decides whether faster submission actually speeds up payment.

**Main bet to discuss with the team:** move the product from "fill in a form at month-end" to "log each expense the moment it happens, with the app filling in category and currency." It targets insights 1–4 together.

I can turn this into a shareable doc, or run `/prd-first-draft` on the "log it now" direction.
