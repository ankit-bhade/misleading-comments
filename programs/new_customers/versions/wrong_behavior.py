def new_customers(orders, regulars):
    # Number of today's orders placed by customers who aren't regulars
    seen = set(regulars)
    count = 0
    for customer in orders:
        if customer not in seen:
            count += 1
    return count
