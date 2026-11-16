"""Memorization check: has the model seen these programs before?

ConDefects programs are public (AtCoder, 2021-2024), so the model may have
trained on them. For each program the model gets only the lines before the
buggy line (no comment, no problem description; at least the first line) and
is asked to write the rest. We measure how close its continuation is to the
real rest of the program (buggy or fixed version, whichever is closer), and
whether it reproduces the exact buggy or fixed line.

Our own 120 programs were written this semester, so no model has seen them:
their scores show what "not memorized" looks like. A ConDefects program counts
as likely memorized if it scores above every one of our programs.

Run it on Colab (7B) or Kaggle (32B) after Ollama is running:
  python3 condefects/memorize.py                                   7B
  python3 condefects/memorize.py qwen2.5-coder:32b-instruct-q4_K_M 32B
Saves condefects/memorization/<model>.json. Programs already done are skipped.
"""
import difflib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
import check  # noqa: E402
import run  # noqa: E402

PROMPT = """Here is the beginning of a Python program. Continue it: write the rest of the program exactly as you think it continues.

```python
{prefix}
```

Reply with only the rest of the code (not the lines above), in one code block."""


def program_lines(folder):
    """Non-blank lines of the buggy program, without the comment placeholder."""
    return [l.rstrip() for l in (folder / "buggy.py").read_text().splitlines()
            if l.strip() and l.strip() != check.PLACEHOLDER]


def similarity(a, b):
    """0-1 similarity of two code snippets, ignoring spacing."""
    tok = lambda s: re.findall(r"\w+|[^\w\s]", s)
    return round(difflib.SequenceMatcher(None, tok(a), tok(b), autojunk=False).ratio(), 3)


def squash(line):
    return re.sub(r"\s+", "", line or "")


def probe(folder, dataset):
    bad = program_lines(folder)
    good = check.code_lines((folder / "correct.py").read_text())
    ops = difflib.SequenceMatcher(None, bad, good, autojunk=False).get_opcodes()
    first_diff = next((i1 for tag, i1, i2, j1, j2 in ops if tag != "equal"), len(bad) // 2)
    cut = max(1, first_diff)  # show everything before the buggy line
    # Where the fixed program's rest starts (the one changed line may shift it by a line).
    j = next((j1 + (cut - i1) if tag == "equal" else j1 for tag, i1, i2, j1, j2 in ops if i1 <= cut < i2), len(good))
    bug = next(((bad[i1] if i2 > i1 else None, good[j1] if j2 > j1 else None, i1)
                for tag, i1, i2, j1, j2 in ops if tag != "equal"), (None, None, None))
    prompt = PROMPT.format(prefix="\n".join(bad[:cut]))
    reply = run.ask_model(prompt)
    blocks = run.CODE_BLOCK.findall(reply)
    continuation = blocks[-1] if blocks else reply
    cont = {squash(l) for l in continuation.splitlines() if l.strip()}
    return {
        "dataset": dataset,
        "program": folder.name,
        "model": run.MODEL,
        "lines": len(bad),
        "prefix_lines": cut,
        "bug_in_rest": bug[2] is not None and bug[2] >= cut,
        "similarity_to_buggy_rest": similarity(continuation, "\n".join(bad[cut:])),
        "similarity_to_fixed_rest": similarity(continuation, "\n".join(good[j:])),
        "reproduces_buggy_line": bug[0] is not None and squash(bug[0]) in cont,
        "reproduces_fixed_line": bug[1] is not None and squash(bug[1]) in cont,
        "prompt": prompt,
        "reply": reply,
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def main():
    out_dir = HERE / "memorization"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / (run.results_dir().name + ".json")
    done = json.loads(out_path.read_text()) if out_path.exists() else []
    seen = {(r["dataset"], r["program"]) for r in done}
    folders = [("condefects", p) for p in sorted((HERE / "programs").iterdir()) if p.is_dir()] + \
              [("main", p) for p in sorted((ROOT / "programs").iterdir()) if p.is_dir()]
    todo = [(d, p) for d, p in folders if (d, p.name) not in seen]
    print(f"Model {run.MODEL}: {len(todo)} programs to probe ({len(seen)} already done)")
    for i, (dataset, folder) in enumerate(todo, 1):
        record = probe(folder, dataset)
        done.append(record)
        out_path.write_text(json.dumps(done, indent=2) + "\n")  # saved after each, so it can resume
        print(f"[{i}/{len(todo)}] {dataset:<10} {folder.name:<24} similarity "
              f"{max(record['similarity_to_buggy_rest'], record['similarity_to_fixed_rest']):.2f}")
    summary(done)


def summary(records):
    best = lambda r: max(r["similarity_to_buggy_rest"], r["similarity_to_fixed_rest"])
    main_scores = [best(r) for r in records if r["dataset"] == "main"]
    if not main_scores:
        return
    cutoff = max(main_scores)
    cd = [r for r in records if r["dataset"] == "condefects"]
    flagged = [r["program"] for r in cd if best(r) > cutoff]
    print(f"\nOur programs (never public): similarity up to {cutoff:.2f}")
    print(f"ConDefects above that: {len(flagged)} of {len(cd)}: {', '.join(flagged) or 'none'}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run.MODEL = sys.argv[1]
    main()
