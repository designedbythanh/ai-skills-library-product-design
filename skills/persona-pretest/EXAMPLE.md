# Example: persona-pretest

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
Before we pay for a usability study, I want a fast sanity check on our new onboarding flow by seeing it through a specific user's eyes.
Persona: Marie, 52, runs a small bakery with 3 employees. Uses her phone for everything, rarely a laptop. Low patience for tech, has been burned by "free trials" that charged her. Goal: stop doing staff schedules on paper.
Flow (mobile web, shift-scheduling app): 1) Landing page: "Schedule your team in 5 minutes", button "Start free trial". 2) Sign-up form: email, password, company name, company size, credit card ("You won't be charged for 14 days"). 3) "Add your team": enter each employee's name + phone number. 4) Empty weekly calendar with a tooltip "Drag to create a shift". 5) "Publish schedule" button sends an SMS to each employee.
```

## Output

**Persona:** Marie, 52, owns a bakery with 3 employees. She does everything on her phone, has little patience for tech, and has been charged by "free trials" before. She wants to stop doing staff schedules on paper.

---

### Step 1: Landing page, "Schedule your team in 5 minutes" / "Start free trial"

- 👀 **Notices:** "5 minutes" catches her eye first. Then "free trial" makes her tense up.
- 🤔 **Expects:** Some pictures of what the schedule looks like and a price, before anything asks her for information.
- ⚠️ **Friction:** "Free trial" is the phrase that cost her money before. She can't see a price on the page, so she doesn't know what happens when the trial ends. She'll scroll looking for a price and might leave if she doesn't find one.
- 💬 **Says:** *"Free trial, sure. How much is it after? Why won't they just tell me?"*

### Step 2: Sign-up form (email, password, company name, company size, credit card)

- 👀 **Notices:** The credit card field. Everything else on the form hardly registers.
- 🤔 **Expects:** Her email and a password, then being allowed to try it.
- ⚠️ **Friction:**
  - The card field on its own is where she's most likely to quit. "You won't be charged for 14 days" means to her that she *will* be charged on day 15. She wants to know if she gets a reminder and how she cancels, and the form tells her neither.
  - "Company size": does she count herself? She'd pick "1–10" or whatever the lowest option is, and it bothers her a little that they're asking.
  - Typing a card number on her phone means standing up, finding her purse, and typing with her thumbs in the middle of her day.
  - It's a long form for something that promised 5 minutes.
- 💬 **Says:** *"No. I'm not giving my card to try a calendar. That's exactly how they got me last time."* If she keeps going, it's only because she's desperate: *"Fine, but I'm setting an alarm to cancel."*

### Step 3: "Add your team" (name + phone number for each employee)

- 👀 **Notices:** This is finally about her bakery and her people, so it feels like progress.
- 🤔 **Expects:** To type three names and be done. Ideally she could pick them from her phone contacts, since their numbers are already there.
- ⚠️ **Friction:**
  - She has to switch between the contacts app and the browser to copy each number. On a phone that's slow and easy to get wrong.
  - She's unsure about giving out her staff's phone numbers. She wonders if they'll get marketing texts and whether her employees will be annoyed with her.
  - She doesn't know if she should add herself too. She works shifts as well.
- 💬 **Says:** *"Do I put myself in? And they're not going to spam Sophie, are they?"*

### Step 4: Empty weekly calendar, tooltip "Drag to create a shift"

- 👀 **Notices:** A big empty grid squeezed onto a small screen, plus a tooltip she reads quickly and doesn't really take in.
- 🤔 **Expects:** To tap a day and have it ask who's working and from when to when.
- ⚠️ **Friction:**
  - "Drag" on a phone is where she gets stuck. When she drags, the page scrolls instead. She tries long-pressing and nothing happens, or the wrong thing happens.
  - The week view is either tiny or needs sideways scrolling, and bakery hours start at 5 or 6 a.m., which may be off the top of the screen.
  - The calendar is empty. On paper, she'd just copy last week's schedule. Here she has to build the whole week from nothing, and the "5 minutes" promise feels broken.
  - She can't tell how a shift gets tied to a person. Does she drag first and pick a name after?
- 💬 **Says:** *"Drag what? It just keeps scrolling. On paper I'd have been done by now."*

### Step 5: "Publish schedule" sends an SMS to each employee

- 👀 **Notices:** The word "Publish". It sounds public and final.
- 🤔 **Expects:** To see the whole week one more time before anyone gets anything.
- ⚠️ **Friction:**
  - The texts go out right away and she can't see what they'll say. She's worried about mistakes going to her staff.
  - She doesn't know what happens if she changes a shift later. Does everyone get texted again?
  - Her employees now get texts from a number they don't know, and she'll be the one who hears about it.
- 💬 **Says:** *"Wait, does it send right now? What does the message say? I don't want Karim thinking it's a scam."*

---

### Would she finish?

**No, most likely.** She quits at Step 2. The credit card field lands on the exact thing that burned her before, and she hasn't seen any value or any price yet. If she's desperate enough to get past it, she gets stuck again at Step 4, because dragging on a phone doesn't work well, and she'll probably give up there with an empty schedule and go back to paper.

### Top 3 fixes before real user testing

1. **Remove the credit card from sign-up, or deal with her fear head-on.** The best option is letting her create and publish a first schedule with no card. If the card has to stay, show the price on the landing page, promise a reminder before day 14, and offer one-tap cancel. The form should be just email and password; ask for company name and size later.
2. **Replace "drag" with tapping on mobile.** Tapping a day should open a picker for who is working and the start and end times. Offer a template ("Same shifts every week?") so she isn't starting from an empty grid, and start the view at early-morning bakery hours.
3. **Make publishing feel safe.** Before anything is sent, show a preview of the text her employees will get, with her bakery's name in it. Explain what happens when she edits a shift later. At Step 3, allow importing from phone contacts and say clearly that staff numbers are only used for schedule texts.

**Worth checking in the real study:** whether "Publish" or "Send to my team" makes more sense to her, and whether she expects to add herself as someone who works shifts.
