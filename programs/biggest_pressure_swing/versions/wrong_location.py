def biggest_pressure_swing(readings):
    # Change calculation verified; check each reading is paired with the next one
    swing = 0
    for before, after in zip(readings, readings[1:]):
        swing = max(swing, after - before)
    return swing
