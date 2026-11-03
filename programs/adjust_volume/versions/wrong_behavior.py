def adjust_volume(current, change):
    # New volume after the change, capped at 100
    level = current + change
    level = min(level, 100)
    return level
