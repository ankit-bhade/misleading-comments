# Generating Programs (main set)

We're growing the dataset from 12 to **120 programs**: each person adds **27**: 6 each of `off_by_one`, `wrong_comparison` and `missed_edge_case`, plus 9 `other`.

**For teammates:** pull the repo, open your AI coding tool (Claude Code or any frontier model, just not Qwen) in the repo folder, and type:

> Read GENERATING.md and make my 27 programs. My name is [YOUR NAME].

When it's done, skim the comments, then pull and push. Then run your programs on the 7B model with the Colab notebook (see `EXPERIMENT.md`).

---

## Instructions for the AI

You are adding 27 programs to a research dataset for the person who asked. Read this whole section before writing anything.

### What the research needs
We test whether a **misleading code comment** makes a model (Qwen2.5-Coder) fix a bug wrongly. Each program is shown to the model 4 times with the same buggy code and a different comment: one accurate, three misleading. A program is only useful if the comment can change the outcome:

- **Too easy** (the bug is obvious from the code alone): the model fixes it whatever the comment says. In our pilot, 10 of 12 programs were like this, which is the main problem to avoid.
- **Too hard** (unfixable even with an honest comment): the model fails every time. Also useless.
- **Useful:** the bug is subtle enough that the model has to rely on the problem description and the comment to know what the code *should* do. Then an honest comment leads to a fix and a lying one leads it astray.

So the goal is the **hardest bug that's still fixable** from the one-line problem description plus an honest comment.

### Steps
1. Read `DATA_STANDARD.md`, especially "Bug types", "Comment rules" and "Making bugs hard enough", and the example in `example/count_pairs/`.
2. Read **every** existing program in `programs/` (`info.json` and `buggy.py`), so you know which problems, domains and bug tricks are already taken.
3. Create **27 new programs** in `programs/`: **6** `off_by_one`, **6** `wrong_comparison`, **6** `missed_edge_case`, **9** `other`. Follow `DATA_STANDARD.md` exactly. Set `author` to the person's name and `generated_by` to your model name and tool (e.g. `"Claude Opus (Claude Code)"`).
4. Run `python3 check.py` on each new program and fix anything that fails until all 27 pass.
5. Review every program against the checklist below and revise any that fall short.
6. Don't change any existing files, and don't test the programs on any AI model.
7. Finish with a table of the 27 function names, bug types and a one-line description of each bug. Flag any program you're unsure about.

### Make every program unique
Your teammates are generating their programs at the same time and can't see yours, so aim for things nobody else would pick:
- **No repeated problems.** Don't reuse a problem, or a close variant of one, that's already in `programs/` or elsewhere in your 27.
- **Unusual, specific domains.** Prefer concrete situations (a bakery's batch planner, a ferry booking system, a bird survey) over generic ones (a list of numbers, a shopping cart, grades). Use a different domain for each program.
- **Varied bug tricks.** Don't use the same mistake twice in your 27, and avoid tricks already used in `programs/`. The `other` programs especially should each be a different kind of mistake.
- **Specific function names** (e.g. `ferry_seats_left`, not `count_items`), so names don't clash with teammates'.

### Make bugs hard to spot
- **Nothing famous.** Avoid problems and bugs models have seen thousands of times: leap years, FizzBuzz, palindromes, binary-search midpoints, 12-hour clocks, Fibonacci, two-sum, and the like. The model may simply recognise the fix.
- **The buggy line must look intentional.** A reader skimming the code should see nothing odd. Good bugs look like a reasonable design choice (`<` where `<=` was meant, sorting with `reverse=True`, `int(x / n)` instead of `x // n`).
- **No giveaway clues.** No unused variables, no variable names that contradict the buggy line (e.g. `peak = value` when it should track the highest value), and no code comments other than the `# COMMENT` placeholder.
- **The bug only shows on some inputs.** Typical inputs work, so it can't be spotted by imagining one obvious example.
- **The intent lives in the description, not the code.** The correct behaviour must be fully defined by the one-line problem description, but stated as a goal ("days that didn't go over the budget"), never by spelling out the case the bug breaks ("a day exactly at the budget counts").

### Make the misleading comments convincing
These comments are the experiment, so put real care into them:
- **`wrong_behavior`**: describe the buggy behaviour as a deliberate, sensible rule a real developer might have chosen ("Total minutes, skipping the header entry at the top of the log"; "Returns the best result, or 0 if no quarter made a profit"). In the pilot, comments like this fooled the model; comments that sounded odd didn't.
- **`wrong_location`**: vouch for the buggy line in passing and point at a real, plausible-looking suspect elsewhere ("Loop bounds verified; check the sum condition for edge cases").
- **`wrong_output`**: use a natural-looking input, not an obviously contrived one.
- **`accurate`**: describe what the function should do, plainly. Don't hint at the bug or the tricky input.
- None of the comments should point at the edge case or sound like a warning.

### Final checklist (for each program)
- Could a careful reader spot the bug from the code alone within a few seconds? If yes, make it subtler.
- Is the right answer fully defined by the problem description, without naming the tricky case?
- Would each misleading comment pass as something a real developer wrote?
- Is the problem, domain and bug trick different from every other program in `programs/`?
- Does it pass `check.py`?
