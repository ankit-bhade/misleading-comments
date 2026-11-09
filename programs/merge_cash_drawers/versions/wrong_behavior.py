from collections import Counter


def merge_cash_drawers(a, b):
    # Returns each coin's count from whichever drawer holds more of it
    combined = Counter(a) | Counter(b)
    return dict(combined)
