# AI Skills Library for Product & Design Teams

16 AI skills for product designers and product managers, from understanding a problem to reading the results after launch. Each skill is a short set of instructions your AI tool follows for one job: critiquing a design, finding edge cases, writing acceptance criteria. They ask for the context they need instead of guessing, and each one comes with a real run you can read before trying it.

by [Thanh Nguyen](https://www.linkedin.com/in/thanh2-nguyen/) · Product Designer, AI-native workflows · [Substack](https://designedbythanh.substack.com) · [Notion templates](https://www.notion.com/@thanh-nguyen)

## What using one looks like

You describe a design and ask for feedback. In Claude you don't have to name the skill: Claude can notice that `design-critique-facilitator` fits and use it. With many skills installed, asking for it is more reliable: on my real work, I always did. Before critiquing, it asks what's already decided, what's still open, and what worries you. Then it answers your worries first. One finding from the [example run](skills/design-critique-facilitator/EXAMPLE.md), a receptionist screen in a clinic app:

> **Your open question: group late patients, or keep time order?** I recommend keeping time order and not moving late patients into their own group. Late status is set automatically, so a separate group would make a row jump to another place at +10 minutes, possibly just as the receptionist goes to click it. That's the "lost my place" problem you're worried about.

Every skill has an example like this next to it, run in Claude Code on a fictional case.

## The 16 skills, in the order you'd use them

| Stage | Skill | What it does | |
|---|---|---|---|
| **Before you start** | [`product-context`](skills/product-context/SKILL.md) | Writes down the context the other skills keep asking for: a `PRODUCT.md` for the product and a brief per feature | [Example](skills/product-context/EXAMPLE.md) |
| **Understand the problem** | [`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) | Finds the real need behind a feature request, then other ways to meet it | [Example](skills/five-whys-root-cause/EXAMPLE.md) · [Real use](REAL-USE.md#five-whys-root-cause) |
| | [`user-interview-synthesis`](skills/user-interview-synthesis/SKILL.md) | Turns raw notes from several interviews into ranked insights and unspoken needs | [Example](skills/user-interview-synthesis/EXAMPLE.md) |
| | [`persona-pretest`](skills/persona-pretest/SKILL.md) | Walks through a design as a specific user, to find confusion and drop-off before real testing | [Example](skills/persona-pretest/EXAMPLE.md) · [Eval](skills/persona-pretest/EVAL.md) · [Real use](REAL-USE.md#persona-pretest) |
| **Find directions** | [`assumption-reversal`](skills/assumption-reversal/SKILL.md) | Flips the design's assumptions and turns the reversed view into concrete ideas | [Example](skills/assumption-reversal/EXAMPLE.md) |
| | [`cross-industry-steal`](skills/cross-industry-steal/SKILL.md) | Finds how 3 unrelated industries solve the same kind of problem, and adapts the best one | [Example](skills/cross-industry-steal/EXAMPLE.md) · [Real use](REAL-USE.md#cross-industry-steal) |
| **Choose a direction** | [`decision-rationale`](skills/decision-rationale/SKILL.md) | Compares two options on explicit criteria and scenarios, and writes down a recommendation with a confidence level | [Example](skills/decision-rationale/EXAMPLE.md) · [Real use](REAL-USE.md#decision-rationale) |
| **Spec it** | [`prd-first-draft`](skills/prd-first-draft/SKILL.md) | Writes a first PRD engineers can build from and executives can read in 5 minutes | [Example](skills/prd-first-draft/EXAMPLE.md) |
| | [`success-metrics-definition`](skills/success-metrics-definition/SKILL.md) | Defines how you'll know the feature worked: a main metric, early signals, and counter-metrics | [Example](skills/success-metrics-definition/EXAMPLE.md) |
| | [`edge-case-finder`](skills/edge-case-finder/SKILL.md) | Lists what breaks: bad input, permissions, two people at once, outages, and how users actually behave | [Example](skills/edge-case-finder/EXAMPLE.md) · [Eval](skills/edge-case-finder/EVAL.md) |
| | [`acceptance-criteria`](skills/acceptance-criteria/SKILL.md) | Turns a user story into Given/When/Then criteria, including errors and edge cases | [Example](skills/acceptance-criteria/EXAMPLE.md) |
| **Get feedback** | [`design-critique-facilitator`](skills/design-critique-facilitator/SKILL.md) | Critiques a design against your intent, with each fix tagged by severity and owner | [Example](skills/design-critique-facilitator/EXAMPLE.md) · [Eval](skills/design-critique-facilitator/EVAL.md) · [Real use](REAL-USE.md#design-critique-facilitator) |
| | [`explain-to-4-audiences`](skills/explain-to-4-audiences/SKILL.md) | Explains one decision to a 10-year-old, an engineer, an executive and a user, to test whether it's clear | [Example](skills/explain-to-4-audiences/EXAMPLE.md) |
| **Under deadline pressure** | [`design-scope-negotiator`](skills/design-scope-negotiator/SKILL.md) | Sorts scope into ship, fast-follow and cut, with the reason for each | [Example](skills/design-scope-negotiator/EXAMPLE.md) |
| **After it ships** | [`experiment-design`](skills/experiment-design/SKILL.md) | Plans an A/B test with a decision rule, and says when traffic is too low to trust the result | [Example](skills/experiment-design/EXAMPLE.md) |
| | [`data-interpretation`](skills/data-interpretation/SKILL.md) | Separates what the numbers show from the explanation, and rules out other causes before acting | [Example](skills/data-interpretation/EXAMPLE.md) |

Two skills sit later than you might expect. `success-metrics-definition` belongs right after the spec, not at the end, and `design-scope-negotiator` comes in under deadline pressure, not right after ideas.

## Does it work?

Claude alone already catches most problems when the facts are in the prompt. I tested the skills against Claude without them (3 runs each way per case) and against redesigns I had made on a real product. They change how Claude gets there:

- **They ask before they answer.** The critique asks what you intend, what's decided and what worries you: 6 of 6 runs, against 1 of 6 without. On my real work, skipping that step is how an older version took my intent from an outdated spec. [Eval](skills/design-critique-facilitator/EVAL.md)
- **They don't praise what they haven't measured.** Every color the critique calls fine comes with a contrast ratio: 6 of 6, against 3 of 6 without.
- **`edge-case-finder` knows what it's looking at.** It asks or states whether it's reviewing a prototype or a production build: 6 of 6, against 0 of 6 without. [Eval](skills/edge-case-finder/EVAL.md)
- **They write things down.** With a brief in place, each skill adds what it found to the brief's Log for the next skill or session: 3 of 3, never without. [Eval](skills/product-context/EVAL.md)

In my tests, they didn't find things Claude alone missed. On two cases rebuilt from my real work, Claude without the skill did as well ([edge-case-finder](skills/edge-case-finder/EVAL.md), [persona-pretest](skills/persona-pretest/EVAL.md)). Against a real redesign, the critique found 9 of the 11 problems it fixed, and still praised two things it shouldn't have.

**On real work.** I used the skills 11 times on my own product in one week. Same pattern as the evals: the skills shaped the work (asking why before merging two pages, a scored comparison of the options, a persona walkthrough that found a real bug), while the key facts came from reading the product, and one "best idea" I rejected on sight. What happened, skill by skill: [REAL-USE.md](REAL-USE.md). How the tests work, and how to run them: [`evals/`](evals/README.md).

## How the skills work together

Each skill ends with a "Next" line: the skill that usually comes after it, and what to carry over. For example, `edge-case-finder` points to `acceptance-criteria`, carrying its high-priority cases.

In Claude Code, the skills also share two files that `product-context` writes:
- **`PRODUCT.md`**: the product, its users, roles, references (each with a link), vocabulary, and where known issues are tracked.
- **`briefs/<feature>.md`**: one per feature, with the goal, the stage, what's decided (with a date and who agreed it), what's open, what worries you, and a **Log**.

Every skill reads these first and only asks for what's missing. When a brief exists, each skill adds a short dated entry to its Log, so the next skill, or the next session, starts from what's already been found. In claude.ai, ChatGPT or Gemini, where skills can't keep files, `product-context` prints both files for you to save and paste.

Two chains have been run so far: `design-critique-facilitator`, then `edge-case-finder` and `persona-pretest` on a test page ([eval](skills/design-critique-facilitator/EVAL.md)), and `five-whys-root-cause` → `decision-rationale` → `cross-industry-steal` → `persona-pretest` → `design-critique-facilitator` on one question from my real work ([real use](REAL-USE.md#one-question-five-skills-should-two-settings-pages-become-one)). The other "Next" suggestions follow from what each skill produces and needs, not from a test.

## How each skill is built

Each skill is one `SKILL.md` file with six parts:
- **When to use it**, so your AI tool knows when to reach for it.
- **What to ask before starting.** If the context is missing, it asks instead of guessing.
- **Context files.** It reads `PRODUCT.md` and the feature's brief first, if they exist, and only asks for what's missing.
- **The output format**, so results look the same every time.
- **A handoff.** It ends with a "Next" line naming the skill that usually follows, and adds a dated entry to the brief's Log when it can write files.
- **One hard rule** the output must follow, so it doesn't drift into generic filler. In the files it's called *Exigence*, French for "requirement". For example, `edge-case-finder` must cover all five kinds of failure every time, and say so when one has nothing to report.

## Install

| Tool | How |
|---|---|
| **Claude** (claude.ai / Desktop) | Download a skill's `.zip` from the [latest release](https://github.com/designedbythanh/ai-skills-library-product-design/releases/latest) (no GitHub account needed) and upload it in Settings → Capabilities (or Skills). Or create a new skill there and paste the name, description and instructions by hand. Claude can pick it up on its own when it fits. |
| **Claude Code** | Install all 16 as a plugin (below), or copy skill folders by hand. |
| **ChatGPT** | Paste a skill's instructions into a Custom GPT (Explore GPTs → Create) or a Project's instructions. You open that GPT or Project yourself when you need it. |
| **Gemini** | Paste a skill's instructions into a Gem (Gems → New Gem), then open that Gem when you need it. |
| **Any other tool** | Paste the instructions into a new chat, followed by your details. |

Claude is the only one that can pick a skill mid-conversation on its own, and with many skills installed, naming the one you want is more reliable. In ChatGPT and Gemini, you choose the GPT or Gem first.

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

The skills and docs are [CC BY 4.0](LICENSE): use, adapt and share freely, including commercially, with attribution. The code (the `scripts/` folders) is [MIT](LICENSE-CODE).
