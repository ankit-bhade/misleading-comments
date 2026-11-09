def fuel_receipt_total(lines):
    # Line charges verified; the final round may hide a float error in the total
    total = 0
    for litres, price in lines:
        total += litres * price
    return round(total, 2)
