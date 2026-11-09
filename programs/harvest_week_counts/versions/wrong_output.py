def harvest_week_counts(picked_days):
    # Example: harvest_week_counts([1, 7, 8]) returns {1: 1, 2: 2}
    counts = {}
    for day in picked_days:
        week = day // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
