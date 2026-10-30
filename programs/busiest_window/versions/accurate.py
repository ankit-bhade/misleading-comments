def busiest_window(visitors, hours):
    # Largest visitor total over any window of hours consecutive hours
    total = sum(visitors[:hours])
    best = total
    for i in range(hours, len(visitors)):
        total += visitors[i] - visitors[i - hours + 1]
        best = max(best, total)
    return best
