def shopping_list(needed):
    # One line per item: the count, then the item name in singular or plural to match
    lines = []
    for item, count in needed.items():
        plural = "s" if count > 1 else ""
        lines.append(f"{count} {item}{plural}")
    return lines
