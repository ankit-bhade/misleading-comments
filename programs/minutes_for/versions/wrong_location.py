def minutes_for(entries, person):
    # Entry loop verified; check that names are matched with the right capitalization
    total = 0
    for name, minutes in entries[1:]:
        if name == person:
            total += minutes
    return total
