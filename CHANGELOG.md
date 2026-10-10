# Changelog

## 1.4.0 · 2026-10-10

From real work between 2 and 9 October 2026.

### All skills except `product-context`
- A suggestion the brief records as rejected is never raised again.
- Findings from skills that ran earlier (in the brief's Log, or earlier in the conversation) aren't repeated; one is mentioned only to add something new to it.
- When there's no brief, the skill offers once per conversation to start one with `product-context`.
- Log entries also record the suggestions the designer rejected.

### Review skills
- `design-critique-facilitator`, `edge-case-finder`, `persona-pretest` and `assumption-reversal`: when several review the same design in one go, they end with one merged list, one line per problem, naming every skill that found it.
- `design-critique-facilitator`: an HTML mockup counts as built. Looking at it means rendering it at each width and reading the screenshots, not reading the CSS. Untested: the eval sandbox blocked the browser in every run.

### `product-context`
- The brief has `Rejected:` lines under Decided.
- What the designer already said earlier in the conversation counts as an answer.
- Asks before adding the files to a commit in a shared repo.

### Evals
- New case [`critique-06-off-scale-values`](evals/critique-06-off-scale-values/case.yaml), rewritten from real work as Northbeam: an HTML mockup with three values off its `DESIGN.md` scale. Result (3 runs with v1.3.2, 3 with a v1.4.0 draft, 3 without): flags all three off-scale values (3 of 3 vs 1 of 3 for the type and the button). The draft's scale rule added nothing measurable, so it was dropped. Details in the [critique eval](skills/design-critique-facilitator/EVAL.md).
- These runs were graded by Claude Haiku, the tool's default, because `--judge-model sonnet` was left out. Every "Run it yourself" command now sets it.
- `context-01` to `context-05` re-run on v1.4.0, graded by Claude Sonnet: no regression, every criterion 3 of 3 with the plugin. Details in the [product-context eval](skills/product-context/EVAL.md).

### Docs
- README: restart Claude Code after installing the plugin, or calling a skill fails with "Unknown skill".
- Each example's "Since then" line says what changed in v1.4.0.

### Repo
- `CLAUDE.md`: rules for editing this repo, a checklist for what a script can't judge, and release steps.
- `scripts/check_repo.py`: seven checks, each from a mistake that once reached the repo (skill counts in prose, example version headers, eval pages starting with At a glance, changelog entry for the current version, README results matching an eval row, every eval case listed, and in CI the GitHub description and profile count). Each was tested by reintroducing the original mistake in a copy: 9 of 9 caught.

## 1.3.2 · 2026-10-01

### Skills
- Plainer descriptions for `acceptance-criteria`, `experiment-design` and `design-scope-negotiator` (dropped "airtight", "statistically-honest", "opinionated"). Re-tested: all 16 skills still get picked on their own from their example prompts (16 of 16).

### Docs
- New [`edge-case-finder` example](skills/edge-case-finder/EXAMPLE.md), run on v1.3.2. The other examples now say which version they ran on and what has changed since.
- README: how each skill is built now includes the context files and the "Next" line.

### License
- The code (`scripts/` folders) is now [MIT](LICENSE-CODE). The skills and docs stay CC BY 4.0.

## 1.3.1 · 2026-10-01

### All skills
- Each SKILL.md carries its version twice: `metadata.version` in the frontmatter, and `<!-- product-design-skills 1.3.1 -->` as the first line of the body. The frontmatter is dropped when a skill loads, so the comment is what shows in a session's transcript: you can tell which version actually ran. The instructions themselves are unchanged.

### Evals
- 2 new cases rewritten from real sessions (neutral Northbeam case):
  - [`edge-06-scope-switch-mid-save`](evals/edge-06-scope-switch-mid-save/prompt.md): a settings page with an agency/client scope selector. Does the skill ask what happens when the scope changes while a save is still running? That bug shipped once and was caught in review.
  - [`persona-01-concept-model`](evals/persona-01-concept-model/prompt.md): a merged "Fields" page. Does the persona question what each row is, and whether fee models belong in a table of fields, or only test what it was asked to find? In the real session it only tested findability, and the designer caught the concept problems.
- Results (3 runs with the plugin, 3 without): no advantage for the skills on either case. edge-06: 3/3 with and without. persona-01: Claude without the skill did as well (one grader judgment apart out of nine, read as a tie). Details in the [edge-case-finder](skills/edge-case-finder/EVAL.md) and [persona-pretest](skills/persona-pretest/EVAL.md) evals.

### Docs
- [REAL-USE.md](REAL-USE.md): what happened when I used the skills on real work for a week, including a five-skill chain, what each skill found and missed, and why none of them fired on their own.

### Repo
- CI checks that every skill's version matches the plugin's.

## 1.3.0 · 2026-09-28

### New skill
- [`product-context`](skills/product-context/SKILL.md) writes a `PRODUCT.md` for the product and a brief per feature (goal, stage, what's decided with a date and who, what's open, worries, and a Log). It marks missing answers "Not provided" instead of guessing, and leaves out references without a link.

### All skills
- Read `PRODUCT.md` and the feature's brief first, and ask only for what's missing.
- End with a "Next" line: the skill that usually follows, and what to carry over.
- When a brief exists and files can be written, add a dated entry to its Log.
- `design-critique-facilitator` treats a brief the designer wrote as their intent, so it doesn't ask again for what the brief already covers.

### Evals
- 5 new cases for the shared files, the Log and the "Next" line; the 10 existing cases re-run. Results in the [product-context eval](skills/product-context/EVAL.md) and each skill's EVAL.md.

## 1.2.0 · 2026-09-28

### design-critique-facilitator
- Lists something as working only after checking it. Ships [`scripts/contrast.py`](skills/design-critique-facilitator/scripts/contrast.py) to measure color contrast; anything it can't check goes under "Not checked".
- Description now says it asks before critiquing and measures before praising, to tell it apart from other critique skills.

### edge-case-finder
- Asks what it's looking at (spec, prototype, staging or production). Cases caused only by prototype shortcuts are tagged "prototype only" and kept out of High priority.

### Evals
- [`evals/`](evals/): 10 cases for `claude plugin eval`, run with and without the plugin. Results are in each skill's EVAL.md.
- Scored runs for [`edge-case-finder`](skills/edge-case-finder/EVAL.md) and [`persona-pretest`](skills/persona-pretest/EVAL.md), from the same test session as the design-critique-facilitator eval.

### Repo
- CI checks skills, manifests and links on every push.

## 1.1.0 · 2026-09-27

### design-critique-facilitator
- Always asks for the designer's intent and concerns before critiquing, even when specs or docs exist.
- Separates decided from open: doesn't reopen decided behavior, critiques how it's executed.
- New lens: Interaction & feedback (does the user know an action worked, can they recover from a mistake).
- Tags every finding by severity, owner and known/new; adds Assumptions and Not checked sections.
- For built designs, opens every state it can set up (roles, empty/filled, narrowest screen) instead of listing them as unverified.
- Tested against v1.0.0 before release: see [EVAL.md](skills/design-critique-facilitator/EVAL.md). New [EXAMPLE.md](skills/design-critique-facilitator/EXAMPLE.md) from the regression run.

### Repo
- Feedback form asks which version you used (optional).

Full diff: [v1.0.0...v1.1.0](https://github.com/designedbythanh/ai-skills-library-product-design/compare/v1.0.0...v1.1.0)

## 1.0.0 · 2026-09-23

First release: 15 skills, from Discovery to Shipping.
