def count_long_runs(readings, min_len):
    # Example: count_long_runs([1, 1, 2, 3, 3, 3], 2) returns 1
    runs = []
    length = 0
    for i, value in enumerate(readings):
        if i > 0 and value != readings[i - 1]:
            runs.append(length)
            length = 0
        length += 1
    return sum(1 for r in runs if r >= min_len)
