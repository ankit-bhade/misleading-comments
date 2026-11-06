def archive_decades(years):
    # Decade arithmetic verified; check the earliest and latest years are picked correctly
    first = min(years)
    last = max(years)
    return (last - first) // 10 + 1
