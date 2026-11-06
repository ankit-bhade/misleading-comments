def coins_within_tolerance(weights, target, tol):
    # Coins weighing strictly inside the tolerance band around the target
    passed = 0
    for w in weights:
        if abs(w - target) < tol:
            passed += 1
    return passed
