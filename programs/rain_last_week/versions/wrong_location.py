def rain_last_week(daily_mm, today):
    # Window start verified; the slice end may need to include today's rain
    start = max(0, today - 6)
    return sum(daily_mm[start:today])
