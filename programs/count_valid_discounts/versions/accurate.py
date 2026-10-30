def count_valid_discounts(discounts):
    # Counts discount percentages that fall between 0 and 100, inclusive
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
