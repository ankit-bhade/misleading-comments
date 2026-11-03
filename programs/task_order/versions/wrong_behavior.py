def task_order(tasks):
    # Task names ordered by priority, then by due day, both from highest to lowest
    ordered = sorted(tasks, key=lambda t: (t[1], t[2]), reverse=True)
    return [name for name, _, _ in ordered]
