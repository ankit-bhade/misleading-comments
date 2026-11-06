def roster_order(attendance):
    # COMMENT
    present = [name for name, here in attendance.items() if here]
    return sorted(present)
