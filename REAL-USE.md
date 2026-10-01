# What happened when I used the skills on real work

The evals in [`evals/`](evals/) use small made-up cases. This page is the other half: what the skills did on my real work, between 25 September and 1 October 2026, read back from the session transcripts. The product stays private, so the cases below are rewritten as Northbeam, the same fictional recruiting tool as the evals. The numbers and what happened are real.

## How often they ran, and how

- **11 uses in 3 sessions**, all by me, a product designer working in the product's code repo with Claude Code (Claude Opus 5.5).
- **None fired on its own.** Every use came after I named a skill or asked Claude to "use the right skill". In one session, Claude read three skill files directly instead of loading them, because they weren't installed there.
- **For visual polish, Claude picked another skill.** Twice I asked to check a page's look and readability and to use whatever skill fit. Claude chose general design-critique and accessibility skills from another plugin, not `design-critique-facilitator`. Mine is built for a structured critique against the designer's intent, so that may be the right call, but the descriptions don't make the difference clear.
- **The versions that ran were old.** All 11 uses ran copies from before v1.1.0 (synced from an earlier upload, or an old plugin cache). So none of the changes I had measured in v1.1.0 to v1.3.0 were in play, and I could only tell by comparing files. From v1.3.1, each skill's first line names its version, and it shows up in the transcript.

## One question, five skills: should two settings pages become one?

Northbeam has two settings pages: one where the agency keeps its value lists (Skills, Seniority, Source channel...) and one where it switches each field on or off per hiring stage. I asked whether to merge them. Claude proposed a chain, and I followed it over about an hour, in this order.

### five-whys-root-cause

**Why merge?** My trigger: creating a field on one page, then going to the other to switch it on, felt like two trips. The key fact didn't come from the five whys. It came from the code: a new field was **already switched on** in the two stages where it's usually needed. The second trip existed because nothing said so. That turned "merge the pages" into cheaper options: ask where the field shows when you create it, show where it shows in its drawer, and link the two pages.

### decision-rationale

**Two pages with links (A) or one page (B)?** First real run of this skill. B scored 39, A 33, on five criteria weighted equally. One of the five was scope safety: definitions are agency-wide, visibility can change per client, and mixing the two on one page had caused a real incident before. It scored 8 against 7, worth no more than "delivery cost". In hindsight, a rule tied to a past incident is a condition to meet, not one score among five. The outcome: I leaned to B but took it to the team, because it's a product change. No decision yet.

### cross-industry-steal

**How do lists stay findable inside one long table?** Three examples (restaurant menus printing the side options under a dish, accounting control accounts, information scent). The "best steal" turned the pricing list (fee models) into a flagged row of the table, like a control account in a ledger. Claude built it. When I opened it, I rejected it: fee models are pricing rules, not a column, so they don't belong among the fields. The steal copied the shape of the example, not just its mechanism.

### persona-pretest

**Does someone still find the lists?** The persona, an agency ops lead who keeps lists in Excel, found **a real bug on the existing page**: a new fee model gets a default unit nobody chose, so it would be saved wrong. That was worth the run on its own. But it tested what I asked (findability) and missed what I saw in a minute on the same screen: rows that didn't say what kind of field they were, an icon nobody explained, and a "New field" form that couldn't take values or stages. Details in the [persona-pretest eval](skills/persona-pretest/EVAL.md).

### design-critique-facilitator

**Twice, on the merged page.** It confirmed my own worry with measurements: the filter control was 44px tall next to a 32px search field and button. It also measured three elements below the contrast they need (1.91, 2.60 and 4.12 to 1: a warning line, a drag handle, unselected filter options) and proposed fixes. At the end of the session, Claude went back over its own recommendations and found several it had made and never applied. Version 1.3.0's Log and "Next" line exist for that, but they weren't in the version that ran.

## What I take from it

- **The skills frame the work; the facts came from the code.** The most useful finding of the hour came from reading the product, not from the skill's steps.
- **A skill answers the question you ask.** The persona tested findability because that was my question. Ask it what the page is for, too.
- **Score against hard rules separately.** A rule that once caused an incident shouldn't be averaged with cost.
- **Name the skill, and check which version ran.** Nothing fired on its own, and I was running an old version without knowing it.

## Limits

- One designer, one product, one week. I chose when to use the skills, and I judged the results.
- No run without the skills on the same work, so this shows what happened, not what the skills added over Claude alone. The two evals below rebuild two moments from this week and compare: in both, Claude without the skill did as well.
- The cases are rewritten. Names, numbers of rows and some wording changed; what each skill found and missed did not.

Two evals come from this week: [`edge-06-scope-switch-mid-save`](evals/edge-06-scope-switch-mid-save/prompt.md) (a bug that got past design) and [`persona-01-concept-model`](evals/persona-01-concept-model/prompt.md) (the persona miss above). Results are in the [edge-case-finder](skills/edge-case-finder/EVAL.md) and [persona-pretest](skills/persona-pretest/EVAL.md) evals.
