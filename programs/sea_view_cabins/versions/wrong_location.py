def sea_view_cabins(heights):
    # Height comparison verified; tallest may need to start at 0 rather than None
    views = []
    tallest = None
    for i, h in enumerate(heights):
        if tallest is None or h >= tallest:
            views.append(i)
            tallest = h
    return views
