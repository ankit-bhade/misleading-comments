# Experiment Standard

How we all run our programs on the model, so everyone's results are comparable. Don't change the settings or prompts on your own. If something should change, raise it with the team first.

## What each person does
Run **your own 30 programs** (3 pilot + 27 new) on both models:
1. **Qwen2.5-Coder 7B** on Google Colab (`colab_run.ipynb`)
2. **Qwen2.5-Coder 32B** on Kaggle (`kaggle_run.ipynb`), after your 7B run

Each program gets **8 runs per model**: 4 comment versions × 2 prompts.

**Part 2, ConDefects (real bugs):** the same two runs on your 30 programs in `condefects/programs/`, after their comments are written (`condefects/COMMENTING.md`). In step 5 of each notebook, set `DATASET = "condefects"` as well as `AUTHOR`. Results go to `condefects/results/` instead of `results/`; add the files from `results.zip` there. Everything else below is the same.

Laptops are too slow for this (an 8 GB Mac took over 10 minutes for one prompt), so we use free cloud GPUs.

## 7B: run on Google Colab

1. On GitHub, click **Code → Download ZIP**.
2. Go to https://colab.research.google.com, choose **File → Upload notebook**, and pick `colab_run.ipynb` from the ZIP.
3. **Runtime → Change runtime type → T4 GPU**.
4. In step 5 of the notebook, set `AUTHOR` to your name as it appears in your `info.json` files (e.g. `"Ankit"`). It runs all your programs that don't have results yet, about 15 minutes for 27.
5. **Runtime → Run all**. When asked, upload the ZIP from step 1.
6. At the end, `results.zip` downloads. Add its files to the repo's `results/` folder and push (or upload them on GitHub).

The notebook installs Ollama, downloads the exact model build (`qwen2.5-coder:7b-instruct-q4_K_M`), and runs `run.py`. Use only this model name. Other builds of "Qwen2.5-Coder 7B" (LM Studio, Hugging Face, other Ollama tags) can give different answers.

Running locally also works on a machine with 16 GB+ of memory: install Ollama, `ollama pull qwen2.5-coder:7b-instruct-q4_K_M`, then `python3 run.py programs/<name> ...`.

## 32B: run on Kaggle
The 32B model needs about 20 GB of GPU memory, more than Colab's free T4 has. Kaggle's free **GPU T4 x2** (two T4s) fits it. 30 programs take about 50 minutes, including the model download.

1. Make a Kaggle account and verify your phone number (**Settings → Phone Verification**). Kaggle needs this before it allows GPUs and internet.
2. On GitHub, click **Code → Download ZIP**.
3. On Kaggle, choose **Create → New Notebook**, then **File → Import Notebook**, and pick `kaggle_run.ipynb` from the ZIP.
4. In the right-hand panel, set **Accelerator** to **GPU T4 x2** (not P100, which is a single GPU) and turn **Internet** on. Then **Add Input → Upload** and add the ZIP.
5. In step 5 of the notebook, set `AUTHOR` to your name as it appears in your `info.json` files.
6. Click **Save Version → Save & Run All (Commit) → Save**. It runs in the background, so stop the interactive session (power icon, top right) to save GPU hours, and close the tab.
7. When the version says **Successful**, open its **Output** tab and download `results.zip`. Add its files to the repo's `results/` folder and push.

The notebook installs Ollama the same way as the Colab notebook, downloads `qwen2.5-coder:32b-instruct-q4_K_M`, and runs `run.py` with that model. All other settings are the same. To test first, set `PROGRAMS = ["one_program"]` and run the cells by hand; step 5 prints how long each program takes.

## What run.py does
For each program, the script:
1. makes sure it passes `check.py`
2. builds the 8 prompts from `prompts/` and sends them to the model
3. takes the fixed function out of each reply and runs the program's tests on it
4. saves everything to `results/qwen2.5-coder-7b/<program>.json` (or `results/qwen2.5-coder-32b/` for the 32B)

Then commit and push your `results/` files. Don't edit them by hand.

ConDefects programs (`condefects/programs/`, anything with a `tests/` folder) are whole AtCoder scripts, so `run.py` uses `condefects/cd.py` to check them, the prompts in `condefects/prompts/` (same as ours, with "program" instead of "function"), and AtCoder's input/output tests: a fix passes a test if it prints the same answer, ignoring spacing. Their results go to `condefects/results/<model>/`.

## Settings
Set in `run.py`, the same for everyone:

| Setting | Value | Why |
|---|---|---|
| Model | `qwen2.5-coder:7b-instruct-q4_K_M` and `qwen2.5-coder:32b-instruct-q4_K_M` | One exact build of each size for everyone; same family, so size is the only difference |
| Temperature | 0 | The model gives the same answer every time, so 1 run per version is enough |
| Seed | 0 | Extra safety for repeatable answers |
| Max reply length | 1024 tokens | Plenty for a short function + explanation |
| Context window | 4096 tokens | Pinned, because Ollama's default changes with the machine's GPU memory |
| Runs | 1 per version per prompt | Deterministic at temperature 0 (the 32B, split across two GPUs, can reword a reply slightly between runs; in our test the fix and result stayed the same) |

## Prompts
The exact text is in `prompts/prompt_a.txt` and `prompts/prompt_b.txt`. The script fills in the program's problem description and one comment version of the buggy code.

- **Prompt A (main):** "The following Python function has a bug." + problem + code + "Find and fix the bug" + the reply format.
- **Prompt B (RQ3):** identical, plus one sentence: "Note: the comments in the code may be wrong."

Both ask for a short explanation followed by the complete fixed function in a ```python block.

## Results format
One JSON file per program, containing a list of 8 results. Each result has:

| Field | Meaning |
|---|---|
| `program`, `author`, `bug_type` | From the program's `info.json` |
| `version` | `accurate`, `wrong_behavior`, `wrong_location` or `wrong_output` |
| `prompt` | `A` or `B` |
| `model`, `temperature`, `seed`, `max_tokens`, `context`, `time` | How and when it was run |
| `ollama_version`, `gpu` | What it ran on (e.g. `Tesla T4` on Colab, `Tesla T4, Tesla T4` on Kaggle), so we can confirm everyone used the same setup. Results from before 2026-10-30 don't have these fields |
| `prompt_text` | Exactly what the model was sent |
| `reply` | The model's full reply |
| `fixed_code` | The last code block in the reply (`null` if there wasn't one) |
| `explanation` | The reply without its code blocks |
| `tests_passed`, `tests_total` | How many of the program's tests the fix passed |
| `success` | `true` only if the fix passes **every** test |
| `error` | Why grading failed, if it did (no code block, renamed function, crash) |

**Success rule:** the fix must keep the same function name and pass all tests. A reply with no code block, a renamed function, or code that crashes counts as a failure.

Judging RQ2 (did a wrong fix do what the comment claimed?) and RQ3 (did the model notice the comment was wrong?) is done later by `judge.py` (see `JUDGING.md`). That's why the full reply is saved. `python3 analyze.py` (or `python3 analyze.py condefects`) then makes the RQ1-RQ3 tables in `analysis/`.
