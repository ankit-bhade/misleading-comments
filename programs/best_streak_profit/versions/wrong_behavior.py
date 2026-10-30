def best_streak_profit(daily):
    # Largest total profit over any run of consecutive days, or 0 if every day is a loss
    best = 0
    current = 0
    for amount in daily:
        current = max(amount, current + amount)
        best = max(best, current)
    return best
