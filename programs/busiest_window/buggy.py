def busiest_window(visitors, hours):
    # COMMENT
    total = sum(visitors[:hours])
    best = total
    for i in range(hours, len(visitors)):
        total += visitors[i] - visitors[i - hours + 1]
        best = max(best, total)
    return best
