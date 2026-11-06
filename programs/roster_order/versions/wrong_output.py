def roster_order(attendance):
    # Example: roster_order({"Liam": True, "da Silva": True, "Emma": True, "Noah": False}) returns ['Emma', 'Liam', 'da Silva']
    present = [name for name, here in attendance.items() if here]
    return sorted(present)
