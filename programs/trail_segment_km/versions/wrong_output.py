def trail_segment_km(daily_km, legs):
    # Example: trail_segment_km([10, 12, 8, 15], [(0, 1)]) returns [10]
    prefix = [0]
    for km in daily_km:
        prefix.append(prefix[-1] + km)
    totals = []
    for first, last in legs:
        totals.append(prefix[last] - prefix[first])
    return totals
