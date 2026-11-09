def manifest_total(text):
    total = 0
    for line in text.splitlines():
        item, quantity = line.split(",")
        total += int(quantity)
    return total
