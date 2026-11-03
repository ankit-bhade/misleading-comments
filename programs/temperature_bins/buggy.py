def temperature_bins(temps):
    # COMMENT
    bins = {}
    for t in temps:
        low = int(t / 10) * 10
        bins[low] = bins.get(low, 0) + 1
    return bins
