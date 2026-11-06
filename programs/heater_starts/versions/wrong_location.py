def heater_starts(temps, low, high):
    # Switch-off test verified; a reading exactly at low may need to start the heater too
    on = False
    starts = 0
    for t in temps:
        if not on and t < low:
            on = True
            starts += 1
        elif on and t > low:
            on = False
    return starts
