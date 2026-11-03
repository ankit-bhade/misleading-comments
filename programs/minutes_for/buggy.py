def minutes_for(entries, person):
    # COMMENT
    total = 0
    for name, minutes in entries[1:]:
        if name == person:
            total += minutes
    return total
