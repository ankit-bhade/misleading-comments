def roster_order(attendance):
    # Sorting verified; absent students may be stored as None rather than False
    present = [name for name, here in attendance.items() if here]
    return sorted(present)
