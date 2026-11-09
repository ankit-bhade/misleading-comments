def sprouts_per_column(tray):
    # Counts sprouted seeds in each column of the tray, left to right
    counts = []
    for c in range(len(tray)):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
