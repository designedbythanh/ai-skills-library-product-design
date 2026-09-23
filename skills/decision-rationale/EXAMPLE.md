# Example: decision-rationale

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
I need to decide between two directions and write down a defensible rationale for my team.
Option A: build a native mobile app (iOS + Android) for our invoicing tool for freelancers.
Option B: spend the same time making the existing web app fully responsive and fast on mobile browsers (plus add-to-home-screen).
Constraints and goals: 2 frontend engineers, one quarter. 35% of sessions are already on mobile, mostly to check whether an invoice was paid and to send reminders; creating invoices happens mostly on desktop. Goal: raise weekly active usage on mobile. No one on the team has shipped a native app before.
```

## Output

# Native app vs. mobile web for the invoicing tool

## Recommendation

- **Option:** B, a responsive and fast mobile web app that can be added to the home screen.
- **Confidence:** about 80%.
- **Key reason:** Your mobile users do two small, repeated tasks (checking whether an invoice was paid and sending a reminder). B makes those better for every mobile user this quarter, with no install step. A asks two engineers who have never shipped a native app to build and maintain two new platforms in 13 weeks.

## The decision

Build native iOS and Android apps (A), or make the existing web app fully responsive and fast on mobile with add-to-home-screen (B). You have 2 frontend engineers for one quarter. The goal is more weekly active users on mobile.

**What the goal depends on:** Mobile use is about checking status and sending reminders, not building invoices. So weekly usage will depend less on whether an app exists and more on two things:
- how quickly and easily those two tasks can be done on a phone
- whether something brings people back, mainly a "you got paid" or "invoice overdue" alert

## 1. Five criteria (scored 1–10)

| # | Criterion | A: Native | B: Mobile web | Reasoning |
|---|---|---|---|---|
| 1 | **Fit to the actual mobile tasks** | 8 | 8 | Both can do "is it paid?" and "send reminder" well. These are simple list and action screens that don't need native-only features like the camera, offline editing or heavy gestures. Tie. |
| 2 | **Delivery risk (2 engineers, 1 quarter, no native experience)** | 3 | 8 | A means a new codebase or a new framework (React Native or Flutter), app store accounts and review, native login and session handling, and release pipelines for two platforms. Teams doing this for the first time usually lose weeks to setup and store review. B builds on skills and code the team already has. |
| 3 | **Bringing users back (notifications, home-screen icon)** | 9 | 6 | This is A's real advantage. Native push is reliable and people know it. B can do web push: fully on Android, and on iOS only after the user adds the app to the home screen (iOS 16.4+). Opt-in on iOS will be lower. |
| 4 | **Reach across the existing 35% mobile traffic** | 4 | 9 | B improves every current mobile session on day one, with no install. A only helps users who find and install the app, and that is usually a minority of an existing web user base. The rest see no change. |
| 5 | **Ongoing cost and reversibility** | 3 | 8 | A leaves you with three things to maintain (web, iOS, Android) and a lasting pull on 2 engineers. B's work also improves the desktop product, and B doesn't rule out going native later. |
| | **Total** | **27** | **39** | |

## 2. Three scenarios

| Scenario | A: Native | B: Mobile web |
|---|---|---|
| **Best case** | Both apps ship in about 10 weeks. Push alerts for "paid" and "overdue" drive frequent opens, and mobile weekly usage rises sharply among users who install. | The mobile experience is fast and clean. Android users and iOS users who install get alerts. Mobile weekly usage rises across the whole mobile base, and the team still has time left for extra polish. |
| **Most likely** | One platform ships near the end of the quarter, or both ship thin. Store review and learning the new stack take up the buffer. Few existing users install, so mobile weekly usage barely changes this quarter. Maintenance cost starts right away. | The responsive and performance work ships by mid-quarter. Web push works on Android. iOS opt-in is limited by the install step, but email or SMS alerts that link straight into the fast mobile view cover the gap. Mobile weekly usage rises modestly and measurably. |
| **Worst case** | Neither app is store-ready by the end of the quarter. The web app got no mobile work during that time. You end with sunk cost and no gain in weekly usage. | The mobile improvements ship but weekly usage barely moves, because the mobile experience wasn't what held usage back. You still keep a better product, and you learn that the lever is elsewhere. |

B's worst case is much milder than A's. A's most likely case also delivers less than B's.

## 3. The deciding question: what would have to be true?

- **To choose A confidently:** someone on the team can ship a store-quality app on two platforms within one quarter, *and* a large share of current mobile users would install it, *and* push notifications (which B can't provide on iOS without an install) are the main thing holding back mobile weekly usage. **The first condition is unlikely** given that no one has shipped native before. All three together are very unlikely. **A is eliminated for this quarter.**
- **To choose B confidently:** the current mobile web experience is actually slow or awkward, *and* useful alerts can be delivered well enough through web push, email or SMS. The first is plausible because you're considering this work at all. The second is achievable. **Both are plausible, so choose B.**

## What would lower my confidence

- **The mobile web experience is already decent.** If so, B's main gain shrinks, and the real lever is notifications. B still wins then, but the quarter's work should shift toward the alert system.
- **Most mobile users are on iOS.** Then web push reach is smaller. It's still worth checking the iOS share in your analytics.

## Suggested next step

In week 1, do three things:
1. Record current mobile weekly usage, mobile load times, and time-to-complete for "check paid status" and "send reminder."
2. Pull the iOS vs. Android split for mobile sessions.
3. Scope a "payment received / invoice overdue" alert (web push on Android and installed iOS, email everywhere) that links straight into the mobile view.

Then set a trigger for reconsidering native: if installed users keep coming back much more than non-installed users, and low iOS push opt-in is clearly the bottleneck, look at a native app next quarter, starting with a thin wrapper around the web app.
