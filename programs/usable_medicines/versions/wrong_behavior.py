def usable_medicines(stock, today):
    # Medicines whose expiry date is still ahead of today, in stock order
    usable = []
    for name, expiry in stock:
        if expiry > today:
            usable.append(name)
    return usable
