def scan_titles(files):
    # Strips everything from the last dot, since every scan is saved with an extension
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot])
    return titles
