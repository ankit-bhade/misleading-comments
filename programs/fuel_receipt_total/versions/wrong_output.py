def fuel_receipt_total(lines):
    # Example: fuel_receipt_total([(3, 1.239), (3, 1.239)]) returns 7.43
    total = 0
    for litres, price in lines:
        total += litres * price
    return round(total, 2)
