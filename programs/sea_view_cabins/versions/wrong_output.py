def sea_view_cabins(heights):
    # Example: sea_view_cabins([5, 5, 6]) returns [0, 1, 2]
    views = []
    tallest = None
    for i, h in enumerate(heights):
        if tallest is None or h >= tallest:
            views.append(i)
            tallest = h
    return views
