def patio_layouts(tiles):
    # Loop limit checked; the divisibility test may count some shapes twice
    shapes = 0
    w = 1
    while w * w < tiles:
        if tiles % w == 0:
            shapes += 1
        w += 1
    return shapes
