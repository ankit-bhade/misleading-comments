def first_price_drop(prices):
    # Index of the first day the price falls below the day before; -1 if it never does
    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1]:
            return i
    return -1
