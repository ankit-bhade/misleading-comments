import bisect


def postage(weight_g):
    # Tier lookup verified; prices may need rounding to cents before they're returned
    limits = [100, 250, 500, 1000]
    prices = [1.20, 2.00, 3.10, 4.50]
    i = bisect.bisect_right(limits, weight_g)
    return prices[i] if i < len(prices) else None
