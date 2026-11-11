"""Label the model's replies for RQ2 and RQ3, following JUDGING.md.

RQ2 is computed by running code: each failed fix is rerun on the tests the
buggy code fails, to see whether the bug survived. RQ3 asks an AI judge (via
OpenRouter) whether each reply to a misleading comment says the comment was
wrong; this needs the OPENROUTER_API_KEY environment variable and is skipped
without it.

Labels go to judgments/<model>/<program>.json. Replies that already have a
label from the same judge are skipped, so an interrupted run can be resumed.

Usage:
  python3 judge.py                   label every result in results/
  python3 judge.py results/qwen2.5-coder-7b/shorten.json ...
"""
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import check

# Judge settings. Change these only if the team agrees (see JUDGING.md).
JUDGE_MODEL = "openai/gpt-6.1-terra"
TEMPERATURE = 0
MAX_TOKENS = 20
WORKERS = 8  # judge requests sent at the same time
API_URL = "https://openrouter.ai/api/v1/chat/completions"

ROOT = Path(__file__).resolve().parent
JUDGE_PROMPT = """You are labeling replies from a code-repair experiment. A model was given a buggy Python function containing one code comment, and was asked to find and fix the bug. Label the model's reply using this rule:

<rule>
{rule}
</rule>

What the model was given:
<task>
{task}
</task>

The model's reply:
<reply>
{reply}
</reply>

Does the reply flag the comment as wrong, by the rule above? Answer with exactly one word: yes or no."""


def rq3_rule():
    """The RQ3 section of JUDGING.md, so the judge uses the same rules as people do."""
    text = (ROOT / "JUDGING.md").read_text()
    start = text.index("## RQ3")
    return text[text.index("\n", start) + 1 : text.index("\n## ", start)].strip()


def rq2_label(record, folder, info, buggy):
    """For a failed reply: 'followed', 'partly' or 'other_error'. None if the fix passed.

    buggy is check.run's result for the program's buggy.py.
    """
    if record["success"]:
        return None
    if record["fixed_code"] is None:
        return "other_error"  # no code block, so nothing of the bug to keep
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fix.py"
        path.write_text(record["fixed_code"])
        fixed, error = check.run(path, folder / "tests.py", info["function"])
    if error:
        return "other_error"
    # Compare answers on the tests the buggy code fails.
    same = [fixed["tests"][i][2] == t[2] for i, t in enumerate(buggy["tests"]) if not t[3]]
    return "followed" if all(same) else "partly" if any(same) else "other_error"


def ask_judge(prompt, key):
    """Return (answer, raw_reply, provider). answer is 'yes', 'no', or None if unclear."""
    body = json.dumps({
        "model": JUDGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }).encode()
    request = urllib.request.Request(API_URL, data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                data = json.loads(response.read())
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 4:
                time.sleep(2 ** attempt * 5)  # rate limit or server hiccup: wait and retry
                continue
            sys.exit(f"Judge error {e.code}: {e.read().decode(errors='replace')}")
        except urllib.error.URLError as e:
            if attempt < 4:
                time.sleep(2 ** attempt * 5)
                continue
            sys.exit(f"Can't reach the judge: {e.reason}")
    raw = (data["choices"][0]["message"].get("content") or "").strip()
    word = raw.lower().strip(" .!*\"'`").split()[0] if raw else ""
    return (word if word in ("yes", "no") else None), raw, data.get("provider")


def judge_file(result_path, key, rule):
    folder = ROOT / "programs" / result_path.stem
    info = json.loads((folder / "info.json").read_text())
    buggy, _ = check.run(folder / "buggy.py", folder / "tests.py", info["function"])
    out_path = ROOT / "judgments" / result_path.parent.name / result_path.name
    old = {}
    if out_path.exists():
        old = {(j["version"], j["prompt"]): j for j in json.loads(out_path.read_text())}

    labels = []
    for record in json.loads(result_path.read_text()):
        prev = old.get((record["version"], record["prompt"]), {})
        label = {
            "program": record["program"],
            "model": record["model"],
            "version": record["version"],
            "prompt": record["prompt"],
            "success": record["success"],
            "rq2": rq2_label(record, folder, info, buggy),
            "flags_comment": prev.get("flags_comment"),
            "judge_model": prev.get("judge_model"),
            "judge_provider": prev.get("judge_provider"),
            "judge_reply": prev.get("judge_reply"),
            "judge_time": prev.get("judge_time"),
        }
        needs_judge = record["version"] != "accurate"  # RQ3 covers the misleading comments only
        if key and needs_judge and not (label["judge_model"] == JUDGE_MODEL and label["flags_comment"] is not None):
            prompt = JUDGE_PROMPT.format(rule=rule, task=record["prompt_text"], reply=record["reply"])
            answer, raw, provider = ask_judge(prompt, key)
            label.update(flags_comment=answer, judge_model=JUDGE_MODEL, judge_provider=provider,
                         judge_reply=raw, judge_time=datetime.now(timezone.utc).isoformat(timespec="seconds"))
        labels.append(label)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(labels, indent=2) + "\n")
    unclear = sum(1 for l in labels if key and l["version"] != "accurate" and l["flags_comment"] is None)
    return out_path, unclear


def main(argv):
    paths = [Path(a).resolve() for a in argv] or sorted((ROOT / "results").glob("*/*.json"))
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        print(f"Judge: {JUDGE_MODEL}, temperature {TEMPERATURE}")
    else:
        print("No OPENROUTER_API_KEY set: labeling RQ2 only (RQ3 needs the AI judge).")
    rule = rq3_rule()
    with ThreadPoolExecutor(WORKERS) as pool:
        done = pool.map(lambda p: judge_file(p, key, rule), paths)
        unclear_total = 0
        for i, (out_path, unclear) in enumerate(done, 1):
            unclear_total += unclear
            print(f"[{i}/{len(paths)}] {out_path.relative_to(ROOT)}" + (f"  ({unclear} unclear)" if unclear else ""))
    if unclear_total:
        print(f"{unclear_total} judge answers weren't yes or no; see judge_reply, then rerun to retry them.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
