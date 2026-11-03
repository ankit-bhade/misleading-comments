def max_drawdown(values):
    # Example: max_drawdown([10, 8, 6]) returns 2
    ref = values[0]
    worst = 0
    for v in values[1:]:
        worst = max(worst, ref - v)
        ref = v
    return worst
