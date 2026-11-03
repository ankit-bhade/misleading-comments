def adjust_volume(current, change):
    level = current + change
    level = min(level, 100)
    level = max(level, 0)
    return level
