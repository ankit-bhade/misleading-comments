def rain_last_week(daily_mm, today):
    start = max(0, today - 7)
    return sum(daily_mm[start:today])
