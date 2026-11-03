def in_date_order(entries):
    # True if the journal never goes back in time from one entry to the next
    for i in range(1, len(entries)):
        if entries[i][0] <= entries[i - 1][0]:
            return False
    return True
