def rain_last_week(daily_mm, today):
    # Total rain over the last six full days, not counting today
    start = max(0, today - 6)
    return sum(daily_mm[start:today])
