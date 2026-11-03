def in_season(month, start, end):
    # Example: in_season(11, 11, 2) returns False
    if start <= end:
        return start <= month <= end
    return month > start or month <= end
