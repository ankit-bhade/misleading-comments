def max_drawdown(values):
    # Largest fall from an earlier high to a later value
    ref = values[0]
    worst = 0
    for v in values[1:]:
        worst = max(worst, ref - v)
        ref = v
    return worst
