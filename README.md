# AI Skills Library for Product & Design Teams

15 AI skills for product designers and product managers, from understanding a problem to reading the results after launch. Each skill is a short set of instructions your AI tool follows for one job: critiquing a design, finding edge cases, writing acceptance criteria. They ask for the context they need instead of guessing, and each one comes with a real, unedited run you can read before trying it.

by [Thanh Nguyen](https://www.linkedin.com/in/thanh2-nguyen/) · Product Designer, AI-native workflows · [Substack](https://designedbythanh.substack.com) · [Notion templates](https://www.notion.com/@thanh-nguyen)

## What using one looks like

You describe a design and ask for feedback. In Claude you don't need to name the skill: Claude notices that `design-critique-facilitator` fits and uses it. Before critiquing, it asks what's already decided, what's still open, and what worries you. Then it answers your worries first. One finding from the [example run](skills/design-critique-facilitator/EXAMPLE.md), a receptionist screen in a clinic app:

> **Your open question: group late patients, or keep time order?** I recommend keeping time order and not moving late patients into their own group. Late status is set automatically, so a separate group would make a row jump to another place at +10 minutes, possibly just as the receptionist goes to click it. That's the "lost my place" problem you're worried about.

Every skill has an example like this next to it, run in Claude Code on a fictional case.

## Does it work?

I tested `design-critique-facilitator` against a redesign I had already made on a real product, rebuilt as a fictional case. The current version found 9 of the 11 problems the real redesign fixed, asked for my intent before critiquing, and pushed back on one of my own decisions. It also praised two things it shouldn't have. The full test, with what it still gets wrong and the limits of the test, is in [EVAL.md](skills/design-critique-facilitator/EVAL.md).

In the same session I ran two more skills on that page, and scored them too. [`edge-case-finder`](skills/edge-case-finder/EVAL.md) found four real problems the critique had missed, but 5 of its 13 "fix before launch" items were shortcuts in my prototype. [`persona-pretest`](skills/persona-pretest/EVAL.md) suggested the same top 3 fixes the real redesign made. Those two are single scored runs, not comparisons. The other 12 skills have their example runs, not a scored test.

## The 15 skills, in the order you'd use them

| Stage | Skill | What it does | |
|---|---|---|---|
| **Understand the problem** | [`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) | Finds the real need behind a feature request, then other ways to meet it | [Example](skills/five-whys-root-cause/EXAMPLE.md) |
| | [`user-interview-synthesis`](skills/user-interview-synthesis/SKILL.md) | Turns raw notes from several interviews into ranked insights and unspoken needs | [Example](skills/user-interview-synthesis/EXAMPLE.md) |
| | [`persona-pretest`](skills/persona-pretest/SKILL.md) | Walks through a design as a specific user, to find confusion and drop-off before real testing | [Example](skills/persona-pretest/EXAMPLE.md) · [Eval](skills/persona-pretest/EVAL.md) |
| **Find directions** | [`assumption-reversal`](skills/assumption-reversal/SKILL.md) | Flips the design's assumptions and turns the reversed view into concrete ideas | [Example](skills/assumption-reversal/EXAMPLE.md) |
| | [`cross-industry-steal`](skills/cross-industry-steal/SKILL.md) | Finds how 3 unrelated industries solve the same kind of problem, and adapts the best one | [Example](skills/cross-industry-steal/EXAMPLE.md) |
| **Choose a direction** | [`decision-rationale`](skills/decision-rationale/SKILL.md) | Compares two options on explicit criteria and scenarios, and writes down a recommendation with a confidence level | [Example](skills/decision-rationale/EXAMPLE.md) |
| **Spec it** | [`prd-first-draft`](skills/prd-first-draft/SKILL.md) | Writes a first PRD engineers can build from and executives can read in 5 minutes | [Example](skills/prd-first-draft/EXAMPLE.md) |
| | [`success-metrics-definition`](skills/success-metrics-definition/SKILL.md) | Defines how you'll know the feature worked: a main metric, early signals, and counter-metrics | [Example](skills/success-metrics-definition/EXAMPLE.md) |
| | [`edge-case-finder`](skills/edge-case-finder/SKILL.md) | Lists what breaks: bad input, permissions, two people at once, outages, and how users actually behave | [Example](skills/edge-case-finder/EXAMPLE.md) · [Eval](skills/edge-case-finder/EVAL.md) |
| | [`acceptance-criteria`](skills/acceptance-criteria/SKILL.md) | Turns a user story into Given/When/Then criteria, including errors and edge cases | [Example](skills/acceptance-criteria/EXAMPLE.md) |
| **Get feedback** | [`design-critique-facilitator`](skills/design-critique-facilitator/SKILL.md) | Critiques a design against your intent, with each fix tagged by severity and owner | [Example](skills/design-critique-facilitator/EXAMPLE.md) · [Eval](skills/design-critique-facilitator/EVAL.md) |
| | [`explain-to-4-audiences`](skills/explain-to-4-audiences/SKILL.md) | Explains one decision to a 10-year-old, an engineer, an executive and a user, to test whether it's clear | [Example](skills/explain-to-4-audiences/EXAMPLE.md) |
| **Under deadline pressure** | [`design-scope-negotiator`](skills/design-scope-negotiator/SKILL.md) | Sorts scope into ship, fast-follow and cut, with the reason for each | [Example](skills/design-scope-negotiator/EXAMPLE.md) |
| **After it ships** | [`experiment-design`](skills/experiment-design/SKILL.md) | Plans an A/B test with a decision rule, and says when traffic is too low to trust the result | [Example](skills/experiment-design/EXAMPLE.md) |
| | [`data-interpretation`](skills/data-interpretation/SKILL.md) | Separates what the numbers show from the explanation, and rules out other causes before acting | [Example](skills/data-interpretation/EXAMPLE.md) |

Two skills sit later than you might expect. `success-metrics-definition` belongs right after the spec, not at the end, and `design-scope-negotiator` comes in under deadline pressure, not right after ideas. In testing, Claude often suggested the next skill in this order on its own, for example offering `acceptance-criteria` after a `prd-first-draft`.

## How each skill is built

Each skill is one `SKILL.md` file with four parts:
- **When to use it**, so your AI tool knows when to reach for it.
- **What to ask before starting.** If the context is missing, it asks instead of guessing.
- **The output format**, so results look the same every time.
- **One hard rule** the output must follow, so it doesn't drift into generic filler. In the files it's called *Exigence*, French for "requirement". For example, `edge-case-finder` must cover all five kinds of failure every time, and say so when one has nothing to report.

## Install

| Tool | How |
|---|---|
| **Claude** (claude.ai / Desktop) | Download a skill's `.zip` from the [latest release](https://github.com/designedbythanh/ai-skills-library-product-design/releases/latest) (no GitHub account needed) and upload it in Settings → Capabilities (or Skills). Or create a new skill there and paste the name, description and instructions by hand. Claude uses it on its own when it fits. |
| **Claude Code** | Install all 15 as a plugin (below), or copy skill folders by hand. |
| **ChatGPT** | Paste a skill's instructions into a Custom GPT (Explore GPTs → Create) or a Project's instructions. You open that GPT or Project yourself when you need it. |
| **Gemini** | Paste a skill's instructions into a Gem (Gems → New Gem), then open that Gem when you need it. |
| **Any other tool** | Paste the instructions into a new chat, followed by your details. |

Claude is the only one that picks the right skill mid-conversation on its own. In ChatGPT and Gemini, you choose the GPT or Gem first.

Claude Code plugin:

```
/plugin marketplace add designedbythanh/ai-skills-library-product-design
/plugin install product-design-skills@designedbythanh
```

<details>
<summary><strong>Copy by hand, custom config folder, and duplicate installs</strong></summary>

Copy all skills into Claude Code by hand:

```bash
git clone https://github.com/designedbythanh/ai-skills-library-product-design.git
cp -r ai-skills-library-product-design/skills/* "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/"
```

To use a skill in one project only, copy its folder into that project's `.claude/skills/` instead.

If you run Claude Code with a custom `CLAUDE_CONFIG_DIR`, skills live in `$CLAUDE_CONFIG_DIR/skills/`, not `~/.claude/skills/`. The command above handles both. The plugin install doesn't depend on the path at all.

**Already have some of these skills?** If you added them earlier (uploaded to claude.ai, pasted from the Notion template, or copied in by hand), remove the old copies before installing. Otherwise you end up with two near-identical versions of the same skill, and Claude picks one unpredictably. Skills uploaded to claude.ai sync into Claude Code too, so check Settings → Capabilities as well as your skills folder.

**Updating:** see the [changelog](CHANGELOG.md) and the notes on each [release](https://github.com/designedbythanh/ai-skills-library-product-design/releases).

</details>

## Feedback

Used a skill on real work? [Tell me how it went](https://github.com/designedbythanh/ai-skills-library-product-design/issues/new?template=skill-feedback.yml). What was missing or wrong is the most useful part.

## License

[CC BY 4.0](LICENSE). Use, adapt and share freely, including commercially, with attribution.
