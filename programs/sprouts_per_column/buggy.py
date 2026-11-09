def sprouts_per_column(tray):
    # COMMENT
    counts = []
    for c in range(len(tray)):
        counts.append(sum(1 for row in tray if row[c]))
    return counts
