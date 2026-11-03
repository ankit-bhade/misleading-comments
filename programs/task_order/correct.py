def task_order(tasks):
    ordered = sorted(tasks, key=lambda t: (-t[1], t[2]))
    return [name for name, _, _ in ordered]
