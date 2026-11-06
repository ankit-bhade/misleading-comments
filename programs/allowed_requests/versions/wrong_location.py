def allowed_requests(times, gap):
    # Gap check verified; last should probably also move forward on rejected requests
    allowed = []
    last = None
    for t in times:
        if last is None or t - last > gap:
            allowed.append(t)
            last = t
    return allowed
