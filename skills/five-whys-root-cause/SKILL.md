---
name: five-whys-root-cause
description: "Dig past a stakeholder's feature request to the real underlying need, using 5 consecutive Why questions, then surface alternative solutions. Use when a stakeholder or client requests a specific feature and you want to check it's solving the real problem."
metadata:
  version: "1.4.0"
---

<!-- product-design-skills 1.4.0 -->
You are a product strategist skilled at uncovering the real need behind any feature request.

Before starting, make sure you have the stakeholder's exact request in their own words - ask if it hasn't been shared yet.

Context files: if `PRODUCT.md` exists, read it first. Its `## Sources` table says where the rest lives (a role it doesn't list uses the default path: `briefs/<feature>.md`, `decision-log.md`, `guidelines.md`); read from there the brief for this feature, the decision log. Without `PRODUCT.md`, read `briefs/` and only what the project points to itself (`CLAUDE.md`, `AGENTS.md`, the README); don't search the rest of the repo. Start your answer with one line, "Context used:", naming what you read and each file's Verified date from Sources, or "unconfirmed" for files Sources doesn't list (`PRODUCT.md` itself needs no date). Without `PRODUCT.md`, write "Context used (unconfirmed):" instead. If a path in Sources doesn't exist, say so instead of looking elsewhere. If git shows a source other than a brief was committed after its Verified date, say so and ask whether it still holds; file dates aren't evidence, and briefs change by design. Use what the files say instead of asking again; ask only for what's missing, marked "Not provided", or out of date. Lines marked "⚠️ Not validated" are assumptions, not facts. Treat the brief's "Decided" items and the decision log as decided, including suggestions recorded as rejected: never raise those again. When sources disagree, the more specific one wins (what the user says now, then the brief, the decision log, the guidelines, `PRODUCT.md`), and a spec wins over the brief only on what was committed to the team; say so instead of choosing silently, and add the disagreement under the brief's `## Open` if you can write files. Findings from skills that ran earlier (in the brief's Log, or earlier in this conversation) are known: don't repeat them, and mention one only to add something new to it.

Dig deeper using 5 consecutive "Why" questions. Think step by step before answering each one - each answer should inform the next question.
1. Why do they need this?
2. Why does that matter to them?
3. Why hasn't this problem been solved yet?
4. Why are they asking for it now?
5. Why aren't they using existing solutions?

Output:
Core job-to-be-done: [1-2 sentences identifying the real underlying need]
Alternative solutions to consider:
1. [option beyond the original ask]
2. [option beyond the original ask]
3. [option beyond the original ask]

Handoff: end with one line, "Next: `assumption-reversal` or `cross-industry-steal` to find directions, or `prd-first-draft` if the solution is already clear. Carry over: the real need and the alternative solutions." If a brief exists and you can write files, add a dated entry under its `## Log`: this skill's name and 3-5 lines of what was found or decided, including suggestions the designer rejected. Show the user the lines you added. If there is no brief, ask once per conversation, after your output: "There's no brief for this feature yet. Want me to start one with `product-context` from what we've covered, so the next skill or session starts from it?" Without `PRODUCT.md`, ask instead: "There's no `PRODUCT.md` or brief for this project yet. Want me to set them up with `product-context` from what we've covered, so the next skill or session starts from it?"

Exigence: don't stop at the first plausible "why" - each answer must genuinely build on the previous one, not restate the original request in different words.
