def in_season(month, start, end):
    # COMMENT
    if start <= end:
        return start <= month <= end
    return month > start or month <= end
