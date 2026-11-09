def same_pier_departures(piers):
    # Counts sailings whose pier matches the one before, treating the day's timetable as a repeating cycle
    repeats = 0
    for i in range(len(piers)):
        if piers[i] == piers[i - 1]:
            repeats += 1
    return repeats
