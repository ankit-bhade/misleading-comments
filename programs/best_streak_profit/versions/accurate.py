def best_streak_profit(daily):
    # Largest total profit over any run of at least one consecutive day
    best = 0
    current = 0
    for amount in daily:
        current = max(amount, current + amount)
        best = max(best, current)
    return best
