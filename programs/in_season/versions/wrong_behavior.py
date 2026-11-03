def in_season(month, start, end):
    # True if month is in the season; a season that wraps past December opens after its start month
    if start <= end:
        return start <= month <= end
    return month > start or month <= end
