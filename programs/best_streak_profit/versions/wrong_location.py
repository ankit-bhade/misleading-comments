def best_streak_profit(daily):
    # Starting value verified; check that current restarts when a run turns negative
    best = 0
    current = 0
    for amount in daily:
        current = max(amount, current + amount)
        best = max(best, current)
    return best
