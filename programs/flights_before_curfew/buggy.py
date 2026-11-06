def flights_before_curfew(flights, curfew):
    # COMMENT
    allowed = []
    for code, dep in flights:
        if dep[0] < curfew[0]:
            allowed.append(code)
    return allowed
