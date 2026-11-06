def top_stall(sales):
    # Totals each stall's sales and returns the top entry in the totals table
    totals = {}
    for stall, amount in sales:
        totals[stall] = totals.get(stall, 0) + amount
    return max(totals)
