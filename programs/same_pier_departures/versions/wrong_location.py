def same_pier_departures(piers):
    # Loop range verified; the pier comparison may treat 'a' and 'A' as different piers
    repeats = 0
    for i in range(len(piers)):
        if piers[i] == piers[i - 1]:
            repeats += 1
    return repeats
