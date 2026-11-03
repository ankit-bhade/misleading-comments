# Generating Programs (main set)

We're growing the dataset from 12 to **120 programs**: each person adds **27**.

**For teammates:** pull the repo, open your AI coding tool (Claude Code or any frontier model, just not Qwen) in the repo folder, and type:

> Read GENERATING.md and make my 27 programs. My name is [YOUR NAME].

When it's done, skim the comments, then push. Don't run the model on them; one person runs all 120 at the end.

---

## Instructions for the AI

You are adding 27 programs to this dataset for the person who asked. Do the following:

1. Read `DATA_STANDARD.md` (all of it, especially "Comment rules" and "Making bugs hard enough") and the example in `example/count_pairs/`.
2. Look at the existing programs in `programs/` so you don't reuse their problems or function names.
3. Create **27 new programs** in `programs/`: **9** with bug type `off_by_one`, **9** with `wrong_comparison`, **9** with `missed_edge_case`. Follow `DATA_STANDARD.md` exactly.
   - `author`: the person's name.
   - `generated_by`: your model name and tool, e.g. `"Claude Opus (Claude Code)"`.
   - Every program is a different, non-textbook problem with a twist, from varied everyday domains (not all just lists of numbers).
   - Follow "Making bugs hard enough" closely: the problem description states the goal without singling out the edge case, comments don't point at the edge case, the buggy line looks like reasonable code, and the bug only shows up on some inputs.
4. Run `python3 check.py` on each new program and fix anything that fails until all 27 pass.
5. Don't change any existing files, and don't test the programs on any AI model.
6. Finish with a table of the 27 function names, their bug types, and a one-line description of each bug, so the person can skim them.
