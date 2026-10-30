def count_valid_discounts(discounts):
    # COMMENT
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
