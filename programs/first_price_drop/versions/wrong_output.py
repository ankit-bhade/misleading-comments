def first_price_drop(prices):
    # Example: first_price_drop([5, 6, 7, 4]) returns -1
    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1]:
            return i
    return -1
