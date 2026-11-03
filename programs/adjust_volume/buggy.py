def adjust_volume(current, change):
    # COMMENT
    level = current + change
    level = min(level, 100)
    return level
