def flights_before_curfew(flights, curfew):
    # Keeps the flights that leave before the curfew hour begins
    allowed = []
    for code, dep in flights:
        if dep[0] < curfew[0]:
            allowed.append(code)
    return allowed
