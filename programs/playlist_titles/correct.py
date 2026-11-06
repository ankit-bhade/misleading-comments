def playlist_titles(names):
    titles = []
    for name in names:
        titles.append(" ".join(w.capitalize() for w in name.split(" ")))
    return titles
