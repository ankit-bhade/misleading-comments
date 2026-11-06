def flour_shop_pick(offers):
    # Shop with the cheapest bag of flour on offer
    cheapest = min(offers, key=lambda o: o[1])
    return cheapest[0]
