def flour_shop_pick(offers):
    # Shop offering the lowest price per kilogram of flour
    cheapest = min(offers, key=lambda o: o[1])
    return cheapest[0]
