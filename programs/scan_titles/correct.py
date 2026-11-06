def scan_titles(files):
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot] if dot != -1 else name)
    return titles
