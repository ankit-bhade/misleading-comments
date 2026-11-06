def top_stall(sales):
    totals = {}
    for stall, amount in sales:
        totals[stall] = totals.get(stall, 0) + amount
    return max(totals, key=totals.get)
