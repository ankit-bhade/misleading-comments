def biggest_pressure_swing(readings):
    # Example: biggest_pressure_swing([1010, 1003, 1005]) returns 2
    swing = 0
    for before, after in zip(readings, readings[1:]):
        swing = max(swing, after - before)
    return swing
