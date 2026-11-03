def first_price_drop(prices):
    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            return i
    return -1
