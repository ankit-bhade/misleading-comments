# Lying Comments

**Can a misleading code comment trick AI into the wrong bug fix?**

Team project for Dr. Bowen Xu's course at NC State (fall 2026): Ankit Bhade, Arnav Yennam, Kushal Upreti, Seung Wook Jung.

We show an LLM a buggy program with a one-line problem description and ask it to fix the bug. Each program is shown four times, changing only one code comment:

| Comment | What it says |
|---|---|
| `accurate` | What the code should do (the baseline) |
| `wrong_behavior` | Describes the buggy behavior as intended |
| `wrong_location` | Vouches for the buggy part and points somewhere else |
| `wrong_output` | An example whose "expected" answer is what the buggy code returns |

A fix counts as a success only if the fixed program passes all of its tests. We test two sizes of one model family (Qwen2.5-Coder 7B and 32B) and two prompts: Prompt A asks for a fix, and Prompt B adds "the comments in the code may be wrong". We do this on two datasets: 120 new programs with one planted bug each, and 120 real one-line bugs from [ConDefects](https://github.com/appmlk/ConDefects). In total that's 3,840 fixes: 240 programs × 4 comments × 2 prompts × 2 models.

## Results at a glance

Fix success, Prompts A and B together (240 replies per cell):

| Dataset | Model | accurate | wrong_behavior | wrong_location | wrong_output |
|---|---|---|---|---|---|
| Our 120 programs | 7B | 71% | 68% | **61%** | 75% |
| | 32B | 85% | 84% | 83% | 89% |
| ConDefects (real bugs) | 7B | 50% | 45% | 47% | 51% |
| | 32B | 72% | 69% | 69% | 69% |

- **RQ1:** misleading comments hurt a little, and mostly the smaller model. The only significant drop is `wrong_location` on 7B: −10 points, p = 0.003 (paired exact McNemar test).
- **RQ2:** `wrong_location` does the most damage. When 7B's fix fails after it, the bug is left in place 76% of the time, against 61% after an accurate comment.
- **RQ3:** models almost never question the comment. Without a warning, 7B flagged 0 of 720 misleading comments and 32B flagged 5. The Prompt B warning raises that to at most 8% (32B, our programs), but it doesn't change fix success.
- The memorization check found no sign that the models had memorized ConDefects.

The full tables are in [`analysis/main.md`](analysis/main.md) and [`analysis/condefects.md`](analysis/condefects.md), and the charts are in [`analysis/charts/`](analysis/charts/).

## What's in the repo

| Path | Contents |
|---|---|
| `programs/<name>/` | Our 120 programs: `correct.py`, `buggy.py` (with a `# COMMENT` placeholder), `tests.py`, `info.json` (description, bug type, the 4 comments, author, generating model), and `versions/` (the 4 commented versions) |
| `condefects/programs/<task>/` | The 120 ConDefects bugs: `buggy.py`, `correct.py`, AtCoder's tests in `tests/in`, `tests/out`, and `info.json` with the source link |
| `example/count_pairs/` | The worked example from the proposal (not part of the dataset) |
| `prompts/`, `condefects/prompts/` | Exact text of Prompts A and B |
| `results/<model>/`, `condefects/results/<model>/` | Every model reply, one JSON per program (8 records: 4 comments × 2 prompts), with the prompt, reply, extracted fix, test outcome, model settings, Ollama version and GPU |
| `judgments/`, `condefects/judgments/` | RQ2 and RQ3 labels for every reply |
| `handcheck/`, `condefects/handcheck/` | Human verification sheets for the AI judge's RQ3 labels |
| `condefects/memorization/` | Memorization-check replies and scores |
| `analysis/` | Final tables (`main.md`, `condefects.md`) and slide charts (`charts/`) |
| `colab_run.ipynb`, `kaggle_run.ipynb` | Notebooks we used to run the models (7B on a Colab T4, 32B on Kaggle 2×T4) |

**Scripts.** Each script's docstring explains how to use it.

| Script | What it does |
|---|---|
| `check.py` | Checks that our programs follow the data standard and builds the 4 versions |
| `condefects/cd.py` | The same, for ConDefects programs |
| `run.py` | Sends the 8 prompts per program to the model via Ollama, grades each fix and saves the results |
| `judge.py` | Labels RQ2 by rerunning failed fixes, and RQ3 with an AI judge via OpenRouter |
| `handcheck.py` | Builds the human verification sheets |
| `analyze.py` | Makes the RQ1-RQ3 tables and statistical tests |
| `analysis/charts/make_charts.py` | Makes the charts |
| `condefects/select_bugs.py` | How the 120 ConDefects bugs were picked |
| `condefects/memorize.py` | The memorization check |

**Docs.**

| File | Contents |
|---|---|
| [`DATA_STANDARD.md`](DATA_STANDARD.md) | Program format, bug types and comment rules |
| [`GENERATING.md`](GENERATING.md) | The instructions our AI coding tools followed to write the programs |
| [`condefects/COMMENTING.md`](condefects/COMMENTING.md) | The same, for the ConDefects descriptions and comments |
| [`EXPERIMENT.md`](EXPERIMENT.md) | Model settings, prompts, results format, and how to run the notebooks |
| [`JUDGING.md`](JUDGING.md) | RQ2 and RQ3 labeling rules |
| [`condefects/README.md`](condefects/README.md) | How the ConDefects bugs were picked, and how that part differs from the main set |

## Requirements

- **Python 3.10 or newer.** Only the standard library is needed, except for the charts (`pip install matplotlib`). Some ConDefects programs fail their tests on older Python.
- **Running the models:** [Ollama](https://ollama.com) and a GPU. 7B (`qwen2.5-coder:7b-instruct-q4_K_M`) fits a 16 GB T4; 32B (`qwen2.5-coder:32b-instruct-q4_K_M`) needs about 20 GB, e.g. two T4s.
- **RQ3 judge only:** an [OpenRouter](https://openrouter.ai) API key in `OPENROUTER_API_KEY`. Labeling all 2,880 misleading-comment replies cost about $2.50.

## Reproducing the results

Run everything from the repo root.

**1. Recompute the tables and charts from the saved results (no GPU needed):**
```
python3 analyze.py               # -> analysis/main.md
python3 analyze.py condefects    # -> analysis/condefects.md
python3 condefects/memorize.py summary
python3 analysis/charts/make_charts.py   # needs matplotlib
```

**2. Check the datasets.** This confirms each correct program passes all its tests, each buggy one fails at least one, and every `wrong_output` example matches the buggy code. It also rebuilds `versions/`.
```
python3 check.py
python3 condefects/cd.py
```

**3. Rerun the models.** Open `colab_run.ipynb` on Google Colab (T4 GPU) for 7B, or `kaggle_run.ipynb` on Kaggle (GPU T4 ×2) for 32B, and set `PROGRAMS` or `AUTHOR` and `DATASET` in step 5. Step-by-step instructions are in `EXPERIMENT.md`. On a machine with Ollama and enough GPU memory:
```
ollama pull qwen2.5-coder:7b-instruct-q4_K_M
python3 run.py programs/count_valid_discounts condefects/programs/abc280_c
```
`run.py` overwrites the saved result for each program it runs. Settings (temperature 0, seed 0, 1024 max tokens, 4096 context) are constants at the top of `run.py`; set `MODEL` there for 32B.

**4. Relabel the replies.** RQ2 labels are computed by running code. RQ3 labels need the OpenRouter key. Labels that already exist are skipped, so delete `judgments/` to redo them.
```
OPENROUTER_API_KEY=... python3 judge.py
```

**5. Memorization check:** step 8 of either notebook, with `MEMORIZE = True`.

**6. Re-select the ConDefects bugs:** `select_bugs.py` needs the ConDefects repository and its test ZIP (about 21 GB); see its docstring. You don't need this to use the 120 bugs already here.

## Notes for replication

- **Determinism.** At temperature 0, the 7B model on one T4 gave word-for-word identical replies on rerun. The 32B model split across two GPUs occasionally rewords a reply; in our test the fix and its result stayed the same.
- **Ollama versions.** Colab and Kaggle install the latest Ollama, so our runs used 0.40.13 to 0.40.16 (recorded in every result). Pin the version if you rerun.
- **Program generation.** The 108 programs added after the pilot, and the descriptions and comments for the ConDefects bugs, were written by Claude Opus 5.5 (Claude Code) following `GENERATING.md` and `condefects/COMMENTING.md`. The 12 pilot programs were made by team members in the same format; `generated_by` in each `info.json` records what is known. New programs were never tested on Qwen before their run, and none were dropped based on results.
- **RQ3 judge.** GPT-6.1 Terra via OpenRouter, with the rules in `JUDGING.md`. We hand-checked each person's 6 randomly sampled programs plus every reply the judge marked "yes" (620 labels in all), and confirmed every label.
- **Time limit.** ConDefects fixes get 10 s per test. One correct but slow brute-force fix (`abc264_c`, 32B) timed out on Kaggle and is counted as failed.
