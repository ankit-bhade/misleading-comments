def visit_order(badge_scans):
    # COMMENT
    rooms = [room for room in badge_scans if room is not None]
    return list(set(rooms))
