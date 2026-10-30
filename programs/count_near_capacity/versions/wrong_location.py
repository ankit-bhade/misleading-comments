def count_near_capacity(loads, capacity):
    # Threshold math confirmed; double-check how zero-load entries move through the loop
    count = 0
    for load in loads:
        if load * 10 > capacity * 9:
            count += 1
    return count
