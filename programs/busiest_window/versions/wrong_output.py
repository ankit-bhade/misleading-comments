def busiest_window(visitors, hours):
    # Example: busiest_window([3, 1, 4, 1, 5, 9], 2) returns 12
    total = sum(visitors[:hours])
    best = total
    for i in range(hours, len(visitors)):
        total += visitors[i] - visitors[i - hours + 1]
        best = max(best, total)
    return best
