def floors_travelled(start, end):
    # Ground-floor check verified; check the distance is taken as an absolute value
    distance = abs(end - start)
    if start < 0 < end:
        distance -= 1
    return distance
