def longest_within_budget(spending, budget):
    # Example: longest_within_budget([5, 10, 10, 3, 12], 10) returns 1
    best = 0
    current = 0
    for amount in spending:
        if amount < budget:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
