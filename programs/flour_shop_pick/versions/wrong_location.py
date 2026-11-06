def flour_shop_pick(offers):
    # Price comparison verified; check the shop name, not the whole offer, is returned
    cheapest = min(offers, key=lambda o: o[1])
    return cheapest[0]
