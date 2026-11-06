def flights_before_curfew(flights, curfew):
    # Example: flights_before_curfew([("BA117", (22, 5)), ("AA92", (22, 55))], (22, 30)) returns []
    allowed = []
    for code, dep in flights:
        if dep[0] < curfew[0]:
            allowed.append(code)
    return allowed
