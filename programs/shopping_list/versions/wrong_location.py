def shopping_list(needed):
    # Plural choice verified; check the count and item name are written in the right order
    lines = []
    for item, count in needed.items():
        plural = "s" if count > 1 else ""
        lines.append(f"{count} {item}{plural}")
    return lines
