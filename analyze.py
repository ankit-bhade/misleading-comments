"""Turn the results and labels into the RQ1-RQ3 tables for the report and slides.

Usage:
  python3 analyze.py               our 120 programs (results/, judgments/, handcheck/)
  python3 analyze.py condefects    the ConDefects programs (condefects/...)

Prints Markdown tables and saves them to analysis/<dataset>.md.

Every program is run under every comment version and both prompts, so
comparisons are paired: we use the exact McNemar test (a two-sided binomial
test on the pairs where only one side succeeded).
"""
import collections
import csv
import json
import sys
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODELS = ["qwen2.5-coder-7b", "qwen2.5-coder-32b"]
MODEL_NAMES = {"qwen2.5-coder-7b": "7B", "qwen2.5-coder-32b": "32B"}
VERSIONS = ["accurate", "wrong_behavior", "wrong_location", "wrong_output"]
MISLEADING = VERSIONS[1:]
BUG_TYPES = ["off_by_one", "wrong_comparison", "missed_edge_case", "other"]


def load(base):
    """All result records, each with its labels (rq2, flags_comment) merged in."""
    records = []
    for model in MODELS:
        for path in sorted((base / "results" / model).glob("*.json")):
            labels = {}
            judged = base / "judgments" / model / path.name
            if judged.exists():
                labels = {(l["version"], l["prompt"]): l for l in json.loads(judged.read_text())}
            for r in json.loads(path.read_text()):
                label = labels.get((r["version"], r["prompt"]), {})
                records.append({"model": model, "program": r["program"], "bug_type": r["bug_type"],
                                "version": r["version"], "prompt": r["prompt"], "success": r["success"],
                                "rq2": label.get("rq2"), "flags": label.get("flags_comment")})
    return records


def mcnemar(pairs):
    """Exact two-sided McNemar test. pairs: list of (baseline ok, other ok). Returns (b, c, p)."""
    b = sum(1 for x, y in pairs if x and not y)  # baseline fixed, other didn't
    c = sum(1 for x, y in pairs if y and not x)  # other fixed, baseline didn't
    n = b + c
    if n == 0:
        return b, c, 1.0
    tail = sum(comb(n, k) for k in range(0, min(b, c) + 1)) / 2 ** n
    return b, c, min(1.0, 2 * tail)


def pct(k, n):
    return f"{k}/{n} ({100 * k / n:.0f}%)" if n else "–"


