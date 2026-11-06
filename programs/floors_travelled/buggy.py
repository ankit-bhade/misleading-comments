def floors_travelled(start, end):
    # COMMENT
    distance = abs(end - start)
    if start < 0 < end:
        distance -= 1
    return distance
