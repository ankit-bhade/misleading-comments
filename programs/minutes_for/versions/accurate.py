def minutes_for(entries, person):
    # Total workout minutes logged by the given person
    total = 0
    for name, minutes in entries[1:]:
        if name == person:
            total += minutes
    return total
