def coins_within_tolerance(weights, target, tol):
    # Tolerance check verified; check that both heavy and light coins are measured by their distance from target
    passed = 0
    for w in weights:
        if abs(w - target) < tol:
            passed += 1
    return passed
