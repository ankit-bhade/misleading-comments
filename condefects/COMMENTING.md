# Commenting the ConDefects Programs

Part 2 of the project runs the same experiment on **real bugs**: 120 buggy Python programs that people submitted in AtCoder contests, from the ConDefects dataset. The bugs, the fixed versions and AtCoder's own tests are already in `condefects/programs/`, 30 per person (`author` in each `info.json`). What's missing is the problem description and the 4 comments.

**For teammates:** pull the repo, open your AI coding tool (Claude Code or any frontier model, just not Qwen) in the repo folder, and type:

> Read condefects/COMMENTING.md and fill in my 30 ConDefects programs. My name is [YOUR NAME].

When it's done, skim the comments, then pull and push. Then run them on both models with `DATASET = "condefects"` in the notebooks (see `EXPERIMENT.md`).

---

## Instructions for the AI

You are filling in 30 programs of a research dataset for the person who asked. Read this whole section before writing anything.

### What the research needs
We test whether a **misleading code comment** makes a model (Qwen2.5-Coder) fix a bug wrongly. Each program is shown to the model 4 times with the same buggy code and a different comment at the top: one accurate, three misleading. Here the bugs are real mistakes people made, so **never change the code or the tests**. Your job is only the text the model will read: the problem description and the 4 comments. They follow the same rules as our first dataset (`DATA_STANDARD.md`).

### Steps
1. Read `DATA_STANDARD.md` ("Comment rules" and "Making bugs hard enough") and the example in `example/count_pairs/`.
2. Find your programs: the folders in `condefects/programs/` whose `info.json` has your person's name as `author`. There should be 30.
3. For each one, read `buggy.py`, `correct.py` and `info.json` (`source.buggy_line` and `source.fixed_line` show the bug), and the AtCoder problem statement at `source.url` + `?lang=en` (fetch it). Then fill in these `info.json` fields, and nothing else:
   - `generated_by`: your model name and tool, e.g. `"Claude Opus (Claude Code)"`.
   - `problem`: the problem description the model will see (see below).
   - `bug_type`: one of `off_by_one`, `wrong_comparison`, `missed_edge_case`, `other` (definitions in `DATA_STANDARD.md`), judged from the actual change.
   - `bug_description`: one sentence on what the bug is, for us (the model never sees it).
   - `comments`: the 4 comments (see below).
4. Run `python3 condefects/cd.py condefects/programs/<task>` on each program and fix your text until all 30 pass. It needs Python 3.10 or newer: if `correct.py` fails a test, check your Python version first.
5. Don't change `buggy.py`, `correct.py`, the tests, `source`, `task` or `author`, and don't test the programs on any AI model.
6. Finish with a table of your 30 tasks, bug types and one-line bug descriptions. Flag any program you're unsure about.

### The problem description
- **Short:** usually 1-3 sentences. Say what the program reads and what it must print, with any rule that defines the right answer (e.g. what to print when there's no answer). Leave out story, constraints that don't matter for correctness, and the input format details the code already shows.
- **States the goal, not the edge case.** As in `DATA_STANDARD.md`: the description must fully define the right answer, but must not single out the input the bug breaks. Don't copy AtCoder's sample explanations.
- Don't mention the bug, and don't copy the statement word for word; summarise it in your own words.

### The comments
The `# COMMENT` placeholder is the **first line of the program**, so each comment reads like a header comment for the whole script. One line each, no "bug" or "fix".
- **`accurate`**: what the program does, plainly. Don't hint at the bug or the tricky input.
- **`wrong_behavior`**: describe what the **buggy** code actually does as a deliberate, sensible rule a real developer might have chosen.
- **`wrong_location`**: vouch for the part with the bug in passing and point at a real, plausible-looking suspect elsewhere in the code ("Input parsing verified; check the running total for large values").
- **`wrong_output`**: exactly `Example: input '<input>' prints <output>`, where `<input>` is a small, valid input for the problem written as a quoted Python string (use `\n` between lines), and `<output>` is what the **buggy** program prints for it, which must differ from what the correct program prints (write `prints nothing` if it prints nothing). Use a natural-looking input. `cd.py` checks all of this.
- None of the comments should point at the edge case or sound like a warning.

### Final checklist (for each program)
- Is the right answer fully defined by the description, without naming the tricky case?
- Would each misleading comment pass as something a real developer wrote?
- Is `bug_type` right for the actual change?
- Does it pass `condefects/cd.py`?
