def heater_starts(temps, low, high):
    # Counts how often the heater kicks in; it switches off as soon as the greenhouse is back above low
    on = False
    starts = 0
    for t in temps:
        if not on and t < low:
            on = True
            starts += 1
        elif on and t > low:
            on = False
    return starts
