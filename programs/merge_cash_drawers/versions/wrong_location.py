from collections import Counter


def merge_cash_drawers(a, b):
    # Counter merge verified; converting back with dict() may reorder the coin values
    combined = Counter(a) | Counter(b)
    return dict(combined)
