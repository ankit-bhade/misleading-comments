def ride_average_speed(legs):
    # Example: ride_average_speed([(36, 1.5), (18, 1.5), (40, 2)]) returns 18.7
    if not legs:
        return 0.0
    return round(sum(km / h for km, h in legs) / len(legs), 1)
