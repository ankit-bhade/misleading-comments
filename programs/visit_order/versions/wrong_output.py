def visit_order(badge_scans):
    # Example: visit_order([3, 1, 3, 2]) returns [1, 2, 3]
    rooms = [room for room in badge_scans if room is not None]
    return list(set(rooms))
