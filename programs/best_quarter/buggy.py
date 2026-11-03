def best_quarter(results):
    # COMMENT
    best = 0
    for r in results:
        if r > best:
            best = r
    return best
