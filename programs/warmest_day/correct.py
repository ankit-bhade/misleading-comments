def warmest_day(temps):
    best = 0
    for i in range(1, len(temps)):
        if temps[i] > temps[best]:
            best = i
    return best
