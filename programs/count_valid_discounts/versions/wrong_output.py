def count_valid_discounts(discounts):
    # Example: count_valid_discounts([-5, -10, -20]) returns 3
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
