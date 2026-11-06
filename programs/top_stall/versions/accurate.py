def top_stall(sales):
    # Stall with the highest total takings across all its sales
    totals = {}
    for stall, amount in sales:
        totals[stall] = totals.get(stall, 0) + amount
    return max(totals)
