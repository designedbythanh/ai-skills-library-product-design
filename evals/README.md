# Evals

Small test cases for `claude plugin eval`. Each case is a prompt plus a few criteria, written in plain words, that Claude Sonnet grades the answer against. Results for each skill are in its EVAL.md.

## The cases

| Cases | Skill | What they check |
|---|---|---|
| `critique-01` to `critique-05` | [`design-critique-facilitator`](../skills/design-critique-facilitator/EVAL.md) | Asks before critiquing, measures contrast before praising, flags failing colors without false alarms, keeps decided items, stays out of a bug fix |
| `edge-01` to `edge-05` | [`edge-case-finder`](../skills/edge-case-finder/EVAL.md) | Asks or states the build stage, ranks prototype shortcuts against it, covers all five kinds of failure, stays out of a translation |
| `edge-06` | [`edge-case-finder`](../skills/edge-case-finder/EVAL.md) | A bug from real work: changing scope while a save is running |
| `persona-01` | [`persona-pretest`](../skills/persona-pretest/EVAL.md) | A miss from real work: concept problems behind a narrow question |
| `context-01` to `context-05` | [`product-context`](../skills/product-context/EVAL.md) | Writes `PRODUCT.md` and a brief, other skills read them, add to the Log and end with a "Next" line |

## Run them

From the repo root:

```bash
claude plugin eval . --case 'edge-*' --runs 3
claude plugin eval . --case 'critique-*' --runs 3 --allow-tools Bash
claude plugin eval . --case 'context-*' --runs 3 --scaffold --allow-tools Bash Write Edit
```

`--case` takes one pattern per command. By default each case also runs without the plugin, so you see the difference. In my runs, one answer cost about $0.05 to $0.40 with Claude Opus 5.5, and more when a case has many criteria to grade. Results go to `evals/results/`, which isn't committed.

## How I test, and what that can't show

- Each case runs 3 times with the plugin and 3 times without it, with Claude Opus 5.5. Claude Sonnet grades.
- **I read every failed criterion myself.** The grader has been wrong in most rounds, in both directions: failing correct answers, and passing loose ones. Where my reading differs, the EVAL pages say so and use mine.
- The cases are small and described in text. The skills never had to find things in a real design.
- One model, 3 runs per arm. The same prompt can give different output on another day.
- I wrote the cases and the criteria, and I scored the results. Nobody else checked the scoring.
- Some cases are rewritten from my real work as "Northbeam", a fictional recruiting tool. The prototypes and answer keys behind them stay private.
