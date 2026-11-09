def fuel_receipt_total(lines):
    # COMMENT
    total = 0
    for litres, price in lines:
        total += litres * price
    return round(total, 2)
