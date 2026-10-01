# How I tested persona-pretest

I ran `persona-pretest` once, on a page I had already redesigned for real, and compared what it found with that redesign. In 51 seconds it walked a fictional account manager through one task. Its top 3 fixes match 3 changes the real redesign made. It also found one problem I hadn't listed, and it showed why a problem the critique had only named mattered: the persona nearly wiped a client's existing setup.

The first test below is a scored run, not a comparison. The second, from real work, compares it with Claude alone.

## v1.3.1: what it misses when the question is narrow, from real work

**What happened.** On my real product, I asked the skill whether people would still find value lists and pricing settings after merging two settings pages into one table. The persona answered that question well, and found a real bug on the existing page: a new pricing entry got a default unit nobody chose. But it missed three things I saw in a minute on the same screen: the pricing settings sat in a table of fields where they didn't belong, the rows didn't say what kind of field each was, and the "New field" form couldn't take values or stages. That run used an old version of the skill. This case rebuilds it as Northbeam: [`persona-01-concept-model`](../../evals/persona-01-concept-model/prompt.md), with the same narrow question ("do people still find the lists and the fee models?").

**How I tested it.** 3 runs with the skill and 3 without, `claude plugin eval` with Claude Opus 5.5 on 1 October 2026, graded by Claude Sonnet. I read all six answers.

| Criterion | With the skill | Without |
|---|---|---|
| Notes that "New field" can't take values or stages | 3 of 3 | 3 of 3 |
| Questions whether fee models belong among the fields (grader) | 2 of 3 | 3 of 3 |
| ...and proposes giving them a place outside the field rows (my reading) | 1 of 3 | 1 of 3 |
| Shows the persona unsure what kind of thing some rows are (grader) | 2 of 3 | 2 of 3 |
| ...asks what a specific row like "Req ID" or "Margin" is (my reading) | 0 of 3 | 0 of 3 |

**What this shows.** No advantage for the skill in this case. With or without it, Claude caught the incomplete form every time and voiced the persona's sense that fees are "money, not fields", but mostly answered my question as asked: make the Fee row easier to find, rather than take it out of the table. On my real page, the fix was a separate tab. The best single idea showed up in one run of each arm: Sam creating a "Day rate" *field* instead of a fee model, a wrong path that looks like success.

The gap in the grader rows (2 vs 3) is one judgment out of nine, on a lenient grader, and the judges split on two of the runs. With 3 runs per arm, I read it as a tie, not as the skill doing worse. One real difference in shape: with the skill, every answer stayed in the step-by-step persona format and ended with exactly 3 fixes; without it, two answers listed 8 or 9 recommendations, including a separate way into fee models from outside the table. Top 3 doesn't drop fixes: it groups them, 3 to 6 per item (tested against an uncapped list, 5 runs each).

The grader was more lenient than I meant: it passed answers that mentioned money without questioning the table. So I added my own stricter reading in the rows marked "my reading".

**If you use this skill:** ask what the page is for, not only whether one thing is findable. Before the tasks, have the persona say what they think the page is and what each kind of row is. That's not in the skill yet; I'd need to test it first.

**Limits.** One case, 3 runs per arm, described in text. My first single run with the skill on this case scored 2 of 4 criteria. I wrote the case knowing what was missed in real life.

## The test

The page is "Pipeline fields" in Northbeam, a fictional recruiting platform, rebuilt from a real settings page. An agency chooses which candidate fields show at each hiring stage, then changes that for a single client. Every change saves instantly. The full setup and the hidden answer key are described in the [design-critique-facilitator eval](../design-critique-facilitator/EVAL.md).

I ran `persona-pretest` on 26 September 2026 with Claude Opus 5.5, right after `design-critique-facilitator` and `edge-case-finder` in the same session. So it had already seen their findings.

## What it did

It started with a question. The spec only named roles, not goals or context, so it drafted two personas and asked me to pick one. I picked Dana, an account manager who has just signed a new client, Harbor Logistics. She's comfortable with admin screens but not technical, and her main fear is changing the agency's defaults for every client by mistake. Her task: hide "Salary expectation" at the Screening stage for Harbor only, then check that nothing else changed.

It then walked her through the page as built, in 9 steps. Each step says what she notices, what she expects, where she gets stuck, and what she'd say.

## Results

| Moment | Score |
|---|---|
| **Step 2.** On the agency view, salary is already off, so she nearly concludes Harbor is done and stops. "It's off already, so Harbor's fine?" | Real, not on my list |
| **Steps 6 and 7.** Reset icons appear on stages she never touched. She reads them as changes she caused, and nearly clicks them to "put them back", which would wipe Harbor's existing setup. "Is this undo? Undo for what? I'll ask Priya before I touch it." | On my list: a client's own settings look like inherited ones, and changes can't be undone |
| **Step 5.** No Save button and no confirmation, so she scrolls looking for one and reloads the page to check. | On my list: no feedback after a change |
| **Step 8.** The only way to compare Harbor with the agency is to flip between two 22-row tables from memory. | On my list: a client's own settings look like inherited ones |

Its verdict: she hides the salary field, but can't confirm nothing else changed, and ends the task unsure.

**Its top 3 fixes match what the real redesign did:**

| persona-pretest suggested | The real redesign |
|---|---|
| Mark each cell where a client has its own setting, and list what differs from the agency | Marks and resets each client setting on its own, and adds an "Only changed fields" filter |
| Label the reset button and make it undoable | Adds undo after each change and a confirmation before a reset |
| Put the client picker with the "Editing for" line above the table, and confirm each change in words | Moves the line saying which client you're editing above the title |

**The critique said, the persona showed.** The critique had already said a client's own settings were hard to tell apart from inherited ones. The persona turned that into a cost: a manager almost deleting a client's setup because she misread one icon.

## What it got wrong

Step 9 checks the page on a phone and finds that "Menu" does nothing. That's a stub in my prototype, not a design problem, and I didn't score it. I only scored the four moments above, so I can't vouch for every detail in the other steps.

It also said clearly what it is: "This simulates the current build; it isn't real user data." It pointed to steps 2, 6 and 7 as the ones to watch in real sessions.

## If you use this skill

- **Pick a persona with a fear and a task.** Dana's fear of changing every client's settings is what made steps 1, 6 and 8 tense, and useful.
- **Run it after the critique.** The critique names a problem. The persona shows what it costs a person, and that's easier to argue for in a review.
- **Treat it as a map for real testing, not a replacement.** It tells you where to look in a real session.

## Limits

- One run, one persona, one task. Another persona would hit other problems.
- It ran after the critique and the edge-case pass, so the findings aren't independent of them.
- No run without the skill, so this doesn't show how much the skill adds over asking Claude directly.
- I built the case, wrote the answer key and scored the results.
- The prototype and the answer key stay private, because the case is rebuilt from real work.
