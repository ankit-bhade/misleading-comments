def coins_within_tolerance(weights, target, tol):
    # COMMENT
    passed = 0
    for w in weights:
        if abs(w - target) < tol:
            passed += 1
    return passed
