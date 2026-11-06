def archive_decades(years):
    # COMMENT
    first = min(years)
    last = max(years)
    return (last - first) // 10 + 1
