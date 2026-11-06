def scan_titles(files):
    # COMMENT
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot])
    return titles
