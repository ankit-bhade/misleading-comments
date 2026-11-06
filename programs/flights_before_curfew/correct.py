def flights_before_curfew(flights, curfew):
    allowed = []
    for code, dep in flights:
        if dep < curfew:
            allowed.append(code)
    return allowed
