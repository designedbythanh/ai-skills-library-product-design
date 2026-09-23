# Example: explain-to-4-audiences

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
We made a design decision and I need to explain it to different people before we ship: we're replacing our 5-step sign-up wizard (company info, team size, role, goals, integrations) with a single screen that asks only for an email address. Everything else will be asked later, in context, when it's actually needed.
```

## Output

🧒 **10-year-old:** Imagine a new club that makes you fill out five pages about yourself before you're allowed through the door. Most kids would give up and go home. Now we just ask your name at the door and let you in, and we ask the other questions later, like "want to join the soccer team?" when you walk past the soccer field.

⚙️ **Engineering team:** Sign-up now creates an account from an email alone, so company, team size, role, goals, and integrations all become nullable. Every flow that currently assumes those fields exist needs a fallback: onboarding personalization, default workspace setup, analytics segmentation, and any CRM or sales-routing sync. We're replacing one blocking funnel with several small prompts that fire when a user first needs the thing, so each prompt needs a trigger condition, a "skip" state, and a rule so we don't nag someone who has already answered or dismissed it.

📊 **CEO/Executive:** Each step in the wizard is a point where signups drop off, and we're asking for five things before anyone has seen the product. Cutting to one field should get more people through the door. The questions don't go away; we ask them when the answer changes what the user sees, so the data we get should be more honest. The trade-off is that sales and marketing lose lead-qualification data at signup, so we should agree now how they'll segment and route new accounts in the meantime.

👤 **End user:** You can start with just your email. There are no forms about your company or your goals to get through before you've seen anything. When you go to connect a tool or invite your team, we'll ask what we need right there, and by then you'll know why we're asking.

**Clarity check:** Two of these were harder to write than they should have been, and both point to open questions in the design, not the wording:

- **Engineering:** "asked later, in context" isn't specified yet. For each of the five fields, the team needs to know which moment triggers the question, what the product does if the user skips it, and whether it's ever required. Without that, everyone will build their own version.
- **Executive:** I couldn't honestly state the ROI. I don't have your current drop-off rate per wizard step, and I don't know how much sales depends on the company and team-size fields. Get those two numbers before this goes to leadership, or the first question in the room ("what does sales lose?") won't have an answer.

The 10-year-old and end-user versions came easily, which suggests the user-facing idea is clear. The unfinished parts are the internal plumbing and who owns the data you'll no longer collect at signup.
