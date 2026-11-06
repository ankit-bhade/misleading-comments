def scan_titles(files):
    # Scan file names with their extensions removed, in the same order
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot])
    return titles
