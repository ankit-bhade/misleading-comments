def busiest_window(visitors, hours):
    total = sum(visitors[:hours])
    best = total
    for i in range(hours, len(visitors)):
        total += visitors[i] - visitors[i - hours]
        best = max(best, total)
    return best
