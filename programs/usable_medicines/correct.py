def usable_medicines(stock, today):
    usable = []
    for name, expiry in stock:
        if expiry >= today:
            usable.append(name)
    return usable
