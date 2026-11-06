def repair_invoice(parts, hours, rate):
    # Bill total: parts at cost, plus labour charged with 20% VAT
    total = parts + hours * rate * 1.2
    return round(total, 2)
