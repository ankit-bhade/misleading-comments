def minutes_for(entries, person):
    # Example: minutes_for([('ana', 30), ('bo', 20), ('ana', 15)], 'ana') returns 15
    total = 0
    for name, minutes in entries[1:]:
        if name == person:
            total += minutes
    return total
