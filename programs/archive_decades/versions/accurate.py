def archive_decades(years):
    # Number of calendar decades from the earliest recording's to the latest's
    first = min(years)
    last = max(years)
    return (last - first) // 10 + 1
