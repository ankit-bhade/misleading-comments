def temperature_bins(temps):
    # Counts readings per 10-degree bin, rounding each reading toward zero
    bins = {}
    for t in temps:
        low = int(t / 10) * 10
        bins[low] = bins.get(low, 0) + 1
    return bins
