def minutes_for(entries, person):
    total = 0
    for name, minutes in entries:
        if name == person:
            total += minutes
    return total
