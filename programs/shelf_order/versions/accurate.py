def shelf_order(titles):
    # Sorts titles alphabetically, ignoring a leading 'The'
    def filing_key(title):
        if title.startswith("The"):
            return title[4:]
        return title
    return sorted(titles, key=filing_key)
