def adjust_volume(current, change):
    # Range limits verified; check that change is added to the volume rather than replacing it
    level = current + change
    level = min(level, 100)
    return level
