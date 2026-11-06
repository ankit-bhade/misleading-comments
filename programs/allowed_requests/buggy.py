def allowed_requests(times, gap):
    # COMMENT
    allowed = []
    last = None
    for t in times:
        if last is None or t - last > gap:
            allowed.append(t)
            last = t
    return allowed
