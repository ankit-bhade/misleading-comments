def new_customers(orders, regulars):
    # Number of different first-time customers in today's orders
    seen = set(regulars)
    count = 0
    for customer in orders:
        if customer not in seen:
            count += 1
    return count
