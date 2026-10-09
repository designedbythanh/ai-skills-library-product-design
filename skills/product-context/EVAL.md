# How I tested product-context

## At a glance

| Date | Test | Compared with Claude alone? | Result |
|---|---|---|---|
| 10 Oct 2026 | The same 5 cases, re-run on v1.4.0 | Yes, 3 runs each way | No regression: every criterion 3 of 3 with the plugin |
| 9 Oct 2026 | 6 small made-up cases for the [context contract](../../CONTEXT-CONTRACT.md): offering a brief, earlier findings, finding the project's own docs, sources that disagree, a missing source | Yes, 3 runs each way. Cases 08 to 11 also against the version before the contract | Finds the project's docs and asks before using them, and writes disagreements under `## Open`: 3 of 3, never without. The version before the contract already let what the user says beat the brief, and named the brief-vs-guidelines conflict |
| 28 Sep 2026 | 5 small made-up cases for the shared files, the Log and the "Next" line | Yes, 3 runs each way | Files, Log and "Next" line written every time with the plugin, never without. A critique with a brief ties Claude alone: the brief saves a round of questions, not quality |

How the tests are run, and the limits they all share: [`evals/`](../../evals/README.md).

## Re-run on v1.4.0

v1.4.0 changes every skill's context paragraph (rejected suggestions, earlier findings, offering a brief), so I re-ran the five cases from the first test (below) on 10 October 2026, 3 runs with the plugin and 3 without, graded by Claude Sonnet. With the plugin, every criterion passed in every run. Without it, the results matched the first test, except that the critique kept the decided sort order in only 1 of 3 runs this time (3 of 3 on 28 September): the other two suggested changing the "newest first" default. In `context-05`, one run without the plugin hit a usage limit and its replacement timed out, so that arm has 2 runs (the replacement pair added a fourth run with the plugin, which also passed).

## The context contract test

The [context contract](../../CONTEXT-CONTRACT.md) changes how every skill finds its context: `PRODUCT.md` gets a `## Sources` table pointing to docs the project already keeps, only `product-context` looks through the repo (and asks before listing anything), every skill starts with a "Context used:" line, and when sources disagree the more specific one wins and the disagreement is written down. I wrote six new cases in [`evals/`](../../evals/) and ran each 3 times with the plugin and 3 times without, with Claude Opus 5.5 on 9 October 2026. For the four contract cases (08 to 11), I also ran the version just before the contract (v1.4.0), to see what the contract adds on its own. I read every failed criterion myself.

| Case | With the contract | Before the contract | Claude alone |
|---|---|---|---|
| `context-06` `edge-case-finder` with no brief offers once to start one | 3 of 3 | not run | 0 of 3 |
| `context-07` `persona-pretest` doesn't repeat the earlier critique's findings, doesn't raise a rejected fix, adds to the Log | 3 of 3 on all three | not run | 0, 1 and 0 of 3 |
| `context-08` `product-context` finds the ADR folder and tokens file the README points to, with the role each could play | 3 of 3 | Named both 3 of 3, but as plain references, without a role | 2 of 3 |
| `context-08` asks the designer to confirm them before using them | 3 of 3 | 0 of 3 | 0 of 3 |
| `context-08` doesn't list them as confirmed or copy the ADR in | 3 of 3 | 0 of 3 | 0 of 3 |
| `context-09` the user says "production Monday", the brief says "Prototype": goes with the user and treats the URL role as a launch fix | 3 of 3 | 3 of 3 | 3 of 3 |
| `context-09` writes the disagreement in the brief | 3 of 3, under `## Open` | 3 of 3, in the Log only | 0 of 3 |
| `context-09` starts with what it read ("Context used:") | 3 of 3 | 1 of 3 | 1 of 3 |
| `context-10` names the conflict between the brief (no confirmation) and `guidelines.md` (always confirm), without recommending a dialog | 3 of 3 | 3 of 3 | 0 of 3 |
| `context-10` writes it in the brief | 3 of 3, under `## Open` | 3 of 3, in the Log only | 0 of 3 |
| `context-11` says the guidelines file named in Sources doesn't exist | 3 of 3 | 3 of 3 | 0 of 3 |
| `context-11` doesn't judge against an old design-system file that Sources doesn't list | 3 of 3 | 1 of 3 | 3 of 3 |

**What this shows.** The clearest change is in `context-08`. Before the contract, `product-context` found the docs too, but it wrote the files straight away, listed both docs as references and copied ADR 0003 into the brief's Decided list without asking. Claude alone wrote a `CLAUDE.md` that pointed to both docs, and also took ADR 0003 as decided without asking. With the contract, it lists what it found with a role for each, asks which ones are current, and waits.

For sources that disagree, the version before the contract was already most of the way there: it went with what the user said over the brief, and named the conflict between the brief and the guidelines, every time. What the contract adds is where the disagreement ends up (under `## Open`, where the next person will see it as a question, not buried in the Log) and the "Context used:" line. In `context-11`, both versions reported the missing file, but before the contract two of three runs went looking for a replacement and judged the toolbar against the old 40px rule. Claude alone never used the old file, but it never mentioned the missing one either.

