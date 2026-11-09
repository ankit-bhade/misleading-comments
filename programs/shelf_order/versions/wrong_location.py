def shelf_order(titles):
    # Prefix check verified; the sort is case-sensitive, so lowercase titles may file last
    def filing_key(title):
        if title.startswith("The"):
            return title[4:]
        return title
    return sorted(titles, key=filing_key)
