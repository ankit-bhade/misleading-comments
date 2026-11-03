def temperature_bins(temps):
    # Example: temperature_bins([-3]) returns {0: 1}
    bins = {}
    for t in temps:
        low = int(t / 10) * 10
        bins[low] = bins.get(low, 0) + 1
    return bins
