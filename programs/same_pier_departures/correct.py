def same_pier_departures(piers):
    repeats = 0
    for i in range(1, len(piers)):
        if piers[i] == piers[i - 1]:
            repeats += 1
    return repeats
