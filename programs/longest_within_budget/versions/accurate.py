def longest_within_budget(spending, budget):
    # Longest run of consecutive days with spending at or below the budget
    best = 0
    current = 0
    for amount in spending:
        if amount < budget:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
