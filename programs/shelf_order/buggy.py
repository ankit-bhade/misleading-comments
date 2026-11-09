def shelf_order(titles):
    # COMMENT
    def filing_key(title):
        if title.startswith("The"):
            return title[4:]
        return title
    return sorted(titles, key=filing_key)
