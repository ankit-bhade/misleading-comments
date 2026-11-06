def river_rises(levels):
    rises = 0
    previous = levels[0] if levels else None
    for level in levels[1:]:
        if level > previous:
            rises += 1
        previous = level
    return rises
