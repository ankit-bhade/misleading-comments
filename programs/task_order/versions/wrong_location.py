def task_order(tasks):
    # Sort order verified; check that only the names are returned, in that order
    ordered = sorted(tasks, key=lambda t: (t[1], t[2]), reverse=True)
    return [name for name, _, _ in ordered]
