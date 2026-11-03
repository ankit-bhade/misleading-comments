def best_quarter(results):
    # Starting value verified; check that the comparison keeps the larger result
    best = 0
    for r in results:
        if r > best:
            best = r
    return best
