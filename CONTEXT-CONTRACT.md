# Context contract

<!-- context-contract 1.0 -->

What the skills read before they start, and where they write what they found. `product-context` writes these files; every other skill reads them. The [Product & Design Knowledge System](https://github.com/designedbythanh/product-design-knowledge-system) is a template that implements this contract.

The contract names **roles**, not files. A team that already keeps its context somewhere else (an ADR folder, a `DESIGN.md`, a design note per feature) keeps it there and points to it from `PRODUCT.md`.

## Roles

| Role | Holds | Default path |
|---|---|---|
| `product` | What the product is and isn't, users, roles and permissions, vocabulary, domain rules | `PRODUCT.md` |
| `guidelines` | Patterns, states, microcopy, review checklist | `guidelines.md` |
| `decisions` | Decisions that apply across features | `decision-log.md` |
| `feature` | One feature's intent: goal, stage, decided, open, worries, log | `briefs/<slug>.md` |
| `evidence` | Real screens, component inventory, design system files | `evidence/` or a link |
| `issues` | Where known issues are tracked | a link |

A role can point to a part of a file: `guidelines.review-checklist` → `docs/review.md`.

## `PRODUCT.md`

```
# [Product]
## Sources
## Product and users
## Roles and permissions
## Vocabulary
## Known issues live in
```

Optional, after `## Vocabulary`: `## Domain` (data definitions, business rules, integrations) when they have no other home.

`## Sources` is the index. One row per role that has a home:

```
| Role | Path | Status | Verified |
|---|---|---|---|
| guidelines | design/DESIGN.md | primary | 2026-10-09 |
| decisions | docs/adr/ | primary | 2026-10-09 |
| feature | docs/designs/<slug>.md | primary | 2026-10-09 |
```

- **Status**: `primary` (the source of truth for that role, one per role) or `supporting`.
- **Verified**: the date the designer confirmed the path is current. Only `product-context` sets it, and only after asking.

## Brief

```
# [Feature]
Spec: [link, or "None"]
## Goal
## Stage
## Decided
- [decision] · [date] · [who]
- Rejected: [suggestion] · [why] · [date]
## Open
## Worries
## Log
```

Optional sections, added below `## Log` when the feature needs them: `## Compositions`, `## States`, `## Edge cases`, `## Flows`, `## Spec` (only when the spec has no other home).

A decision that applies beyond this feature moves to `decisions`, and its line here becomes `[decision] · see DL-012`. Skills suggest the move; the designer makes it.

## `guidelines.md`

Fixed headings, so a skill can read only the part it needs:

```
## Values
## Patterns
## States
## AI features
## Microcopy
## Examples
## Review checklist
## Open questions
```

`## AI features` is optional, for products without AI features.

## Markers

- `Not provided`: nobody gave this. Skills ask for it.
- `⚠️ Not validated`: written from an assumption. Skills use it, say so, and never treat it as a fact.

## How skills find context

1. Read `PRODUCT.md`. Read the sources the task needs from its `## Sources`; a role with no row uses its default path.
2. No `PRODUCT.md`: read `briefs/` and only what the project points to itself (`CLAUDE.md`, `AGENTS.md`, `README`). Don't search the rest of the repo. Say the context is unconfirmed and offer `product-context`.
3. A path in Sources that doesn't exist: say so. Don't look for a replacement.
4. A source modified after its Verified date: say so and ask whether it still holds.
5. Start the output with one line: `Context used: [files, with Verified dates, or "unconfirmed"]`.

Only `product-context` searches the repository, and it asks the designer to confirm each source before writing it to Sources.

## When sources disagree

The more specific source wins:

1. What the designer says in this conversation
2. The brief's `## Decided`
3. `decisions`, newest entry first
4. `guidelines`
5. `product`

Brief against spec: the brief wins on intent, the spec wins on what was committed to the team. Either way, a disagreement is reported, never resolved silently: as a finding, and under the brief's `## Open` when the skill can write files.

## What skills write

- A dated entry under the brief's `## Log`: the skill's name and 3-5 lines of what was found or decided, including rejected suggestions.
- A line under the brief's `## Open` for a disagreement between sources.
- Nothing else. `PRODUCT.md`, `guidelines`, `decisions` and Sources are written only by `product-context` or by the designer.

## Versions

This contract has its own version (the comment at the top). It changes only when a role, heading, marker or rule above changes. The Knowledge System's README states the version it implements, and `scripts/check_repo.py` checks it in CI.
