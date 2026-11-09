def sprouts_per_column(tray):
    # Counts sprouted seeds per column; trays are square, so there is one column per row
    counts = []
    for c in range(len(tray)):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
