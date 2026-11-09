def harvest_week_counts(picked_days):
    # Counts picking days per week, where a day's week is its number of completed weeks plus one
    counts = {}
    for day in picked_days:
        week = day // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
