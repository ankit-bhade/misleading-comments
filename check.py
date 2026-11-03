"""Check that programs follow DATA_STANDARD.md, and save the 4 versions of each
program that passes to its versions/ folder.

Usage:
  python3 check.py                   check every folder in programs/
  python3 check.py programs/foo ...  check specific folders
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = ["correct.py", "buggy.py", "tests.py", "info.json"]
INFO_KEYS = ["function", "author", "generated_by", "problem", "bug_type", "bug_description", "comments"]
BUG_TYPES = ["off_by_one", "wrong_comparison", "missed_edge_case"]
COMMENT_KEYS = ["accurate", "wrong_behavior", "wrong_location", "wrong_output"]
BANNED_WORDS = ["bug", "fix"]
PLACEHOLDER = "# COMMENT"
WRONG_OUTPUT = re.compile(r"^Example: (.+) returns (.+)$")
MIN_TESTS = 5
TIMEOUT = 10

# Runs in a separate process so a crash or infinite loop can't take down the checker.
RUNNER = r"""
import ast, copy, json, os, sys
code_path, tests_path, func, call, expected = sys.argv[1:6]
out = sys.stdout
sys.stdout = open(os.devnull, "w")  # hide anything the code prints
ns = {}
exec(open(code_path).read(), ns)
tns = {}
exec(open(tests_path).read(), tns)
f = ns[func]
tests = []
for args, want in tns["TESTS"]:
    if not isinstance(args, tuple):
        args = (args,)
    try:
        got = f(*copy.deepcopy(args))
    except Exception as e:
        got = "raised %s: %s" % (type(e).__name__, e)
    tests.append([repr(args), repr(want), repr(got), got == want])
call_result = None
if call:
    try:
        got = eval(call, ns)
        call_result = [repr(got), got == ast.literal_eval(expected)]
    except Exception as e:
        call_result = ["raised %s: %s" % (type(e).__name__, e), False]
print(json.dumps({"tests": tests, "call": call_result}), file=out)
"""


def run(code_path, tests_path, func, call="", expected=""):
    """Run the tests (and optional example call) against one code file."""
    try:
        proc = subprocess.run(
            [sys.executable, "-I", "-c", RUNNER, str(code_path), str(tests_path), func, call, expected],
            capture_output=True, text=True, timeout=TIMEOUT, stdin=subprocess.DEVNULL,
        )
    except subprocess.TimeoutExpired:
        return None, f"timed out after {TIMEOUT}s"
    if proc.returncode != 0:
        lines = proc.stderr.strip().splitlines()
        return None, lines[-1] if lines else "crashed"
    return json.loads(proc.stdout), None


def code_lines(text):
    return [line.rstrip() for line in text.splitlines() if line.strip()]


def changed_lines(a, b):
    sm = difflib.SequenceMatcher(None, a, b)
    return sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal")


def check(folder):
    """Return (problems, summary) for one program folder."""
    missing = [f for f in FILES if not (folder / f).exists()]
    if missing:
        return [f"missing file(s): {', '.join(missing)}"], ""

    problems = []
    try:
        info = json.loads((folder / "info.json").read_text())
    except json.JSONDecodeError as e:
        return [f"info.json is not valid JSON: {e}"], ""

    for key in INFO_KEYS:
        if not info.get(key):
            problems.append(f"info.json: '{key}' is missing or empty")
    if info.get("bug_type") and info["bug_type"] not in BUG_TYPES:
        problems.append(f"info.json: bug_type must be one of {BUG_TYPES}")

    comments = info.get("comments") or {}
    for key in COMMENT_KEYS:
        text = comments.get(key, "")
        if not isinstance(text, str) or not text.strip():
            problems.append(f"comment '{key}' is missing or empty")
        elif "\n" in text:
            problems.append(f"comment '{key}' must be one line")
        else:
            for word in BANNED_WORDS:
                if re.search(rf"\b{word}", text, re.IGNORECASE):
                    problems.append(f"comment '{key}' uses the word '{word}'")

    buggy_text = (folder / "buggy.py").read_text()
    placeholders = [l for l in buggy_text.splitlines() if l.strip() == PLACEHOLDER]
    if len(placeholders) != 1:
        problems.append(f"buggy.py must have exactly one '{PLACEHOLDER}' line (found {len(placeholders)})")

    correct = code_lines((folder / "correct.py").read_text())
    buggy = [l for l in code_lines(buggy_text) if l.strip() != PLACEHOLDER]
    n = changed_lines(correct, buggy)
    if n != 1:
        problems.append(f"buggy.py should differ from correct.py by exactly 1 line (differs by {n})")

    func = info.get("function", "")
    if not func:
        return problems, ""

    call, expected = "", ""
    match = WRONG_OUTPUT.match(comments.get("wrong_output", "") or "")
    if not match:
        problems.append("comment 'wrong_output' must look like 'Example: <call> returns <value>'")
    else:
        call, expected = match.group(1).strip(), match.group(2).strip()
        if not call.startswith(func + "("):
            problems.append(f"comment 'wrong_output' should call {func}(...)")

    tests_path = folder / "tests.py"
    good, err = run(folder / "correct.py", tests_path, func, call, expected)
    if err:
        return problems + [f"correct.py could not run: {err}"], ""
    bad, err = run(folder / "buggy.py", tests_path, func, call, expected)
    if err:
        return problems + [f"buggy.py could not run: {err}"], ""

    total = len(good["tests"])
    if total < MIN_TESTS:
        problems.append(f"need at least {MIN_TESTS} tests (found {total})")
    for args, want, got, ok in good["tests"]:
        if not ok:
            problems.append(f"correct.py fails test {func}{args}: expected {want}, got {got}")
    buggy_fails = sum(1 for t in bad["tests"] if not t[3])
    if buggy_fails == 0:
        problems.append("buggy.py passes every test; it must fail at least one")

    if call:
        if not bad["call"][1]:
            problems.append(f"wrong_output example: buggy code gives {bad['call'][0]}, not {expected}")
        if good["call"][1]:
            problems.append(f"wrong_output example: correct code also gives {expected}, so it isn't misleading")

    return problems, f"{total} tests, buggy fails {buggy_fails}"


def versions(folder):
    """Build the 4 versions of the buggy code, one per comment type."""
    info = json.loads((folder / "info.json").read_text())
    lines = (folder / "buggy.py").read_text().splitlines()
    out = {}
    for key in COMMENT_KEYS:
        out[key] = "\n".join(
            l[: len(l) - len(l.lstrip())] + "# " + info["comments"][key] if l.strip() == PLACEHOLDER else l
            for l in lines
        ) + "\n"
    return out


def write_versions(folder):
    out_dir = folder / "versions"
    out_dir.mkdir(exist_ok=True)
    for key, code in versions(folder).items():
        (out_dir / f"{key}.py").write_text(code)


def main(argv):
    folders = [Path(a) for a in argv] or sorted(p for p in (ROOT / "programs").glob("*") if p.is_dir())
    if not folders:
        print("No programs found in programs/.")
        return 0

    failed = 0
    for folder in folders:
        problems, summary = check(folder)
        if problems:
            failed += 1
            print(f"FAIL  {folder.name}")
            for p in problems:
                print(f"      - {p}")
        else:
            write_versions(folder)
            print(f"PASS  {folder.name}  ({summary}; saved 4 versions to versions/)")
    print(f"\n{len(folders) - failed}/{len(folders)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
