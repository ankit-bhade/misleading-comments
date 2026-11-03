def first_price_drop(prices):
    # COMMENT
    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1]:
            return i
    return -1
