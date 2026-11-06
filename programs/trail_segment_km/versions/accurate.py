def trail_segment_km(daily_km, legs):
    # Kilometres walked in each leg, using running totals of the daily distances
    prefix = [0]
    for km in daily_km:
        prefix.append(prefix[-1] + km)
    totals = []
    for first, last in legs:
        totals.append(prefix[last] - prefix[first])
    return totals
