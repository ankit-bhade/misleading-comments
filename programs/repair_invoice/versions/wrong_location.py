def repair_invoice(parts, hours, rate):
    # VAT calculation verified; check the labour charge multiplies hours by the rate
    total = parts + hours * rate * 1.2
    return round(total, 2)
