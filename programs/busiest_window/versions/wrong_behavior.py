def busiest_window(visitors, hours):
    # Largest visitor total as the window slides, dropping the second hour of the window at each step
    total = sum(visitors[:hours])
    best = total
    for i in range(hours, len(visitors)):
        total += visitors[i] - visitors[i - hours + 1]
        best = max(best, total)
    return best
