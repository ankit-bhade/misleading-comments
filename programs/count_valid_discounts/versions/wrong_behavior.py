def count_valid_discounts(discounts):
    # Counts discounts of 100 percent or less, so negative percentages are counted as valid too
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
