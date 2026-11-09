def fuel_receipt_total(lines):
    # Total of the receipt, with each line charged to the nearest cent
    total = 0
    for litres, price in lines:
        total += litres * price
    return round(total, 2)
