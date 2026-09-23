# Example: design-critique-facilitator

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
I'm presenting this design for feedback on Thursday and I'd like a structured critique instead of vague opinions.
Design: the home screen of a clinic's staff app, used by receptionists.
Goal: let a receptionist see at a glance who is arriving next and who is late, and check someone in with one tap.
Target user: receptionists in small medical clinics, often interrupted by phone calls, using a desktop screen at the front desk.
Stage: mid-fidelity.
Description: a left sidebar with navigation (Today, Calendar, Patients, Billing, Settings). The main area shows today's appointments as a table sorted by time: time, patient name, practitioner, status (Scheduled / Arrived / Late / No-show) as colored dots only. A "Check in" button appears on hover on each row. A large search bar sits at the top. A statistics card on the right shows "Appointments today", "No-show rate", and "Revenue this week".
```

## Output

🎯 **Goal:** A receptionist who has just been interrupted should be able to glance at the screen, see who's next and who's late, and check a patient in with one click.

---

## 1. Clarity: does the user immediately understand what to do?

✅ **Working**
- Putting today's appointments in the main area is the right choice. It's the screen's reason to exist, and it gets the most space.
- Time, patient, practitioner and status are the right columns for front-desk work. There's nothing extra in the table.

⚠️ **Needs attention**
- **The main action is hidden behind hover.** Nothing tells a receptionist that "Check in" exists until they move the mouse over a row. That makes it two steps (find the row, hover, then click), and it disappears on touch screens, which some front desks use.
  💡 Show a "Check in" button on every row whose status is Scheduled or Late. Once someone has arrived, replace the button with the arrival time ("Arrived 9:42"). The button should appear only where it's actually needed.
- **Status is shown by color alone.** About 1 in 12 men has some form of color blindness, and red and green dots also look alike at a glance on a bright monitor. It also fails WCAG 1.4.1 (Use of Color).
  💡 Pair each dot with a text label, e.g. "● Late · 12 min". For "Late", show how late: "Late" tells the receptionist less than "Late · 12 min" does.
- **"Who is next" isn't answered.** A table sorted by time mixes past, current and future rows equally. After a phone call, the receptionist has to scan the whole list to find where they are.
  💡 Add a current-time line across the table, and scroll to it automatically when the screen loads or regains focus. You could also put a small "Up next" strip above the table showing the next 2–3 arrivals.

## 2. Hierarchy: does visual weight match priority?

✅ **Working**
- The sidebar is secondary, which is correct. Navigation isn't the job on this screen.

⚠️ **Needs attention**
- **Late patients get the same weight as everyone else.** "Who is late" is half the goal, but a late patient is just a dot inside a time-sorted list, and may already have scrolled out of view.
  💡 Pin late patients to the top in a "Needs attention" group, or give their whole row a tint as well as the text label. Being late is the exception the screen should call out.
- **The large search bar competes with the table.** It's the most prominent element, but the goal is glancing at the schedule, not searching.
  💡 Keep search, since receptionists do look people up when a patient calls or walks in, but make it normal size and give it a keyboard shortcut (e.g. `/`). If walk-in check-in through search turns out to be a main flow, that's a reason to keep it large. See the open questions below.
- **The statistics card uses valuable space on the wrong audience.** "Revenue this week" and "No-show rate" are clinic-manager metrics. They don't help anyone check a patient in, and they take the right-hand column, where the eye goes after the table.
  💡 Use that column for a **"Waiting room"** panel: arrived patients, who they're seeing, and how long they've waited (e.g. "Sam K. · Dr Lee · waiting 18 min"). That's the receptionist's second most frequent question. Move the stats to a manager dashboard or to Billing.

## 3. Consistency: does it follow established patterns?

✅ **Working**
- A left sidebar with a table is a familiar desktop admin layout, so there's nothing new to learn.
- Four fixed status values give you a clear vocabulary.

⚠️ **Needs attention**
- **The status list stops at arrival.** Scheduled, Arrived, Late and No-show cover the time before the visit, but not "In consultation", "Done" or "Cancelled". If the practitioner's side of the app uses those states, this screen will disagree with it.
  💡 Map out the full lifecycle of an appointment once, then decide which states this screen shows and which it combines. For example, Done could be shown greyed out.
- **"Today" and "Calendar" overlap.** Today is presumably the calendar filtered to today. If the two screens show the same appointments in different formats, receptionists have to learn both.
  💡 Either make Today a clearly different view (a live front-desk list) with a "Today" button on Calendar, or reuse the same row component and status labels in both screens.
- **Hover-reveal actions:** Check whether other tables in the app use this pattern. If this is the only one, it's inconsistent. If they all do, the problem above applies to all of them.
  💡 Make a system-wide rule: actions a user takes often are always visible, and only secondary actions hide behind hover or a "⋯" menu.

## 4. Edge cases: which states are missing?

⚠️ **Needs attention**, with a 💡 suggestion for each:

| State | Risk | Suggestion |
|---|---|---|
| **Wrong check-in** | One click on a crowded table is easy to get wrong, and a wrong status misleads practitioners | A toast after checking in, "Checked in Maria Lopez · Undo", visible for about 8 seconds |
| **Check-in fails** (network, server) | The receptionist believes it worked, but the practitioner is never notified | Show the row as pending until the server confirms. If it fails, show an error on that row with "Retry", not only a toast that disappears |
| **Stale or offline data** | "Late" depends on the current time. A frozen screen shows wrong statuses with full confidence | "Updated 2 min ago" indicator, plus an offline banner if the connection drops |
| **Two receptionists at once** | Both check in the same patient, or one marks No-show while the other checks in | Update rows live, and show "Already checked in by Anna at 9:41" |
| **Empty day / clinic closed** | A blank table looks like a loading error | "No appointments today" with a link to Calendar |
| **Loading** | A layout jump when the table appears loses the receptionist's place | Skeleton rows with the same height as real rows |
| **Patients with the same name** | The wrong John Smith gets checked in | Show a second identifier (date of birth or last 4 digits of phone) on the row or in the hover |
| **Walk-in / no appointment** | There's no row to check in | An "Add walk-in" action next to search |
| **Early arrival** | The patient's row is far down the list | Search → check in should work for any row, and scroll to that row |
| **Late → arrives / No-show rules** | When does Late become No-show? Automatically or by hand? | Define the threshold and allow a manual override. Let a late patient be checked in directly |
| **Permissions** | Receptionists may not be allowed to see revenue | Another reason to remove the stats card. At minimum, hide revenue based on role |
| **Busy day (40+ rows)** | "At a glance" stops working | Filter by practitioner, collapse or grey out finished appointments, keep the header visible when scrolling |

---

## Top 3 priorities before the next review
1. **Make check-in visible and one click, with undo.** Show the button on every row that needs it, and add Undo and a failure state.
2. **Make "late" and "next" stand out without scanning.** Use text labels plus color ("Late · 12 min"), a current-time line with auto-scroll, and put late patients at the top or tint their rows.
3. **Replace the statistics card with a Waiting room panel.** It serves the receptionist, and it avoids exposing revenue to the wrong role.

## Open questions for the designer
- Have you watched receptionists work? How often do they look people up by name compared with scanning the list? The answer decides how prominent search should be.
- Is the front-desk screen ever a touchscreen or tablet? If so, hover-reveal actions have to go.
- What happens after check-in? Is the practitioner notified, and does this screen need to show that the notification went through?
- Who defines "Late" and "No-show": fixed thresholds, per-clinic settings, or manual marking?
- Is one receptionist usually handling several practitioners at once? If so, do they need to filter or group the list by practitioner?
- Why did the statistics card make it into this screen? If a stakeholder asked for it, it's worth knowing before Thursday, since removing it may need some argument.

For Thursday, it may help to present this as a **30-second interruption test**: a receptionist looks away for a phone call, then looks back. Can they tell who's next and who's late in under 3 seconds? That gives reviewers a concrete test to judge the design against instead of trading opinions.
