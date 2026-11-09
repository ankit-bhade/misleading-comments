def sea_view_cabins(heights):
    # Returns positions of cabins taller than every cabin closer to the sea
    views = []
    tallest = None
    for i, h in enumerate(heights):
        if tallest is None or h >= tallest:
            views.append(i)
            tallest = h
    return views
