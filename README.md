# AI Skills Library for Product & Design Teams

15 structured AI skills covering the full product cycle, from Discovery to Shipping. Paste once, and your AI tool runs them on its own. No terminal, no code editor, no setup beyond copy-paste.

Most people rewrite the same AI prompt every sprint: copy it from a doc, fill in the blanks, hope it remembers what "good" looks like this time. These aren't prompts to paste and edit by hand. They're **Skills**: instructions your AI tool keeps and reaches for on its own once it recognizes the situation.

Every skill has:
- a stated **trigger** (when to use it)
- instructions that tell your AI tool **what to ask for before starting**, so it never guesses at missing context
- a defined **output format**
- one hard rule (**Exigence**) that keeps the output from turning into generic AI filler

**Who it's for:** product designers, UX/UI designers, product managers, and design engineers who already use AI daily and want structured, repeatable output instead of re-explaining context every time.

by [Thanh Nguyen](https://www.linkedin.com/in/thanh2-nguyen/) · Product Designer, AI-native workflows · [Notion templates](https://www.notion.com/@thanh-nguyen) · [Substack](https://designedbythanh.substack.com)

## How to use it

Each skill lives in `skills/<name>/SKILL.md`: a `name` and `description` (when to use it) in the header, and the instructions below it. Next to it, `EXAMPLE.md` shows a real run in Claude Code on a fictional scenario. Where you put it depends on your tool.

| Tool | Setup |
|---|---|
| **Claude** (claude.ai / Desktop) | Settings → Capabilities (or Skills) → New skill. Paste Name + Description into their fields, the instructions into the body. Or zip a skill folder and upload it. Claude reaches for it on its own once it recognizes the situation. |
| **Claude Code** | Copy a skill folder into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project). |
| **ChatGPT** | Create a Custom GPT (Explore GPTs → Create) or add it to a Project's custom instructions. You open that GPT/Project yourself when you want it; it doesn't auto-trigger mid-chat. |
| **Gemini** | Create a Gem (Gemini → Gems → New Gem). Paste the instructions in, then open that Gem when you need it. |
| **Any other tool** | Paste the instructions straight into a new chat, followed by your specific details. Works everywhere; you just re-paste each time. |

> 💡 One real difference worth knowing before you commit to a tool: Claude's Skills can notice mid-conversation that one applies and use it without you asking. ChatGPT and Gemini need you to manually open the right GPT/Gem first.

Install all skills in Claude Code at once:

```bash
git clone https://github.com/designedbythanh/ai-skills-library-product-design.git
cp -r ai-skills-library-product-design/skills/* ~/.claude/skills/
```

## The 15 skills

### Discovery & Research

