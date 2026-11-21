# Results: ConDefects (real bugs)
120 programs, 1920 replies (7B: 960), (32B: 960)

## RQ1: is a misleading comment worse than an accurate one?
Fix success rate (all tests pass), Prompts A and B together.

| Model | accurate | wrong_behavior | wrong_location | wrong_output | all misleading |
|---|---|---|---|---|---|
| 7B | 119/240 (50%) | 107/240 (45%) | 113/240 (47%) | 123/240 (51%) | 343/720 (48%) |
| 32B | 172/240 (72%) | 166/240 (69%) | 165/240 (69%) | 166/240 (69%) | 497/720 (69%) |

Paired test against the accurate comment, per program and prompt (exact McNemar). 'Lost' = fixed with the accurate comment but not this one; 'gained' = the reverse.

| Model | Comment | Change vs accurate (− = worse) | Lost | Gained | p |
|---|---|---|---|---|---|
| 7B | wrong_behavior | -5.0 pts | 39 | 27 | 0.175 |
| 7B | wrong_location | -2.5 pts | 30 | 24 | 0.497 |
| 7B | wrong_output | +1.7 pts | 27 | 31 | 0.694 |
| 7B | all misleading | -1.9 pts | 96 | 82 | 0.330 |
| 32B | wrong_behavior | -2.5 pts | 24 | 18 | 0.441 |
| 32B | wrong_location | -2.9 pts | 21 | 14 | 0.311 |
| 32B | wrong_output | -2.5 pts | 25 | 19 | 0.451 |
| 32B | all misleading | -2.6 pts | 70 | 51 | 0.101 |

By bug type (success rate; accurate vs. all misleading).

| Model | Bug type | Accurate | Misleading |
|---|---|---|---|
| 7B | off_by_one | 22/46 (48%) | 65/138 (47%) |
| 7B | wrong_comparison | 14/24 (58%) | 41/72 (57%) |
| 7B | missed_edge_case | 9/22 (41%) | 29/66 (44%) |
| 7B | other | 74/148 (50%) | 208/444 (47%) |
| 32B | off_by_one | 37/46 (80%) | 100/138 (72%) |
| 32B | wrong_comparison | 18/24 (75%) | 54/72 (75%) |
| 32B | missed_edge_case | 10/22 (45%) | 43/66 (65%) |
| 32B | other | 107/148 (72%) | 300/444 (68%) |

## RQ2: which misleading kind does the most damage?
Among failed fixes: did the bug survive? 'followed' = the fix still gives the buggy code's answers on every test the buggy code fails; 'partly' = on some. Failures under the accurate comment are the baseline.

| Model | Comment | Failed fixes | Followed | Partly | Other error |
|---|---|---|---|---|---|
| 7B | accurate | 121 | 61/121 (50%) | 14/121 (12%) | 46/121 (38%) |
| 7B | wrong_behavior | 133 | 63/133 (47%) | 17/133 (13%) | 53/133 (40%) |
| 7B | wrong_location | 127 | 60/127 (47%) | 11/127 (9%) | 56/127 (44%) |
| 7B | wrong_output | 117 | 53/117 (45%) | 10/117 (9%) | 54/117 (46%) |
| 32B | accurate | 68 | 36/68 (53%) | 6/68 (9%) | 26/68 (38%) |
| 32B | wrong_behavior | 74 | 42/74 (57%) | 8/74 (11%) | 24/74 (32%) |
| 32B | wrong_location | 75 | 34/75 (45%) | 11/75 (15%) | 30/75 (40%) |
| 32B | wrong_output | 74 | 32/74 (43%) | 8/74 (11%) | 34/74 (46%) |

## RQ3: do models notice the conflict, and does a warning help?
Share of replies to a misleading comment that say the comment is wrong (AI judge, see JUDGING.md).

| Model | Prompt | wrong_behavior | wrong_location | wrong_output | all |
|---|---|---|---|---|---|
| 7B | A | 0/120 (0%) | 0/120 (0%) | 0/120 (0%) | 0/360 (0%) |
| 7B | B | 2/120 (2%) | 0/120 (0%) | 0/120 (0%) | 2/360 (1%) |
| 32B | A | 0/120 (0%) | 0/120 (0%) | 1/120 (1%) | 1/360 (0%) |
| 32B | B | 4/120 (3%) | 1/120 (1%) | 5/120 (4%) | 10/360 (3%) |

Flagging vs. fixing (replies to misleading comments).

| Model | Flags comment | Replies | Fixed |
|---|---|---|---|
| 7B | yes | 2 | 2/2 (100%) |
| 7B | no | 718 | 341/718 (47%) |
| 32B | yes | 11 | 8/11 (73%) |
| 32B | no | 709 | 489/709 (69%) |

Does the warning (Prompt B) change success? Paired per program and comment version (exact McNemar).

| Model | Comment | Prompt A | Prompt B | Only A fixed | Only B fixed | p |
|---|---|---|---|---|---|---|
| 7B | accurate | 62/120 (52%) | 57/120 (48%) | 11 | 6 | 0.332 |
| 7B | misleading | 175/360 (49%) | 168/360 (47%) | 34 | 27 | 0.443 |
| 32B | accurate | 83/120 (69%) | 89/120 (74%) | 0 | 6 | 0.031 |
| 32B | misleading | 252/360 (70%) | 245/360 (68%) | 22 | 15 | 0.324 |

Hand check of the AI judge (people saw the judge's label, so this is the share confirmed by hand, not independent agreement).

| Sheet | Rows filled | Judge 'yes' confirmed | Judge 'no' confirmed |
|---|---|---|---|
| ankit | 75/75 | 3/3 (100%) | 72/72 (100%) |
| arnav | 74/74 | 2/2 (100%) | 72/72 (100%) |
| kushal | 76/76 | 4/4 (100%) | 72/72 (100%) |
| seung | 75/75 | 4/4 (100%) | 71/71 (100%) |
| **all** |  | 13/13 (100%) | 287/287 (100%) |
