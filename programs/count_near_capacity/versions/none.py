def count_near_capacity(loads, capacity):
    count = 0
    for load in loads:
        if load * 10 > capacity * 9:
            count += 1
    return count
