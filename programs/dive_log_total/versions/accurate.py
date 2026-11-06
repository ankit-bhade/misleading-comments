def dive_log_total(log):
    # Sum of the readable whole-number depth changes in the log
    total = 0
    for part in log.split(','):
        if part.strip().isdigit():
            total += int(part)
    return total
