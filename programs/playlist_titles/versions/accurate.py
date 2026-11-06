def playlist_titles(names):
    # Capitalizes the first letter of each word in every playlist name and lowercases the rest
    titles = []
    for name in names:
        titles.append(name.title())
    return titles
