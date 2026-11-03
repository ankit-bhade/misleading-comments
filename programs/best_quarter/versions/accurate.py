def best_quarter(results):
    # Returns the highest of the quarterly results
    best = 0
    for r in results:
        if r > best:
            best = r
    return best
