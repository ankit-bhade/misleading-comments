"""Slide charts (RQ1-RQ3, our programs vs ConDefects) from the results and labels.

Needs matplotlib (pip install matplotlib). Run from the repo root:
  python3 analysis/charts/make_charts.py   ->  analysis/charts/*.png
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))
import analyze  # noqa: E402

OUT = ROOT / "analysis" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

INK, INK2, MUTED, GRID, AXIS = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
MODEL_COLOR = {"qwen2.5-coder-7b": BLUE, "qwen2.5-coder-32b": ORANGE}
MODEL_LABEL = {"qwen2.5-coder-7b": "Qwen2.5-Coder 7B", "qwen2.5-coder-32b": "Qwen2.5-Coder 32B"}
VERSION_LABEL = {"accurate": "Accurate", "wrong_behavior": "Wrong\nbehavior",
                 "wrong_location": "Wrong\nlocation", "wrong_output": "Wrong\noutput"}
DATASETS = [("Our 120 programs", ROOT), ("ConDefects (120 real bugs)", ROOT / "condefects")]

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "sans-serif"],
    "font.size": 14, "text.color": INK, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": MUTED, "axes.edgecolor": AXIS,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})

DATA = {name: analyze.load(base) for name, base in DATASETS}


def style(ax, ymax, step, fmt="{:.0f}%"):
    ax.set_ylim(0, ymax)
    ax.set_yticks(range(0, ymax + 1, step))
    ax.set_yticklabels([fmt.format(t) for t in range(0, ymax + 1, step)], fontsize=12)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="both", length=0)


def bars(ax, groups, series, values, colors, labels, width=0.36, fmt="{:.0f}%", label_size=12, off=1):
    """Grouped bars with a 2px-ish gap and a value label above each bar."""
    n = len(series)
    for i, s in enumerate(series):
        xs = [g + (i - (n - 1) / 2) * width for g in range(len(groups))]
        ys = [values[(g, s)] for g in groups]
        rects = ax.bar(xs, ys, width * 0.92, color=colors[s], label=labels[s], zorder=2)
        for r, y in zip(rects, ys):
            ax.text(r.get_x() + r.get_width() / 2, y + off, fmt.format(y), ha="center", va="bottom",
                    fontsize=label_size, color=INK)


def rate(rs, cond=lambda r: r["success"]):
    return 100 * sum(1 for r in rs if cond(r)) / len(rs)


def legend(fig, handles_from, ncol=2):
    h, l = handles_from.get_legend_handles_labels()
    fig.legend(h, l, loc="upper right", ncol=ncol, frameon=False, fontsize=13, bbox_to_anchor=(0.995, 1.075))


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("saved", OUT / name)


# 1. RQ1: success rate by comment version
fig, axes = plt.subplots(1, 2, figsize=(13, 5.4), sharey=True)
for ax, (name, _) in zip(axes, DATASETS):
    recs = DATA[name]
    vals = {(v, m): rate([r for r in recs if r["model"] == m and r["version"] == v])
            for v in analyze.VERSIONS for m in analyze.MODELS}
    bars(ax, analyze.VERSIONS, analyze.MODELS, vals, MODEL_COLOR, MODEL_LABEL)
    ax.set_xticks(range(4))
    ax.set_xticklabels([VERSION_LABEL[v] for v in analyze.VERSIONS], fontsize=13)
    ax.set_title(name, fontsize=15, loc="left", color=INK, pad=12)
    style(ax, 100, 20)
axes[0].set_ylabel("Bugs fixed (all tests pass)")
fig.suptitle("RQ1: Fix success by comment shown", x=0.01, ha="left", fontsize=18, fontweight="bold", y=1.03)
legend(fig, axes[0])
save(fig, "rq1_success_by_comment.png")


# 2. RQ1: change vs accurate (points), with p-values
def change(recs, model, version):
    ok = {(r["program"], r["version"], r["prompt"]): r["success"] for r in recs if r["model"] == model}
    keys = sorted({(p, pr) for p, v, pr in ok})
    pairs = [(ok[(p, "accurate", pr)], ok[(p, version, pr)]) for p, pr in keys]
    _, _, p = analyze.mcnemar(pairs)
    return 100 * (sum(y for _, y in pairs) - sum(x for x, _ in pairs)) / len(pairs), p


fig, axes = plt.subplots(1, 2, figsize=(13, 5.4), sharey=True)
width = 0.36
for ax, (name, _) in zip(axes, DATASETS):
    recs = DATA[name]
    for i, m in enumerate(analyze.MODELS):
        for g, v in enumerate(analyze.MISLEADING):
            d, p = change(recs, m, v)
            x = g + (i - 0.5) * width
            ax.bar(x, d, width * 0.92, color=MODEL_COLOR[m], label=MODEL_LABEL[m] if g == 0 else None, zorder=2)
            txt = f"{d:+.1f}" + (f"\np = {p:.3f}" if p < 0.05 else "")
            ax.text(x, d + (0.4 if d >= 0 else -0.4), txt, ha="center", va="bottom" if d >= 0 else "top",
                    fontsize=12, color=INK, fontweight="bold" if p < 0.05 else "normal")
    ax.axhline(0, color=INK2, linewidth=1.2, zorder=3)
    ax.set_xticks(range(3))
    ax.set_xticklabels([VERSION_LABEL[v] for v in analyze.MISLEADING], fontsize=13)
    ax.set_title(name, fontsize=15, loc="left", color=INK, pad=12)
    ax.set_ylim(-16, 8)
    ax.set_yticks(range(-16, 9, 4))
    ax.set_yticklabels([f"{t:+d}" if t else "0" for t in range(-16, 9, 4)], fontsize=12)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left", "bottom"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="both", length=0)
axes[0].set_ylabel("Change vs. accurate comment (points)")
fig.suptitle("RQ1: How much each misleading comment costs", x=0.01, ha="left", fontsize=18,
             fontweight="bold", y=1.03)
fig.text(0.01, -0.04, "Paired exact McNemar test vs. the accurate comment; p shown only where p < 0.05. "
         "240 pairs per bar (120 programs × Prompts A and B).", fontsize=11, color=MUTED)
legend(fig, axes[0])
save(fig, "rq1_change_vs_accurate.png")


# 3. RQ2: bug survived among failed fixes
fig, axes = plt.subplots(1, 2, figsize=(13, 5.4), sharey=True)
for ax, (name, _) in zip(axes, DATASETS):
    recs = DATA[name]
    vals = {}
    for v in analyze.VERSIONS:
        for m in analyze.MODELS:
            fails = [r for r in recs if r["model"] == m and r["version"] == v and not r["success"]]
            vals[(v, m)] = rate(fails, lambda r: r["rq2"] == "followed")
    bars(ax, analyze.VERSIONS, analyze.MODELS, vals, MODEL_COLOR, MODEL_LABEL)
    ax.set_xticks(range(4))
    ax.set_xticklabels([VERSION_LABEL[v] for v in analyze.VERSIONS], fontsize=13)
    ax.set_title(name, fontsize=15, loc="left", color=INK, pad=12)
    style(ax, 100, 20)
axes[0].set_ylabel("Failed fixes where the bug survived")
fig.suptitle("RQ2: When the fix fails, is the bug still there?", x=0.01, ha="left", fontsize=18,
             fontweight="bold", y=1.03)
fig.text(0.01, -0.04, "'Bug survived' = the fix still gives the buggy code's answers on every test the buggy "
         "code fails. Accurate = baseline.", fontsize=11, color=MUTED)
legend(fig, axes[0])
save(fig, "rq2_bug_survived.png")


# 4. RQ3: share of misleading-comment replies that flag the comment, Prompt A vs B
PROMPT_COLOR = {"A": AQUA, "B": YELLOW}
PROMPT_LABEL = {"A": "Prompt A (no warning)", "B": "Prompt B (\"comments may be wrong\")"}
fig, axes = plt.subplots(1, 2, figsize=(13, 5.4), sharey=True)
for ax, (name, _) in zip(axes, DATASETS):
    recs = DATA[name]
    vals = {(m, pr): rate([r for r in recs if r["model"] == m and r["prompt"] == pr
                           and r["version"] in analyze.MISLEADING], lambda r: r["flags"] == "yes")
            for m in analyze.MODELS for pr in "AB"}
    bars(ax, analyze.MODELS, ["A", "B"], vals, PROMPT_COLOR, PROMPT_LABEL, fmt="{:.1f}%", off=0.15)
    ax.set_xticks(range(2))
    ax.set_xticklabels(["7B", "32B"], fontsize=14)
    ax.set_title(name, fontsize=15, loc="left", color=INK, pad=12)
    style(ax, 10, 2)
axes[0].set_ylabel("Replies that say the comment is wrong")
fig.suptitle("RQ3: Do models notice the misleading comment?", x=0.01, ha="left", fontsize=18,
             fontweight="bold", y=1.03)
fig.text(0.01, -0.04, "360 replies to misleading comments per bar. Labeled by an AI judge (GPT-6.1 Terra); "
         "every hand-checked label was confirmed.", fontsize=11, color=MUTED)
legend(fig, axes[0])
save(fig, "rq3_flag_rate.png")
