# How I tested design-critique-facilitator v1.1.0

Before releasing v1.1.0, I ran both versions on the same page and scored every finding against a redesign I had already made on the real product. The biggest change is in how it works. v1.1.0 asks what I'm trying to do before it critiques, instead of taking the goal from an old spec. It found the root of a problem v1.0.0 only saw the surface of, and it pushed back on one of my own decisions. It still praises things it shouldn't, and it missed one problem v1.0.0 caught. The counts (9 against 8 of the 11 problems found) come from one run of each version, so they're a rough sign at best.

## The test

I rebuilt a real settings page as a fictional one, so I could publish the test. "Northbeam" is a made-up recruiting platform for staffing agencies. On its "Pipeline fields" page, an agency chooses which candidate fields show at each hiring stage (Sourcing, Screening, Interview, Offer), then changes that choice for a single client. Names, domain and visuals are all different from the original.

The agent could see a clickable prototype of the page before the redesign, plus a spec, design guidelines, a developer's UX review and a backlog. The prototype has an agency view and a client view, and three roles: manager, recruiter and viewer.

The agent could not see my answer key: 11 problems the real redesign fixed, and 7 more it saw and left for later. One of those 7, the contrast of a confirm button, can't be checked because the prototype has no confirm dialog, so the results count 6. Among them:
- The "Editing for" block showing the client was louder than the page title.
- Every change saved instantly, with no undo.
- A client's own settings looked exactly like the ones inherited from the agency.
- On a phone, only one and a half of the four stages fit on screen.

I ran each version in a fresh Claude Code setup, with the same model (Claude Opus 5.5), on 26 September 2026:
- **Run 1:** v1.0.0, called the way I usually call it: page open, skill name, nothing else.
- **Run 2:** v1.1.0. It asked me four questions first, and I answered in my own words. Then I ran two more skills from this library on the same page, `edge-case-finder` and `persona-pretest`.

## Results

These numbers compare the critique skill alone. The two extra skills in run 2 are covered further down.

| | v1.0.0 | v1.1.0 |
|---|---|---|
| Asked what I was trying to do before critiquing | No. It took the goal from the spec, wrote "Correct me if any of that is wrong", and carried on | Yes: my intent, my worries, what's decided vs still open, and the stage |
| Views it opened itself | One client, at desktop and 500px wide | Every role, agency and client, phone and desktop |
| Problems the redesign fixed, found | 8 of 11 (3 only partly) | 9 of 11 (1 only partly) |
| Problems the redesign left for later, found | 2 of 6 | 3 of 6 |
| Real problems that weren't in my list | 3 | 5 |
| Findings already in the dev review or backlog | 3. It said so for 2 | 4. It labeled 6 of its findings as already known, covering all 4 |
| Things it praised that my list flags as problems | 3 | 2 |
| Time | 1 min 14 s | 1 min 48 s, plus one round of questions |

The 3 real problems v1.0.0 added: a failed save shows nothing, a search with no match shows an empty table, and the agency page says "Changes here reach all clients", which is false for clients that set their own value. v1.1.0 found the same 3, plus 2 of its own (below). Both versions also suggested explaining why some fields are locked. I left that out of the count: my list had an item about the lock, but I dropped it once I decided to keep the lock for this case, so neither version was really tested on it.

## Where v1.1.0 did better

**It found the real problem with autosave.** v1.0.0 only flagged the small reset button, because it resets a whole stage with no warning. v1.1.0 went further. Any wrong click saves instantly and leaves no trace, and a wrong click at agency level reaches every client that hasn't set its own value. It proposed a status line with Undo after each change.

**It pushed back on me.** I said the "coming soon" notice wasn't needed. v1.1.0 pointed out that the approved spec requires it, asked whether the boards had launched or the spec should change, and suggested shrinking it to one line if they hadn't. The real redesign did keep that information, as a small badge next to the title.

**It checked the phone layout itself.** At 375px it saw that only one and a half stages fit, and proposed one stage at a time in tabs. That is what the real redesign does.

**It noticed a filter that looks like a setting.** The "Active fields only" filter uses the same switch as the settings, so it reads like one more thing that saves.

## What two more skills added

