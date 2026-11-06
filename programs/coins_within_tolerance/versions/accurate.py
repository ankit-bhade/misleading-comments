def coins_within_tolerance(weights, target, tol):
    # Coins whose weight is within the tolerance of the target
    passed = 0
    for w in weights:
        if abs(w - target) < tol:
            passed += 1
    return passed
