def adjust_volume(current, change):
    # Example: adjust_volume(10, -30) returns -20
    level = current + change
    level = min(level, 100)
    return level
