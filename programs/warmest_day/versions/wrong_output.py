def warmest_day(temps):
    # Example: warmest_day([20, 25, 25]) returns 2
    best = 0
    for i in range(1, len(temps)):
        if temps[i] >= temps[best]:
            best = i
    return best
