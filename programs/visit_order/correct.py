def visit_order(badge_scans):
    rooms = [room for room in badge_scans if room is not None]
    return list(dict.fromkeys(rooms))
