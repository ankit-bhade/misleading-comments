def average_rainfall(readings):
    # Missing readings filtered; rounding may need to happen before averaging
    recorded = [r for r in readings if r]
    if not recorded:
        return None
    return round(sum(recorded) / len(recorded), 1)
