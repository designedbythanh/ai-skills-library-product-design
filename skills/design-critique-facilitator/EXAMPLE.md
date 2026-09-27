# Example: design-critique-facilitator

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-26 with the v1.1.0 draft of this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.
> Same prompt as the [v1.0.0 example](https://github.com/designedbythanh/ai-skills-library-product-design/blob/v1.0.0/skills/design-critique-facilitator/EXAMPLE.md), so the two can be compared ([eval](EVAL.md)). Two accidental pastes (the launch command, and the answers sent a second time) are left out. After this run, the owner tag gained a fourth value, "design + dev".

**What to notice:**
- The skill asks four questions before critiquing, even though the prompt already gives the goal, the user and the stage. It wants what the prompt can't give: what's decided, what's open, and what worries the designer.
- It answers the designer's open question (group late patients or keep time order?) with a reason taken from their own answers.
- It keeps the stats card the clinic owners asked for, because that's decided, and critiques where it sits instead.

## Prompt

```text
I'm presenting this design for feedback on Thursday and I'd like a structured critique instead of vague opinions.
Design: the home screen of a clinic's staff app, used by receptionists.
Goal: let a receptionist see at a glance who is arriving next and who is late, and check someone in with one tap.
Target user: receptionists in small medical clinics, often interrupted by phone calls, using a desktop screen at the front desk.
Stage: mid-fidelity.
Description: a left sidebar with navigation (Today, Calendar, Patients, Billing, Settings). The main area shows today's appointments as a table sorted by time: time, patient name, practitioner, status (Scheduled / Arrived / Late / No-show) as colored dots only. A "Check in" button appears on hover on each row. A large search bar sits at the top. A statistics card on the right shows "Appointments today", "No-show rate", and "Revenue this week".
```

## The skill asks first

Before I start the critique I need a few things from you. The skill starts from your own intent and concerns, and I can't guess those from the description.

1. **Your concerns.** What made you want a critique? Is there a part of this screen you're unsure about or expect pushback on?
2. **Decided vs. open.** Which parts are already settled (for example the sidebar nav, the table format, or the stats card) and which are still open to change?
3. **What to compare against.** Is there a design system or component library, or sibling screens like Calendar and Patients, it should match? A competitor or current tool the receptionists use would also help.
4. **Your intent for a few specific choices.** You may want to cover these in your answer to question 1:
   - Is showing status as colored dots only (no text labels) deliberate?
   - Is "Late" set automatically, for example X minutes after the appointment time, or by staff?
   - Who is the stats card for: the receptionist, or a clinic manager who also uses this screen?

**My one assumption so far:** this is a single-clinic view on a standard desktop monitor, used with a mouse. That matters for the "Check in" button, which only appears on hover.

Once you reply, I'll run the critique through all five lenses (clarity, hierarchy, consistency, interaction and feedback, edge cases) and finish with your top 3 priorities for Thursday.

## Designer's answers

```text
Decided: it's a desktop web app; check-in happens from this screen; the stats card is requested by clinic owners and stays somewhere.
Open: whether late patients get their own group or stay in time order.
My concerns: receptionists get interrupted constantly and lose their place; I'm not sure the hover-only Check in button is discoverable.
Compare with: the Calendar screen of the same app (same table style and status dots).
Dots only: not deliberate, it's mid-fidelity.
Late: set automatically, 10 minutes after the appointment time.
Stats card: for the clinic owner, who sometimes looks at this screen.
```

## Output

# Design critique: Receptionist home screen ("Today")

🎯 **Goal reminder:** A receptionist who keeps getting interrupted should be able to glance at the screen, see who is arriving next and who is late, and check a patient in with one tap.

📋 **Assumptions:** I haven't seen the screen, so this critique works only from your description. I'm assuming a mouse on a standard monitor, one clinic, several practitioners, and a front-desk screen that patients can sometimes see.

---

### 1. Clarity
✅ **Working**
- A single table sorted by time fits how receptionists think about their day.
- Setting "Late" automatically at +10 minutes means the receptionist never has to track the time themselves.

⚠️ **Needs attention**
- **You asked: the hover-only "Check in" button.** Your worry is justified. A button that only appears on hover can't be seen at a glance, so the screen doesn't show which rows still need action. The receptionist also has to hunt for it with the mouse, often while on the phone.
  💡 Show "Check in" permanently, but only on rows that can still be checked in (Scheduled and Late). On Arrived rows, replace it with plain text such as "Arrived 9:02". The column then shows who still needs to be checked in without any extra element. `major · design-only · known (your concern)`
- **The screen doesn't answer "who is next?"** The table lists the whole day, so by 11:00 the next arrivals sit below a list of finished rows.
  💡 Add a "Now" line in the table. Scroll to it when the page loads, and collapse past rows that are already done into a "Earlier today (12)" group. `major · design-only · new`
- **Color is the only thing showing status.** People with color blindness can't tell the statuses apart, and nobody can read them at a distance.
  💡 Pair each dot with a text label, and add an icon or shape for Late. `major · design-only · known (you confirmed it's a mid-fi gap)`

### 2. Hierarchy
✅ **Working**
- The appointments table is the main area, which matches the goal.

⚠️ **Needs attention**
- **The large search bar is the strongest element on the screen, but it's a secondary task.** Search is useful for "Is Mrs. X booked today?" calls, but it shouldn't pull the eye away from what's next and who's late.
  💡 Make it normal size, keep it at the top, and give it a keyboard shortcut (`/` or Ctrl+K) so it stays fast to reach while on the phone. `minor · design-only · new`
- **The stats card takes the prime right-hand column, but it serves an occasional viewer (the owner).** "Revenue this week" on a front-desk screen could also be seen by patients standing at the desk.
  💡 The card stays, since that's decided, but shrink it to a collapsible strip or move it below the fold. Consider hiding revenue by default or showing it only to the owner role. `major · design-only for placement / needs product decision for revenue visibility · new`
- **Your open question: group late patients, or keep time order?** I recommend keeping time order and not moving late patients into their own group. Late status is set automatically, so a separate group would make a row jump to another place at +10 minutes, possibly just as the receptionist goes to click it. That's the "lost my place" problem you're worried about.
  💡 Keep late rows where they are and style them strongly: a tinted row with a label. Add a "2 late" chip above the table that scrolls to or highlights those rows. `major · design-only · new`

### 3. Consistency
✅ **Working**
- It reuses the Calendar table style and status dots, so receptionists learn one visual language.

⚠️ **Needs attention**
- **Adding text labels to statuses here will create a mismatch with Calendar.**
  💡 Build status as one shared component (dot + label) and update Calendar at the same time. `minor · needs dev · new`
- **Status list:** four statuses may not cover the whole visit. Does Calendar have states like "In consultation", "Done" or "Cancelled"?
  💡 Both screens should use the same status list. If there's no "Done" status, a patient who has left stays "Arrived" and clutters the view of who is waiting. `minor · needs product decision · new`

### 4. Interaction & feedback
✅ **Working**
- One-tap check-in directly from the list, with no extra screen, is the right weight for this task.

⚠️ **Needs attention**
- **You asked: interruptions and losing their place.** Nothing described helps someone who comes back after a call.
  💡 Keep the row being worked on (selected or last-touched) highlighted after the receptionist looks away. Never re-sort or auto-scroll while the pointer is over the table. Add a small "Recent actions" list, e.g. "Checked in J. Ramos, 9:02", so they can see what they did before the call. `major · design-only (live-update behavior needs dev) · known (your concern)`
- **No feedback or undo after check-in.** An interrupted user mis-clicking the row next to the right one is the most likely error on this screen.
  💡 On check-in, update the row in place (status + time) and show a toast like "Checked in Maria Lopez · Undo" for about 10 seconds. Also make an Arrived patient reversible from the row. Don't add a confirmation dialog, which would slow down the common case. `major · design-only · new`
- **Search behavior is undefined.** If search navigates to Patients, the receptionist loses their spot in today's list.
  💡 When the query is typed, filter today's table in place first, and link to "Search all patients" as a second option. `minor · design-only · new`

### 5. Edge cases
⚠️ **Needs attention**
💡 For each of these, add a state or a rule:
- **Two patients with the same or similar name at close times.** The receptionist could check in the wrong person. Show date of birth or another identifier on hover or in the row. `major · design-only · new`
- **Check-in fails because of a network or server error.** The row must not look like Arrived. Show an inline error with Retry. `major · needs dev · new`
- **A late patient arrives.** Check-in must still work from Late. Should the arrival time show as late for the record? `minor · needs product decision · new`
- **No-show:** is it set automatically or by staff, and can it be reversed when the patient turns up? `major · needs product decision · new`
- **Walk-ins or patients not on today's list.** There's no path for them from this screen. Add "Add walk-in" near the table. `minor · needs product decision · new`
- **Empty day, clinic closed, loading, end of day with everyone done.** Each needs its own state. `minor · design-only · new`
- **Busy day** (40+ rows, several practitioners): consider a practitioner filter. Also check long names and overlapping slots. `minor · design-only · new`

---

### Top 3 priorities before Thursday
1. **Make "Check in" always visible on actionable rows, and add in-row feedback plus Undo.** This answers both of your concerns directly.
2. **Anchor the view on "now".** Add the Now line, collapse past rows, keep late patients in time order with a "late" chip, and never reshuffle rows under the user's cursor. That settles your open question.
3. **Rebalance the hierarchy.** Add text labels to statuses, reduce the search bar, and demote the stats card, with a decision on whether revenue should show at the front desk.

### Not checked
- **The screen itself:** I worked only from your written description, so I couldn't judge spacing, contrast, type sizes or real density.
- **The Calendar screen:** I haven't seen it, so the consistency findings are based only on your note that it shares the table style and dots.
- **Missing states:** no loading, empty, error or permission states were described.

### Open questions for you
- Can patients see the front-desk screen? This decides how prominent revenue, and even full patient names, should be.
- Who sets No-show, and when? Can it be undone?
- Does the receptionist need to see only today, or also tomorrow's first appointments at the end of the day?
- Is there a "Done" or "Left" status after the consultation, or does "Arrived" last until the end of the day?
- Do receptionists use the keyboard a lot? If so, keyboard check-in could beat one-tap: arrow keys to move between rows and Enter to check in.
