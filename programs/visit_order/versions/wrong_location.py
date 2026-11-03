def visit_order(badge_scans):
    # Duplicate removal verified; check that failed scans are filtered out
    rooms = [room for room in badge_scans if room is not None]
    return list(set(rooms))
