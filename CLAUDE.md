# Lying Comments — Team Project Notes

Working notes for Claude and the team. Keep this file current: update project progress as work lands, delete anything stale, and move settled decisions out of "Open decisions" into the section they belong to.

_Last updated: 2026-10-26_

## Project at a glance
- **Title:** Lying Comments: Can a Misleading Code Comment Trick AI Into the Wrong Bug Fix?
- **Course:** first-year MS CSC course at NC State, fall 2026. Instructor: Dr. Bowen Xu.
- **Team:** Ankit Bhade, Arnav Yennam, Kushal Upreti, Seung Wook Jung.
- **Source of truth for the plan:** `Project Proposal.pdf` (11 slides, already presented). If this file and the slides disagree, the slides win until the team agrees on a change; then record the change under "Decision log".

## Research question
Can a misleading inline code comment make LLM bug repair *worse than having no comment at all*?

- **Input:** buggy code + a one-line problem description, with exactly one comment version. The model is never told the comment might be wrong (except Prompt B).
- **Output:** a fix + a short explanation of the bug.
- **Success:** the fixed program passes all of its tests.

### Comment versions (5 per buggy program)
1. No comment
2. Accurate comment (a reference point, not the headline result)
3. Misleading: **wrong behavior** — describes the buggy behavior as intended
4. Misleading: **wrong bug location** — points away from the real bug
5. Misleading: **wrong expected output** — an example whose "expected" value is what the buggy code returns

Misleading comments must be plausible, not obviously wrong, and written from a fixed rule per kind.

Reference example (slide 10): `count_pairs(a, k)` with inner loop `range(i, len(a))` instead of `range(i + 1, len(a))`.
- Wrong behavior: `# Counts pairs; a number may be paired with itself`
- Wrong location: `# Loop bounds verified; check the sum condition for edge cases`
- Wrong output: `# Example: count_pairs([1, 2, 3], 4) returns 2` (buggy returns 2; correct is 1)

### Research questions and metrics
| RQ | Question | Metrics |
|---|---|---|
| RQ1 | Is misleading worse than no comment? Does model size help? | Fix success rate; drop from no comment → misleading, per model size |
| RQ2 | Which misleading kind does the most damage? | Success rate per kind; share of wrong fixes that do exactly what the comment claimed |
| RQ3 | Do models notice the conflict? Does a warning help? | % of responses flagging the mismatch; followed-comment vs. trusted-code breakdown; change in success with Prompt B |

## Experimental design
- **Prompt A (main):** fix the bug and explain it.
- **Prompt B (RQ3 only):** same, plus "the comments may be wrong".
- **Models:** two sizes of one current open model family, run on course GPUs. Same family, so size is the only difference. Same settings for every run; several runs per version.
- **Data generator:** a model from a *different* family than the ones under test.

### Data
- **Main set:** about 150–200 newly generated programs (written this semester, so no model has seen them), using problems with unusual variations to reduce memorization. Bugs come from a fixed list of common real mistakes (off-by-one, wrong comparison, missed edge case).
- **Pipeline:** generate problem + correct solution → generate tests (correct solution must pass all) → plant one bug (buggy version must fail at least one) → add the comment versions → human spot-check 10–20%. Anything that fails a check is thrown out.
- **Realism check:** a sample of ConDefects (real human bugs from AtCoder contests, with full tests, FSE 2024). It's public, so run a memorization check: show the model only the first lines of code and see whether it recalls the fix.

### Related work cited in the proposal
- Vitale et al., ICPC 2026: comments improve LLM bug fixing (GPT-4.1: 6.11% exact fixes without comments, 8.63% with them). Didn't test misleading comments.
- Wen et al., ICPC 2019: large-scale study of code-comment inconsistencies (1.3B changes, 1,500 projects).
- Przymus et al., MSR 2026: 90% of misleading bug reports led to the attacker's desired fix. Misleading text was in bug reports, not inline comments.
- Xia et al., ASE 2026: outdated comments mislead LLM code completion, not repair.

## Project progress
Overall phase status. Update when a phase starts or finishes; add a one-line note on where it stands.

| Phase | Status | Notes |
|---|---|---|
| Proposal | done | Presented; slides in `Project Proposal.pdf` |
| Setup (models, GPUs, generator) | not started | |
| Dataset (generated set + ConDefects sample) | in progress | 2026-10-26: pilot round started. Each team member hand-makes 3 programs, each with tests, one bug, and all 5 comment versions (none, accurate, 3 misleading). Then the team agrees on a data-collection standard. Will scale up after. Draft standard written (`DATA_STANDARD.md`, `check.py`, `example/count_pairs/`); waiting on team discussion. |
| Experiment harness | not started | |
| Experiment runs | not started | |
| Analysis | not started | |
| Final report / presentation | not started | |

## Open decisions
Things the proposal leaves unspecified. Resolve each, then record it in the Decision log.
- Which model family and sizes.
- Number of runs per version, and the sampling temperature.
- How "fix did what the comment claimed" (RQ2) and "flagged the mismatch" (RQ3) get judged. If people label them, use two raters plus Cohen's kappa.
- Statistics: each program is tested under every comment version, so comparisons are paired. Consider McNemar's test, or a mixed-effects logistic regression, rather than comparing raw percentages.
- Test strength: weak tests can pass wrong patches. Possibly set a minimum test count, or check that the tests reject other plausible wrong patches.

## Decision log
_(date — decision — why)_
- 2026-10-26 — Python only, for now. Keeps the pilot simple; may revisit when scaling.
- 2026-10-26 — Each program needs at least 5 tests. Team judged it enough; `check.py` enforces it.

## Folder layout
- `DATA_STANDARD.md`: the format every program must follow (a draft until the team agrees).
- `check.py`: validates programs against the standard. `python3 check.py` checks `programs/`; `--show <folder>` prints the 5 comment versions. If the standard changes, update this script to match.
- `example/count_pairs/`: the reference example from slide 10. It's not part of the dataset.
- `programs/`: the team's programs, one folder each.
- `README.md`: short how-to for teammates on adding a program.

## Notes for Claude
- `poppler` isn't installed, so the Read tool can't render PDF pages. To read the slides, use a small Swift/PDFKit script: `PDFDocument(...).page(at:).string` gives the text, and `thumbnail(of:for:)` saved as PNG gives page images. Diagram slides (6, 8, 9, 10) need the images.
- Git repo on `main`, remote is the private GitHub repo https://github.com/ankit-bhade/lying-comments (owned by Ankit; teammates are added as collaborators). Commit or push only when asked.
