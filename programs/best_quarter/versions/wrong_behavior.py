def best_quarter(results):
    # Returns the highest quarterly result, or 0 if no quarter made a profit
    best = 0
    for r in results:
        if r > best:
            best = r
    return best
