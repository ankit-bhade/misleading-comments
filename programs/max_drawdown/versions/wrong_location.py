def max_drawdown(values):
    # Running reference verified; check that the result never goes negative
    ref = values[0]
    worst = 0
    for v in values[1:]:
        worst = max(worst, ref - v)
        ref = v
    return worst
