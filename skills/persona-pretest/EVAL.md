# How I tested persona-pretest

I ran `persona-pretest` once, on a page I had already redesigned for real, and compared what it found with that redesign. In 51 seconds it walked a fictional account manager through one task. Its top 3 fixes match 3 changes the real redesign made. It also found one problem I hadn't listed, and it showed why a problem the critique had only named mattered: the persona nearly wiped a client's existing setup.

This is a scored run, not a comparison. There is only one version of this skill, and I didn't run it without the skill to compare.

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
