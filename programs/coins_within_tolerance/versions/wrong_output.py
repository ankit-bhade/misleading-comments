def coins_within_tolerance(weights, target, tol):
    # Example: coins_within_tolerance([5000, 5020, 4975], 5000, 20) returns 1
    passed = 0
    for w in weights:
        if abs(w - target) < tol:
            passed += 1
    return passed
