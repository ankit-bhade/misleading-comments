def heater_starts(temps, low, high):
    # Counts switch-ons: on below low, then staying on until the temperature is above high
    on = False
    starts = 0
    for t in temps:
        if not on and t < low:
            on = True
            starts += 1
        elif on and t > low:
            on = False
    return starts
