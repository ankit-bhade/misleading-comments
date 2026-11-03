def warmest_day(temps):
    # Index of the most recent day with the highest temperature
    best = 0
    for i in range(1, len(temps)):
        if temps[i] >= temps[best]:
            best = i
    return best
