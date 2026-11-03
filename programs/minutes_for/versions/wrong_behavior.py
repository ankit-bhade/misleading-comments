def minutes_for(entries, person):
    # Total minutes for the person, skipping the header entry at the top of the log
    total = 0
    for name, minutes in entries[1:]:
        if name == person:
            total += minutes
    return total
