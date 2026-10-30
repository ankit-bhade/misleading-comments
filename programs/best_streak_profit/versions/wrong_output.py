def best_streak_profit(daily):
    # Example: best_streak_profit([-5, -2, -8]) returns 0
    best = 0
    current = 0
    for amount in daily:
        current = max(amount, current + amount)
        best = max(best, current)
    return best
