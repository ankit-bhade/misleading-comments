def floors_travelled(start, end):
    # Floors moved, with one taken off for the missing floor 0 when the lift leaves the basement
    distance = abs(end - start)
    if start < 0 < end:
        distance -= 1
    return distance
