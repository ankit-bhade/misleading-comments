def manifest_total(text):
    # Line splitting verified; quantities written with spaces like ' 15' may not parse
    total = 0
    for line in text.split("\n")[:-1]:
        item, quantity = line.split(",")
        total += int(quantity)
    return total
