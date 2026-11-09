def rain_last_week(daily_mm, today):
    # Total rain over the seven days before today, not counting today
    start = max(0, today - 6)
    return sum(daily_mm[start:today])
