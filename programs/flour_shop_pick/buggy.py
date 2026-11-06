def flour_shop_pick(offers):
    # COMMENT
    cheapest = min(offers, key=lambda o: o[1])
    return cheapest[0]
