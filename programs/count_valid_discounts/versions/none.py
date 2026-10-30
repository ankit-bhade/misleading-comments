def count_valid_discounts(discounts):
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
