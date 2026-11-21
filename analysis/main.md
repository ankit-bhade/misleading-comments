# Results: our 120 programs
120 programs, 1920 replies (7B: 960), (32B: 960)

## RQ1: is a misleading comment worse than an accurate one?
Fix success rate (all tests pass), Prompts A and B together.

| Model | accurate | wrong_behavior | wrong_location | wrong_output | all misleading |
|---|---|---|---|---|---|
| 7B | 170/240 (71%) | 162/240 (68%) | 146/240 (61%) | 181/240 (75%) | 489/720 (68%) |
| 32B | 205/240 (85%) | 201/240 (84%) | 199/240 (83%) | 213/240 (89%) | 613/720 (85%) |

Paired test against the accurate comment, per program and prompt (exact McNemar). 'Lost' = fixed with the accurate comment but not this one; 'gained' = the reverse.

| Model | Comment | Change vs accurate (− = worse) | Lost | Gained | p |
|---|---|---|---|---|---|
| 7B | wrong_behavior | -3.3 pts | 25 | 17 | 0.280 |
| 7B | wrong_location | -10.0 pts | 42 | 18 | 0.003 |
| 7B | wrong_output | +4.6 pts | 17 | 28 | 0.135 |
| 7B | all misleading | -2.9 pts | 84 | 63 | 0.099 |
| 32B | wrong_behavior | -1.7 pts | 15 | 11 | 0.557 |
| 32B | wrong_location | -2.5 pts | 15 | 9 | 0.307 |
| 32B | wrong_output | +3.3 pts | 5 | 13 | 0.096 |
| 32B | all misleading | -0.3 pts | 35 | 33 | 0.904 |

By bug type (success rate; accurate vs. all misleading).

| Model | Bug type | Accurate | Misleading |
|---|---|---|---|
| 7B | off_by_one | 42/56 (75%) | 128/168 (76%) |
| 7B | wrong_comparison | 42/56 (75%) | 110/168 (65%) |
| 7B | missed_edge_case | 37/56 (66%) | 107/168 (64%) |
| 7B | other | 49/72 (68%) | 144/216 (67%) |
| 32B | off_by_one | 51/56 (91%) | 146/168 (87%) |
| 32B | wrong_comparison | 49/56 (88%) | 145/168 (86%) |
| 32B | missed_edge_case | 41/56 (73%) | 125/168 (74%) |
| 32B | other | 64/72 (89%) | 197/216 (91%) |

## RQ2: which misleading kind does the most damage?
Among failed fixes: did the bug survive? 'followed' = the fix still gives the buggy code's answers on every test the buggy code fails; 'partly' = on some. Failures under the accurate comment are the baseline.

| Model | Comment | Failed fixes | Followed | Partly | Other error |
|---|---|---|---|---|---|
| 7B | accurate | 70 | 43/70 (61%) | 3/70 (4%) | 24/70 (34%) |
| 7B | wrong_behavior | 78 | 52/78 (67%) | 1/78 (1%) | 25/78 (32%) |
| 7B | wrong_location | 94 | 71/94 (76%) | 6/94 (6%) | 17/94 (18%) |
| 7B | wrong_output | 59 | 39/59 (66%) | 5/59 (8%) | 15/59 (25%) |
| 32B | accurate | 35 | 26/35 (74%) | 0/35 (0%) | 9/35 (26%) |
| 32B | wrong_behavior | 39 | 28/39 (72%) | 2/39 (5%) | 9/39 (23%) |
| 32B | wrong_location | 41 | 32/41 (78%) | 1/41 (2%) | 8/41 (20%) |
| 32B | wrong_output | 27 | 20/27 (74%) | 2/27 (7%) | 5/27 (19%) |

## RQ3: do models notice the conflict, and does a warning help?
Share of replies to a misleading comment that say the comment is wrong (AI judge, see JUDGING.md).

| Model | Prompt | wrong_behavior | wrong_location | wrong_output | all |
|---|---|---|---|---|---|
| 7B | A | 0/120 (0%) | 0/120 (0%) | 0/120 (0%) | 0/360 (0%) |
| 7B | B | 2/120 (2%) | 4/120 (3%) | 0/120 (0%) | 6/360 (2%) |
| 32B | A | 0/120 (0%) | 1/120 (1%) | 3/120 (2%) | 4/360 (1%) |
| 32B | B | 12/120 (10%) | 7/120 (6%) | 11/120 (9%) | 30/360 (8%) |

Flagging vs. fixing (replies to misleading comments).

| Model | Flags comment | Replies | Fixed |
|---|---|---|---|
| 7B | yes | 6 | 2/6 (33%) |
| 7B | no | 714 | 487/714 (68%) |
| 32B | yes | 34 | 19/34 (56%) |
| 32B | no | 686 | 594/686 (87%) |

Does the warning (Prompt B) change success? Paired per program and comment version (exact McNemar).

| Model | Comment | Prompt A | Prompt B | Only A fixed | Only B fixed | p |
|---|---|---|---|---|---|---|
| 7B | accurate | 85/120 (71%) | 85/120 (71%) | 10 | 10 | 1.000 |
| 7B | misleading | 245/360 (68%) | 244/360 (68%) | 19 | 18 | 1.000 |
| 32B | accurate | 103/120 (86%) | 102/120 (85%) | 5 | 4 | 1.000 |
| 32B | misleading | 307/360 (85%) | 306/360 (85%) | 11 | 10 | 1.000 |

Hand check of the AI judge (people saw the judge's label, so this is the share confirmed by hand, not independent agreement).

| Sheet | Rows filled | Judge 'yes' confirmed | Judge 'no' confirmed |
|---|---|---|---|
| ankit | 83/83 | 12/12 (100%) | 71/71 (100%) |
| arnav | 81/81 | 9/9 (100%) | 72/72 (100%) |
| kushal | 79/79 | 12/12 (100%) | 67/67 (100%) |
| seung | 77/77 | 7/7 (100%) | 70/70 (100%) |
| **all** |  | 40/40 (100%) | 280/280 (100%) |
