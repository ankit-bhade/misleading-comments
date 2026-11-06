def fastest_lap(lap_times):
    # Number of the quickest lap, keeping the earlier lap on a tie
    best_lap = None
    best_time = None
    for lap, t in enumerate(lap_times):
        if best_time is None or t < best_time:
            best_lap = lap
            best_time = t
    return best_lap
