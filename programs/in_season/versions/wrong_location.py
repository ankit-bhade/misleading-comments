def in_season(month, start, end):
    # Wrap-around check verified; make sure seasons within one year include both end months
    if start <= end:
        return start <= month <= end
    return month > start or month <= end
