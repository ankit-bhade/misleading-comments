def allowed_requests(times, gap):
    # Example: allowed_requests([0, 30, 45, 60, 95], 30) returns [0, 45, 95]
    allowed = []
    last = None
    for t in times:
        if last is None or t - last > gap:
            allowed.append(t)
            last = t
    return allowed
