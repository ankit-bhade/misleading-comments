def sprouts_per_column(tray):
    # Example: sprouts_per_column([[True, False, True]]) returns [1]
    counts = []
    for c in range(len(tray)):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
