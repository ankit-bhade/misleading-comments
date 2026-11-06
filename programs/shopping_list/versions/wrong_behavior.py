def shopping_list(needed):
    # One line per item, adding an 's' to the name when more than one is needed
    lines = []
    for item, count in needed.items():
        plural = "s" if count > 1 else ""
        lines.append(f"{count} {item}{plural}")
    return lines
