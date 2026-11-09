def sprouts_per_column(tray):
    counts = []
    for c in range(len(tray[0])):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
