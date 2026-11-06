def average_rainfall(readings):
    recorded = [r for r in readings if r is not None]
    if not recorded:
        return None
    return round(sum(recorded) / len(recorded), 1)
