"""Pick the ConDefects bugs for our second dataset and set up their folders.

Run once, by one person (it needs the ConDefects repo and its 20.8 GB Test.zip):
  python3.12 condefects/select_bugs.py <ConDefects repo folder> <Test.zip>

Rules (decided 2026-11-15, see condefects/README.md):
- Python, AtCoder Beginner Contest (ABC), difficulty under 800, 5-60 lines.
  Standard library only.
- Exactly one line differs between the buggy and fixed code (ignoring comments),
  and the change is logic: not only a comment, output wording or format (how
  the same value is printed), import, input reading or recursion setting, and
  not a misspelled word (the few cases no rule catches are listed in BY_HAND).
- One bug per problem: the problem's Python submissions in random order (seed
  2026), first one that meets the rules above. Problems are tried in random
  order (seed 2026). Both orders come from the full ConDefects list, so a
  filter change only affects the problems it touches.
- Tests: AtCoder's own, minus any test over 100 KB (keeps the repo small and
  grading fast; the big tests mostly check speed) and any the fixed code needs
  over 1 s for on the selecting laptop (speed tests too; leaves room for slower
  cloud CPUs, where grading allows 10 s per test). The fixed code must pass all
  of the rest, and the buggy code must give a wrong answer or crash
  on at least one (failing only by timing out is a speed bug, not a logic bug).
- The first 120 problems that pass are dealt out 30 per person in that order.
Reads only the needed tests straight from the ZIP; nothing else is extracted.
"""
import collections
import difflib
import io
import json
import random
import re
import shutil
import sys
import tempfile
import time
import tokenize
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cd  # noqa: E402

SEED = 2026
TARGET = 120
PEOPLE = ["Ankit", "Arnav", "Kushal", "Seung Wook"]
MAX_DIFFICULTY = 800
MAX_TEST_BYTES = 100_000
SLOW = 1.0  # seconds; tests the fixed code needs longer for are dropped, leaving room for slower cloud CPUs
# Excluded after reading the picks: misspelled words (no rule tells these apart from meaningful
# strings such as "LURD" -> "RULD") and an output-format change the rule misses (f-string).
BY_HAND = {"abc324_a": 'typo: "Yse" for "Yes"', "abc267_a": 'typo: "Friay" for "Friday"',
           "abc246_a": "output format only: print(x) vs print(f'{x[0]} {x[1]}')",
           "abc342_c": 'typo: "...uvwsyz" for "...uvwxyz"',
           "abc356_a": "output format only: debug-style print(f\"A' = ({result})\") vs print(result)",
           "abc271_a": "output format only: print(a) vs print('0'+a) (zero padding)"}
STDLIB = set(sys.stdlib_module_names)


def strip_comments(src):
    """Remove comments (and lines that held only a comment), leaving the code itself unchanged."""
    original = src.splitlines()
    lines = list(original)
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type == tokenize.COMMENT:
            row, col = tok.start
            lines[row - 1] = lines[row - 1][:col].rstrip()
    keep = [l.rstrip() for l, o in zip(lines, original) if l.strip() or not o.strip()]
    while keep and not keep[-1].strip():
        keep.pop()
    while keep and not keep[0].strip():
        keep.pop(0)
    return "\n".join(keep) + "\n"


def imports(src):
    return {m.split(".")[0] for m in re.findall(r"^\s*(?:from\s+(\S+)\s+import|import\s+([\w., ]+))", src, re.M)
            for m in (m[0] or m[1]).replace(" ", "").split(",") if m}


def print_values(line):
    """A print line reduced to the values it prints: no strings, sep/end, *, int/float/str, spaces or brackets."""
    line = re.sub(r"(['\"]).*?\1", "", line)
    line = re.sub(r"\b(sep|end)\s*=\s*[^,)]*", "", line)
    line = re.sub(r"\b(int|float|str)\b|\.join\b", "", line)
    return re.sub(r"[\s*(),]", "", line)


