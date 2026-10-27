def longest_within_budget(spending, budget):
    # COMMENT
    best = 0
    current = 0
    for amount in spending:
        if amount < budget:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
