"""Run the experiment on programs, following EXPERIMENT.md.

For each program, sends all 4 comment versions to the model with Prompt A and
Prompt B (8 requests), tests each fix, and saves the results to
results/<model>/<program>.json.

Usage:
  python3 run.py programs/foo [programs/bar ...]
"""
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import check

# Experiment settings. Change these only if the team agrees (see EXPERIMENT.md).
MODEL = "qwen2.5-coder:7b-instruct-q4_K_M"
TEMPERATURE = 0
SEED = 0
MAX_TOKENS = 1024
CONTEXT = 4096  # pinned: Ollama's default depends on the machine's GPU memory
OLLAMA_URL = "http://localhost:11434/api/chat"

ROOT = Path(__file__).resolve().parent
PROMPTS = {"A": ROOT / "prompts" / "prompt_a.txt", "B": ROOT / "prompts" / "prompt_b.txt"}
CODE_BLOCK = re.compile(r"```(?:python|py)?[ \t]*\n(.*?)```", re.DOTALL)


def ask_model(prompt):
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": TEMPERATURE, "seed": SEED, "num_predict": MAX_TOKENS, "num_ctx": CONTEXT},
    }).encode()
    request = urllib.request.Request(OLLAMA_URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            return json.loads(response.read())["message"]["content"]
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        if "not found" in detail:
            sys.exit(f"Model not installed. Run: ollama pull {MODEL}")
        sys.exit(f"Ollama error: {detail}")
    except urllib.error.URLError:
        sys.exit("Can't reach Ollama. Open the Ollama app (or run `ollama serve`) and try again.")


def results_dir():
    """Where this model's results go, e.g. results/qwen2.5-coder-7b."""
    return ROOT / "results" / MODEL.split("-instruct")[0].replace(":", "-")


def machine_info():
    """Return (ollama_version, gpu) so results show what they were run on."""
    try:
        url = OLLAMA_URL.replace("/api/chat", "/api/version")
        with urllib.request.urlopen(url, timeout=10) as response:
            version = json.loads(response.read())["version"]
    except Exception:
        version = None
    try:
        gpu = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
                             capture_output=True, text=True, timeout=10).stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        gpu = None  # no NVIDIA GPU, e.g. a Mac
    return version, gpu


def split_reply(reply):
    """Return (fixed_code, explanation). The fix is the last code block in the reply."""
    blocks = CODE_BLOCK.findall(reply)
    code = blocks[-1].strip() + "\n" if blocks else None
    explanation = CODE_BLOCK.sub("", reply).strip()
    if explanation.startswith("Explanation:"):
        explanation = explanation[len("Explanation:"):].strip()
    return code, explanation


def grade(code, folder, func):
    """Return (tests_passed, tests_total, error) for a fixed function."""
    if code is None:
        return 0, None, "no code block in reply"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fix.py"
        path.write_text(code)
        result, error = check.run(path, folder / "tests.py", func)
    if error:
        return 0, None, error
    tests = result["tests"]
    return sum(1 for t in tests if t[3]), len(tests), None


def run_program(folder):
    problems, _ = check.check(folder)
    if problems:
        print(f"SKIP  {folder.name}: fails check.py; run python3 check.py {folder} first")
        return False
    check.write_versions(folder)
    ollama_version, gpu = machine_info()

    info = json.loads((folder / "info.json").read_text())
    records = []
    for prompt_id, template_path in PROMPTS.items():
        template = template_path.read_text()
        for version, code in check.versions(folder).items():
            prompt = template.replace("{problem}", info["problem"]).replace("{code}", code.rstrip())
            print(f"  {folder.name}  prompt {prompt_id}  {version:<15}", end="", flush=True)
            reply = ask_model(prompt)
            fixed_code, explanation = split_reply(reply)
            passed, total, error = grade(fixed_code, folder, info["function"])
            success = error is None and passed == total
            print("PASS" if success else "FAIL")
            records.append({
                "program": folder.name,
                "author": info["author"],
                "bug_type": info["bug_type"],
                "version": version,
                "prompt": prompt_id,
                "model": MODEL,
                "temperature": TEMPERATURE,
                "seed": SEED,
                "max_tokens": MAX_TOKENS,
                "context": CONTEXT,
                "ollama_version": ollama_version,
                "gpu": gpu,
                "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "prompt_text": prompt,
                "reply": reply,
                "fixed_code": fixed_code,
                "explanation": explanation,
                "tests_passed": passed,
                "tests_total": total,
                "success": success,
                "error": error,
            })

    out_dir = results_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{folder.name}.json"
    out_path.write_text(json.dumps(records, indent=2) + "\n")
    wins = sum(r["success"] for r in records)
    print(f"DONE  {folder.name}: {wins}/{len(records)} fixed; saved {out_path.relative_to(ROOT)}")
    return True


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 1
    ollama_version, gpu = machine_info()
    print(f"Model: {MODEL}, temperature {TEMPERATURE}, seed {SEED}, Ollama {ollama_version}, GPU {gpu}")
    ok = [run_program(Path(a)) for a in argv]
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
