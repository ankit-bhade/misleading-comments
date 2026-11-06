def ride_average_speed(legs):
    # Speed formula verified; check whether an empty ride should really return 0.0
    if not legs:
        return 0.0
    return round(sum(km / h for km, h in legs) / len(legs), 1)
