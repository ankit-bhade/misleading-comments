# Experiment Standard (pilot)

How we all run our programs on the model, so everyone's results are comparable. Don't change the settings or prompts on your own. If something should change, raise it with the team first.

## What each person does
Run **your own 3 programs** on Qwen2.5-Coder 7B. The 32B round comes later.

Each program gets **8 runs**: 4 comment versions × 2 prompts.

## Setup (once)
1. Install Ollama: https://ollama.com/download
2. Download the exact model build we all use (about 4.7 GB):
   ```
   ollama pull qwen2.5-coder:7b-instruct-q4_K_M
   ```
3. Make sure the Ollama app is running.

Use this exact model name. Other builds of "Qwen2.5-Coder 7B" (LM Studio, Hugging Face, other Ollama tags) can give different answers.

## Run
Pull the repo first, then:
```
python3 run.py programs/<your_function_1> programs/<your_function_2> programs/<your_function_3>
```
For each program, the script:
1. makes sure it passes `check.py`
2. builds the 8 prompts from `prompts/` and sends them to the model
3. takes the fixed function out of each reply and runs the program's tests on it
4. saves everything to `results/qwen2.5-coder-7b/<program>.json`

Then commit and push your `results/` files. Don't edit them by hand.

## Settings
Set in `run.py`, the same for everyone:

| Setting | Value | Why |
|---|---|---|
| Model | `qwen2.5-coder:7b-instruct-q4_K_M` | One exact build for everyone |
| Temperature | 0 | The model gives the same answer every time, so 1 run per version is enough |
| Seed | 0 | Extra safety for repeatable answers |
| Max reply length | 1024 tokens | Plenty for a short function + explanation |
| Runs | 1 per version per prompt | Deterministic at temperature 0 |

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
| `model`, `temperature`, `seed`, `max_tokens`, `time` | How and when it was run |
| `prompt_text` | Exactly what the model was sent |
| `reply` | The model's full reply |
| `fixed_code` | The last code block in the reply (`null` if there wasn't one) |
| `explanation` | The reply without its code blocks |
| `tests_passed`, `tests_total` | How many of the program's tests the fix passed |
| `success` | `true` only if the fix passes **every** test |
| `error` | Why grading failed, if it did (no code block, renamed function, crash) |

**Success rule:** the fix must keep the same function name and pass all tests. A reply with no code block, a renamed function, or code that crashes counts as a failure.

Judging RQ2 (did a wrong fix do what the comment claimed?) and RQ3 (did the model notice the comment was wrong?) is done later by reading `fixed_code` and `explanation`. That's why the full reply is saved.
