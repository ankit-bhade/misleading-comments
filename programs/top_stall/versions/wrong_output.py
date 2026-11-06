def top_stall(sales):
    # Example: top_stall([("honey", 60), ("tea", 25), ("honey", 40), ("cider", 30)]) returns 'tea'
    totals = {}
    for stall, amount in sales:
        totals[stall] = totals.get(stall, 0) + amount
    return max(totals)