def p_text(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


def rq1(records):
    out = ["## RQ1: is a misleading comment worse than an accurate one?",
           "Fix success rate (all tests pass), Prompts A and B together.", ""]
    rows = []
    for model in MODELS:
        rs = [r for r in records if r["model"] == model]
        row = [MODEL_NAMES[model]]
        for v in VERSIONS:
            vs = [r for r in rs if r["version"] == v]
            row.append(pct(sum(r["success"] for r in vs), len(vs)))
        mis = [r for r in rs if r["version"] in MISLEADING]
        row.append(pct(sum(r["success"] for r in mis), len(mis)))
        rows.append(row)
    out.append(table(["Model"] + VERSIONS + ["all misleading"], rows))

    out += ["", "Paired test against the accurate comment, per program and prompt (exact McNemar). "
            "'Lost' = fixed with the accurate comment but not this one; 'gained' = the reverse.", ""]
    rows = []
    for model in MODELS:
        ok = {(r["program"], r["version"], r["prompt"]): r["success"] for r in records if r["model"] == model}
        keys = sorted({(p, pr) for p, v, pr in ok})
        for v in MISLEADING + ["all misleading"]:
            vs = MISLEADING if v == "all misleading" else [v]
            pairs = [(ok[(p, "accurate", pr)], ok[(p, x, pr)]) for p, pr in keys for x in vs
                     if (p, "accurate", pr) in ok and (p, x, pr) in ok]
            b, c, p = mcnemar(pairs)
            acc = sum(x for x, _ in pairs)
            other = sum(y for _, y in pairs)
            rows.append([MODEL_NAMES[model], v, f"{100 * (other - acc) / len(pairs):+.1f} pts" if pairs else "–",
                         b, c, p_text(p)])
    out.append(table(["Model", "Comment", "Change vs accurate (− = worse)", "Lost", "Gained", "p"], rows))

    out += ["", "By bug type (success rate; accurate vs. all misleading).", ""]
    rows = []
    for model in MODELS:
        for t in BUG_TYPES:
            rs = [r for r in records if r["model"] == model and r["bug_type"] == t]
            if not rs:
                continue
            acc = [r for r in rs if r["version"] == "accurate"]
            mis = [r for r in rs if r["version"] in MISLEADING]
            rows.append([MODEL_NAMES[model], t, pct(sum(r["success"] for r in acc), len(acc)),
                         pct(sum(r["success"] for r in mis), len(mis))])
    out.append(table(["Model", "Bug type", "Accurate", "Misleading"], rows))
    return out


def rq2(records):
    out = ["## RQ2: which misleading kind does the most damage?",
           "Among failed fixes: did the bug survive? 'followed' = the fix still gives the buggy code's answers on "
           "every test the buggy code fails; 'partly' = on some. Failures under the accurate comment are the baseline.",
           ""]
    rows = []
    for model in MODELS:
        for v in VERSIONS:
            fails = [r for r in records if r["model"] == model and r["version"] == v and not r["success"]]
            c = collections.Counter(r["rq2"] for r in fails)
            rows.append([MODEL_NAMES[model], v, len(fails), pct(c["followed"], len(fails)),
                         pct(c["partly"], len(fails)), pct(c["other_error"], len(fails))])
    out.append(table(["Model", "Comment", "Failed fixes", "Followed", "Partly", "Other error"], rows))
    if any(r["rq2"] is None and not r["success"] for r in records):
        out += ["", "**Note:** some failed fixes have no RQ2 label yet; run `judge.py`."]
    return out


def rq3(records, base):
    out = ["## RQ3: do models notice the conflict, and does a warning help?",
           "Share of replies to a misleading comment that say the comment is wrong (AI judge, see JUDGING.md).", ""]
    rows = []
    for model in MODELS:
        for prompt in ["A", "B"]:
            rs = [r for r in records if r["model"] == model and r["prompt"] == prompt and r["version"] in MISLEADING]
            row = [MODEL_NAMES[model], prompt]
            for v in MISLEADING:
                vs = [r for r in rs if r["version"] == v]
                row.append(pct(sum(r["flags"] == "yes" for r in vs), len(vs)))
            row.append(pct(sum(r["flags"] == "yes" for r in rs), len(rs)))
            rows.append(row)
    out.append(table(["Model", "Prompt"] + MISLEADING + ["all"], rows))

    out += ["", "Flagging vs. fixing (replies to misleading comments).", ""]
    rows = []
    for model in MODELS:
        rs = [r for r in records if r["model"] == model and r["version"] in MISLEADING]
        for flag in ["yes", "no"]:
            fs = [r for r in rs if r["flags"] == flag]
            rows.append([MODEL_NAMES[model], flag, len(fs), pct(sum(r["success"] for r in fs), len(fs))])
    out.append(table(["Model", "Flags comment", "Replies", "Fixed"], rows))

    out += ["", "Does the warning (Prompt B) change success? Paired per program and comment version (exact McNemar).",
            ""]
    rows = []
    for model in MODELS:
        ok = {(r["program"], r["version"], r["prompt"]): r["success"] for r in records if r["model"] == model}
        for group, vs in [("accurate", ["accurate"]), ("misleading", MISLEADING)]:
            pairs = [(ok[(p, v, "A")], ok[(p, v, "B")]) for p, v, pr in ok if pr == "A" and v in vs
                     and (p, v, "B") in ok]
            b, c, p = mcnemar(pairs)
            rows.append([MODEL_NAMES[model], group, pct(sum(x for x, _ in pairs), len(pairs)),
                         pct(sum(y for _, y in pairs), len(pairs)), b, c, p_text(p)])
    out.append(table(["Model", "Comment", "Prompt A", "Prompt B", "Only A fixed", "Only B fixed", "p"], rows))

    sheets = sorted((base / "handcheck").glob("*.csv"))
    if sheets:
        out += ["", "Hand check of the AI judge (people saw the judge's label, so this is the share confirmed by "
                "hand, not independent agreement).", ""]
        rows, total = [], collections.Counter()
        for sheet in sheets:
            with open(sheet, newline="", encoding="utf-8-sig") as f:
                rs = list(csv.DictReader(f))
            filled = [r for r in rs if r["agree (yes/no)"].strip()]
            c = collections.Counter()
            for r in filled:
                said, agree = r["ai_says_flags_comment"], r["agree (yes/no)"].strip().lower() == "yes"
                c[said] += 1
                c[said + "_ok"] += agree
            total.update(c)
            rows.append([sheet.stem, f"{len(filled)}/{len(rs)}", pct(c["yes_ok"], c["yes"]), pct(c["no_ok"], c["no"])])
        rows.append(["**all**", "", pct(total["yes_ok"], total["yes"]), pct(total["no_ok"], total["no"])])
        out.append(table(["Sheet", "Rows filled", "Judge 'yes' confirmed", "Judge 'no' confirmed"], rows))
    return out


def main(argv):
    dataset = argv[0] if argv else "main"
    base = ROOT / "condefects" if dataset == "condefects" else ROOT
    records = load(base)
    if not records:
        sys.exit(f"No results found for {dataset}.")
    programs = len({r["program"] for r in records})
    header = [f"# Results: {'ConDefects (real bugs)' if dataset == 'condefects' else 'our 120 programs'}",
              f"{programs} programs, {len(records)} replies "
              + ", ".join(f"({MODEL_NAMES[m]}: {sum(r['model'] == m for r in records)})" for m in MODELS), ""]
    text = "\n".join(header + rq1(records) + [""] + rq2(records) + [""] + rq3(records, base)) + "\n"
    out_dir = ROOT / "analysis"
    out_dir.mkdir(exist_ok=True)
    (out_dir / f"{dataset}.md").write_text(text)
    print(text)
    print(f"Saved analysis/{dataset}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
