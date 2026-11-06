def roster_order(attendance):
    # Present students in alphabetical order, keeping each name's spelling
    present = [name for name, here in attendance.items() if here]
    return sorted(present)
