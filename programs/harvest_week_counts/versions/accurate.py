def harvest_week_counts(picked_days):
    # Counts picking days in each harvest week, seven days to a week starting from day 1
    counts = {}
    for day in picked_days:
        week = day // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
