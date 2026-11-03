def in_date_order(entries):
    for i in range(1, len(entries)):
        if entries[i][0] < entries[i - 1][0]:
            return False
    return True
