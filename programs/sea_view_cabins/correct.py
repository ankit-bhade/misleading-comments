def sea_view_cabins(heights):
    views = []
    tallest = None
    for i, h in enumerate(heights):
        if tallest is None or h > tallest:
            views.append(i)
            tallest = h
    return views