def one_line_change(bad, good):
    """Return (line index in bad, bad line, good line) if exactly one line differs, else None."""
    b, g = bad.splitlines(), good.splitlines()
    ops = [o for o in difflib.SequenceMatcher(None, b, g, autojunk=False).get_opcodes() if o[0] != "equal"]
    if len(ops) == 1 and ops[0][0] == "replace" and ops[0][2] - ops[0][1] == 1 and ops[0][4] - ops[0][3] == 1:
        return ops[0][1], b[ops[0][1]].strip(), g[ops[0][3]].strip()
    return None


def candidates(repo):
    difficulty = {l.split()[0]: int(l.split()[1]) for l in open(repo / "difficulty.txt")
                  if len(l.split()) == 2 and l.split()[1].lstrip("-").isdigit()}
    date = {l.split()[0]: l.split()[1] for l in open(repo / "date.txt") if len(l.split()) == 2}
    why = collections.Counter()
    by_task = collections.defaultdict(list)
    files = sorted(repo.glob("Code/*/Python/*/faultyVersion.py"))
    random.Random(SEED).shuffle(files)  # fixed order, so each problem's first valid bug is stable
    for f in files:
        task, pid = f.parts[-4], f.parts[-2]
        d = difficulty.get(task)
        if not task.startswith("abc") or d is None or d >= MAX_DIFFICULTY:
            why["not an easy ABC problem"] += 1
            continue
        try:
            bad = strip_comments(f.read_text())
            good = strip_comments((f.parent / "correctVersion.py").read_text())
        except (tokenize.TokenError, IndentationError, SyntaxError, UnicodeDecodeError):
            why["can't be read"] += 1
            continue
        if not 5 <= len(bad.splitlines()) <= 60:
            why["not 5-60 lines"] += 1
            continue
        if not imports(bad + good) <= STDLIB:
            why["uses a non-standard library"] += 1
            continue
        change = one_line_change(bad, good)
        if not change:
            why["not exactly one line changed"] += 1
            continue
        _, bl, gl = change
        strip_strings = lambda s: re.sub(r"(['\"]).*?\1", "", s)
        if re.search(r"\bprint\(", bl + gl) and strip_strings(bl) == strip_strings(gl):
            why["only output wording changed"] += 1
            continue
        if re.search(r"\bprint\(", bl) and re.search(r"\bprint\(", gl) and print_values(bl) == print_values(gl):
            why["only output format changed"] += 1
            continue
        if task in BY_HAND:
            why["excluded by hand (typo or output format)"] += 1
            continue
        if re.search(r"setrecursionlimit|\bimport\b|stdin|input\s*=", bl + gl) or ("input(" in bl) != ("input(" in gl):
            why["I/O, import or recursion setting"] += 1
            continue
        by_task[task].append({"task": task, "condefects_id": pid, "difficulty": d, "contest_date": date.get(task),
                              "buggy": bad, "correct": good, "line": change[0], "buggy_line": bl, "fixed_line": gl})
    for k, v in why.most_common():
        print(f"  skipped {v:4}  {k}")
    return by_task


def task_tests(zf, names, task):
    """Map test name -> (input, output) for one task, from the ZIP's Test/<contest>/<LETTER>/{in,out}/."""
    contest, letter = task.split("_")
    out = {}
    for sub in (letter.upper(), "Ex"):
        prefix = f"Test/{contest}/{sub}/"
        ins = [n for n in names.get(prefix + "in", []) if not n.endswith("/")]
        if ins:
            for n in ins:
                base = n.rsplit("/", 1)[1]
                o = f"{prefix}out/{base}"
                if o in names["__all__"]:
                    out[base] = (zf.read(n), zf.read(o))
            return out
    return out


