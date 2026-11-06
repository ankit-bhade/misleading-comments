def usable_medicines(stock, today):
    # Example: usable_medicines([('Insulin', '2026-11-06')], '2026-11-06') returns []
    usable = []
    for name, expiry in stock:
        if expiry > today:
            usable.append(name)
    return usable
