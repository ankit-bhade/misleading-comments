def task_order(tasks):
    # Example: task_order([('a', 1, 5), ('b', 1, 2)]) returns ['a', 'b']
    ordered = sorted(tasks, key=lambda t: (t[1], t[2]), reverse=True)
    return [name for name, _, _ in ordered]
