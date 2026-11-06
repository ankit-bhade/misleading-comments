def trail_segment_km(daily_km, legs):
    prefix = [0]
    for km in daily_km:
        prefix.append(prefix[-1] + km)
    totals = []
    for first, last in legs:
        totals.append(prefix[last + 1] - prefix[first])
    return totals
