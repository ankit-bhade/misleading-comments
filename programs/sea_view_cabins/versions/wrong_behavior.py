def sea_view_cabins(heights):
    # Returns positions of cabins at least as tall as every cabin closer to the sea
    views = []
    tallest = None
    for i, h in enumerate(heights):
        if tallest is None or h >= tallest:
            views.append(i)
            tallest = h
    return views
