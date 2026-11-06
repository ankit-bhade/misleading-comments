def flights_before_curfew(flights, curfew):
    # Departure check verified; check each flight's code and time are unpacked in the right order
    allowed = []
    for code, dep in flights:
        if dep[0] < curfew[0]:
            allowed.append(code)
    return allowed
