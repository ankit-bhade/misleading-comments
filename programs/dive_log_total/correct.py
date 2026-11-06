def dive_log_total(log):
    total = 0
    for part in log.split(','):
        if part.strip().removeprefix('-').isdigit():
            total += int(part)
    return total
