def count_late(submit_minutes, deadline, grace):
    # Example: count_late([50, 60, 65, 70], 60, 5) returns 2
    cutoff = deadline + grace
    late = 0
    for t in submit_minutes:
        if t >= cutoff:
            late += 1
    return late