def main(repo, zip_path):
    by_task = candidates(repo)
    all_tasks = sorted({f.parts[-4] for f in repo.glob("Code/*/Python/*/faultyVersion.py")})
    random.Random(SEED).shuffle(all_tasks)  # from the full list, so filters don't reorder it
    tasks = [t for t in all_tasks if t in by_task]
    print(f"{sum(map(len, by_task.values()))} candidate bugs in {len(tasks)} problems")

    zf = zipfile.ZipFile(zip_path)
    names = collections.defaultdict(list)
    names["__all__"] = set(zf.namelist())
    for n in names["__all__"]:
        if "/in/" in n or "/out/" in n:
            names[n.rsplit("/", 1)[0]].append(n)

    out_root = HERE / "programs"
    out_root.mkdir(exist_ok=True)
    chosen, why = [], collections.Counter()
    for task in tasks:
        if len(chosen) == TARGET:
            break
        bug = by_task[task][0]
        tests = {k: v for k, v in task_tests(zf, names, task).items() if len(v[0]) + len(v[1]) <= MAX_TEST_BYTES}
        if len(tests) < 5:
            why["fewer than 5 tests"] += 1
            continue
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / task
            (folder / "tests" / "in").mkdir(parents=True)
            (folder / "tests" / "out").mkdir()
            for name, (i, o) in tests.items():
                (folder / "tests" / "in" / name).write_bytes(i)
                (folder / "tests" / "out" / name).write_bytes(o)
            (folder / "correct.py").write_text(bug["correct"])
            (folder / "buggy.py").write_text(bug["buggy"])
            for name in tests:  # drop speed tests: the fixed code must answer each within SLOW seconds here
                start = time.time()
                cd.run_input(folder / "correct.py", (folder / "tests" / "in" / name).read_text(errors="replace"))
                if time.time() - start > SLOW:
                    (folder / "tests" / "in" / name).unlink()
                    (folder / "tests" / "out" / name).unlink()
            tests = {k: v for k, v in tests.items() if (folder / "tests" / "in" / k).exists()}
            if len(tests) < 5:
                why["fewer than 5 tests"] += 1
                continue
            good = cd.run_tests(folder / "correct.py", folder)
            if not all(t[3] for t in good):
                why["fixed code fails or is too slow on a test"] += 1
                continue
            bad = cd.run_tests(folder / "buggy.py", folder, stop_after_timeout=False)
            fails = [t for t in bad if not t[3]]
            if not fails:
                why["buggy code passes every test"] += 1
                continue
            if all(t[2].startswith("error: timed out") for t in fails):
                why["buggy code only too slow"] += 1
                continue
            lines = bug["buggy"].splitlines()
            (folder / "buggy.py").write_text("\n".join([cd.check.PLACEHOLDER] + lines) + "\n")
            person = PEOPLE[len(chosen) % len(PEOPLE)]
            contest = task.split("_")[0]
            info = {
                "task": task,
                "author": person,
                "generated_by": "",
                "problem": "",
                "bug_type": "",
                "bug_description": "",
                "comments": {"accurate": "", "wrong_behavior": "", "wrong_location": "", "wrong_output": ""},
                "source": {
                    "dataset": "ConDefects",
                    "condefects_id": bug["condefects_id"],
                    "url": f"https://atcoder.jp/contests/{contest}/tasks/{task}",
                    "difficulty": bug["difficulty"],
                    "contest_date": bug["contest_date"],
                    "buggy_line": bug["buggy_line"],
                    "fixed_line": bug["fixed_line"],
                    "tests": len(tests),
                    "buggy_fails": len(fails),
                },
            }
            (folder / "info.json").write_text(json.dumps(info, indent=2, ensure_ascii=False) + "\n")
            dest = out_root / task
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(folder, dest)
        chosen.append(task)
        print(f"  [{len(chosen):3}] {task:10} {person:10} {len(tests):3} tests, buggy fails {len(fails):3}  "
              f"{bug['buggy_line'][:40]!r} -> {bug['fixed_line'][:40]!r}")
    for k, v in why.most_common():
        print(f"  rejected {v:4}  {k}")
    print(f"Chose {len(chosen)} problems.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__.strip())
    main(Path(sys.argv[1]), Path(sys.argv[2]))
