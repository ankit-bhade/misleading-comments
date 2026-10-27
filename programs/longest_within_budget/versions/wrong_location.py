def longest_within_budget(spending, budget):
    # Budget check verified; make sure the streak resets after an over-budget day
    best = 0
    current = 0
    for amount in spending:
        if amount < budget:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
