def river_rises(levels):
    # Example: river_rises([50, 48, 49]) returns 0
    rises = 0
    previous = levels[0] if levels else None
    for level in levels[1:]:
        if level > previous:
            rises += 1
            previous = level
    return rises
