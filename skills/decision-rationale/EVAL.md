# How I tested decision-rationale

## At a glance

| Date | Test | Compared with Claude alone? | Result |
|---|---|---|---|
| 10 Oct 2026 | A miss from real work, rebuilt as a case: a team rule set after an incident, scored as one criterion among five | Yes, 3 runs each way, plus 3 runs on v1.5.0 | v1.6.0 rules the option out before scoring in 3 of 3 runs; v1.5.0 scored the rule in 3 of 3. Claude alone also treated the rule as decisive (3 of 3), but gave no confidence level |
| 10 Oct 2026 | Four options instead of two | Yes, 3 runs each way, plus 3 runs on v1.5.0 | No difference: all of them compared the four options and said what would make another option win |

How the tests are run, and the limits they all share: [`evals/`](../../evals/README.md).

## A rule from a past incident, scored like any other criterion (v1.6.0)

**What happened.** On my real work, I used the skill to choose between two settings pages with links (A) and one page (B). One of the five criteria was scope safety: mixing agency-wide and per-client settings on one page had caused a real incident before. It scored 8 against 7, worth no more than delivery cost. A rule tied to a past incident is a condition to meet, not one score among five ([real use](../../REAL-USE.md#decision-rationale)). This case rebuilds it as Northbeam: [`decision-02-must-meet-condition`](../../evals/decision-02-must-meet-condition/prompt.md). Option A breaks the team's rule but is cheaper and what users asked for.

**How I tested it.** 3 runs with v1.6.0, 3 without the plugin, and 3 with v1.5.0, on 10 October 2026, graded by Claude Sonnet. I read all nine answers.

| Criterion | v1.6.0 | v1.5.0 | Without |
|---|---|---|---|
| Rules out Option A for breaking the rule, before or instead of scoring it | 3 of 3 | 0 of 3 | 3 of 3 |
| Ends with a recommendation, a confidence level, a key reason and a next step | 3 of 3 | 3 of 3 | 0 of 3 |
| Skill used without being named | 3 of 3 | 3 of 3 | (not applicable) |

**What this shows.** Every answer recommended B. The difference is how they got there. v1.5.0 put the rule in its score table ("Follows the team rule: A 1, B 10" in two runs) and added it up with cost and clicks, so a cheaper or better-liked option could have outscored it on another day. One v1.5.0 run eliminated A only at the end, at the deciding question. v1.6.0 opens with a "Must-meet conditions" table, rules A out, says what A would need to change to pass, and scores what's left. Claude alone also treated the rule as decisive, without any scoring. So the skill's 5-3-1 format was what turned the rule into a score, and v1.6.0 removes that. Without the plugin, none of the answers gave a confidence level.

## Four options (v1.6.0)

**Why.** Until v1.5.0 the skill was written for exactly two options ("evaluate both options", "Recommended option: A or B"). Real decisions often have three or four, including keeping things as they are. Case: [`decision-01-four-options`](../../evals/decision-01-four-options/prompt.md), options 0 (keep it, add a help article), A, B and C.

| Criterion | v1.6.0 | v1.5.0 | Without |
|---|---|---|---|
| Compares all four options, or rules one out with a reason | 3 of 3 | 3 of 3 | 3 of 3 |
| Names a runner-up and what would make it win (grader) | 3 of 3 | 2 of 3 | 3 of 3 |
| ...counting a runner-up that isn't called one (my reading) | 3 of 3 | 3 of 3 | 3 of 3 |
| Skill used without being named | 3 of 3 | 3 of 3 | (not applicable) |

**What this shows.** Little. v1.5.0 already handled four options despite its wording. The grader failed one v1.5.0 run, which never used the word runner-up but did say what would make B win (account managers wanting a separate list of their changes) and when to reopen the decision. I count it as a pass. This case doesn't separate the versions. It stays as a check that four options keep working.

**Limits.** I wrote both cases knowing what I wanted the skill to do, and the first one from a miss I had already analyzed. 3 runs per arm.
