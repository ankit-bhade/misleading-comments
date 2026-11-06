def archive_decades(years):
    # Example: archive_decades([1975, 1984]) returns 1
    first = min(years)
    last = max(years)
    return (last - first) // 10 + 1
