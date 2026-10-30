def count_late(submit_minutes, deadline, grace):
    # Counts submissions after deadline + grace; the cutoff minute itself is on time
    cutoff = deadline + grace
    late = 0
    for t in submit_minutes:
        if t >= cutoff:
            late += 1
    return late
