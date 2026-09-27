# How I tested edge-case-finder

I ran `edge-case-finder` once, on a page I had already redesigned for real, and scored what it found against that redesign. It listed 29 cases across all five kinds of failure (its own summary says 28), and reproduced 14 of them in a browser instead of guessing. Four of its findings were real problems the design critique had missed, including one the real redesign had noted and left open. Its weak spot: 5 of its 13 "fix before launch" items were shortcuts in my prototype, not design problems.

This is a scored run, not a comparison. There is only one version of this skill, and I didn't run it without the skill to compare.

## The test

The page is "Pipeline fields" in Northbeam, a fictional recruiting platform, rebuilt from a real settings page. An agency chooses which candidate fields show at each hiring stage, then changes that for a single client. Every change saves instantly. The full setup and the hidden answer key are described in the [design-critique-facilitator eval](../design-critique-facilitator/EVAL.md).

I ran `edge-case-finder` on 26 September 2026 with Claude Opus 5.5, right after `design-critique-facilitator` in the same session. So it had already seen the critique and my answers to its questions. That's how I'd use it on real work, but it means this run doesn't show what the skill finds on its own.

## What it did

It didn't ask anything: "I have enough context to run this without asking." Then, before writing anything up, it wrote small scripts to test the risky cases in a browser: two tabs editing at once, rage clicks, a client that doesn't exist, a save that fails. It marked the 14 cases it reproduced this way and said the rest came from reading the code.

It took 2 min 23 s and covered all five kinds of failure (input, permissions, two people at once, outside systems, user behavior), which is the skill's one hard rule.

## Results

I scored the cases that were design problems and new compared with the critique:

| Finding | Score |
|---|---|
| A client's setting switched back by hand still counts as the client's own, so later agency changes skip that client. It reproduced this with saved data. | On my "left for later" list. The critique missed it |
| Two tabs or two managers editing at once: the last save silently undoes the other's change. Reproduced in two tabs. | Real, not on my list. Depends on how the real product saves, which I haven't checked |
| With "Active fields only" on, turning off a field's last stage makes the row vanish, so you can't click it again to undo | Real, not on my list |
| An account manager who handles a few clients can still change Agency defaults for everyone | Real, not on my list. Needs a product decision |
| The client picker is far from the table and the page looks the same after switching, so it's easy to edit the wrong client | On my list (partly) |

The other cases I didn't score as design findings:
- **Engineering cases:** store settings by field ID so a rename doesn't lose them, rage clicks, slow saves, an expired session, the role coming from the URL, deleted fields, long names. These are real, but they're for the developer.
- **Repeats of the critique:** it said so for four of them ("from the critique").
- **Bugs in my prototype:** a locked field saved as off gets stuck off, and two crashes from bad or missing client data.

Its top pick, "The case I'd raise first", was the two-editor overwrite, because nobody can see it happen.

## What it got wrong

**It couldn't tell my prototype's shortcuts from design problems.** 5 of its 13 "fix before launch" items came from the prototype itself: two crashes, a locked field stuck off, recruiters able to edit, and the role read from the URL. It did flag the URL role as "fine in a prototype", but still ranked it high. On a real build, a developer would want these, so they're not wrong. But a designer reading the list has to sort them out by hand. The skill should ask what it's looking at (prototype, staging, production) and rank against that.

## If you use this skill

- **Run it after a critique, in the same conversation.** It built on the critique's findings instead of repeating them.
- **Tell it what stage the build is at.** Otherwise prototype shortcuts fill the top of the list.
- **Read the "reproduced" marks.** A case it reproduced is a fact about the build. A case from reading code is a lead to check.

## Limits

- One run, on one case. The same prompt can give different output on another day.
- It ran after the critique, so the findings aren't independent of it.
- No run without the skill, so this doesn't show how much the skill adds over asking Claude directly.
- I built the case, wrote the answer key and scored the results.
- The prototype and the answer key stay private, because the case is rebuilt from real work.