In run 2, I followed the critique with two more skills from this library:
- **`edge-case-finder`** found a problem from my "left for later" list that the critique missed: a client's setting switched back by hand still counts as the client's own, so later agency changes skip that client. It also found 3 new real problems. One depends on how the real product saves, which I haven't checked.
- **`persona-pretest`** played an account manager setting up a client. She read the agency view and nearly concluded the client was already done. Then she read the reset icon as "undo my change" and almost wiped the client's existing setup. The critique had said a client's own settings were hard to tell apart from inherited ones. The persona showed what that costs.

All of run 2 took about 5 minutes, against 1 min 14 s for run 1.

## Second check: the old example

I also re-ran v1.1.0 on the fictional clinic prompt from the v1.0.0 example, to see what it lost. That run is now the [example](EXAMPLE.md).

- **Kept:** all the main findings. The hover-only Check in button, status shown by color alone, no answer to "who is next?", no undo after check-in, failed check-in, two patients with the same name, walk-ins, no-show rules, and empty and busy days.
- **Better:** it answered my open question with a reason taken from my own answers. Late patients should stay in time order, because "Late" is set automatically after 10 minutes, and a row that moves would jump under the receptionist's cursor. It also kept the stats card that clinic owners asked for and critiqued its placement. v1.0.0 had recommended removing it. And it noticed that revenue on a front-desk screen could be seen by patients.
- **Lost, among others:** out-of-date data, two receptionists working at once, and early arrivals.
- **Cost:** one extra round of questions, even though the prompt already gave the goal, the user and the stage.

## Still wrong in v1.1.0

- **It praises without checking.** Both versions listed the switch colors as working. v1.0.0 said they're easy to scan, v1.1.0 said they follow the guidelines. The grey "off" switch is about 1.2:1 against white, well below the 3:1 accessibility minimum. Both also praised the header block the redesign changed. Praise needs the same evidence as criticism.
- **It's narrower.** v1.1.0 missed the mixed wording ("visible", "active", "shown" for the same thing) that v1.0.0 caught, and lost some breadth on the clinic example.
- **It asks even when it doesn't need to.** The extra round of questions happens even when the prompt already answers most of them.

## If you use this skill

- **Answer its questions in your own words,** especially what's already decided and what worries you. The best findings in run 2 came straight from those answers.
- **Read the "Working" list first, and check it.** Both versions praised things that were problems. A wrong "needs attention" costs a minute to reject. A wrong "working" goes unchallenged.
- **For a risky flow, run `edge-case-finder` and `persona-pretest` after it.** They found problems the critique missed, for about 3 more minutes.

## What changed in the skill

I wrote v1.1.0 on 25 September, the day before these runs, after a real work session where v1.0.0 took its idea of what I wanted from an outdated spec and suggested something we had already decided against. These runs tested v1.1.0. They didn't produce it.

| Change | Where it shows in the runs |
|---|---|
| Asks for my intent and worries first, even when specs exist | v1.0.0 took the goal from the spec without waiting for an answer |
| Doesn't reopen what's decided, but critiques how it's done | On the clinic example, v1.0.0 recommended removing a card the owners had asked for |
| New lens: after each action, does the user know it worked, and can they undo it? | v1.0.0 saw the reset button but not the wider autosave problem |
| Labels findings as already known or new | v1.0.0 cited the dev review for only 2 of its 3 known findings |
| Opens every state it can set up itself | v1.0.0 looked at one client, at two widths |
| Severity and owner on each finding, plus a "Not checked" list | v1.0.0 gave no way to sort findings or see what it skipped |

## How I scored it, and the limits

I scored every finding by hand. A finding counted if it matched a problem on my list and pointed in a sound direction. "Real problems that weren't in my list" are ones I checked and agree with. "Already known" means the problem was in the dev review or the backlog, so the finding confirms rather than discovers. I left out findings caused by bugs in my own prototype (for example a menu button that does nothing, or a role check I got wrong), and generic ones such as "add a loading state" to a static prototype.

The limits:
- **One run per version per case.** The same prompt can give different output on another day.
- **I built the case, wrote the answer key and scored the results.** Nobody else checked the scoring.
- **The answer key is what the real redesign did.** That isn't proof it was right. A skill could disagree with it and have a point.
- **Run 2 changed three things at once:** the skill version, my answers to its questions, and the two extra skills. That is why the results table only compares the critique itself.
- **The runs used a draft of v1.1.0.** One label option ("design + dev" as an owner) was added after run 2.
- **In run 1, the agent reviewed the page on its own before the skill loaded,** and the skill's output partly repeats that first reply.
- **The prototype and the answer key stay private,** because the case is rebuilt from real work.
