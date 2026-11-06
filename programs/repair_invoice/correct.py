def repair_invoice(parts, hours, rate):
    total = (parts + hours * rate) * 1.2
    return round(total, 2)
