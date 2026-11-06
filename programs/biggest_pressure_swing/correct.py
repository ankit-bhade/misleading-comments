def biggest_pressure_swing(readings):
    swing = 0
    for before, after in zip(readings, readings[1:]):
        swing = max(swing, abs(after - before))
    return swing
