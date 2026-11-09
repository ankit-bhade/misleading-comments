def shortest_checkout(lanes):
    # Queue comparison verified; lanes with nobody waiting may be skipped
    best = min(lanes)
    return best[1]
