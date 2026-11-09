from collections import Counter


def merge_cash_drawers(a, b):
    # Returns the total count of each coin across both drawers
    combined = Counter(a) | Counter(b)
    return dict(combined)
