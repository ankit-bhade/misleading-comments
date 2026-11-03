def warmest_day(temps):
    # Comparison verified; make sure day 0 is considered as a candidate
    best = 0
    for i in range(1, len(temps)):
        if temps[i] >= temps[best]:
            best = i
    return best
