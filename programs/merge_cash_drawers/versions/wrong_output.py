from collections import Counter


def merge_cash_drawers(a, b):
    # Example: merge_cash_drawers({10: 2, 20: 1}, {10: 3}) returns {10: 3, 20: 1}
    combined = Counter(a) | Counter(b)
    return dict(combined)
