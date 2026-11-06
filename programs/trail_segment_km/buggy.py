def trail_segment_km(daily_km, legs):
    # COMMENT
    prefix = [0]
    for km in daily_km:
        prefix.append(prefix[-1] + km)
    totals = []
    for first, last in legs:
        totals.append(prefix[last] - prefix[first])
    return totals
