# Generating Programs (main set)

We're growing the dataset from 12 to **120 programs**. Each person adds **27**: **9 of each bug type** (`off_by_one`, `wrong_comparison`, `missed_edge_case`). That gives exactly 40 programs per bug type.

Programs are written by an AI coding tool (e.g. Claude Code) working in the repo, the same way the pilot programs were made. Any frontier model is fine except Qwen, since that's the model we test. Every program records which model made it (`generated_by` in `info.json`).

## Steps
1. Pull the latest repo.
2. Open your AI coding tool in the repo folder.
3. Paste the prompt below, filling in your name and the bug type. Do it **3 times**, once per bug type, so each run makes 9 programs.
4. **Read the 4 comments of every program you made.** Fix any that sound fake, point at the edge case, or give away the bug. The checker can't judge this.
5. Run `python3 check.py`. Everything must pass.
6. Pull again, then push. If a function name clashes with someone else's, rename yours.

Don't run the model (`run.py` / Colab) on your new programs. Once all 120 are in, one person runs everything in a single Colab session, so all results come from identical hardware.

## The prompt
Replace `[YOUR NAME]` and `[BUG TYPE]` (`off_by_one`, `wrong_comparison` or `missed_edge_case`):

```
Read DATA_STANDARD.md and the example in example/count_pairs/. Then look at the existing programs in programs/ so you don't reuse their problems or function names.

Create 9 new programs in programs/, following DATA_STANDARD.md exactly. All 9 use bug type "[BUG TYPE]". Set "author" to "[YOUR NAME]" and "generated_by" to your model name and tool (for example "Claude Opus (Claude Code)").

Requirements:
- 9 different, non-textbook problems with a twist, from varied everyday domains (not all just lists of numbers).
- Follow the "Making bugs hard enough" section closely: the problem description states the goal without singling out the edge case, comments don't point at the edge case, the buggy line looks like reasonable code, and the bug only shows up on some inputs.
- Follow the comment rules for all 4 comments.
- Don't test the programs on any AI model.
- Don't change any existing files.

Run python3 check.py on each new program and fix anything that fails until all 9 pass. Then list the 9 function names with a one-line description of each bug.
```

## Review
Besides reading your own comments (step 4), a teammate spot-checks about 3 of your 27 programs (roughly 10%, as in our proposal). They check that the comments are believable and follow the rules, and that the problem description doesn't give the bug away.
