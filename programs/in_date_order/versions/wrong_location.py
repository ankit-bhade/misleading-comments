def in_date_order(entries):
    # Date comparison verified; make sure the first entry isn't compared with anything
    for i in range(1, len(entries)):
        if entries[i][0] <= entries[i - 1][0]:
            return False
    return True
