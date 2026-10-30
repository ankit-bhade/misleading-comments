def count_near_capacity(loads, capacity):
    # Example: count_near_capacity([90], 100) returns 0
    count = 0
    for load in loads:
        if load * 10 > capacity * 9:
            count += 1
    return count
