# Working in this repo

Instructions for Claude (or anyone) editing this skills library. Each rule here comes from a mistake that once reached the public repo.

## Before saying anything is done

1. Run `python3 scripts/check_repo.py`. It covers what a script can check: skill counts, version markers, example headers, changelog entry, README numbers against the eval pages, the eval case list, links. CI runs it too, plus the GitHub description and profile README count.
2. Go through the checklist below for everything the script can't judge.
3. Say what you did not check.

## Rules for editing

- **Re-read the whole file after editing it**, not just the diff. Inserting a section once split another section's intro from its body.
- **Every number and claim must trace to a source**: a result file in `evals/results/`, a transcript, or a command you ran. Check it before writing it, not after.
- **Before changing a claim, grep for every place that states it** (README, EVAL pages, CHANGELOG, release notes, REAL-USE.md) and change them together.
- **A hypothesis is not a finding.** Don't publish "X can cause Y" until it's tested. If it's worth mentioning untested, say "untested".
- **Test on a copy.** Mutation tests, trial edits and eval scaffolds go in a copy or a temp folder, never in the working tree.
- **Real-work cases are rewritten as Northbeam**, the fictional recruiting tool. No real company, client, person or product names, and no real screenshots.

## Checklist (what the script can't judge)

Run it over the whole repo, not only the files you touched.

| Area | Check |
|---|---|
| README | Every claim matches what the current version does (not an older one). Nothing overstated ("unedited", "always", "on its own"). Skill table comes before the evidence. |
| EVAL pages | The at-a-glance table matches the sections. Sections are newest first. Each test says whether it compared with Claude alone. Limits specific to the test only; shared limits live in `evals/README.md`. |
| Examples | The "Since then" line still describes what changed after the run. |
| Skill descriptions | Plain words, what + when. If you change one, re-run the trigger test (every example prompt should still pick its skill). |
| CHANGELOG and release notes | Say the same thing as the eval pages, in the same words where a result is involved. |
| REAL-USE.md | Matches the transcripts. Nothing that identifies the real product. |
| GitHub metadata | Description, topics, homepage, latest release. |

## Releasing

1. Bump `version` in both `.claude-plugin/*.json`, then every `metadata.version` and `<!-- product-design-skills X -->` line (the script fails until all match).
2. Add the `## X · date` entry to CHANGELOG.md.
3. Run the script and the checklist. Commit, push, wait for CI.
4. Tag, then build one zip per skill (without EXAMPLE.md and EVAL.md) plus `all-skills.zip`, same layout as the previous release. Publish the release with "How to update" notes.
5. Don't name a branch the same as a tag.

## Evals

See [`evals/README.md`](evals/README.md). Read every failed criterion yourself before reporting a number: the grader has been wrong in most rounds.
