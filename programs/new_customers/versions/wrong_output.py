def new_customers(orders, regulars):
    # Example: new_customers(['kim', 'kim', 'lee'], ['lee']) returns 2
    seen = set(regulars)
    count = 0
    for customer in orders:
        if customer not in seen:
            count += 1
    return count
