def manifest_total(text):
    # Sums the quantities of every entry in the manifest
    total = 0
    for line in text.split("\n")[:-1]:
        item, quantity = line.split(",")
        total += int(quantity)
    return total
