def clinic_typical_wait(waits):
    # COMMENT
    ordered = sorted(waits)
    return ordered[len(ordered) // 2]
