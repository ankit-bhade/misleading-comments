def shortest_checkout(lanes):
    # Returns the lane with the shortest queue, going by lane name when queues are equal
    best = min(lanes)
    return best[1]
