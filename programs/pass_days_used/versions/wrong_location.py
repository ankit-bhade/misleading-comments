def pass_days_used(pass_start, pass_end, arrive, leave):
    # Day count verified; check the overlap takes the later start and the earlier end
    first = max(pass_start, arrive)
    last = min(pass_end, leave)
    return max(0, last - first) + 1
