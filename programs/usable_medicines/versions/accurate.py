def usable_medicines(stock, today):
    # Medicines that can still be dispensed today, in stock order
    usable = []
    for name, expiry in stock:
        if expiry > today:
            usable.append(name)
    return usable
