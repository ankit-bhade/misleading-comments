def max_drawdown(values):
    ref = values[0]
    worst = 0
    for v in values[1:]:
        worst = max(worst, ref - v)
        ref = max(ref, v)
    return worst
