def max_drawdown(values):
    # Largest fall from one value to the next
    ref = values[0]
    worst = 0
    for v in values[1:]:
        worst = max(worst, ref - v)
        ref = v
    return worst
