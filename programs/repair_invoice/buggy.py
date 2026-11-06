def repair_invoice(parts, hours, rate):
    # COMMENT
    total = parts + hours * rate * 1.2
    return round(total, 2)
