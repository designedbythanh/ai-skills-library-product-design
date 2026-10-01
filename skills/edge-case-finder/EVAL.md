# How I tested edge-case-finder

## At a glance

| Date | Test | Compared with Claude alone? | Result |
|---|---|---|---|
| 1 Oct 2026 | A bug from real work, rebuilt as a case: changing scope while a save is running | Yes, 3 runs each way | Found every time, and so did Claude alone |
| 27 and 28 Sep 2026 | 5 small made-up cases, run on v1.2.0 then v1.3.0 | Yes, 6 runs each way | Same findings as Claude alone. The difference: it asks or states the build stage (6 of 6 vs 0 of 6) |
| 26 Sep 2026 | One run on a redesign I made on a real product | No | 4 real problems the critique missed. 5 of its 13 top items were prototype shortcuts, which led to the v1.2.0 change |

How the tests are run, and the limits they all share: [`evals/`](../../evals/README.md).

## A bug that got past design, from real work (v1.3.1)

**What happened.** On a real settings page with an agency/client scope selector, a bug got through my design and my browser checks: if you changed the scope while a change was still saving, Undo could act on the wrong level, the other scope's value could show in the table, and a cell could stay locked. A developer caught it in code review and fixed it with five tests. My browser checks couldn't see it, because the mock data answered instantly, so there was never a moment "while saving". I asked whether `edge-case-finder` would have raised it at design time. This case answers that, rewritten as Northbeam: [`edge-06-scope-switch-mid-save`](../../evals/edge-06-scope-switch-mid-save/prompt.md).

**How I tested it.** A spec-only description of the page, 3 runs with the skill and 3 without, on 1 October 2026.

| Criterion | With the skill | Without |
|---|---|---|
| Names a scope change during a save, undo or reset, and what goes wrong | 3 of 3 | 3 of 3 |
| Ties each request to the scope it was sent from (drop late answers, bind Undo to its level, or hold the switch) | 3 of 3 | 3 of 3 |

**What this shows.** Claude doesn't need the skill to find this one. Given the spec, it raised the case every time, with or without it. The bug didn't get through because the question was hard. It got through because nobody asked for an edge-case pass on that page before building it. The skill's value here is making that pass a habit, not finding something Claude couldn't.

**Limits.** The prompt says that changing the scope reloads the table in place, which points toward the problem. A real spec might not say that. The skill raises the question; it can't check that the code handles it, and that took a code review and tests.

## With and without the skill (v1.2.0 and v1.3.0)

**What changed.** In the first test, 5 of its 13 "fix before launch" items were shortcuts in my prototype. v1.2.0 asks what it's looking at (spec, prototype, staging or production). Cases that only exist because of a prototype shortcut get tagged "prototype only" and stay out of High priority, unless the build is going to production. v1.3.0 then added context files and a "Next" line, so I ran the same cases again.

**How I tested it.** Five short, made-up cases in [`evals/`](../../evals/README.md), on 27 September (v1.2.0) and 28 September 2026 (v1.3.0). Two describe the same invite feature with the same shortcuts (role read from the URL, a hard-coded team, a Send button that sends nothing): once as a prototype for user testing, once as a build shipping Monday. Each round ran every case 3 times with the skill and 3 times without.

| Case | With the skill | Without |
|---|---|---|
| Asks or states what's being reviewed, when I didn't say | 6 of 6 | 0 of 6 |
| Prototype: doesn't rank the shortcuts as problems to fix | 6 of 6 | 5 of 6 |
| Production: treats the same shortcuts as blockers | 6 of 6 | 6 of 6 |
| Covers bad input, permissions, two things at once, outside failures and user behavior | 6 of 6 | 6 of 6 |
| Stays out of a request that isn't about edge cases (a translation) | Not used, 6 of 6 | n/a |

**What this shows.** Claude without the skill handles most of this well. Told it's a prototype, it usually sets the shortcuts aside by itself. The one run that "failed" put the fake Send button first, because it would ruin the user test: participants would all "succeed" without learning anything. That's a fair point, and I wouldn't count it against Claude. The clear difference is the first row: without the skill, Claude never asked or said what kind of build it was looking at. That matters when the stage isn't obvious from the prompt, which is most of the time on real work. In my first test, before this rule, I had to sort 5 prototype shortcuts out of a 13-item "fix before launch" list by hand. Every finished answer in the second round ended with the "Next" line (pointing to `acceptance-criteria`).

**The grader was biased, then wrong.** In the pilot, three criteria rewarded the skill's format (a "High priority" list, five named sections) instead of what the answer said, so Claude without the skill failed them while saying the right things. I rewrote them to grade content. In the second round, the grader failed two answers without the skill that were right: one listed typos, duplicates and inviting someone already on the team as real cases, and one covered all five areas under its own headings. I counted both as passes.

In a separate case (see the [product-context eval](../product-context/EVAL.md)), the skill read the build stage from a brief instead of asking, and added its findings to the brief's Log.

**Run it yourself:** `claude plugin eval . --case 'edge-*' --runs 3`

## First test: one scored run on a real redesign (v1.1.0)

I ran `edge-case-finder` once, on a page I had already redesigned for real, and scored what it found against that redesign. It listed 29 cases across all five kinds of failure (its own summary says 28), and reproduced 14 of them in a browser instead of guessing. Four of its findings were real problems the design critique had missed, including one the real redesign had noted and left open. Its weak spot: 5 of its 13 "fix before launch" items were shortcuts in my prototype, not design problems.

This first test was a single scored run on v1.1.0, with no run without the skill to compare.

### The test

The page is "Pipeline fields" in Northbeam, a fictional recruiting platform, rebuilt from a real settings page. An agency chooses which candidate fields show at each hiring stage, then changes that for a single client. Every change saves instantly. The full setup and the hidden answer key are described in the [design-critique-facilitator eval](../design-critique-facilitator/EVAL.md).

I ran `edge-case-finder` on 26 September 2026 with Claude Opus 5.5, right after `design-critique-facilitator` in the same session. So it had already seen the critique and my answers to its questions. That's how I'd use it on real work, but it means this run doesn't show what the skill finds on its own.

### What it did

It didn't ask anything: "I have enough context to run this without asking." Then, before writing anything up, it wrote small scripts to test the risky cases in a browser: two tabs editing at once, rage clicks, a client that doesn't exist, a save that fails. It marked the 14 cases it reproduced this way and said the rest came from reading the code.

It took 2 min 23 s and covered all five kinds of failure (input, permissions, two people at once, outside systems, user behavior), which is the skill's one hard rule.

### Results

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

### What it got wrong

**It couldn't tell my prototype's shortcuts from design problems.** (Fixed in v1.2.0, see above.) 5 of its 13 "fix before launch" items came from the prototype itself: two crashes, a locked field stuck off, recruiters able to edit, and the role read from the URL. It did flag the URL role as "fine in a prototype", but still ranked it high. On a real build, a developer would want these, so they're not wrong. But a designer reading the list has to sort them out by hand. The skill should ask what it's looking at (prototype, staging, production) and rank against that.

### If you use this skill

- **Run it after a critique, in the same conversation.** It built on the critique's findings instead of repeating them.
- **Tell it what stage the build is at.** Otherwise prototype shortcuts fill the top of the list.
- **Read the "reproduced" marks.** A case it reproduced is a fact about the build. A case from reading code is a lead to check.

### Limits

- One run, with no run without the skill to compare.
- It ran after the critique, so the findings aren't independent of it.
