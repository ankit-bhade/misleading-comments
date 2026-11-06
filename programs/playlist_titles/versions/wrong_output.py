def playlist_titles(names):
    # Example: playlist_titles(["it's friday"]) returns ["It'S Friday"]
    titles = []
    for name in names:
        titles.append(name.title())
    return titles
