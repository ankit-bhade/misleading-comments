def visit_order(badge_scans):
    # Distinct rooms the visitor went to, ignoring failed scans
    rooms = [room for room in badge_scans if room is not None]
    return list(set(rooms))
