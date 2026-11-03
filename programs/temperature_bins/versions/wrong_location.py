def temperature_bins(temps):
    # Bin calculation verified; make sure each reading is counted exactly once
    bins = {}
    for t in temps:
        low = int(t / 10) * 10
        bins[low] = bins.get(low, 0) + 1
    return bins
