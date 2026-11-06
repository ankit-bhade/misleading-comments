def biggest_pressure_swing(readings):
    # COMMENT
    swing = 0
    for before, after in zip(readings, readings[1:]):
        swing = max(swing, after - before)
    return swing
