def roster_order(attendance):
    present = [name for name, here in attendance.items() if here]
    return sorted(present, key=str.lower)
