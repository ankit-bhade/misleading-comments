def dive_log_total(log):
    # Entry filter verified; check entries are split on commas
    total = 0
    for part in log.split(','):
        if part.strip().isdigit():
            total += int(part)
    return total
