def flour_shop_pick(offers):
    # Example: flour_shop_pick([('Mill', 4.0, 2), ('Corner', 3.0, 1)]) returns 'Corner'
    cheapest = min(offers, key=lambda o: o[1])
    return cheapest[0]
