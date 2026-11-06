def scan_titles(files):
    # Extension cut verified; check names with several dots keep everything before the last one
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot])
    return titles
