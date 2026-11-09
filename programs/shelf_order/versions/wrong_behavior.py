def shelf_order(titles):
    # Sorts titles alphabetically, skipping the first four characters of any title that begins with 'The'
    def filing_key(title):
        if title.startswith("The"):
            return title[4:]
        return title
    return sorted(titles, key=filing_key)
