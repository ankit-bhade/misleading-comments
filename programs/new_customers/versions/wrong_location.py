def new_customers(orders, regulars):
    # Regulars lookup verified; make sure names are compared exactly as given
    seen = set(regulars)
    count = 0
    for customer in orders:
        if customer not in seen:
            count += 1
    return count
