def archive_decades(years):
    first = min(years)
    last = max(years)
    return last // 10 - first // 10 + 1
