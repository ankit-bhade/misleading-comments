def heater_starts(temps, low, high):
    on = False
    starts = 0
    for t in temps:
        if not on and t < low:
            on = True
            starts += 1
        elif on and t > high:
            on = False
    return starts
