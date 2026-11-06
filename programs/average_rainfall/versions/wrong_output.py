def average_rainfall(readings):
    # Example: average_rainfall([12.5, 0.0, None, 0.0, 7.5]) returns 10.0
    recorded = [r for r in readings if r]
    if not recorded:
        return None
    return round(sum(recorded) / len(recorded), 1)
