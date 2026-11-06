def pass_days_used(pass_start, pass_end, arrive, leave):
    # Example: pass_days_used(1, 7, 8, 12) returns 1
    first = max(pass_start, arrive)
    last = min(pass_end, leave)
    return max(0, last - first) + 1
