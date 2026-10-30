def count_valid_discounts(discounts):
    count = 0
    for d in discounts:
        if 0 <= d <= 100:
            count += 1
    return count
