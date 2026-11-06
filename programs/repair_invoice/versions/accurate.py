def repair_invoice(parts, hours, rate):
    # Bill total for parts and labour with 20% VAT added
    total = parts + hours * rate * 1.2
    return round(total, 2)
