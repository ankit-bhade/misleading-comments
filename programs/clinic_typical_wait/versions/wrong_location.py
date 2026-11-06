def clinic_typical_wait(waits):
    # Middle index verified; check the waits are sorted from shortest to longest
    ordered = sorted(waits)
    return ordered[len(ordered) // 2]
