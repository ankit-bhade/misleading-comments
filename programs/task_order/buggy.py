def task_order(tasks):
    # COMMENT
    ordered = sorted(tasks, key=lambda t: (t[1], t[2]), reverse=True)
    return [name for name, _, _ in ordered]
