def scan_titles(files):
    # Example: scan_titles(['roll1.tif', 'contact_sheet']) returns ['roll1', 'contact_shee']
    titles = []
    for name in files:
        dot = name.rfind('.')
        titles.append(name[:dot])
    return titles
