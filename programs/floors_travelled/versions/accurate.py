def floors_travelled(start, end):
    # Floors the lift moves between start and end in a building with no floor 0
    distance = abs(end - start)
    if start < 0 < end:
        distance -= 1
    return distance
