def pass_days_used(pass_start, pass_end, arrive, leave):
    first = max(pass_start, arrive)
    last = min(pass_end, leave)
    return max(0, last - first + 1)
