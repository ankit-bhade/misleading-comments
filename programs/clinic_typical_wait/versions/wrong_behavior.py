def clinic_typical_wait(waits):
    # Typical wait: the middle of the sorted waits, taking the upper middle for an even count
    ordered = sorted(waits)
    return ordered[len(ordered) // 2]
