"""Build the hand-check sheets from the AI judge's labels (see JUDGING.md).

Each person verifies the judge's RQ3 labels on 6 of their own programs (the
replies to the misleading comments), plus every other reply of theirs that the
judge labeled yes, since yes is rare. Run after judge.py. Writes
handcheck/<first name>.csv, and won't overwrite a sheet someone has started.

Usage:
  python3 handcheck.py
"""
import csv
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODELS = ["qwen2.5-coder-7b", "qwen2.5-coder-32b"]
# 6 programs per person: one per bug type plus two more, drawn with seed 2026 without looking at results.
SAMPLE = {
    "Ankit": ["chunk_sums", "in_date_order", "minutes_until", "visit_order", "shorten", "best_quarter"],
    "Arnav": ["last_entry", "motion_passes", "setlist_length", "visits_by_site", "parse_record", "tote_bag_winners"],
    "Kushal": ["rain_last_week", "sea_view_cabins", "split_label", "transit_hours", "watch_rota", "same_pier_departures"],
    "Seung Wook": ["fastest_lap", "cable_car_boarding", "best_streak_profit", "attendance_growth", "busiest_window",
                   "dive_log_total"],
}
COLUMNS = ["row", "program", "comment_shown_to_model", "model_reply", "ai_says_flags_comment",
           "agree (yes/no)", "note", "model", "version", "prompt"]


def sheet_rows(person):
    """Rows for one person: their sample, plus their other replies the judge labeled yes."""
    rows = []
    for folder in sorted((ROOT / "programs").iterdir()):
        if not folder.is_dir():
            continue
        info = json.loads((folder / "info.json").read_text())
        if info["author"].strip() != person:
            continue
        for model in MODELS:
            results = {(r["version"], r["prompt"]): r
                       for r in json.loads((ROOT / "results" / model / f"{folder.name}.json").read_text())}
            judged_path = ROOT / "judgments" / model / f"{folder.name}.json"
            judged = json.loads(judged_path.read_text()) if judged_path.exists() else []
            for label in judged:
                if label["version"] == "accurate":
                    continue
                if label["flags_comment"] is None:
                    sys.exit(f"{judged_path.relative_to(ROOT)} has replies without a judge label. Run judge.py first.")
                if folder.name in SAMPLE[person] or label["flags_comment"] == "yes":
                    result = results[(label["version"], label["prompt"])]
                    rows.append([folder.name, info["comments"][label["version"]], result["reply"],
                                 label["flags_comment"], "", "", model, label["version"], label["prompt"]])
            if not judged and folder.name in SAMPLE[person]:
                sys.exit(f"No judge labels for {model}/{folder.name}. Run judge.py first.")
    random.Random(2026).shuffle(rows)  # mixed order, so models and comment kinds aren't grouped
    return rows


def main():
    out_dir = ROOT / "handcheck"
    out_dir.mkdir(exist_ok=True)
    for person in SAMPLE:
        path = out_dir / f"{person.split()[0].lower()}.csv"
        if path.exists():
            with open(path, newline="") as f:
                if any(row["agree (yes/no)"].strip() for row in csv.DictReader(f)):
                    print(f"SKIP  {path.relative_to(ROOT)}: already being filled in")
                    continue
        rows = sheet_rows(person)
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(COLUMNS)
            for i, row in enumerate(rows, 1):
                writer.writerow([i] + row)
        extra = len(rows) - 12 * len(SAMPLE[person])
        print(f"WROTE {path.relative_to(ROOT)}: {len(rows)} rows ({extra} extra yes rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