**The grader made mistakes again.** In `context-08` it couldn't grade the third criterion in two runs, because the file it was told to read didn't exist yet (the skill was waiting for confirmation, as it should). I fixed that criterion and read those runs myself. In the runs before the contract, it failed a `context-10` brief whose Log did mention the conflict, and a `context-11` answer that said "That rule may be out of date, so I haven't used it as the standard". It passed a `context-08` answer as "asked to confirm" when it had written both files first and only asked about one decision; I counted that as a fail. The table uses my reading.

The "with the contract" runs were made on the version just before one last fix: a source counts as possibly stale only when git shows it changed after its Verified date, and never a brief. The other cases don't touch that rule; `context-09` does, so I ran it again after the fix, 3 times with the plugin only, and the table shows that run (the earlier one: 3 of 3 on everything except "Context used:", 2 of 3). I also ran four older cases once each on this version, as a smoke test (`critique-03`, `critique-04`, `edge-01`, `edge-03`): all passed, one of them by my reading after the grader failed an answer that asked its questions and gave no critique.

## Limits of the context contract test

- The cases are small made-up projects with a handful of files. A real repo has more docs, and more ways to point to them.
- Git doesn't run in the eval sandbox, so the check for a source changed after its Verified date wasn't tested. Two runs said so.
- The version before the contract wasn't run on `context-06` and `context-07`.
- One path is untested: a skill reusing what was said earlier in the same conversation when there's no brief.
- With no `PRODUCT.md`, skills start with "Context used: none", but in the smoke runs none of them said the context was unconfirmed or offered `product-context` at that point, as the contract asks. Not fixed yet.

## The first test

`product-context` is new in v1.3.0, together with the shared files it writes and the "Next" line every skill now ends with. I tested the whole mechanism, not just this skill: five small made-up cases in [`evals/`](../../evals/), each run 3 times with the plugin and 3 times without it, using `claude plugin eval` with Claude Opus 5.5 on 28 September 2026. Claude Sonnet graded each answer against criteria I wrote, and I read every answer that failed a criterion.

## Results

| Case | With the plugin | Without |
|---|---|---|
| Writes `PRODUCT.md` and a brief from what I told it, marking references without links as "Not provided" instead of inventing URLs | 3 of 3 | 0 of 3 (no files written) |
| `edge-case-finder` reads the brief (so it doesn't ask what stage the build is at) and adds a dated entry to its Log | 3 of 3 | 0 of 3 |
| `prd-first-draft` ends with a "Next" line naming the skills that usually follow and what to carry over | 3 of 3 | 0 of 3 |
| `design-critique-facilitator` with a brief already in place critiques without asking again, answers the brief's worry, and keeps its decided items | 3 of 3 | 3 of 3 |
| Stays out of an unrelated request (release notes) | Not used, 3 of 3 | n/a |

**What this shows.** The files and the log only exist with the plugin: without it, Claude answered in chat and wrote nothing down, so the next session would start from zero again. That's the point of this release.

The critique row is a tie, and it's worth being clear about why. Given a request with no questions in it, Claude without the skill just critiques, and it guessed the obvious worry (overdue invoices don't stand out) on its own. With the skill, the brief means it doesn't have to ask its intake questions, which removes the extra round trip v1.1.0 added. So the brief saves a step. It doesn't make this critique better.

**The grader made mistakes again.** It failed one `PRODUCT.md` that met every criterion (the references were correctly marked "Not provided", with no invented URL). In the first pilot it also failed an `edge-case-finder` answer that had put the prototype shortcuts in their own "not ranked" section, as asked, apparently because a real spec item ("only admins can invite, enforced on the server") sat in the top list. I rewrote both criteria. The table uses my reading of those answers.

## If you use it

- **Run it once per project, then once per feature.** Everything after reads the files, so you stop re-typing the same context.
- **Confirm the docs it finds.** It lists the docs your project already keeps and asks which ones are current; only those go into Sources, and the other skills read from there.
- **Leave gaps as "Not provided".** Later skills ask about exactly those fields, instead of guessing.
- **Put a date and a name on each decision.** That's what lets a critique tell a current decision from an old spec.
- **The Log only works in Claude Code**, where skills can write files. In claude.ai, ChatGPT or Gemini, the skill prints both files for you to save and paste.

**Run it yourself:** `claude plugin eval . --case 'context-*' --runs 3 --judge-model sonnet --scaffold --allow-tools Bash Write Edit`

## Limits

- Five small made-up cases, 3 runs each. The files were short and written in one go.
- It doesn't test a long project, where the brief and Log grow over weeks and could go stale.
- Only three of the sixteen "Next" lines showed up in the test runs: `prd-first-draft`, `edge-case-finder` and `design-critique-facilitator` ended every finished answer with theirs. The rest follow from what each skill produces and needs, not from a test.
- The limits shared by every test are in [`evals/`](../../evals/README.md).
