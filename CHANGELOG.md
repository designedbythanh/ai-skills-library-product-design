# Changelog

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