| Skill | When to use | Example |
|---|---|---|
| [`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md) | Dig past a stakeholder's feature request to the real underlying need, using 5 consecutive Why questions, then surface alternative solutions. Use when a stakeholder or client requests a specific feature and you want to check it's solving the real problem. | [See output](skills/five-whys-root-cause/EXAMPLE.md) |
| [`user-interview-synthesis`](skills/user-interview-synthesis/SKILL.md) | Turn messy interview notes from multiple users into ranked insights, frustrations, and unspoken needs. Use after collecting raw notes from user interviews. | [See output](skills/user-interview-synthesis/EXAMPLE.md) |
| [`persona-pretest`](skills/persona-pretest/SKILL.md) | Simulate how a specific user persona would react to a design or flow, surfacing likely confusion, objections, and drop-off points before real user testing. Use when you want a fast sanity check on a design before investing in a usability study. | [See output](skills/persona-pretest/EXAMPLE.md) |

### Ideation

| Skill | When to use | Example |
|---|---|---|
| [`assumption-reversal`](skills/assumption-reversal/SKILL.md) | Flip your current design assumptions 180° and generate concrete ideas from the reversed perspective. Use when stuck on ideas or wanting to pressure-test the current design direction. | [See output](skills/assumption-reversal/EXAMPLE.md) |
| [`cross-industry-steal`](skills/cross-industry-steal/SKILL.md) | Find 3 solutions from unrelated industries that solve a structurally similar problem, and translate the strongest one into a concrete idea. Use when stuck on ideas or need fresh inspiration outside the category. | [See output](skills/cross-industry-steal/EXAMPLE.md) |

### Prioritization

| Skill | When to use | Example |
|---|---|---|
| [`decision-rationale`](skills/decision-rationale/SKILL.md) | Document a design decision between 2 options with explicit criteria, scenario testing, and a confidence-rated recommendation. Use when torn between two directions and need a defensible, written rationale - not just a gut call. | [See output](skills/decision-rationale/EXAMPLE.md) |
| [`design-scope-negotiator`](skills/design-scope-negotiator/SKILL.md) | Sort a design scope into Ship / Fast-follow / Cut buckets using effort vs. impact-if-removed, with opinionated reasoning for each. Use when pushing back on scope creep or negotiating what gets cut before a deadline. | [See output](skills/design-scope-negotiator/EXAMPLE.md) |

### Execution & Spec Writing

| Skill | When to use | Example |
|---|---|---|
| [`prd-first-draft`](skills/prd-first-draft/SKILL.md) | Write a PRD first draft that's clear enough for engineers to build from and concise enough for executives to read in 5 minutes. Use when starting to spec a feature or product. | [See output](skills/prd-first-draft/EXAMPLE.md) |
| [`edge-case-finder`](skills/edge-case-finder/SKILL.md) | Stress-test a feature across 5 failure dimensions (input, permissions, concurrency, dependencies, user behavior) before it ships. Use before handing a spec to engineering, to catch what breaks. | [See output](skills/edge-case-finder/EXAMPLE.md) |
| [`acceptance-criteria`](skills/acceptance-criteria/SKILL.md) | Turn a user story into airtight Given/When/Then acceptance criteria covering happy path, errors, and edge cases. Use to define "done" before engineering starts building. | [See output](skills/acceptance-criteria/EXAMPLE.md) |

### Communication

| Skill | When to use | Example |
|---|---|---|
| [`design-critique-facilitator`](skills/design-critique-facilitator/SKILL.md) | Facilitate a structured design critique across 4 lenses (clarity, hierarchy, consistency, edge cases), separating what's working from what needs attention. Use when presenting work for feedback, to get specific critique instead of vague opinions. | [See output](skills/design-critique-facilitator/EXAMPLE.md) |
| [`explain-to-4-audiences`](skills/explain-to-4-audiences/SKILL.md) | Translate one design decision into 4 audience-specific explanations (10-year-old, engineering, executive, end user) to pressure-test whether it's actually clear. Use after designing, before presenting, writing docs, or shipping. | [See output](skills/explain-to-4-audiences/EXAMPLE.md) |

### Analysis & Metrics

| Skill | When to use | Example |
|---|---|---|
| [`success-metrics-definition`](skills/success-metrics-definition/SKILL.md) | Design a metrics framework (primary metric, leading/lagging indicators, counter-metrics) that proves a feature solved the real problem, not just that it was used. Use when defining what success looks like before building. | [See output](skills/success-metrics-definition/EXAMPLE.md) |
| [`experiment-design`](skills/experiment-design/SKILL.md) | Design a full, statistically-honest experiment plan - hypothesis, control/variant, duration, decision rule - and flag if traffic is too low for a reliable result. Use when planning an A/B test or any product experiment. | [See output](skills/experiment-design/EXAMPLE.md) |
| [`data-interpretation`](skills/data-interpretation/SKILL.md) | Interpret metrics or experiment results by separating fact from explanation and ruling out alternative causes before recommending action. Use when reviewing results and need to draw a real conclusion, not just eyeball a chart. | [See output](skills/data-interpretation/EXAMPLE.md) |

## Recommended order

The categories are useful for browsing by type of work, but two skills sit at a different point in a real product timeline than their category suggests: `success-metrics-definition` belongs right after spec'ing, not at the end, and `design-scope-negotiator` fires under deadline pressure during execution, not right after ideation. To run the library end-to-end on a real feature, follow this order:


**1. Understand the problem**
- [`five-whys-root-cause`](skills/five-whys-root-cause/SKILL.md)
- [`user-interview-synthesis`](skills/user-interview-synthesis/SKILL.md)
- [`persona-pretest`](skills/persona-pretest/SKILL.md)
**2. Find directions**
- [`assumption-reversal`](skills/assumption-reversal/SKILL.md)
- [`cross-industry-steal`](skills/cross-industry-steal/SKILL.md)
**3. Choose a direction**
- [`decision-rationale`](skills/decision-rationale/SKILL.md)
**4. Spec it, define success alongside it**
- [`prd-first-draft`](skills/prd-first-draft/SKILL.md)
- [`success-metrics-definition`](skills/success-metrics-definition/SKILL.md)
- [`edge-case-finder`](skills/edge-case-finder/SKILL.md)
- [`acceptance-criteria`](skills/acceptance-criteria/SKILL.md)
**5. Get feedback before shipping**
- [`design-critique-facilitator`](skills/design-critique-facilitator/SKILL.md)
- [`explain-to-4-audiences`](skills/explain-to-4-audiences/SKILL.md)
**6. Under deadline pressure**
- [`design-scope-negotiator`](skills/design-scope-negotiator/SKILL.md)
**7. After it ships**
- [`experiment-design`](skills/experiment-design/SKILL.md)
- [`data-interpretation`](skills/data-interpretation/SKILL.md)

## License

[CC BY 4.0](LICENSE). Use, adapt, and share freely, including commercially, with attribution.
