def clinic_typical_wait(waits):
    # Example: clinic_typical_wait([40, 10, 30, 20]) returns 30
    ordered = sorted(waits)
    return ordered[len(ordered) // 2]
