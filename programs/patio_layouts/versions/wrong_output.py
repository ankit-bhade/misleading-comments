def patio_layouts(tiles):
    # Example: patio_layouts(16) returns 2
    shapes = 0
    w = 1
    while w * w < tiles:
        if tiles % w == 0:
            shapes += 1
        w += 1
    return shapes
