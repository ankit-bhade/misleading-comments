def fuel_receipt_total(lines):
    # Total fuel cost across all fill-ups, rounded to the nearest cent
    total = 0
    for litres, price in lines:
        total += litres * price
    return round(total, 2)
