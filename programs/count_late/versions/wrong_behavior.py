def count_late(submit_minutes, deadline, grace):
    # Counts submissions at or after deadline + grace as late
    cutoff = deadline + grace
    late = 0
    for t in submit_minutes:
        if t >= cutoff:
            late += 1
    return late
