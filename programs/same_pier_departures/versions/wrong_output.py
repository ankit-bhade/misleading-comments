def same_pier_departures(piers):
    # Example: same_pier_departures(['A', 'B', 'A']) returns 1
    repeats = 0
    for i in range(len(piers)):
        if piers[i] == piers[i - 1]:
            repeats += 1
    return repeats
