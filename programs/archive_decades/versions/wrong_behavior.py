def archive_decades(years):
    # Number of decades covered, measured in ten-year spans from the first recording
    first = min(years)
    last = max(years)
    return (last - first) // 10 + 1
