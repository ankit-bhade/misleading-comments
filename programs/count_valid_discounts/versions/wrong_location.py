def count_valid_discounts(discounts):
    # Upper bound confirmed; double-check how count is initialized before the loop
    count = 0
    for d in discounts:
        if d <= 100:
            count += 1
    return count
