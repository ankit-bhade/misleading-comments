"""Checker for the ConDefects programs (see condefects/README.md).

ConDefects programs are whole AtCoder scripts: they read the input and print
the answer, and their tests are AtCoder's own input/output files. Otherwise
they follow DATA_STANDARD.md: one buggy line, a "# COMMENT" placeholder, and
the 4 comments in info.json.

Usage:
  python3 condefects/cd.py                        check every ConDefects program
  python3 condefects/cd.py condefects/programs/abc280_c ...
"""
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import check  # noqa: E402  (reuses the comment rules and version building)

FILES = ["correct.py", "buggy.py", "info.json"]
INFO_KEYS = ["task", "author", "generated_by", "problem", "bug_type", "bug_description", "comments"]
WRONG_OUTPUT = re.compile(r"^Example: input (.+) prints (.+)$")
TIMEOUT = 10  # seconds per test (the fixed programs take under 1 s per test on a laptop)


def tests(folder):
    """The (name, input text, expected output) of every test, in name order."""
    out = []
    for path in sorted((folder / "tests" / "in").iterdir()):
        expected = folder / "tests" / "out" / path.name
        out.append((path.name, path.read_text(errors="replace"), expected.read_text(errors="replace")))
    return out


def same_output(got, want):
    """AtCoder-style comparison: the same tokens, ignoring spacing and blank lines."""
    return got is not None and got.split() == want.split()


def run_input(code_path, stdin):
    """Run a program on one input. Return (stdout, error)."""
    try:
        proc = subprocess.run([sys.executable, "-I", str(code_path)], input=stdin, capture_output=True,
                              text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, f"timed out after {TIMEOUT}s"
    if proc.returncode != 0:
        lines = proc.stderr.strip().splitlines()
        return proc.stdout, lines[-1] if lines else "crashed"
    return proc.stdout, None


def run_tests(code_path, folder, stop_after_timeout=True):
    """Run every test. Returns a list of [name, expected, got, passed].

    After a test times out, the remaining tests are marked as not run, so a fix
    with an infinite loop doesn't take minutes to grade.
    """
    results, timed_out = [], False
    for name, stdin, want in tests(folder):
        if timed_out:
            results.append([name, want.strip(), "not run (an earlier test timed out)", False])
            continue
        got, error = run_input(code_path, stdin)
        if error and error.startswith("timed out") and stop_after_timeout:
            timed_out = True
        shown = got.strip() if error is None else f"error: {error}"
        results.append([name, want.strip(), shown, error is None and same_output(got, want)])
    return results


def check_folder(folder):
    """Return (problems, summary) for one ConDefects program folder."""
    missing = [f for f in FILES if not (folder / f).exists()]
    if not (folder / "tests" / "in").is_dir():
        missing.append("tests/in/")
    if missing:
        return [f"missing: {', '.join(missing)}"], ""
    problems = []
    info = json.loads((folder / "info.json").read_text())
    for key in INFO_KEYS:
        if not info.get(key):
            problems.append(f"info.json: '{key}' is missing or empty")
    if info.get("bug_type") and info["bug_type"] not in check.BUG_TYPES:
        problems.append(f"info.json: bug_type must be one of {check.BUG_TYPES}")
    comments = info.get("comments") or {}
    for key in check.COMMENT_KEYS:
        text = comments.get(key, "")
        if not isinstance(text, str) or not text.strip():
            problems.append(f"comment '{key}' is missing or empty")
        elif "\n" in text:
            problems.append(f"comment '{key}' must be one line")
        else:
            for word in check.BANNED_WORDS:
                if re.search(rf"\b{word}", text, re.IGNORECASE):
                    problems.append(f"comment '{key}' uses the word '{word}'")

    buggy_text = (folder / "buggy.py").read_text()
    if sum(1 for l in buggy_text.splitlines() if l.strip() == check.PLACEHOLDER) != 1:
        problems.append(f"buggy.py must have exactly one '{check.PLACEHOLDER}' line")
    correct = check.code_lines((folder / "correct.py").read_text())
    buggy = [l for l in check.code_lines(buggy_text) if l.strip() != check.PLACEHOLDER]
    n = check.changed_lines(correct, buggy)
    if n != 1:
        problems.append(f"buggy.py should differ from correct.py by exactly 1 line (differs by {n})")

    good = run_tests(folder / "correct.py", folder)
    bad = run_tests(folder / "buggy.py", folder)
    for name, want, got, ok in good:
        if not ok:
            problems.append(f"correct.py fails test {name}: expected {want[:40]!r}, got {got[:40]!r}")
    buggy_fails = sum(1 for t in bad if not t[3])
    if buggy_fails == 0:
        problems.append("buggy.py passes every test; it must fail at least one")

    match = WRONG_OUTPUT.match(comments.get("wrong_output", "") or "")
    if not match:
        problems.append("comment 'wrong_output' must look like: Example: input '3 4\\n1 2 3' prints 2")
    else:
        try:
            stdin = ast.literal_eval(match.group(1).strip())
            assert isinstance(stdin, str)
        except Exception:
            problems.append("wrong_output: the input must be a quoted Python string, e.g. '3 4\\n1 2 3'")
        else:
            claimed = match.group(2).strip()
            if claimed == "nothing":  # "prints nothing" = empty output
                claimed = ""
            got_bad, err_bad = run_input(folder / "buggy.py", stdin + "\n")
            got_good, err_good = run_input(folder / "correct.py", stdin + "\n")
            if err_bad or not same_output(got_bad, claimed):
                problems.append(f"wrong_output example: buggy code prints {(got_bad or err_bad or '').strip()!r}, "
                                f"not {claimed!r}")
            if err_good:
                problems.append(f"wrong_output example: the input isn't valid; correct code says {err_good}")
            elif same_output(got_good, claimed):
                problems.append("wrong_output example: correct code prints the same, so it isn't misleading")
    return problems, f"{len(good)} tests, buggy fails {buggy_fails}"


def main(argv):
    folders = [Path(a) for a in argv] or sorted(p for p in (HERE / "programs").glob("*") if p.is_dir())
    failed = 0
    for folder in folders:
        problems, summary = check_folder(folder)
        if problems:
            failed += 1
            print(f"FAIL  {folder.name}")
            for p in problems:
                print(f"      - {p}")
        else:
            check.write_versions(folder)
            print(f"PASS  {folder.name}  ({summary}; saved 4 versions to versions/)")
    print(f"\n{len(folders) - failed}/{len(folders)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
