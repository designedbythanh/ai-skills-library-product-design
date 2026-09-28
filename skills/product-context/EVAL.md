# How I tested product-context

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
- **Leave gaps as "Not provided".** Later skills ask about exactly those fields, instead of guessing.
- **Put a date and a name on each decision.** That's what lets a critique tell a current decision from an old spec.
- **The Log only works in Claude Code**, where skills can write files. In claude.ai, ChatGPT or Gemini, the skill prints both files for you to save and paste.

**Run it yourself:** `claude plugin eval . --case 'context-*' --runs 3 --scaffold --allow-tools Bash Write Edit`

## Limits

- Five small made-up cases, 3 runs each. The files were short and written in one go.
- It doesn't test a long project, where the brief and Log grow over weeks and could go stale.
- Only three of the sixteen "Next" lines showed up in the test runs: `prd-first-draft`, `edge-case-finder` and `design-critique-facilitator` ended every finished answer with theirs. The rest follow from what each skill produces and needs, not from a test.
- The grader is a model, and it was wrong often enough that its score alone isn't enough.
