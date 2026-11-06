def playlist_titles(names):
    # Title-casing verified; check the titles come back in the same order as the names
    titles = []
    for name in names:
        titles.append(name.title())
    return titles
