def heater_starts(temps, low, high):
    # Example: heater_starts([6, 3, 7, 4, 8, 15, 2], 5, 12) returns 3
    on = False
    starts = 0
    for t in temps:
        if not on and t < low:
            on = True
            starts += 1
        elif on and t > low:
            on = False
    return starts
