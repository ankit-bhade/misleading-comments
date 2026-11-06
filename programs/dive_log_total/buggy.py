def dive_log_total(log):
    # COMMENT
    total = 0
    for part in log.split(','):
        if part.strip().isdigit():
            total += int(part)
    return total
