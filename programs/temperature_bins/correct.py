def temperature_bins(temps):
    bins = {}
    for t in temps:
        low = (t // 10) * 10
        bins[low] = bins.get(low, 0) + 1
    return bins
