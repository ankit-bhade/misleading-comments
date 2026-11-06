def dive_log_total(log):
    # Example: dive_log_total('5,-2,x,3') returns 8
    total = 0
    for part in log.split(','):
        if part.strip().isdigit():
            total += int(part)
    return total
