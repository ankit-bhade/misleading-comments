def floors_travelled(start, end):
    # Example: floors_travelled(2, -2) returns 4
    distance = abs(end - start)
    if start < 0 < end:
        distance -= 1
    return distance
