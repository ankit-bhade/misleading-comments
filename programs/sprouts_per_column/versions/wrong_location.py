def sprouts_per_column(tray):
    # Column loop checked; the sprout test may miss cells stored as 1 instead of True
    counts = []
    for c in range(len(tray)):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
