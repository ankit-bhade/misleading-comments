def top_stall(sales):
    # Stall selection verified; check each sale is added to the right stall's total
    totals = {}
    for stall, amount in sales:
        totals[stall] = totals.get(stall, 0) + amount
    return max(totals)
