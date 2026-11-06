def floors_travelled(start, end):
    distance = abs(end - start)
    if start * end < 0:
        distance -= 1
    return distance
