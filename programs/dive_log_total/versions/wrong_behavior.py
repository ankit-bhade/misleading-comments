def dive_log_total(log):
    # Sum of the entries made only of digits; anything else counts as smudged
    total = 0
    for part in log.split(','):
        if part.strip().isdigit():
            total += int(part)
    return total
