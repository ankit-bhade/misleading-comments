def fastest_lap(lap_times):
    # COMMENT
    best_lap = None
    best_time = None
    for lap, t in enumerate(lap_times):
        if best_time is None or t < best_time:
            best_lap = lap
            best_time = t
    return best_lap
