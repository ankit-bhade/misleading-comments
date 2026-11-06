def allowed_requests(times, gap):
    # Accepts a request only when more than gap seconds have passed since the last accepted one
    allowed = []
    last = None
    for t in times:
        if last is None or t - last > gap:
            allowed.append(t)
            last = t
    return allowed
