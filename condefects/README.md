# Part 2: ConDefects (real bugs)

The same experiment as our main set, on real bugs instead of AI-written ones. [ConDefects](https://github.com/appmlk/ConDefects) (FSE 2024) collects buggy Python submissions from AtCoder contests (2021-2024), each with the fixed submission and AtCoder's official tests.

## What's here
- `programs/<task>/`: one AtCoder problem each (e.g. `abc280_c`), 120 in all, 30 per person:
  - `buggy.py`: the real buggy submission, with its own comments removed and a `# COMMENT` placeholder as the first line
  - `correct.py`: the same person's fixed submission (comments removed)
  - `tests/in/`, `tests/out/`: AtCoder's tests for the problem
  - `info.json`: like the main set (`problem`, `bug_type`, `bug_description`, `comments`, `author`, `generated_by`), plus `task` and `source` (ConDefects ID, AtCoder link, difficulty, the buggy and fixed line)
  - `versions/`: the 4 comment versions, made by `cd.py`
- `COMMENTING.md`: instructions for the AI tool that writes each program's description and comments
- `cd.py`: the checker (`python3 condefects/cd.py [folders]`), the ConDefects version of `check.py`
- `prompts/`: Prompts A and B, identical to ours except "program" instead of "function"
- `select_bugs.py`: how the 120 were picked (run once; needs ConDefects and its 20.8 GB test ZIP)
- `memorize.py`: the memorization check
- `results/`, `judgments/`, `handcheck/`, `memorization/`: same as the main set's folders

## How the 120 were picked
`select_bugs.py`, run once by Ankit on 2026-11-15:
- Python submissions to AtCoder Beginner Contest problems with difficulty under 800, 5-60 lines.
- Exactly one line differs between the buggy and fixed code (ignoring comments), and the change is logic: not only a comment, output wording, import, input reading or recursion setting. Standard library only.
- Not just output format (the same value printed differently) or a misspelled word; the few such cases no rule catches are listed in `BY_HAND` in `select_bugs.py`, and hard-coded test input left in the code doesn't count either.
- One bug per problem (its submissions in a fixed random order, first that fits), and problems tried in a fixed random order (seed 2026 for both).
- AtCoder's tests, minus any over 100 KB and any the fixed code needs over 1 second for (both mostly check speed; this keeps the repo small and leaves room for slower cloud CPUs, where grading allows 10 seconds per test). The fixed code must pass all the rest, and the buggy code must give a wrong answer or crash on at least one, not just run too slowly.
- The first 120 problems that pass, dealt out to the four of us in turn.

## Differences from the main set
- The programs are whole scripts that read input and print the answer, so a fix passes a test if it prints the same answer as AtCoder's expected output (ignoring spacing).
- The comment goes at the top of the program instead of inside a function.
- The bugs are real, so the `bug_type` mix is whatever the bugs are, not 30/30/30/30.
- `wrong_output` comments look like `Example: input '3 4\n1 2 3' prints 2`.

## Memorization check
These programs are public, so the models may have seen them in training. `memorize.py` shows each model every program (ours and ConDefects) only up to just before the buggy line, and asks it to write the rest, so we see whether it recalls the buggy line, the fixed line, or the rest of the program. Our programs are new, so their scores show what "not memorized" looks like; ConDefects programs scoring above all of ours are likely memorized, and we report the results with and without them. One person runs it once per model, with step 8 of `colab_run.ipynb` (7B, a few minutes) and `kaggle_run.ipynb` (32B, about half an hour); everyone else skips that step.

## Labeling and analysis
Same as the main set (`JUDGING.md`): `judge.py` labels these results too, `python3 handcheck.py condefects` builds the hand-check sheets (6 random programs per person, drawn before any results), and `python3 analyze.py condefects` makes the tables.
