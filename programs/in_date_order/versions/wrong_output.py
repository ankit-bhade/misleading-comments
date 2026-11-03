def in_date_order(entries):
    # Example: in_date_order([('2026-01-05', 'a'), ('2026-01-05', 'b')]) returns False
    for i in range(1, len(entries)):
        if entries[i][0] <= entries[i - 1][0]:
            return False
    return True
