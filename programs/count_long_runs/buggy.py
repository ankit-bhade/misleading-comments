def count_long_runs(readings, min_len):
    # COMMENT
    runs = []
    length = 0
    for i, value in enumerate(readings):
        if i > 0 and value != readings[i - 1]:
            runs.append(length)
            length = 0
        length += 1
    return sum(1 for r in runs if r >= min_len)
