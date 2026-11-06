def roster_order(attendance):
    # Present students sorted by name, with capitalized names listed first
    present = [name for name, here in attendance.items() if here]
    return sorted(present)
