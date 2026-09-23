# Example: five-whys-root-cause

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
Our head of sales wants us to add an "Export to PDF" button on every dashboard in our B2B analytics product. His exact words: "Clients keep asking for PDF exports, we're losing deals without it." Before we commit a sprint to it, help me check it's solving the real problem.
```

## Output

I don't have your deal data, so each answer below is a best guess built on the one before it. Take it into a 20-minute talk with your head of sales and check each step.

## The five whys

**1. Why do clients need a PDF export?**
Probably not to read the dashboard themselves, since they can already do that in the product. They want to **get the numbers to people who never log in**: their execs, their board, their own clients, or a monthly review pack.

**2. Why does that matter to them?**
Our buyer is usually the analyst or ops lead, but the people who approve the budget are those non-users. If insights can't leave the product, the buyer can't show its value to the people who pay for it. So in a sales cycle, "can I export to PDF?" often really means "how do I show my CFO this was worth buying?"

**3. Why hasn't this been solved already?**
The product assumes everyone who sees a dashboard is logged in and exploring. Sharing with people who don't use it isn't a real feature. If seats are paid, adding viewers also costs money. What people do today is screenshot charts into slides every week or month. It works, but it's manual and repetitive, and nobody tells us about it until a prospect asks during evaluation.

**4. Why is it coming up now?**
This is the part to check. Likely causes:
- Bigger deals with more stakeholders, where reporting to leadership is a formal requirement.
- A competitor demoing scheduled reports.
- A procurement or RFP checklist item.

Each needs a different response. "We're losing deals" is also different from "it comes up in deals." Ask which deals, at what stage, and whether PDF was the reason they were lost or just one line on a list.

**5. Why aren't they using what already exists?**
- Browser print breaks the layout.
- CSV export gives raw data when they need a story.
- Screenshots have to be redone every period.
- Nothing arrives on a schedule.

The word that keeps coming up is **recurring**. A one-off PDF button still leaves someone clicking it every Monday.

## Result

**Core job-to-be-done:** When I have to report results to stakeholders who don't use the tool, I want a presentable snapshot delivered to them regularly without manual work, so I can prove the product's value and keep the budget.

**Alternatives to consider:**
1. **Scheduled report delivery.** Email a snapshot of a chosen dashboard (inline image and/or PDF attachment) weekly or monthly to any address. This covers the recurring part that a button doesn't. It's likely the better sprint investment, and PDF generation comes with it.
2. **Free read-only share links or viewer access.** A live, view-only link execs can open without a paid seat. It stays current, and it brings new people into the product, which helps expansion.
3. **A print stylesheet on the 2–3 most-used dashboards.** Days of work instead of a sprint. It clears the checklist item quickly and shows whether the objection disappears or the real request turns out to be scheduling or sharing.

## Before committing the sprint
- Ask sales for **3–5 specific deals** where this came up, with the client's exact words, the deal stage, and the outcome. Check the CRM loss reasons as well.
- In those conversations, ask the prospect: **"Who would you send the PDF to, and how often?"** If the answer is "my VP, every month," that points to alternative 1.
- Drop "every dashboard." Usage data will probably show a few dashboards cover most sharing needs.

My recommendation: do alternative 3 now as a cheap stopgap, and spend the sprint on alternative 1 if the deal review confirms the need is recurring reporting to people outside the product.
