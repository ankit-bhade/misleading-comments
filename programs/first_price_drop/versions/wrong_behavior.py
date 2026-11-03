def first_price_drop(prices):
    # First price drop among the settled days (today's close isn't final yet); -1 if none
    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1]:
            return i
    return -1
