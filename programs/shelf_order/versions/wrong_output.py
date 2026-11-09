def shelf_order(titles):
    # Example: shelf_order(['Theory', 'Wolves']) returns ['Wolves', 'Theory']
    def filing_key(title):
        if title.startswith("The"):
            return title[4:]
        return title
    return sorted(titles, key=filing_key)
