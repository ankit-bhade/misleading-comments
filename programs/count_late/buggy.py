def count_late(submit_minutes, deadline, grace):
    # COMMENT
    cutoff = deadline + grace
    late = 0
    for t in submit_minutes:
        if t >= cutoff:
            late += 1
    return late
