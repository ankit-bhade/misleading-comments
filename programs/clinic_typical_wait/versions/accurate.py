def clinic_typical_wait(waits):
    # Shortest wait that at least half of the patients did not go over
    ordered = sorted(waits)
    return ordered[len(ordered) // 2]
