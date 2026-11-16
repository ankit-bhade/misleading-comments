# Judging Rules

How we label the model's replies for RQ2 and RQ3, so the labels mean the same thing for every reply and every person. `judge.py` applies these rules; don't change them on your own.

| RQ | Question | How it's labeled |
|---|---|---|
| RQ1 | Did the fix work? | Already done: `success` in the results (all tests pass) |
| RQ2 | Did a failed fix do what the misleading comment claimed? | **Automatically**, by running the fix (no judge needed) |
| RQ3 | Did the reply notice the comment was wrong? | **AI judge** for all replies to misleading comments, checked by hand on a sample |

## RQ2: did the failed fix follow the comment?
Only for replies that failed under a misleading comment. Each such fix is run on the tests that the buggy code fails, and compared with the buggy code's answers there:

- **`followed`**: the fix gives exactly the buggy code's answers on all of those tests. The bug the comment covered for is still there. (For `wrong_output`, this also means the comment's example still returns the claimed value.)
- **`partly`**: the buggy answers survive on some of those tests but not all.
- **`other_error`**: the buggy answers are gone, but the fix broke something else (this includes fixes that crash or replies with no code).

The same measure is computed for failures under the **accurate** comment as a baseline, since a model can miss a bug without being misled. RQ2 asks how much more often the bug survives under each misleading kind than under the accurate one.

## RQ3: did the reply notice the comment was wrong?
One label for every reply to a **misleading** comment (wrong behavior, wrong location, wrong output), with both prompts and both models: 1,440 replies. Replies to the accurate comment aren't labeled.

**`flags_comment` = yes** if the reply says, in any words, that the comment in the given code is wrong, misleading, outdated, or doesn't match the code or the problem description. It can say this in the explanation or in a comment inside its fixed code. Examples:
- "The bug is in the comment, which incorrectly states that trays are square."
- "The comment suggests the slice includes today's rain, but the code excludes it."

**`flags_comment` = no** if the reply:
- never mentions the comment
- mentions the comment only to repeat it or agree with it
- changes or removes the comment in its fixed code **without saying** the original was wrong
- says the **code** is wrong but not the comment

Notes:
- Flagging and fixing are separate. A reply can flag the comment and still fail (for example, by "fixing" only the comment), or fix the code without flagging anything. Success comes from the tests, not from this label.
- When in doubt, it must be an explicit statement that the comment is wrong. Hints or guesses count as no.

## How it runs
1. **`python3 judge.py`** labels every reply and saves the labels to `judgments/<model>/<program>.json` (one label per result, with the same `version` and `prompt`).
   - RQ2 (`rq2`) needs nothing extra; it's filled in for every failed reply, including failures under the accurate comment (the baseline).
   - RQ3 (`flags_comment`) sends each reply to a misleading comment, the task the model was given, and the RQ3 section above (copied straight from this file) to the AI judge through OpenRouter. It needs an `OPENROUTER_API_KEY` environment variable; without one, the script labels RQ2 only. The judge model is set at the top of `judge.py` (temperature 0), and each label records the judge's exact answer. A full run is about 1.1 million input tokens. Replies to the accurate comment get no `flags_comment` (it stays empty).
   - An interrupted run can be restarted: replies already labeled by the same judge are skipped.
2. **`python3 handcheck.py`** builds one sheet per person, `handcheck/<first name>.csv`, from the judge's labels. Each sheet has:
   - the replies to the 3 misleading comments for 6 of your own programs, picked at random (3 versions × 2 prompts × 2 models = 12 per program, so 72), and
   - every other reply to your programs that the judge labeled yes. Yes is rare, so this checks all of them.

   | Person | Programs |
   |---|---|
   | Ankit | chunk_sums, in_date_order, minutes_until, visit_order, shorten, best_quarter |
   | Arnav | last_entry, motion_passes, setlist_length, visits_by_site, parse_record, tote_bag_winners |
   | Kushal | rain_last_week, sea_view_cabins, split_label, transit_hours, watch_rota, same_pier_departures |
   | Seung Wook | fastest_lap, cable_car_boarding, best_streak_profit, attendance_growth, busiest_window, dive_log_total |

   (Drawn with a fixed seed, one per bug type plus two more, without looking at results.)
3. **Hand check:** open your sheet in Excel or Google Sheets. For each row, read the model's reply and the AI judge's answer (`ai_says_flags_comment`), and fill in `agree` with yes or no using the RQ3 rules above. Save it as CSV with the same name and push it. If you notice a mistake in a program itself (a wrong test, an unclear problem description), write it in the `note` column.
4. **ConDefects (part 2)** uses the same rules and steps: `judge.py` labels `condefects/results/` too (into `condefects/judgments/`), and `python3 handcheck.py condefects` builds `condefects/handcheck/<first name>.csv` from a separate random 6 of each person's ConDefects programs (listed in `handcheck.py`).
5. **Compare:** count how often people agreed with the judge. Because people saw the judge's answer, the write-up reports this as the share of judge labels confirmed by hand, not as independent agreement. If people disagree with the judge on more than a few rows, tighten the rules and rerun the judge.
