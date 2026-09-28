# Changelog

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
