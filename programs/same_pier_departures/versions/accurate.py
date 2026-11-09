def same_pier_departures(piers):
    # Counts sailings that left from the same pier as the previous sailing
    repeats = 0
    for i in range(len(piers)):
        if piers[i] == piers[i - 1]:
            repeats += 1
    return repeats
