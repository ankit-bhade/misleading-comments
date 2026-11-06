def ride_average_speed(legs):
    # Average of the speeds ridden on each leg, in km/h
    if not legs:
        return 0.0
    return round(sum(km / h for km, h in legs) / len(legs), 1)
