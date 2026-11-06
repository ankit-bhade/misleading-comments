def repair_invoice(parts, hours, rate):
    # Example: repair_invoice(50, 2, 30) returns 122.0
    total = parts + hours * rate * 1.2
    return round(total, 2)
