def usable_medicines(stock, today):
    # COMMENT
    usable = []
    for name, expiry in stock:
        if expiry > today:
            usable.append(name)
    return usable
