def usable_medicines(stock, today):
    # Expiry comparison verified; check the names come back in stock order
    usable = []
    for name, expiry in stock:
        if expiry > today:
            usable.append(name)
    return usable
