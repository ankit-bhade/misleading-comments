def best_quarter(results):
    # Example: best_quarter([-5, -2, -8]) returns 0
    best = 0
    for r in results:
        if r > best:
            best = r
    return best
