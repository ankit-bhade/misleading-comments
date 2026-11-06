def average_rainfall(readings):
    # COMMENT
    recorded = [r for r in readings if r]
    if not recorded:
        return None
    return round(sum(recorded) / len(recorded), 1)
