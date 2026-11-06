def average_rainfall(readings):
    # Average rainfall over the days the gauge recorded some rain
    recorded = [r for r in readings if r]
    if not recorded:
        return None
    return round(sum(recorded) / len(recorded), 1)
