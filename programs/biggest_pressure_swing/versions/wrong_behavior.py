def biggest_pressure_swing(readings):
    # Largest hour-to-hour rise in pressure seen in the readings
    swing = 0
    for before, after in zip(readings, readings[1:]):
        swing = max(swing, after - before)
    return swing
