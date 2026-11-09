def rain_last_week(daily_mm, today):
    # COMMENT
    start = max(0, today - 6)
    return sum(daily_mm[start:today])
