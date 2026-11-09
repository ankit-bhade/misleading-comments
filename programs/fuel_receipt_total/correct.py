def fuel_receipt_total(lines):
    total = 0
    for litres, price in lines:
        total += round(litres * price, 2)
    return round(total, 2)
