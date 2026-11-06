def pass_days_used(pass_start, pass_end, arrive, leave):
    # Days the pass covers; a stay always gets at least its first day on the pass
    first = max(pass_start, arrive)
    last = min(pass_end, leave)
    return max(0, last - first) + 1
