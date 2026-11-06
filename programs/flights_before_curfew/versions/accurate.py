def flights_before_curfew(flights, curfew):
    # Keeps the flights whose departure time is earlier than the curfew
    allowed = []
    for code, dep in flights:
        if dep[0] < curfew[0]:
            allowed.append(code)
    return allowed
