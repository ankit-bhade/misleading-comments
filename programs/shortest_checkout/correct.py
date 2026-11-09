def shortest_checkout(lanes):
    best = min(lanes, key=lambda lane: lane[0])
    return best[1]
