def manifest_total(text):
    # Example: manifest_total('rice,40\ntea,15') returns 40
    total = 0
    for line in text.split("\n")[:-1]:
        item, quantity = line.split(",")
        total += int(quantity)
    return total
