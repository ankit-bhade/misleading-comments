def harvest_week_counts(picked_days):
    # COMMENT
    counts = {}
    for day in picked_days:
        week = day // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
