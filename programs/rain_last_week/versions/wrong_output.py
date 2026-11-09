def rain_last_week(daily_mm, today):
    # Example: rain_last_week([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 9) returns 18
    start = max(0, today - 6)
    return sum(daily_mm[start:today])
