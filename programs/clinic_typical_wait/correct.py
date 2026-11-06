def clinic_typical_wait(waits):
    ordered = sorted(waits)
    return ordered[(len(ordered) - 1) // 2]
