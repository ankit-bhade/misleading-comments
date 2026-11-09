def harvest_week_counts(picked_days):
    # Week calculation checked; weeks with no picking days may be missing from the result
    counts = {}
    for day in picked_days:
        week = day // 7 + 1
        counts[week] = counts.get(week, 0) + 1
    return counts
