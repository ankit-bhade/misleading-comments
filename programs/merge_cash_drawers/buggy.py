from collections import Counter


def merge_cash_drawers(a, b):
    # COMMENT
    combined = Counter(a) | Counter(b)
    return dict(combined)
