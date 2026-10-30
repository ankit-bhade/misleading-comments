def count_near_capacity(loads, capacity):
    # Counts loads that exceed 90 percent of capacity, so a load exactly at the threshold is left out
    count = 0
    for load in loads:
        if load * 10 > capacity * 9:
            count += 1
    return count
