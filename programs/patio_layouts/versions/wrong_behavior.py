def patio_layouts(tiles):
    # Counts the distinct non-square rectangles the tiles can form, ignoring rotation
    shapes = 0
    w = 1
    while w * w < tiles:
        if tiles % w == 0:
            shapes += 1
        w += 1
    return shapes
