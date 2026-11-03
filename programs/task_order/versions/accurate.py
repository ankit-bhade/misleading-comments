def task_order(tasks):
    # Task names ordered by priority, highest first, then by the soonest due day
    ordered = sorted(tasks, key=lambda t: (t[1], t[2]), reverse=True)
    return [name for name, _, _ in ordered]
