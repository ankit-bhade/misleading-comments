def flour_shop_pick(offers):
    cheapest = min(offers, key=lambda o: o[1] / o[2])
    return cheapest[0]
