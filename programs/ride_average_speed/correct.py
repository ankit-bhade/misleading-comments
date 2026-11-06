def ride_average_speed(legs):
    if not legs:
        return 0.0
    return round(sum(km for km, h in legs) / sum(h for km, h in legs), 1)
