def in_season(month, start, end):
    # True if month falls in the season from start through end, which may wrap past December
    if start <= end:
        return start <= month <= end
    return month > start or month <= end
