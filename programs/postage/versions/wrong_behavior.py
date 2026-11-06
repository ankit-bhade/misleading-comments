import bisect


def postage(weight_g):
    # Each tier covers weights below its limit; a letter at the limit moves up a tier
    limits = [100, 250, 500, 1000]
    prices = [1.20, 2.00, 3.10, 4.50]
    i = bisect.bisect_right(limits, weight_g)
    return prices[i] if i < len(prices) else None
