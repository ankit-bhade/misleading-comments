def harvest_week_counts(picked_days):
    counts = {}
    for day in picked_days:
        week = (day - 1) // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
